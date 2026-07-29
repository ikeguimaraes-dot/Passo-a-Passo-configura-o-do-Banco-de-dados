#!/usr/bin/env python3
"""Gera documentação Markdown a partir de database/schema.sql.

Não usa rede nem credenciais e só substitui conteúdo entre marcadores
AUTO-GENERATED nos documentos de destino.
"""
from __future__ import annotations

import argparse
import hashlib
import re
import sys
from collections import defaultdict
from pathlib import Path

START = "<!-- AUTO-GENERATED:START -->"
END = "<!-- AUTO-GENERATED:END -->"


def split_top_level(text: str) -> list[str]:
    parts, buf, depth, quote = [], [], 0, None
    i = 0
    while i < len(text):
        c = text[i]
        if quote:
            buf.append(c)
            if c == quote:
                if i + 1 < len(text) and text[i + 1] == quote:
                    buf.append(text[i + 1]); i += 1
                else:
                    quote = None
        elif c in "'\"":
            quote = c; buf.append(c)
        elif c == "(":
            depth += 1; buf.append(c)
        elif c == ")":
            depth -= 1; buf.append(c)
        elif c == "," and depth == 0:
            parts.append("".join(buf).strip()); buf = []
        else:
            buf.append(c)
        i += 1
    if "".join(buf).strip():
        parts.append("".join(buf).strip())
    return parts


def statements(sql: str, prefix: str) -> list[str]:
    pattern = re.compile(rf"(?ms)^{re.escape(prefix)}.*?;\s*$")
    return [m.group(0).strip() for m in pattern.finditer(sql)]


def md(text: str | None) -> str:
    if not text:
        return "—"
    return text.replace("|", r"\|").replace("\n", " ").strip()


def replace_generated(path: Path, body: str) -> None:
    generated = f"{START}\n{body.rstrip()}\n{END}"
    old = path.read_text(encoding="utf-8") if path.exists() else ""
    if START in old and END in old:
        new = old[:old.index(START)] + generated + old[old.index(END) + len(END):]
    else:
        new = old.rstrip() + ("\n\n" if old.strip() else "") + generated + "\n"
    path.write_text(new, encoding="utf-8", newline="\n")


