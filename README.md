# Documentação do Banco de Dados

## Objetivo

Este conjunto de documentos permite recriar e compreender a estrutura PostgreSQL usada pelo sistema em um novo projeto Supabase. O conteúdo foi preparado para leitores iniciantes sem omitir os detalhes técnicos necessários à manutenção.

> `database/schema.sql` é a fonte oficial da estrutura. O arquivo contém somente objetos do schema `public`, sem dados. Não o edite manualmente: altere o banco, valide e gere um novo dump.

## Conteúdo

- [GUIA RÁPIDO PARA ENTREGA.md](GUIA%20R%C3%81PIDO%20PARA%20ENTREGA.md): versão curta e prática para gestores e responsáveis pela entrega.
- [01 - como importar o banco.md](01%20-%20como%20importar%20o%20banco.md): criação do projeto e importação via SQL Editor ou `psql`.
- [02 - configurar o projeto.md](02%20-%20configurar%20o%20projeto.md): chaves, variáveis de ambiente, execução e deploy.
- [03 - estrutura das tabelas.md](03%20-%20estrutura%20das%20tabelas.md): catálogo automático de tabelas, colunas, chaves, índices, triggers e RLS.
- [04 - documentação técnica do banco.md](04%20-%20documenta%C3%A7%C3%A3o%20t%C3%A9cnica%20do%20banco.md): inventário técnico dos objetos e limites do dump.
- [05 - controle de versão.md](05%20-%20controle%20de%20vers%C3%A3o.md): SemVer, changelog e processo de publicação.
- [06 - solução de problemas.md](06%20-%20solu%C3%A7%C3%A3o%20de%20problemas.md): diagnóstico de falhas comuns.
- `database/schema.sql`: dump estrutural oficial gerado por `pg_dump`.
- `supabase/`: configuração local do Supabase; deve ser preservada.
- `scripts/documentar-schema.js`: regenera os inventários automáticos sem alterar o dump.
- `scripts/documentar-schema.py`: alternativa equivalente para ambientes com Python.

## Ordem recomendada

Leia este arquivo e siga os documentos de `01` a `06`. Consulte os catálogos `03` e `04` sempre que precisar confirmar um objeto.

## Pré-requisitos

- Conta no Supabase e acesso para criar projetos.
- Editor de texto capaz de abrir um arquivo SQL grande.
- Para a alternativa por terminal: cliente PostgreSQL compatível (`psql`/`pg_dump`).
- Para Supabase CLI local: Node.js, Supabase CLI e, em operações locais, Docker Desktop.
- Projeto da aplicação separado, com seus arquivos de dependências e scripts.

## Checklist rápido

- [ ] Criar um projeto Supabase vazio na região correta.
- [ ] Guardar a senha do banco em um gerenciador seguro.
- [ ] Fazer backup antes de usar qualquer banco que já exista.
- [ ] Executar `database/schema.sql`.
- [ ] Conferir tabelas e demais objetos.
- [ ] Configurar apenas variáveis de ambiente genéricas no local apropriado.
- [ ] Manter a `service_role` exclusivamente no backend.
- [ ] Validar conexão e RLS com usuários de teste.

## Regenerar a documentação automática

Na raiz desta pasta:

```powershell
node scripts/documentar-schema.js
```

Somente o conteúdo entre `AUTO-GENERATED:START` e `AUTO-GENERATED:END` é substituído. Para analisar sem escrever:

```powershell
node scripts/documentar-schema.js --check
```
