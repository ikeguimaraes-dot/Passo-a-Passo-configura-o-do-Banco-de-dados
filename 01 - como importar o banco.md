# Como importar o banco

> Não execute uma restauração em produção sem backup testado e janela de manutenção. O procedimento mais seguro é validar primeiro em um projeto vazio.

## Pelo SQL Editor (iniciantes)

1. Acesse o site oficial do Supabase, crie uma conta ou faça login.
2. Escolha **New project** e selecione a organização correta.
3. Informe um nome que identifique o ambiente, escolha uma região próxima dos usuários e defina uma senha forte para o banco. Guarde-a em um gerenciador de senhas.
4. Aguarde o projeto terminar de ser provisionado.
5. Abra **SQL Editor** e crie uma nova query.
6. Abra localmente `database/schema.sql`, selecione todo o conteúdo e copie.
7. Cole no editor e execute. Como o arquivo é grande, aguarde a conclusão e não feche a página durante o processamento.
8. No **Table Editor**, confirme as tabelas do schema `public`.
9. No painel do banco, verifique **Functions**, tipos/enums, views, triggers e policies. A posição desses menus pode mudar; use a busca do painel se necessário.
10. Compare os objetos com [03 - estrutura das tabelas.md](03%20-%20estrutura%20das%20tabelas.md) e [04 - documentação técnica do banco.md](04%20-%20documenta%C3%A7%C3%A3o%20t%C3%A9cnica%20do%20banco.md).

O SQL Editor pode impor limite de tamanho ou tempo. Se isso ocorrer, use `psql`.

## Alternativa com `psql`

Obtenha a string de conexão no painel do projeto. Prefira o **Session pooler** quando sua rede não oferece IPv6; a conexão direta do Supabase pode resolver para IPv6. Nunca salve a senha no repositório ou no histórico do terminal.

Exemplo genérico:

```powershell
psql "postgresql://USUARIO:SENHA_URL_ENCODED@HOST:5432/postgres?sslmode=require" -v ON_ERROR_STOP=1 -f "database/schema.sql"
```

Substitua os marcadores localmente. Se a senha contiver `@`, `:`, `/`, `?`, `#`, `%` ou outros caracteres reservados, aplique **URL encoding** (por exemplo, `@` torna-se `%40`). Uma alternativa mais segura é omitir a senha da URL e permitir que `psql` a solicite:

```powershell
psql "host=HOST port=5432 dbname=postgres user=USUARIO sslmode=require" -v ON_ERROR_STOP=1 -f "database/schema.sql"
```

## Possíveis erros durante a importação

- **Objeto já existe:** o destino não está vazio. Use outro projeto ou faça limpeza somente após backup e autorização.
- **Permissão negada:** use o usuário proprietário indicado pelo Supabase e confirme a string de conexão.
- **Objeto dependente ausente:** o dump é apenas do schema `public` e pode referenciar recursos gerenciados pelo Supabase, como `auth`.
- **Erro em função/policy:** confirme a versão do PostgreSQL e se as dependências Supabase do projeto foram provisionadas.
- **Tempo excedido ou importação parcial:** execute novamente em um projeto vazio usando `psql` com `ON_ERROR_STOP=1`; não presuma que o primeiro resultado ficou consistente.
- **Comandos `\restrict` desconhecidos:** use um `psql` compatível com a versão do `pg_dump` indicada no cabeçalho.

Consulte [06 - solução de problemas.md](06%20-%20solu%C3%A7%C3%A3o%20de%20problemas.md) para diagnóstico detalhado.

## Validação final

- [ ] A execução terminou sem erro.
- [ ] Todas as tabelas do catálogo foram criadas.
- [ ] Enums, views, functions e triggers aparecem no banco.
- [ ] RLS está habilitada nas tabelas indicadas e as policies existem.
- [ ] Índices, chaves primárias e estrangeiras foram criados.
- [ ] Um acesso de teste com chave `anon` respeita RLS.
- [ ] Nenhum dado de produção foi copiado: este dump contém somente estrutura.