def parse(sql: str) -> dict:
    data: dict = {
        "tables": {}, "enums": {}, "views": {}, "materialized_views": {},
        "sequences": [], "functions": [], "procedures": [], "triggers": [],
        "indexes": [], "policies": [], "rls": set(), "foreign_keys": [],
        "extensions": set(), "pg_dump": None, "server": None,
    }
    v = re.search(r"Dumped by pg_dump version ([^\r\n]+)", sql)
    s = re.search(r"Dumped from database version ([^\r\n]+)", sql)
    data["pg_dump"], data["server"] = (v.group(1) if v else None), (s.group(1) if s else None)

    for m in re.finditer(r"(?ms)^CREATE TYPE public\.([^\s]+) AS ENUM \(\s*(.*?)\s*\);", sql):
        data["enums"][m.group(1).strip('"')] = re.findall(r"'((?:''|[^'])*)'", m.group(2))

    for m in re.finditer(r"(?ms)^CREATE TABLE public\.([^\s(]+) \(\s*(.*?)\n\);", sql):
        name, body = m.group(1).strip('"'), m.group(2)
        cols, constraints = [], []
        for item in split_top_level(body):
            item = item.strip()
            if re.match(r"^(CONSTRAINT|PRIMARY KEY|UNIQUE|CHECK|FOREIGN KEY)\b", item, re.I):
                constraints.append(item); continue
            cm = re.match(r'^"([^"]+)"\s+(.+)$|^([^\s]+)\s+(.+)$', item, re.S)
            if not cm:
                constraints.append(item); continue
            col, rest = (cm.group(1), cm.group(2)) if cm.group(1) else (cm.group(3), cm.group(4))
            cut = re.search(r"\s+(DEFAULT|NOT NULL|NULL|GENERATED|CONSTRAINT|CHECK|REFERENCES)\b", rest, re.I)
            typ = rest[:cut.start()].strip() if cut else rest.strip()
            default = None
            dm = re.search(r"\bDEFAULT\s+(.+?)(?=\s+(?:NOT NULL|NULL|CONSTRAINT|CHECK|REFERENCES)\b|$)", rest, re.I | re.S)
            if dm: default = dm.group(1).strip()
            gm = re.search(r"\bGENERATED\s+(.+)$", rest, re.I | re.S)
            if gm: default = "GENERATED " + gm.group(1).strip()
            cols.append({"name": col, "type": typ, "not_null": bool(re.search(r"\bNOT NULL\b", rest, re.I)),
                         "default": default, "raw": rest})
        data["tables"][name] = {"columns": cols, "constraints": constraints}

    for st in statements(sql, "ALTER TABLE ONLY public."):
        tm = re.match(r"ALTER TABLE ONLY public\.([^\s]+)", st)
        if not tm: continue
        table = tm.group(1).strip('"')
        cm = re.search(r"ADD CONSTRAINT\s+(.+?)\s+(PRIMARY KEY|UNIQUE|CHECK|FOREIGN KEY)\s*(.*);$", st, re.I | re.S)
        if cm and table in data["tables"]:
            cname, kind, tail = cm.group(1).strip('"'), cm.group(2).upper(), cm.group(3).strip()
            data["tables"][table]["constraints"].append(f"CONSTRAINT {cname} {kind} {tail}")
            if kind == "FOREIGN KEY":
                fm = re.search(r"\(([^)]+)\)\s+REFERENCES\s+([^\s(]+)\.([^\s(]+)\s*\(([^)]+)\)(.*)", tail, re.I | re.S)
                if fm:
                    fk = {"table": table, "name": cname, "columns": fm.group(1), "ref_schema": fm.group(2),
                          "ref_table": fm.group(3).strip('"'), "ref_columns": fm.group(4), "actions": fm.group(5).strip()}
                    data["foreign_keys"].append(fk)

    for m in re.finditer(r"(?ms)^CREATE (?:UNIQUE )?INDEX\s+([^\s]+)\s+ON\s+(?:ONLY\s+)?public\.([^\s]+)\s+(.+?);\s*$", sql):
        data["indexes"].append({"name": m.group(1).strip('"'), "table": m.group(2).strip('"'), "definition": m.group(3).strip()})

    for m in re.finditer(r'(?ms)^CREATE TRIGGER\s+(".*?"|[^\s]+)\s+(.*?)\s+ON\s+public\.([^\s]+)\s+(.*?);\s*$', sql):
        data["triggers"].append({"name": m.group(1).strip('"'), "table": m.group(3).strip('"'),
                                 "definition": (m.group(2) + " " + m.group(4)).strip()})

    for m in re.finditer(r'(?ms)^CREATE POLICY\s+(".*?"|[^\s]+)\s+ON\s+public\.([^\s]+)\s*(.*?);\s*$', sql):
        data["policies"].append({"name": m.group(1).strip('"'), "table": m.group(2).strip('"'), "definition": m.group(3).strip() or "ALL"})
    for m in re.finditer(r"^ALTER TABLE public\.([^\s]+) ENABLE ROW LEVEL SECURITY;", sql, re.M):
        data["rls"].add(m.group(1).strip('"'))

    for m in re.finditer(r"(?ms)^CREATE FUNCTION public\.([^\s(]+)(\(.*?\)) RETURNS (.+?)\n\s+LANGUAGE\s+([^\s]+)(.*?)(?=\n--\n-- Name:|\nSET default_tablespace|\Z)", sql):
        data["functions"].append({"name": m.group(1).strip('"'), "signature": m.group(2), "returns": m.group(3).strip(),
                                  "language": m.group(4), "security_definer": "SECURITY DEFINER" in m.group(5)})
    for m in re.finditer(r"(?ms)^CREATE PROCEDURE public\.([^\s(]+)(\(.*?\))\s+LANGUAGE\s+([^\s]+)", sql):
        data["procedures"].append({"name": m.group(1).strip('"'), "signature": m.group(2), "language": m.group(3)})

    for kind, key in (("VIEW", "views"), ("MATERIALIZED VIEW", "materialized_views")):
        for name in re.findall(rf"^-- Name: (.+); Type: {kind}; Schema: public; Owner: -$", sql, re.M):
            data[key][name] = "Definição presente no dump."
    data["sequences"] = re.findall(r"^-- Name: (.+); Type: SEQUENCE; Schema: public; Owner: -$", sql, re.M)
    data["extensions"].update(re.findall(r"\b(?:extensions|auth|storage|graphql_public)\.([A-Za-z_][A-Za-z0-9_]*)", sql))
    return data


