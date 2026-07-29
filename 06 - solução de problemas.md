# Solução de problemas

## Docker Desktop is a prerequisite

- **Sintoma:** a Supabase CLI informa que Docker Desktop é pré-requisito ou não inicia os serviços locais.
- **Causa provável:** Docker ausente, parado ou inacessível.
- **Como corrigir:** instalar/iniciar o Docker Desktop e confirmar `docker version`. Para importar diretamente em projeto remoto com `psql`, Docker não é necessário.
- **Como evitar:** validar os pré-requisitos da CLI antes do trabalho.

## Virtualização não habilitada

- **Sintoma:** Docker/WSL2 não inicia ou relata virtualização indisponível.
- **Causa provável:** recurso desabilitado no BIOS/UEFI ou no Windows.
- **Como corrigir:** habilitar Intel VT-x/AMD-V no firmware e os recursos exigidos pelo WSL2; reiniciar.
- **Como evitar:** conferir virtualização no Gerenciador de Tarefas antes de instalar.

## WSL2 não instalado

- **Sintoma:** Docker no Windows solicita WSL2 ou falha no backend Linux.
- **Causa provável:** WSL ausente ou desatualizado.
- **Como corrigir:** em terminal administrativo, seguir a documentação oficial do Windows para instalar/atualizar WSL e reiniciar.
- **Como evitar:** manter Windows, WSL e kernel atualizados.

## `pg_dump` ou `psql` não reconhecido

- **Sintoma:** “não é reconhecido como nome de cmdlet”.
- **Causa provável:** cliente PostgreSQL ausente ou pasta `bin` fora do `PATH`.
- **Como corrigir:** instalar as ferramentas PostgreSQL; no Windows, localizar `pg_dump.exe` em caminhos como `C:\Program Files\PostgreSQL\<versão>\bin` e adicionar essa pasta ao `PATH`, ou chamar pelo caminho completo.
- **Como evitar:** confirmar `pg_dump --version` e `psql --version`.

## `password authentication failed`

- **Sintoma:** servidor rejeita o login.
- **Causa provável:** usuário/senha incorretos, projeto errado ou senha mal codificada.
- **Como corrigir:** copie novamente os parâmetros do painel, redefina a senha se autorizado e prefira o prompt de senha.
- **Como evitar:** use gerenciador de senhas e não monte URLs manualmente.

## `could not translate host name`

- **Sintoma:** nome do host não pode ser resolvido.
- **Causa provável:** host digitado errado, DNS/rede/VPN indisponível.
- **Como corrigir:** recopie o host, teste DNS e rede, desative VPN apenas se a política local permitir.
- **Como evitar:** use a string fornecida pelo painel sem espaços.

## Conexão direta e IPv6

- **Sintoma:** timeout ou “network unreachable” na conexão direta.
- **Causa provável:** o host direto usa IPv6 e a rede local não tem rota IPv6.
- **Como corrigir:** use o **Session pooler** e seus host/porta/usuário exibidos no painel, ou habilite IPv6 na rede.
- **Como evitar:** escolha o tipo de conexão compatível com a infraestrutura.

## Caracteres especiais na senha

- **Sintoma:** autenticação falha apesar de a senha parecer correta.
- **Causa provável:** caracteres reservados quebram a URL.
- **Como corrigir:** aplique URL encoding ou use parâmetros separados com prompt.
- **Como evitar:** não concatene credenciais diretamente em URLs.

## Tabela já existe

- **Sintoma:** `relation ... already exists`.
- **Causa provável:** destino não vazio ou tentativa anterior parcial.
- **Como corrigir:** importe em projeto vazio. Só remova objetos existentes com backup e autorização explícita.
- **Como evitar:** valide o destino antes de restaurar.

## Schema `public` já existe

- **Sintoma:** `schema "public" already exists`.
- **Causa provável:** o projeto já provisionou `public`.
- **Como corrigir:** use um destino vazio compatível ou ajuste controladamente o procedimento após revisar o dump; não remova `public` em produção.
- **Como evitar:** teste a restauração completa cedo em projeto descartável.

