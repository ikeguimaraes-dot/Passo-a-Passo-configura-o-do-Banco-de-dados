# Guia rápido do banco de dados

Este guia apresenta o caminho mais simples para criar um novo banco no Supabase usando os arquivos desta pasta.

## O que será criado

O arquivo `database/schema.sql` contém a estrutura do banco de dados do sistema:

- tabelas;
- colunas e relacionamentos;
- funções e triggers;
- índices;
- regras de acesso — RLS.

Ele não contém dados, usuários, senhas, arquivos enviados ou configurações externas.

## Antes de começar

É necessário ter:

- uma conta no Supabase;
- permissão para criar um projeto;
- o arquivo `database/schema.sql`;
- uma senha forte para o novo banco.

> Não faça este procedimento diretamente em produção sem backup.

## Passo a passo

### 1. Criar o projeto

1. Entre no Supabase.
2. Clique em **New project**.
3. Escolha a organização.
4. Informe o nome do projeto.
5. Escolha a região mais próxima dos usuários.
6. Crie uma senha forte e guarde-a em local seguro.
7. Aguarde o projeto ficar pronto.

### 2. Importar o banco

1. No Supabase, abra **SQL Editor**.
2. Clique em **New query**.
3. Abra o arquivo `database/schema.sql` no computador.
4. Copie todo o conteúdo do arquivo.
5. Cole no SQL Editor.
6. Clique em **Run**.
7. Aguarde a conclusão.

Se aparecer algum erro, não continue repetindo a execução. Anote a primeira mensagem e consulte [06 - solução de problemas.md](06%20-%20solu%C3%A7%C3%A3o%20de%20problemas.md).

### 3. Conferir o resultado

Depois da importação:

1. Abra o **Table Editor**.
2. Confirme que as tabelas foram criadas.
3. Verifique se o SQL Editor terminou sem erros.
4. Confirme as funções e regras de acesso no painel do banco.

Resultado esperado conforme o arquivo atual:

| Item | Quantidade |
|---|---:|
| Tabelas | 228 |
| Enums | 9 |
| Views | 17 |
| Funções | 89 |
| Triggers | 22 |
| Políticas de acesso | 439 |
| Índices | 314 |
| Chaves estrangeiras | 317 |

### 4. Entregar as informações à equipe técnica

No painel do Supabase, localize:

- Project URL;
- chave pública `anon`;
- chave privada `service_role`;
- dados de conexão do banco, se forem necessários.

Envie as credenciais somente por um canal seguro.

> A chave `service_role` nunca deve ser colocada no frontend, enviada em grupo aberto ou salva no repositório.

## Checklist final

- [ ] O novo projeto foi criado na organização e região corretas.
- [ ] A senha foi guardada com segurança.
- [ ] O arquivo `schema.sql` foi executado sem erros.
- [ ] As tabelas aparecem no Table Editor.
- [ ] As quantidades principais foram conferidas.
- [ ] As credenciais foram entregues por canal seguro.
- [ ] A chave `service_role` ficou restrita ao backend.
- [ ] A aplicação foi testada pela equipe técnica.

## Onde encontrar mais detalhes

- Importação completa: [01 - como importar o banco.md](01%20-%20como%20importar%20o%20banco.md)
- Configuração da aplicação: [02 - configurar o projeto.md](02%20-%20configurar%20o%20projeto.md)
- Catálogo das tabelas: [03 - estrutura das tabelas.md](03%20-%20estrutura%20das%20tabelas.md)
- Documentação técnica: [04 - documentação técnica do banco.md](04%20-%20documenta%C3%A7%C3%A3o%20t%C3%A9cnica%20do%20banco.md)
- Solução de erros: [06 - solução de problemas.md](06%20-%20solu%C3%A7%C3%A3o%20de%20problemas.md)