def infer_purpose(name: str) -> str:
    return (f"Descrição inferida pela estrutura: armazena registros relacionados a "
            f"`{name.replace('_', ' ')}`. A finalidade de negócio exata deve ser confirmada com a equipe responsável.")


def table_doc(data: dict) -> str:
    idx = defaultdict(list); trg = defaultdict(list); pol = defaultdict(list); fks = defaultdict(list)
    for x in data["indexes"]: idx[x["table"]].append(x)
    for x in data["triggers"]: trg[x["table"]].append(x)
    for x in data["policies"]: pol[x["table"]].append(x)
    for x in data["foreign_keys"]: fks[x["table"]].append(x)
    out = [f"_Inventário automático: {len(data['tables'])} tabelas no schema `public`._"]
    for name, table in data["tables"].items():
        pk = [c for c in table["constraints"] if "PRIMARY KEY" in c.upper()]
        out += [f"\n## {name}", "\n### Finalidade", f"\n{infer_purpose(name)}",
                "\n### Colunas", "\n| Coluna | Tipo | Obrigatória | Padrão | Observação |",
                "|---|---|---|---|---|"]
        for c in table["columns"]:
            notes = []
            if "GENERATED" in c["raw"].upper(): notes.append("Coluna gerada")
            checks = re.findall(r"\bCHECK\s*(\(.*\))", c["raw"], re.I)
            if checks: notes.append("CHECK: " + checks[0])
            out.append(f"| {md(c['name'])} | {md(c['type'])} | {'Sim' if c['not_null'] else 'Não'} | {md(c['default'])} | {md('; '.join(notes))} |")
        out += ["\n### Chave primária", "\n" + ("\n".join(f"- `{md(x)}`" for x in pk) if pk else "Não identificada no dump."),
                "\n### Relacionamentos"]
        out.append("\n".join(f"- `{x['name']}`: `{x['columns']}` → `{x['ref_schema']}.{x['ref_table']}({x['ref_columns']})`"
                             + (f" ({md(x['actions'])})" if x["actions"] else "") for x in fks[name]) or "Nenhuma chave estrangeira identificada.")
        others = [c for c in table["constraints"] if "PRIMARY KEY" not in c.upper() and "FOREIGN KEY" not in c.upper()]
        out += ["\n### Constraints", "\n".join(f"- `{md(x)}`" for x in others) or "Nenhuma constraint adicional identificada.",
                "\n### Índices", "\n".join(f"- `{x['name']}`: `{md(x['definition'])}`" for x in idx[name]) or "Nenhum índice adicional identificado.",
                "\n### Triggers", "\n".join(f"- `{x['name']}`: `{md(x['definition'])}`" for x in trg[name]) or "Nenhum trigger associado.",
                "\n### Políticas RLS", f"\nRLS: **{'habilitada' if name in data['rls'] else 'não habilitada no dump'}**.",
                "\n".join(f"- `{x['name']}`: `{md(x['definition'])}`" for x in pol[name]) or "Nenhuma política associada."]
    return "\n".join(out)


