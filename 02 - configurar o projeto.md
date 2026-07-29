# Configurar o projeto

## Localizar URL e chaves

No painel do Supabase, abra as configurações do projeto e a seção de API. Os nomes do menu podem mudar; procure por **Project URL**, **Publishable/anon key** e **service_role/secret key**.

- **Project URL:** endereço público da API do projeto.
- **anon key:** usada pelo frontend. Ela identifica o projeto, mas não concede acesso irrestrito; as permissões dependem da autenticação, grants e RLS.
- **service role key:** credencial privilegiada que normalmente ignora RLS. Use somente em backend confiável, jobs ou servidor. Nunca a inclua no frontend, bundle, aplicativo móvel, log ou repositório.

Se uma `service_role` for exposta, revogue/rotacione a chave imediatamente, remova-a do histórico publicável e investigue acessos.

## Variáveis de ambiente

Exemplo sem valores:

```dotenv
NEXT_PUBLIC_SUPABASE_URL=
NEXT_PUBLIC_SUPABASE_ANON_KEY=
SUPABASE_SERVICE_ROLE_KEY=
DATABASE_URL=
```

Os prefixos `NEXT_PUBLIC_` tornam valores acessíveis ao navegador em aplicações Next.js; portanto, nunca os use na variável de `service_role`. `DATABASE_URL` deve ficar no servidor.

Procure na raiz do projeto da aplicação por `.env.example`, `.env.local.example`, documentação do framework e configuração de deploy. Arquivos `.env` reais podem estar ocultos e devem estar no `.gitignore`. Esta pasta de documentação não contém o código da aplicação nem `package.json`, então não foi possível confirmar framework, gerenciador ou scripts reais.

## Instalar e iniciar a aplicação

No projeto da aplicação, primeiro leia `package.json`. Use somente o gerenciador correspondente ao lockfile (`package-lock.json`, `pnpm-lock.yaml` ou `yarn.lock`) e apenas scripts presentes em `scripts`.

Exemplos condicionais — execute somente se existirem no `package.json`:

```powershell
npm install
npm run dev
```

Não assuma que os scripts se chamam `dev`, `start`, `build` ou `test`. Confirme os nomes reais.

## Validar a conexão

1. Inicie a aplicação no ambiente local.
2. Abra uma tela que faça uma leitura simples e não sensível.
3. Verifique no console/servidor se não há erro de URL, chave ou rede.
4. Teste deslogado e autenticado para confirmar o comportamento das policies.
5. Para rotinas administrativas, valide no backend e confirme que a chave privilegiada não foi enviada ao navegador.

Um `SELECT` vazio não significa necessariamente falha: RLS pode estar filtrando todas as linhas. Consulte os logs e teste a policy correta.

## Deploy sem plataforma específica

1. Faça o build local usando o script real.
2. Cadastre URL e `anon key` como variáveis públicas apenas quando o framework exigir.
3. Cadastre `service_role` e `DATABASE_URL` como secrets exclusivamente do runtime de backend.
4. Configure separadamente desenvolvimento, homologação e produção.
5. Nunca reutilize credenciais de produção em preview.
6. Defina URLs de callback/autenticação no Supabase de acordo com os domínios do ambiente.
7. Faça deploy, execute um teste básico e examine logs sem imprimir secrets.

## Checklist

- [ ] URL e chave pública apontam para o mesmo projeto.
- [ ] `service_role` existe apenas no backend.
- [ ] `.env` real não está versionado.
- [ ] Dependências e scripts foram confirmados no projeto da aplicação.
- [ ] Build e inicialização funcionam.
- [ ] Conexão foi testada como visitante e usuário autenticado.
- [ ] RLS foi validada, não desabilitada para contornar erros.
- [ ] Secrets do deploy estão separados por ambiente.
