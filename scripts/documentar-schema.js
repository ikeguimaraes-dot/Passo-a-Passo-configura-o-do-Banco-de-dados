#!/usr/bin/env node
"use strict";

// Gerador sem dependências externas. Substitui somente trechos delimitados.
const fs = require("fs");
const path = require("path");
const crypto = require("crypto");
const START = "<!-- AUTO-GENERATED:START -->";
const END = "<!-- AUTO-GENERATED:END -->";
const root = path.resolve(__dirname, "..");
const checkOnly = process.argv.includes("--check");

function splitTop(text) {
  const out = []; let buf = "", depth = 0, quote = null;
  for (let i = 0; i < text.length; i++) {
    const c = text[i]; buf += c;
    if (quote) {
      if (c === quote && text[i + 1] === quote) buf += text[++i];
      else if (c === quote) quote = null;
    } else if (c === "'" || c === '"') quote = c;
    else if (c === "(") depth++;
    else if (c === ")") depth--;
    else if (c === "," && depth === 0) { out.push(buf.slice(0, -1).trim()); buf = ""; }
  }
  if (buf.trim()) out.push(buf.trim());
  return out;
}
function all(re, text) { return [...text.matchAll(re)]; }
function esc(s) { return (s || "—").replace(/\|/g, "\\|").replace(/\s+/g, " ").trim(); }
function replaceGenerated(file, body) {
  const old = fs.existsSync(file) ? fs.readFileSync(file, "utf8") : "";
  const generated = `${START}\n${body.trimEnd()}\n${END}`;
  const next = old.includes(START) && old.includes(END)
    ? old.slice(0, old.indexOf(START)) + generated + old.slice(old.indexOf(END) + END.length)
    : old.trimEnd() + "\n\n" + generated + "\n";
  fs.writeFileSync(file, next.replace(/\r\n/g, "\n"), "utf8");
}