def technical_doc(data: dict) -> str:
    out = [f"## Inventário automático", "",
           f"- PostgreSQL de origem: **{data['server'] or 'não identificado'}**",
           f"- pg_dump: **{data['pg_dump'] or 'não identificado'}**",
           f"- Tabelas: **{len(data['tables'])}**",
           f"- Enums: **{len(data['enums'])}**",
           f"- Views: **{len(data['views'])}**",
           f"- Materialized views: **{len(data['materialized_views'])}**",
           f"- Sequences explícitas: **{len(data['sequences'])}**",
           f"- Functions: **{len(data['functions'])}**",
           f"- Procedures: **{len(data['procedures'])}**",
           f"- Triggers: **{len(data['triggers'])}**",
           f"- Índices: **{len(data['indexes'])}**",
           f"- Foreign keys: **{len(data['foreign_keys'])}**",
           f"- Políticas RLS: **{len(data['policies'])}**",
           f"- Tabelas com RLS habilitada: **{len(data['rls'])}**"]
    out += ["\n## Tipos ENUM"]
    for name, vals in data["enums"].items():
        out.append(f"\n### {name}\n\nValores: " + ", ".join(f"`{v}`" for v in vals) + ".")
    for title, key in (("Views", "views"), ("Materialized views", "materialized_views")):
        out += [f"\n## {title}"]
        if data[key]:
            out += [f"- `{x}`" for x in data[key]]
        else: out.append("\nNenhuma identificada.")
    out += ["\n## Sequences", "\n".join(f"- `{x}`" for x in data["sequences"]) or "Nenhuma sequence explícita identificada.",
            "\n## Functions", "\n| Função | Retorno | Linguagem | SECURITY DEFINER |", "|---|---|---|---|"]
    for x in data["functions"]:
        out.append(f"| `{md(x['name'] + x['signature'])}` | `{md(x['returns'])}` | `{x['language']}` | {'Sim' if x['security_definer'] else 'Não'} |")
    out += ["\n## Procedures", "\n".join(f"- `{x['name']}{x['signature']}` — `{x['language']}`" for x in data["procedures"]) or "Nenhuma procedure identificada.",
            "\n## Triggers"]
    out += [f"- `{x['table']}.{x['name']}` — `{md(x['definition'])}`" for x in data["triggers"]] or ["Nenhum trigger identificado."]
    out += ["\n## Índices", "\n".join(f"- `{x['table']}.{x['name']}` — `{md(x['definition'])}`" for x in data["indexes"]) or "Nenhum índice identificado.",
            "\n## Foreign keys", "\n".join(f"- `{x['name']}`: `{x['table']}({x['columns']})` → `{x['ref_schema']}.{x['ref_table']}({x['ref_columns']})`" for x in data["foreign_keys"]) or "Nenhuma foreign key identificada.",
            "\n## Políticas RLS"]
    out += [f"- `{x['table']}.{x['name']}` — `{md(x['definition'])}`" for x in data["policies"]] or ["Nenhuma política identificada."]
    out += ["\n## Referências fora de `public`",
            "\nO analisador encontrou qualificadores externos usados por objetos do dump: " +
            (", ".join(f"`{x}`" for x in sorted(data["extensions"])) if data["extensions"] else "nenhum") +
            ". Isso indica dependências/referências; não comprova que suas definições estejam incluídas neste dump."]
    return "\n".join(out)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true", help="analisa e valida sem escrever")
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parents[1])
    args = parser.parse_args()
    schema = args.root / "database" / "schema.sql"
    try:
        raw = schema.read_bytes()
        sql = raw.decode("utf-8")
        data = parse(sql)
        counts = {k: len(data[k]) for k in ("tables", "enums", "views", "materialized_views", "functions",
                                            "procedures", "triggers", "policies", "indexes", "foreign_keys")}
        if not args.check:
            replace_generated(args.root / "03 - estrutura das tabelas.md", table_doc(data))
            replace_generated(args.root / "04 - documentação técnica do banco.md", technical_doc(data))
        print("SHA256 schema.sql:", hashlib.sha256(raw).hexdigest())
        print("Contagens:", ", ".join(f"{k}={v}" for k, v in counts.items()))
        if not data["tables"]:
            raise ValueError("nenhuma tabela public foi identificada")
        return 0
    except (OSError, UnicodeError, ValueError) as exc:
        print(f"Erro: {exc}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