## `permission denied`

- **Sintoma:** criação/alteração de objeto é negada.
- **Causa provável:** usuário sem propriedade ou privilégio.
- **Como corrigir:** use a conexão de banco apropriada do projeto e confirme privilégios.
- **Como evitar:** documente qual identidade executa restaurações e aplique menor privilégio.

## Erro em função, trigger ou policy

- **Sintoma:** erro de sintaxe, função ausente ou tipo incompatível.
- **Causa provável:** versão incompatível, dependência não criada ou objeto externo ao dump.
- **Como corrigir:** leia o primeiro erro, confirme versões no cabeçalho e compare a ordem/dependências no catálogo técnico.
- **Como evitar:** restaure com cliente compatível e valide em projeto Supabase novo.

## Objeto dependente não encontrado

- **Sintoma:** `does not exist` ao criar view, FK, função ou policy.
- **Causa provável:** etapa anterior falhou ou dependência fica fora de `public`.
- **Como corrigir:** corrija o primeiro erro e reinicie em banco vazio; confirme componentes gerenciados do Supabase.
- **Como evitar:** use `psql -v ON_ERROR_STOP=1`.

## Importação parcial

- **Sintoma:** algumas tabelas existem e outras não.
- **Causa provável:** execução interrompida ou editor excedeu limite.
- **Como corrigir:** descarte o projeto de teste/incompleto quando permitido e repita em destino vazio com `psql`.
- **Como evitar:** interrompa no primeiro erro e valide contagens.

## Variável de ambiente ausente

- **Sintoma:** aplicação informa URL/chave indefinida.
- **Causa provável:** `.env` ausente, nome incorreto ou servidor não reiniciado.
- **Como corrigir:** compare com `.env.example`, preencha sem espaços indevidos e reinicie o processo.
- **Como evitar:** valide variáveis obrigatórias na inicialização sem imprimir valores.

## Conexão com Supabase falhando

- **Sintoma:** erro de rede, 401 ou projeto não encontrado.
- **Causa provável:** URL/chave de projetos diferentes, chave revogada, rede ou CORS/callback.
- **Como corrigir:** recopie URL e chave do mesmo ambiente e consulte logs do Supabase/aplicação.
- **Como evitar:** separe secrets por ambiente e faça teste após cada deploy.

## RLS bloqueando acesso

- **Sintoma:** consulta retorna vazio ou 401/403 embora existam dados.
- **Causa provável:** RLS habilitada sem policy aplicável ao papel/JWT.
- **Como corrigir:** teste com o papel real e revise `USING`/`WITH CHECK`; não desabilite RLS para contornar.
- **Como evitar:** mantenha testes de autorização para visitante, usuário e papéis administrativos.

## `service_role` exposta no frontend

- **Sintoma:** chave privilegiada aparece no bundle, DevTools ou repositório.
- **Causa provável:** variável pública ou uso direto no cliente.
- **Como corrigir:** rotacione/revogue imediatamente, mova a operação ao backend e investigue logs.
- **Como evitar:** jamais use prefixo público na chave e adote varredura de secrets.

## Confirmar se `schema.sql` foi gerado

- **Sintoma:** dúvida se o dump existe ou está vazio.
- **Causa provável:** comando falhou, caminho diferente ou arquivo antigo.
- **Como corrigir:** confira tamanho/data, início com cabeçalho de dump e fim com “database dump complete”; execute `node scripts/documentar-schema.js --check`.
- **Como evitar:** gere para `schema.novo.sql`, valide e só então promova.

## Localizar `pg_dump` no Windows

- **Sintoma:** não se sabe onde o executável foi instalado.
- **Causa provável:** múltiplas instalações ou `PATH` não configurado.
- **Como corrigir:** procure em `C:\Program Files\PostgreSQL\<versão>\bin\pg_dump.exe` ou use a pesquisa do Windows; confirme a versão pelo executável.
- **Como evitar:** registre a versão e configure o `PATH` da equipe.
