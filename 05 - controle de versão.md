# Controle de versão

## Padrão SemVer

Use `MAJOR.MINOR.PATCH`:

- **MAJOR:** alteração incompatível, remoção/renomeação de objeto ou mudança que exige adaptação dos consumidores.
- **MINOR:** novo objeto ou recurso compatível com os consumidores existentes.
- **PATCH:** correção compatível, ajuste documental ou de constraint sem quebra esperada.

Versão inicial: **1.0.0**, representando o primeiro dump documentado desta entrega. O número descreve a versão do schema documentado, não a versão do PostgreSQL.

## Changelog

```markdown
## [1.1.0] - AAAA-MM-DD

### Adicionado
- ...

### Alterado
- ...

### Corrigido
- ...

### Removido
- ...

### Migração
- Impacto, ordem e rollback.
```

Registro inicial:

```markdown
## [1.0.0] - 2026-07-29

### Adicionado
- Primeiro dump estrutural do schema public documentado.
- Guias de importação, configuração, catálogo técnico, versionamento e solução de problemas.
```

## Processo recomendado

1. Alterar o banco por migração revisável.
2. Validar constraints, funções, triggers e RLS.
3. Gerar um novo `schema.sql` por ferramenta, nunca por edição manual.
4. Revisar o diff e procurar dados ou credenciais acidentais.
5. Executar `node scripts/documentar-schema.js`.
6. Atualizar documentos manuais e changelog.
7. Atualizar a versão SemVer.
8. Restaurar e testar em projeto vazio.
9. Criar o commit; esta documentação não faz commits automaticamente.

## Convenção de commits

```text
feat(db): adiciona tabela ...
fix(db): corrige constraint ...
docs(db): atualiza documentação ...
```

Use descrição objetiva, relacione a migração e destaque breaking changes no corpo/rodapé.

## Checklist de publicação

- [ ] Migração revisada e reversão planejada.
- [ ] Backup e teste de restauração confirmados.
- [ ] Novo dump gerado do banco validado.
- [ ] Diff contém somente mudanças esperadas.
- [ ] Inventários automáticos regenerados.
- [ ] Tabelas, enums, functions, views, triggers, índices, FKs e policies conferidos.
- [ ] Nenhum dado, secret ou URL com credencial foi incluído.
- [ ] Importação em projeto vazio passou.
- [ ] Aplicação e RLS foram testadas.
- [ ] Changelog, versão e documentação foram atualizados.