function parse(sql) {
  const d = { tables: {}, enums: {}, views: [], materialized: [], sequences: [], functions: [],
    procedures: [], triggers: [], indexes: [], policies: [], rls: new Set(), fks: [] };
  d.server = (sql.match(/Dumped from database version ([^\r\n]+)/) || [])[1] || "não identificado";
  d.pgDump = (sql.match(/Dumped by pg_dump version ([^\r\n]+)/) || [])[1] || "não identificado";
  for (const m of all(/^CREATE TYPE public\.([^\s]+) AS ENUM \(\s*([\s\S]*?)\s*\);/gm, sql))
    d.enums[m[1].replaceAll('"', "")] = all(/'((?:''|[^'])*)'/g, m[2]).map(x => x[1]);
  for (const m of all(/^CREATE TABLE public\.([^\s(]+) \(\s*([\s\S]*?)\n\);/gm, sql)) {
    const name = m[1].replaceAll('"', ""), columns = [], constraints = [];
    for (const item of splitTop(m[2])) {
      if (/^(CONSTRAINT|PRIMARY KEY|UNIQUE|CHECK|FOREIGN KEY)\b/i.test(item)) { constraints.push(item); continue; }
      const cm = item.match(/^"([^"]+)"\s+([\s\S]+)$/) || item.match(/^([^\s]+)\s+([\s\S]+)$/);
      if (!cm) { constraints.push(item); continue; }
      const rest = cm[2], cut = rest.search(/\s+(DEFAULT|NOT NULL|NULL|GENERATED|CONSTRAINT|CHECK|REFERENCES)\b/i);
      const dm = rest.match(/\bDEFAULT\s+([\s\S]+?)(?=\s+(?:NOT NULL|NULL|CONSTRAINT|CHECK|REFERENCES)\b|$)/i);
      const gm = rest.match(/\bGENERATED\s+([\s\S]+)$/i);
      columns.push({ name: cm[1], type: (cut < 0 ? rest : rest.slice(0, cut)).trim(),
        required: /\bNOT NULL\b/i.test(rest), def: gm ? "GENERATED " + gm[1].trim() : dm ? dm[1].trim() : "", raw: rest });
    }
    d.tables[name] = { columns, constraints };
  }
  for (const m of all(/^ALTER TABLE ONLY public\.([^\s]+)[\s\S]*?ADD CONSTRAINT\s+(".*?"|[^\s]+)\s+(PRIMARY KEY|UNIQUE|CHECK|FOREIGN KEY)\s*([\s\S]*?);$/gm, sql)) {
    const table = m[1].replaceAll('"', ""), cname = m[2].replaceAll('"', ""), kind = m[3].toUpperCase(), tail = m[4].trim();
    if (d.tables[table]) d.tables[table].constraints.push(`CONSTRAINT ${cname} ${kind} ${tail}`);
    if (kind === "FOREIGN KEY") {
      const f = tail.match(/\(([^)]+)\)\s+REFERENCES\s+([^\s(]+)\.([^\s(]+)\s*\(([^)]+)\)([\s\S]*)/i);
      if (f) d.fks.push({ table, name: cname, columns: f[1], schema: f[2], ref: f[3].replaceAll('"', ""), refcols: f[4], actions: f[5].trim() });
    }
  }
  for (const m of all(/^CREATE (?:UNIQUE )?INDEX\s+([^\s]+)\s+ON\s+(?:ONLY\s+)?public\.([^\s]+)\s+([\s\S]*?);$/gm, sql))
    d.indexes.push({ name: m[1].replaceAll('"', ""), table: m[2].replaceAll('"', ""), def: m[3].trim() });
  for (const m of all(/^CREATE TRIGGER\s+(".*?"|[^\s]+)\s+([\s\S]*?)\s+ON\s+public\.([^\s]+)\s+([\s\S]*?);$/gm, sql))
    d.triggers.push({ name: m[1].replaceAll('"', ""), table: m[3].replaceAll('"', ""), def: `${m[2]} ${m[4]}`.trim() });
  for (const m of all(/^CREATE POLICY\s+(".*?"|[^\s]+)\s+ON\s+public\.([^\s]+)\s*([\s\S]*?);$/gm, sql))
    d.policies.push({ name: m[1].replaceAll('"', ""), table: m[2].replaceAll('"', ""), def: m[3].trim() || "ALL" });
  for (const m of all(/^ALTER TABLE public\.([^\s]+) ENABLE ROW LEVEL SECURITY;/gm, sql)) d.rls.add(m[1].replaceAll('"', ""));
  for (const m of all(/^CREATE FUNCTION public\.([^\s(]+)(\([\s\S]*?\)) RETURNS ([^\r\n]+)\r?\n\s+LANGUAGE\s+([^\s]+)([\s\S]*?)(?=\r?\n--\r?\n-- Name:|\r?\nSET default_tablespace|\s*$)/gm, sql))
    d.functions.push({ name: m[1].replaceAll('"', ""), sig: m[2], returns: m[3].trim(), lang: m[4], security: /SECURITY DEFINER/.test(m[5]) });
  for (const m of all(/^CREATE PROCEDURE public\.([^\s(]+)(\([\s\S]*?\))\s+LANGUAGE\s+([^\s]+)/gm, sql))
    d.procedures.push({ name: m[1].replaceAll('"', ""), sig: m[2], lang: m[3] });
  // Cabeçalhos do pg_dump incluem também views com opções, CREATE OR REPLACE
  // posterior e sequences criadas implicitamente por colunas IDENTITY.
  d.views = all(/^-- Name: (.+); Type: VIEW; Schema: public; Owner: -$/gm, sql).map(m => m[1]);
  d.materialized = all(/^-- Name: (.+); Type: MATERIALIZED VIEW; Schema: public; Owner: -$/gm, sql).map(m => m[1]);
  d.sequences = all(/^-- Name: (.+); Type: SEQUENCE; Schema: public; Owner: -$/gm, sql).map(m => m[1]);
  return d;
}

function tablesDoc(d) {
  const by = list => Object.groupBy(list, x => x.table);
  const idx = by(d.indexes), trg = by(d.triggers), pol = by(d.policies), fks = by(d.fks);
  const out = [`_Inventário automático: ${Object.keys(d.tables).length} tabelas no schema \`public\`._`];
  for (const [name, t] of Object.entries(d.tables)) {
    const pk = t.constraints.filter(x => /PRIMARY KEY/i.test(x));
    const others = t.constraints.filter(x => !/PRIMARY KEY|FOREIGN KEY/i.test(x));
    out.push(`\n## ${name}`, "\n### Finalidade",
      `\nDescrição inferida pela estrutura: armazena registros relacionados a \`${name.replaceAll("_", " ")}\`. A finalidade de negócio exata deve ser confirmada com a equipe responsável.`,
      "\n### Colunas", "\n| Coluna | Tipo | Obrigatória | Padrão | Observação |", "|---|---|---|---|---|");
    for (const c of t.columns) out.push(`| ${esc(c.name)} | ${esc(c.type)} | ${c.required ? "Sim" : "Não"} | ${esc(c.def)} | ${/GENERATED/i.test(c.raw) ? "Coluna gerada" : "—"} |`);
    out.push("\n### Chave primária", pk.map(x => `- \`${esc(x)}\``).join("\n") || "\nNão identificada no dump.",
      "\n### Relacionamentos", (fks[name] || []).map(x => `- \`${x.name}\`: \`${x.columns}\` → \`${x.schema}.${x.ref}(${x.refcols})\`${x.actions ? ` (${esc(x.actions)})` : ""}`).join("\n") || "\nNenhuma chave estrangeira identificada.",
      "\n### Constraints", others.map(x => `- \`${esc(x)}\``).join("\n") || "\nNenhuma constraint adicional identificada.",
      "\n### Índices", (idx[name] || []).map(x => `- \`${x.name}\`: \`${esc(x.def)}\``).join("\n") || "\nNenhum índice adicional identificado.",
      "\n### Triggers", (trg[name] || []).map(x => `- \`${x.name}\`: \`${esc(x.def)}\``).join("\n") || "\nNenhum trigger associado.",
      "\n### Políticas RLS", `\nRLS: **${d.rls.has(name) ? "habilitada" : "não habilitada no dump"}**.`,
      (pol[name] || []).map(x => `- \`${x.name}\`: \`${esc(x.def)}\``).join("\n") || "\nNenhuma política associada.");
  }
  return out.join("\n");
}
function techDoc(d) {
  const count = x => x.length;
  const out = ["## Inventário automático", "",
    `- PostgreSQL de origem: **${d.server}**`, `- pg_dump: **${d.pgDump}**`,
    `- Tabelas: **${Object.keys(d.tables).length}**`, `- Enums: **${Object.keys(d.enums).length}**`,
    `- Views: **${count(d.views)}**`, `- Materialized views: **${count(d.materialized)}**`,
    `- Sequences explícitas: **${count(d.sequences)}**`, `- Functions: **${count(d.functions)}**`,
    `- Procedures: **${count(d.procedures)}**`, `- Triggers: **${count(d.triggers)}**`,
    `- Índices: **${count(d.indexes)}**`, `- Foreign keys: **${count(d.fks)}**`,
    `- Políticas RLS: **${count(d.policies)}**`, `- Tabelas com RLS habilitada: **${d.rls.size}**`,
    "\n## Tipos ENUM"];
  for (const [n, vals] of Object.entries(d.enums)) out.push(`\n### ${n}\n\nValores: ${vals.map(x => `\`${x}\``).join(", ")}.`);
  out.push("\n## Views", d.views.map(x => `- \`${x}\``).join("\n") || "\nNenhuma identificada.",
    "\n## Materialized views", d.materialized.map(x => `- \`${x}\``).join("\n") || "\nNenhuma identificada.",
    "\n## Sequences", d.sequences.map(x => `- \`${x}\``).join("\n") || "\nNenhuma sequence explícita identificada.",
    "\n## Functions", "\n| Função | Retorno | Linguagem | SECURITY DEFINER |", "|---|---|---|---|");
  for (const x of d.functions) out.push(`| \`${esc(x.name + x.sig)}\` | \`${esc(x.returns)}\` | \`${x.lang}\` | ${x.security ? "Sim" : "Não"} |`);
  out.push("\n## Procedures", d.procedures.map(x => `- \`${esc(x.name + x.sig)}\` — \`${x.lang}\``).join("\n") || "\nNenhuma procedure identificada.",
    "\n## Triggers", d.triggers.map(x => `- \`${x.table}.${x.name}\` — \`${esc(x.def)}\``).join("\n") || "\nNenhum trigger identificado.",
    "\n## Índices", d.indexes.map(x => `- \`${x.table}.${x.name}\` — \`${esc(x.def)}\``).join("\n") || "\nNenhum índice identificado.",
    "\n## Foreign keys", d.fks.map(x => `- \`${x.name}\`: \`${x.table}(${x.columns})\` → \`${x.schema}.${x.ref}(${x.refcols})\``).join("\n") || "\nNenhuma foreign key identificada.",
    "\n## Políticas RLS", d.policies.map(x => `- \`${x.table}.${x.name}\` — \`${esc(x.def)}\``).join("\n") || "\nNenhuma política identificada.");
  return out.join("\n");
}

try {
  const schemaPath = path.join(root, "database", "schema.sql");
  const raw = fs.readFileSync(schemaPath), sql = raw.toString("utf8"), d = parse(sql);
  if (!Object.keys(d.tables).length) throw new Error("nenhuma tabela public foi identificada");
  if (!checkOnly) {
    replaceGenerated(path.join(root, "03 - estrutura das tabelas.md"), tablesDoc(d));
    replaceGenerated(path.join(root, "04 - documentação técnica do banco.md"), techDoc(d));
  }
  const counts = { tabelas: Object.keys(d.tables).length, enums: Object.keys(d.enums).length,
    views: d.views.length, materialized_views: d.materialized.length, functions: d.functions.length,
    procedures: d.procedures.length, triggers: d.triggers.length, policies: d.policies.length,
    indexes: d.indexes.length, foreign_keys: d.fks.length };
  console.log("SHA256 schema.sql:", crypto.createHash("sha256").update(raw).digest("hex"));
  console.log("Contagens:", Object.entries(counts).map(([k, v]) => `${k}=${v}`).join(", "));
} catch (e) {
  console.error("Erro:", e.message); process.exitCode = 1;
}
