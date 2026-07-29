# Documentação técnica do banco

## Índice

- [Visão geral](#visão-geral)
- [Ordem de criação e dependências](#ordem-de-criação-e-dependências)
- [Limitações do dump](#limitações-do-dump)
- [Regenerar o schema](#regenerar-o-schema)
- [Segurança e produção](#segurança-e-produção)
- [Inventário automático](#inventário-automático)

## Visão geral

O banco é PostgreSQL hospedado no Supabase e o dump documenta o schema principal `public`. O cabeçalho e o inventário automático registram as versões exatas do servidor de origem e do `pg_dump`.

Convenções observadas incluem nomes em `snake_case`, chaves frequentemente chamadas `id`, referências com sufixo `_id`, timestamps com sufixos como `_at`/`_em` e funções auxiliares/trigger com prefixos como `fn_`. São observações estruturais, não regras garantidas.

## Ordem de criação e dependências

Em termos gerais, o dump configura a sessão, cria `public`, tipos, funções necessárias, tabelas, views/sequences, constraints e chaves estrangeiras, índices, triggers, grants e políticas RLS. A ordem real do arquivo deve ser preservada porque objetos posteriores podem depender dos anteriores. Functions podem referenciar tabelas criadas mais adiante graças à configuração `check_function_bodies = false`; isso não elimina a necessidade dessas tabelas em tempo de execução.

## Limitações do dump

O arquivo foi gerado somente para a estrutura de `public` e não contém dados. Também não representa, por si só:

- usuários de `auth`;
- arquivos e buckets de `storage`;
- Edge Functions e seu código;
- secrets, senhas, tokens ou API keys;
- configurações externas do Supabase, provedores de autenticação e callbacks;
- configurações de rede, domínio, e-mail ou deploy;
- objetos de outros schemas, embora objetos de `public` possam referenciá-los.

Uma referência a `auth`, `storage` ou extensão não significa que sua definição esteja no dump. Projetos Supabase novos normalmente provisionam componentes gerenciados, mas dependências devem ser verificadas durante a restauração.

### Extensões e schemas externos referenciados

O dump não contém comandos `CREATE EXTENSION`, portanto não permite enumerar com segurança as extensões instaladas. O SQL usa as funções `unaccent(...)` e `gen_random_uuid()`; a primeira é normalmente fornecida pela extensão PostgreSQL `unaccent`, enquanto a origem efetiva deve ser confirmada no projeto. Há também referências explícitas a `auth.uid()` e a papéis Supabase (`anon`, `authenticated` e `service_role`). Essas referências são dependências, não definições incluídas no arquivo.

## Regenerar o schema

Depois de alterar e validar o banco, gere um arquivo temporário e revise o diff antes de substituir a versão oficial.

Com `pg_dump`:

```powershell
pg_dump "postgresql://USUARIO@HOST:5432/postgres?sslmode=require" --schema=public --schema-only --no-owner --no-privileges --file="database/schema.novo.sql"
```

Evite senha na linha de comando; permita o prompt ou use mecanismo seguro do PostgreSQL. Caracteres reservados em URL precisam de URL encoding.

Com Supabase CLI, conforme os comandos disponíveis na versão instalada:

```powershell
supabase db dump --linked --schema public --file database/schema.novo.sql
```

A CLI pode exigir login/vínculo do projeto e Docker Desktop em fluxos de banco local. Consulte `supabase --help` antes de executar e não confirme a substituição até revisar o diff.

## Segurança e produção

- Faça backup verificável antes de restaurar ou migrar produção.
- Teste o dump em projeto vazio e na mesma versão principal do PostgreSQL.
- Planeje indisponibilidade e rollback.
- Não desabilite RLS como solução permanente.
- Revise com atenção funções `SECURITY DEFINER`, `search_path`, grants e policies.
- Nunca publique `service_role`, URL com senha, dumps de dados ou arquivos `.env`.
- Use menor privilégio e credenciais distintas por ambiente.

<!-- AUTO-GENERATED:START -->
## Inventário automático

- PostgreSQL de origem: **17.6**
- pg_dump: **18.4**
- Tabelas: **228**
- Enums: **9**
- Views: **17**
- Materialized views: **0**
- Sequences explícitas: **25**
- Functions: **89**
- Procedures: **0**
- Triggers: **22**
- Índices: **314**
- Foreign keys: **317**
- Políticas RLS: **439**
- Tabelas com RLS habilitada: **207**

## Tipos ENUM

### checklist_area

Valores: `cozinha`, `bar`, `salao`, `higiene`, `geral`.

### checklist_turno

Valores: `abertura`, `almoco`, `jantar`, `fechamento`.

### conversation_status

Valores: `ativa`, `assumida`, `encerrada`.

### event_status

Valores: `rascunho`, `pendente_aprovacao`, `confirmado`, `aprovado`, `em_andamento`, `concluido`, `realizado`, `cancelado`.

### menu_item_category

Valores: `bar`, `cozinha`, `bebida_alcoolica`, `bebida_nao_alcoolica`, `entrada`, `prato_principal`, `sobremesa`, `outros`.

### purchase_order_status

Valores: `rascunho`, `enviado`, `parcial`, `recebido`, `cancelado`.

### quote_status

Valores: `rascunho`, `enviada`, `recebida`, `aprovada`, `cancelada`.

### reservation_origem

Valores: `whatsapp`, `telefone`, `email`, `tagme`, `presencial`, `instagram`.

### reservation_status

Valores: `pendente`, `confirmada`, `cancelada`, `no_show`, `finalizada`.

## Views
- `tips_records`
- `v_alertas`
- `v_aprovacoes_pendentes`
- `v_cadastro_saude`
- `v_cmv_produto`
- `v_despesa_canonica`
- `v_dre_canonico`
- `v_dre_consolidado`
- `v_eventos_kpi`
- `v_fonte_saude`
- `v_gorjeta_periodo_dia`
- `v_gorjeta_saude`
- `v_headcount_por_marca`
- `v_lorean_canonico`
- `v_proximos_eventos`
- `v_recrutamento_saude`
- `v_vagas_pipeline`

## Materialized views

Nenhuma identificada.

## Sequences
- `auditoria_nutricional_id_seq`
- `dre_contratos_fixos_id_seq`
- `dre_despesa_detalhada_id_seq`
- `dre_faturamento_historico_id_seq`
- `dre_folha_id_seq`
- `dre_gorjeta_mensal_id_seq`
- `dre_indicadores_id_seq`
- `dre_linhas_detalhadas_id_seq`
- `dre_manutencao_detalhada_id_seq`
- `dre_mensal_id_seq`
- `dre_pessoal_detalhado_id_seq`
- `dre_prestadores_id_seq`
- `dre_receita_detalhada_id_seq`
- `lorean_cancelamentos_detalhe_id_seq`
- `lorean_descontos_detalhe_id_seq`
- `lorean_produtos_dia_id_seq`
- `metas_dia_override_id_seq`
- `metas_dia_semana_id_seq`
- `metas_projecoes_id_seq`
- `notas_detalhadas_id_seq`
- `notas_nutri_id_seq`
- `produtos_relatorio_id_seq`
- `purchase_orders_numero_seq`
- `relatorio_produtos_id_seq`
- `vendas_diarias_id_seq`

## Functions

| Função | Retorno | Linguagem | SECURITY DEFINER |
|---|---|---|---|
| `_sync_employee_tier()` | `trigger` | `plpgsql` | Sim |
| `buscar_talentos(p_statuses text[], p_termo text DEFAULT NULL::text, p_cargo text DEFAULT NULL::text, p_cidade text DEFAULT NULL::text, p_escolaridade text DEFAULT NULL::text, p_habilidade text DEFAULT NULL::text, p_turno text DEFAULT NULL::text, p_limit integer DEFAULT 50, p_offset integer DEFAULT 0)` | `TABLE(id uuid, full_name text, area_interesse text, cidade text, escolaridade_nivel text, habilidades text[], cv_storage_path text, status text, origem text, created_at timestamp with time zone, total_count bigint)` | `sql` | Sim |
| `calculate_recipe_cost(p_menu_item_id uuid)` | `numeric` | `sql` | Não |
| `check_primo_acesso(p_cpf text)` | `json` | `sql` | Sim |
| `check_survey_response(p_employee_id uuid, p_survey_id uuid)` | `boolean` | `plpgsql` | Sim |
| `create_employee_auth(p_employee_id uuid, p_cpf text, p_password_hash text)` | `void` | `sql` | Sim |
| `create_punch_adjustment(p_employee_id uuid, p_data_referencia date, p_horario_saida_almoco time without time zone, p_horario_retorno_almoco time without time zone, p_motivo text)` | `uuid` | `plpgsql` | Sim |
| `events_set_updated_at()` | `trigger` | `plpgsql` | Não |
| `fn_ingredient_price_change()` | `trigger` | `plpgsql` | Não |
| `fn_oa_set_atualizado_em()` | `trigger` | `plpgsql` | Não |
| `fn_recalc_menu_item_custo()` | `trigger` | `plpgsql` | Não |
| `fn_recalc_status_prazo()` | `trigger` | `plpgsql` | Não |
| `fn_set_updated_at()` | `trigger` | `plpgsql` | Não |
| `fn_sync_qtd_alvo()` | `trigger` | `plpgsql` | Não |
| `get_active_campaigns()` | `json` | `sql` | Sim |
| `get_active_survey(p_unit_id uuid)` | `TABLE(survey_id uuid, titulo text, descricao text, tipo text, questions jsonb)` | `plpgsql` | Sim |
| `get_auth_by_cpf(p_cpf text)` | `json` | `sql` | Sim |
| `get_avaliacao(p_candidate_id uuid)` | `public.candidate_avaliacao` | `sql` | Sim |
| `get_cargo_salarios()` | `TABLE(id uuid, cargo_id uuid, cargo_nome text, setor text, grupo text, tem_nivel boolean, nivel integer, unit_id uuid, salario_min numeric, salario_ref numeric, salario_max numeric, observacao text)` | `sql` | Sim |
| `get_cargos()` | `TABLE(id uuid, nome text, setor text, grupo text, tem_nivel boolean)` | `sql` | Sim |
| `get_employee_profile(p_employee_id uuid)` | `json` | `sql` | Sim |
| `get_feedback_operacional(p_candidate_id uuid)` | `public.candidate_feedback_operacional` | `sql` | Sim |
| `get_gap_headcount(p_unit_id uuid)` | `TABLE(departamento text, cargo text, grupo text, qtd_alvo integer, headcount_atual integer, gap integer)` | `sql` | Sim |
| `get_my_adjustment_requests(p_employee_id uuid)` | `TABLE(id uuid, data_referencia date, horario_saida_almoco text, horario_retorno_almoco text, motivo text, status text, created_at text)` | `plpgsql` | Sim |
| `get_my_dept()` | `text` | `sql` | Sim |
| `get_my_development(p_employee_id uuid)` | `json` | `sql` | Sim |
| `get_my_documents(p_employee_id uuid)` | `json` | `sql` | Sim |
| `get_my_gorjetas(p_employee_id uuid)` | `json` | `sql` | Sim |
| `get_my_home(p_employee_id uuid)` | `json` | `sql` | Sim |
| `get_my_hour_bank(p_employee_id uuid)` | `json` | `sql` | Sim |
| `get_my_last_punch(p_employee_id uuid)` | `json` | `sql` | Sim |
| `get_my_level()` | `text` | `sql` | Sim |
| `get_my_payments(p_employee_id uuid)` | `json` | `sql` | Sim |
| `get_my_payslips(p_employee_id uuid)` | `json` | `sql` | Sim |
| `get_my_punch_history(p_employee_id uuid, p_days integer DEFAULT 30)` | `TABLE(dia date, punches jsonb)` | `plpgsql` | Sim |
| `get_my_punches_today(p_employee_id uuid)` | `TABLE(id uuid, tipo text, timestamp_punch timestamp with time zone)` | `sql` | Sim |
| `get_my_registro(p_employee_id uuid)` | `json` | `sql` | Sim |
| `get_my_role()` | `text` | `sql` | Sim |
| `get_my_sector()` | `text` | `sql` | Sim |
| `get_my_tier()` | `text` | `sql` | Sim |
| `get_my_tier_real()` | `text` | `sql` | Sim |
| `get_my_unit()` | `uuid` | `sql` | Sim |
| `get_my_vacations(p_employee_id uuid)` | `json` | `sql` | Sim |
| `get_organograma()` | `TABLE(id uuid, nome text, setor text, grupo text, reporta_a_cargo_id uuid, ordem_hierarquia integer)` | `sql` | Sim |
| `get_produto_meses(p_unit_id uuid)` | `TABLE(mes integer, ano integer, total bigint)` | `sql` | Não |
| `get_punches_by_unit(p_unit_id uuid, p_date date)` | `TABLE(employee_id uuid, nome_completo text, funcao text, unit_id uuid, tipo text, registrado_em timestamp with time zone, gps_failed boolean)` | `sql` | Sim |
| `get_quadro_completo(p_unit_id uuid)` | `TABLE(id uuid, cargo_id uuid, cargo_nome text, setor text, grupo text, tem_nivel boolean, alvo_manha integer, alvo_tarde integer, alvo_noite integer, alvo_madrugada integer, alvo_intermediario integer, qtd_alvo integer, headcount_atual integer, gap integer, reporta_a_cargo_id uuid, reporta_a_nome text)` | `sql` | Sim |
| `get_quadro_ideal(p_unit_id uuid)` | `TABLE(id uuid, unit_id uuid, departamento text, cargo text, cargo_grupo_nome text, qtd_alvo integer, vigente_desde date, vigente_ate date)` | `sql` | Sim |
| `get_survey_results(p_survey_id uuid)` | `TABLE(question_id uuid, texto_pergunta text, total_respostas integer, media_escala numeric, distribuicao jsonb)` | `plpgsql` | Sim |
| `get_unit_geofence(p_unit_id uuid)` | `TABLE(latitude double precision, longitude double precision, radius_meters integer)` | `plpgsql` | Sim |
| `get_unit_surveys(p_unit_id uuid, p_employee_id uuid)` | `json` | `sql` | Sim |
| `handle_new_user()` | `trigger` | `plpgsql` | Sim |
| `insert_document(p_employee_id uuid, p_unit_id uuid, p_name text, p_type text, p_storage_path text)` | `json` | `sql` | Sim |
| `insert_punch(p_employee_id uuid, p_tipo text, p_timestamp timestamp with time zone, p_latitude double precision, p_longitude double precision, p_device_info text)` | `json` | `sql` | Sim |
| `insert_punch(p_employee_id uuid, p_tipo text, p_timestamp timestamp with time zone, p_latitude double precision, p_longitude double precision, p_device_info text, p_aprovado boolean DEFAULT true, p_distance_meters integer DEFAULT NULL::integer, p_gps_failed boolean DEFAULT false)` | `json` | `sql` | Sim |
| `kph_accessible_unit_ids()` | `SETOF uuid` | `sql` | Sim |
| `kph_can_delete_event_brand(p_brand_id uuid)` | `boolean` | `sql` | Sim |
| `kph_can_write_event_brand(p_brand_id uuid)` | `boolean` | `sql` | Sim |
| `kph_has_role_for_brand(p_brand_id uuid)` | `boolean` | `sql` | Sim |
| `kph_has_role_for_group(p_group_id uuid)` | `boolean` | `sql` | Sim |
| `kph_has_role_for_unit(p_unit_id uuid)` | `boolean` | `sql` | Sim |
| `kph_is_founder()` | `boolean` | `sql` | Sim |
| `kph_is_founder_or_cfo()` | `boolean` | `sql` | Sim |
| `norm_fone_br(p text)` | `text` | `sql` | Não |
| `payroll_cc_fopag(p_departamento text, p_cargo text)` | `text` | `sql` | Não |
| `payroll_competencia_mes_ano(p_competencia text)` | `TABLE(mes integer, ano integer)` | `plpgsql` | Não |
| `payroll_interval_to_decimal_br(v interval)` | `text` | `sql` | Não |
| `payroll_num_to_br(v numeric)` | `text` | `sql` | Não |
| `payroll_parse_hhmm(v text)` | `interval` | `sql` | Não |
| `recalc_purchase_order_total()` | `trigger` | `plpgsql` | Não |
| `resolve_punch_adjustment(p_request_id uuid, p_aprovado_por uuid, p_status text, p_inserir_punches boolean DEFAULT true)` | `void` | `plpgsql` | Sim |
| `rpc_payroll_coletar_periodo(p_unit_id uuid, p_competencia text)` | `jsonb` | `plpgsql` | Sim |
| `rpc_payroll_espelho_fopag(p_periodo_id uuid)` | `TABLE(employee_id uuid, cod_folha text, regime text, cc text, nome text, cargo text, admissao text, salario numeric, gorjeta_1q numeric, gorjeta_2q numeric, gorjeta_compulsoria numeric, adicional_noturno text, bonus numeric, quitacao_bh numeric, feriado numeric, emprestimo numeric, falta numeric, dsr numeric, plano_dependente numeric, coopart_plano numeric, desconto_vt text, liquido numeric, total_liquido numeric)` | `plpgsql` | Sim |
| `rpc_payroll_gerar_txt_dominio(p_periodo_id uuid, p_cod_empresa text DEFAULT '567'::text, p_tipo_registro text DEFAULT '10'::text)` | `jsonb` | `plpgsql` | Sim |
| `rpc_payroll_listar_fechamento(p_periodo_id uuid)` | `TABLE(employee_id uuid, nome text, cod_folha text, cod_kph text, descricao_rubrica text, grupo text, tipo_rubrica text, valor numeric, valor_horas text, origem_lancamento text, unidade_rubrica text)` | `plpgsql` | Sim |
| `rpc_payroll_listar_periodos(p_unit_id uuid)` | `TABLE(periodo_id uuid, competencia text, status text, custo_total_folha numeric, colabs bigint)` | `sql` | Sim |
| `rpc_payroll_txt_pendencias(p_periodo_id uuid)` | `TABLE(motivo text, nome text, cod_folha text, cod_kph text, descricao text, valor numeric)` | `sql` | Sim |
| `rpc_payroll_upsert_lancamento_manual(p_periodo_id uuid, p_employee_id uuid, p_cod_kph text, p_valor numeric DEFAULT NULL::numeric, p_valor_horas text DEFAULT NULL::text, p_observacao text DEFAULT NULL::text)` | `jsonb` | `plpgsql` | Sim |
| `set_updated_at()` | `trigger` | `plpgsql` | Não |
| `submit_survey_responses(p_responses json)` | `void` | `plpgsql` | Sim |
| `submit_survey_responses(p_employee_id uuid, p_survey_id uuid, p_responses jsonb)` | `void` | `plpgsql` | Sim |
| `update_employee_photo(p_employee_id uuid, p_photo_url text)` | `void` | `sql` | Sim |
| `update_updated_at()` | `trigger` | `plpgsql` | Não |
| `update_updated_at_column()` | `trigger` | `plpgsql` | Não |
| `upsert_avaliacao(p_candidate_id uuid, p_aderencia numeric, p_experiencia numeric, p_tec numeric, p_comp numeric, p_aderencia_ia boolean, p_experiencia_ia boolean)` | `public.candidate_avaliacao` | `plpgsql` | Sim |
| `upsert_cargo_salario(p_id uuid, p_salario_min numeric, p_salario_ref numeric, p_salario_max numeric, p_observacao text DEFAULT NULL::text)` | `public.cargo_salarios` | `plpgsql` | Sim |
| `upsert_feedback_operacional(p_candidate_id uuid, p_agendamento_id uuid, p_postura numeric, p_ritmo numeric, p_dominio numeric, p_higiene numeric, p_equipe numeric, p_parecer text)` | `public.candidate_feedback_operacional` | `plpgsql` | Sim |
| `upsert_feedback_operacional(p_candidate_id uuid, p_agendamento_id uuid DEFAULT NULL::uuid, p_postura numeric DEFAULT NULL::numeric, p_ritmo numeric DEFAULT NULL::numeric, p_dominio numeric DEFAULT NULL::numeric, p_higiene numeric DEFAULT NULL::numeric, p_equipe numeric DEFAULT NULL::numeric, p_parecer text DEFAULT NULL::text, p_avaliador_id uuid DEFAULT NULL::uuid)` | `public.candidate_feedback_operacional` | `plpgsql` | Sim |
| `upsert_push_token(p_employee_id uuid, p_token text)` | `void` | `plpgsql` | Sim |

## Procedures

Nenhuma procedure identificada.

## Triggers
- `candidates.candidates_updated_at` — `BEFORE UPDATE FOR EACH ROW EXECUTE FUNCTION public.set_updated_at()`
- `pdis.pdis_updated_at` — `BEFORE UPDATE FOR EACH ROW EXECUTE FUNCTION public.set_updated_at()`
- `hos_runs.runs_updated_at` — `BEFORE UPDATE FOR EACH ROW EXECUTE FUNCTION public.update_updated_at()`
- `brand_targets.trg_brand_targets_updated_at` — `BEFORE UPDATE FOR EACH ROW EXECUTE FUNCTION public.update_updated_at_column()`
- `clients.trg_clients_updated_at` — `BEFORE UPDATE FOR EACH ROW EXECUTE FUNCTION public.update_updated_at_column()`
- `events.trg_events_updated_at` — `BEFORE UPDATE FOR EACH ROW EXECUTE FUNCTION public.events_set_updated_at()`
- `gorjeta_cargo_pontos.trg_gorjeta_cargo_pontos_updated_at` — `BEFORE UPDATE FOR EACH ROW EXECUTE FUNCTION public.fn_set_updated_at()`
- `gorjeta_periodos.trg_gorjeta_periodos_updated_at` — `BEFORE UPDATE FOR EACH ROW EXECUTE FUNCTION public.fn_set_updated_at()`
- `ingredients.trg_ingredient_price_change` — `AFTER UPDATE FOR EACH ROW EXECUTE FUNCTION public.fn_ingredient_price_change()`
- `job_openings.trg_job_openings_status_prazo` — `BEFORE INSERT OR UPDATE FOR EACH ROW EXECUTE FUNCTION public.fn_recalc_status_prazo()`
- `manutencao_aprovacoes.trg_mnt_aprov_updated` — `BEFORE UPDATE FOR EACH ROW EXECUTE FUNCTION public.set_updated_at()`
- `manutencao_chamados.trg_mnt_chamados_updated` — `BEFORE UPDATE FOR EACH ROW EXECUTE FUNCTION public.set_updated_at()`
- `orkestri_achados.trg_oa_atualizado` — `BEFORE UPDATE FOR EACH ROW EXECUTE FUNCTION public.fn_oa_set_atualizado_em()`
- `performance_reviews.trg_performance_reviews_updated_at` — `BEFORE UPDATE FOR EACH ROW EXECUTE FUNCTION public.update_updated_at_column()`
- `performance_templates.trg_performance_templates_updated_at` — `BEFORE UPDATE FOR EACH ROW EXECUTE FUNCTION public.update_updated_at_column()`
- `purchase_orders.trg_purchase_orders_updated_at` — `BEFORE UPDATE FOR EACH ROW EXECUTE FUNCTION public.update_updated_at_column()`
- `purchase_order_items.trg_recalc_po_total_iud` — `AFTER INSERT OR DELETE OR UPDATE FOR EACH ROW EXECUTE FUNCTION public.recalc_purchase_order_total()`
- `recipe_items.trg_recipe_items_recalc` — `AFTER INSERT OR DELETE OR UPDATE FOR EACH ROW EXECUTE FUNCTION public.fn_recalc_menu_item_custo()`
- `employees.trg_sync_employee_tier` — `BEFORE INSERT OR UPDATE OF role_id FOR EACH ROW EXECUTE FUNCTION public._sync_employee_tier()`
- `quadro_ideal.trg_sync_qtd_alvo` — `BEFORE INSERT OR UPDATE FOR EACH ROW EXECUTE FUNCTION public.fn_sync_qtd_alvo()`
- `training_records.trg_training_records_updated_at` — `BEFORE UPDATE FOR EACH ROW EXECUTE FUNCTION public.update_updated_at_column()`
- `training_templates.trg_training_templates_updated_at` — `BEFORE UPDATE FOR EACH ROW EXECUTE FUNCTION public.update_updated_at_column()`

## Índices
- `access_requests.access_requests_employee_idx` — `USING btree (employee_id)`
- `access_requests.access_requests_status_idx` — `USING btree (status, approver_tier)`
- `reuniao_action_items.action_items_reuniao` — `USING btree (reuniao_id)`
- `agent_conversations.agent_conversations_agent_phone` — `USING btree (agent, phone)`
- `agent_metrics.agent_metrics_agent_created` — `USING btree (agent, created_at DESC)`
- `agent_runs.agent_runs_agent_name_idx` — `USING btree (agent_name)`
- `agent_runs.agent_runs_created_at_idx` — `USING btree (created_at DESC)`
- `agent_runs.agent_runs_week_idx` — `USING btree (year, week_number)`
- `candidates.candidates_phone_unique` — `USING btree (phone)`
- `checklist_records.checklist_records_checklist_idx` — `USING btree (checklist_id)`
- `checklist_records.checklist_records_unit_data_idx` — `USING btree (unit_id, data)`
- `contractors.contractors_responsavel_sem_cnpj` — `USING btree (responsavel) WHERE (cnpj IS NULL)`
- `documents.documents_employee_id_idx` — `USING btree (employee_id)`
- `employee_availability.employee_availability_unit_data_idx` — `USING btree (unit_id, data)`
- `employees.employees_manager` — `USING btree (manager_id)`
- `feedbacks.feedbacks_para_employee` — `USING btree (para_employee_id)`
- `feedbacks.feedbacks_unit` — `USING btree (unit_id)`
- `gorjeta_distribuicao.gorjeta_distribuicao_employee_idx` — `USING btree (employee_id)`
- `gorjeta_distribuicao.gorjeta_distribuicao_unit_period_idx` — `USING btree (unit_id, mes, ano)`
- `hos_runs.hos_runs_active_idx` — `USING btree (created_at DESC) WHERE (archived_at IS NULL)`
- `hos_runs.hos_runs_deployment_id_job_idx` — `USING btree (deployment_id, job_id) WHERE (deployment_id IS NOT NULL)`
- `hos_runs.hos_runs_employee_id_idx` — `USING btree (employee_id)`
- `absences.idx_absences_employee` — `USING btree (employee_id, data DESC)`
- `reuniao_action_items.idx_action_items_reuniao` — `USING btree (reuniao_id)`
- `candidate_agendamentos.idx_agendamentos_candidate_tipo` — `USING btree (candidate_id, tipo)`
- `candidate_agendamentos.idx_agendamentos_data_hora` — `USING btree (data_hora)`
- `agent_conversations.idx_agent_conversations_agent_status` — `USING btree (agent, status, last_activity DESC)`
- `agent_conversations.idx_agent_conversations_last_activity` — `USING btree (last_activity DESC)`
- `agent_prompt_versions.idx_agent_prompt_versions_agent` — `USING btree (agent)`
- `agent_prompt_versions.idx_agent_prompt_versions_ativo` — `USING btree (agent, ativo)`
- `contratos_arquivos.idx_arquivos_contrato` — `USING btree (contrato_id)`
- `audit_log.idx_audit_resource` — `USING btree (resource, resource_id)`
- `audit_log.idx_audit_user` — `USING btree (user_id, created_at DESC)`
- `avaliacao_ciclos.idx_av_ciclos_unit` — `USING btree (unit_id)`
- `avaliacao_participantes.idx_av_part_avaliado` — `USING btree (avaliado_id)`
- `avaliacao_participantes.idx_av_part_ciclo` — `USING btree (ciclo_id)`
- `brand_links.idx_brand_links_brand` — `USING btree (brand_id, ordem)`
- `brand_targets.idx_brand_targets_brand` — `USING btree (brand_id)`
- `brand_targets.idx_brand_targets_periodo` — `USING btree (periodo)`
- `brand_targets.idx_brand_targets_unit` — `USING btree (unit_id)`
- `brands.idx_brands_group` — `USING btree (group_id)`
- `campaigns.idx_campaigns_active` — `USING btree (active, starts_at, ends_at)`
- `campaigns.idx_campaigns_brand` — `USING btree (brand_id)`
- `lorean_cancelamentos_detalhe.idx_cancel_det_wd` — `USING btree (workday_id_fk)`
- `candidate_agendamentos.idx_cand_agend_cand_tipo` — `USING btree (candidate_id, tipo)`
- `candidate_agendamentos.idx_cand_agend_data` — `USING btree (data_hora)`
- `candidates.idx_candidates_access_code` — `USING btree (access_code)`
- `candidates.idx_candidates_cidade` — `USING btree (cidade) WHERE (cidade IS NOT NULL)`
- `candidates.idx_candidates_escolaridade` — `USING btree (escolaridade_nivel) WHERE (escolaridade_nivel IS NOT NULL)`
- `candidates.idx_candidates_job_opening` — `USING btree (job_opening_id)`
- `candidates.idx_candidates_opening` — `USING btree (job_opening_id)`
- `candidates.idx_candidates_origem` — `USING btree (origem)`
- `candidates.idx_candidates_pretensao` — `USING btree (pretensao_salarial) WHERE (pretensao_salarial IS NOT NULL)`
- `candidates.idx_candidates_status` — `USING btree (status)`
- `candidates.idx_candidates_unit` — `USING btree (unit_id)`
- `candidates.idx_candidates_welcome_sid` — `USING btree (welcome_message_sid) WHERE (welcome_message_sid IS NOT NULL)`
- `candidatos_maya.idx_candidatos_maya_status` — `USING btree (status)`
- `candidatos_maya.idx_candidatos_maya_telefone` — `USING btree (telefone)`
- `client_interactions.idx_client_interactions_cli` — `USING btree (client_id, data DESC)`
- `clients.idx_clients_ativo` — `USING btree (ativo)`
- `clients.idx_clients_brand` — `USING btree (brand_id)`
- `clients.idx_clients_created_at` — `USING btree (created_at DESC)`
- `clients.idx_clients_origem` — `USING btree (origem)`
- `clients.idx_clients_unit` — `USING btree (unit_id)`
- `contatos_kph.idx_contatos_kph_candidate` — `USING btree (candidate_id)`
- `contatos_kph.idx_contatos_kph_employee` — `USING btree (employee_id)`
- `contatos_kph.idx_contatos_kph_telefone` — `USING btree (telefone)`
- `contatos_kph.idx_contatos_kph_tipo` — `USING btree (tipo)`
- `contratos.idx_contratos_fim` — `USING btree (data_fim)`
- `contratos.idx_contratos_unit` — `USING btree (unit_id)`
- `dependents.idx_dependents_employee` — `USING btree (employee_id)`
- `lorean_descontos_detalhe.idx_descontos_det_wd` — `USING btree (workday_id_fk)`
- `documents.idx_documents_employee` — `USING btree (employee_id)`
- `documents.idx_documents_type` — `USING btree (type)`
- `dre_contratos_fixos.idx_dre_contratos_unit_id` — `USING btree (unit_id)`
- `dre_despesa_detalhada.idx_dre_despesa_cls` — `USING btree (classificacao_dre)`
- `dre_despesa_detalhada.idx_dre_despesa_det_unit_id` — `USING btree (unit_id)`
- `dre_despesa_detalhada.idx_dre_despesa_mes` — `USING btree (mes_ano)`
- `dre_despesa_detalhada.idx_dre_despesa_tipo` — `USING btree (tipo_despesa)`
- `dre_folha.idx_dre_folha_competencia` — `USING btree (unit_id, competencia)`
- `dre_folha.idx_dre_folha_unit_id` — `USING btree (unit_id)`
- `dre_gorjeta_mensal.idx_dre_gorjeta_unit_id` — `USING btree (unit_id)`
- `dre_faturamento_historico.idx_dre_historico_unit_id` — `USING btree (unit_id)`
- `dre_indicadores.idx_dre_indicadores_unit_id` — `USING btree (unit_id)`
- `dre_kpis_mensais.idx_dre_kpis_unit_id` — `USING btree (unit_id)`
- `dre_linhas_detalhadas.idx_dre_linhas_det_unit_id` — `USING btree (unit_id)`
- `dre_manutencao_detalhada.idx_dre_manutencao_det_unit_id` — `USING btree (unit_id)`
- `dre_mensal.idx_dre_mensal_unit_id` — `USING btree (unit_id)`
- `dre_pessoal_detalhado.idx_dre_pessoal_det_unit_id` — `USING btree (unit_id)`
- `dre_prestadores.idx_dre_prestadores_unit_id` — `USING btree (unit_id)`
- `dre_receita_detalhada.idx_dre_receita_det_unit_id` — `USING btree (unit_id)`
- `employee_codigos_dominio.idx_ecd_folha` — `USING btree (cod_folha)`
- `employee_codigos_dominio.idx_ecd_unit` — `USING btree (unit_id)`
- `employee_documents.idx_emp_docs_employee` — `USING btree (employee_id)`
- `employee_documents.idx_emp_docs_tipo` — `USING btree (tipo)`
- `employee_documents.idx_emp_docs_validade` — `USING btree (data_validade) WHERE (data_validade IS NOT NULL)`
- `employee_auth.idx_employee_auth_cpf` — `USING btree (cpf)`
- `employee_auth.idx_employee_auth_employee` — `USING btree (employee_id)`
- `employees.idx_employees_employee_code` — `USING btree (employee_code)`
- `employees.idx_employees_score` — `USING btree (score DESC)`
- `employees.idx_employees_status_rh` — `USING btree (status_rh)`
- `employees.idx_employees_unit` — `USING btree (unit_id)`
- `event_attachments.idx_event_attachments_event_id` — `USING btree (event_id)`
- `event_infra_items.idx_event_infra_items_event_id` — `USING btree (event_id)`
- `event_menu_items.idx_event_menu_items_event_id` — `USING btree (event_id)`
- `event_staff.idx_event_staff_event_id` — `USING btree (event_id)`
- `event_status_log.idx_event_status_log_event_id` — `USING btree (event_id, created_at DESC)`
- `events.idx_events_brand_id` — `USING btree (brand_id)`
- `events.idx_events_data_inicio` — `USING btree (data_inicio DESC)`
- `events.idx_events_status` — `USING btree (status)`
- `events.idx_events_unit_id` — `USING btree (unit_id)`
- `feedback.idx_feedback_created` — `USING btree (created_at DESC)`
- `feedback.idx_feedback_status` — `USING btree (status)`
- `feedback.idx_feedback_user` — `USING btree (user_id)`
- `feedbacks.idx_feedbacks_de` — `USING btree (de_employee_id)`
- `feedbacks.idx_feedbacks_para` — `USING btree (para_employee_id)`
- `feedbacks.idx_feedbacks_unit` — `USING btree (unit_id)`
- `gorjeta_dias.idx_gorjeta_dias_employee` — `USING btree (employee_id)`
- `gorjeta_dias.idx_gorjeta_dias_periodo` — `USING btree (periodo_id)`
- `gorjeta_dias.idx_gorjeta_dias_unit_data` — `USING btree (unit_id, data)`
- `gorjeta_distribuicao.idx_gorjeta_periodo_emp` — `USING btree (unit_id, periodo)`
- `gorjeta_periodos.idx_gorjeta_periodos_unit_data` — `USING btree (unit_id, data)`
- `gorjeta_distribuicao.idx_gorjeta_recibo_pendente` — `USING btree (unit_id, mes, ano) WHERE (recibo_gerado_at IS NULL)`
- `hos_insights.idx_hos_insights_created_at` — `USING btree (created_at DESC)`
- `hos_jobs.idx_hos_jobs_unit` — `USING btree (unit_id)`
- `ingredient_stock.idx_ingredient_stock_unit` — `USING btree (unit_id, ingredient_id)`
- `ingredients.idx_ingredients_ativo` — `USING btree (ativo) WHERE (ativo = true)`
- `ingredients.idx_ingredients_categoria` — `USING btree (categoria)`
- `ingredients.idx_ingredients_codigo_group` — `USING btree (group_id, codigo) WHERE (codigo IS NOT NULL)`
- `ingredients.idx_ingredients_group` — `USING btree (group_id)`
- `kph_intelligence_scores.idx_intelligence_score_semana` — `USING btree (semana DESC)`
- `interviews.idx_interviews_candidate` — `USING btree (candidate_id)`
- `interviews.idx_interviews_data` — `USING btree (data_entrevista DESC)`
- `job_descriptions.idx_job_descriptions_brand_status` — `USING btree (brand_id, status, created_at DESC)`
- `job_opening_logs.idx_job_opening_logs_opening` — `USING btree (opening_id)`
- `job_openings.idx_job_openings_ativas` — `USING btree (unit_id, status) WHERE ((congelada = false) AND (cancelada = false))`
- `job_openings.idx_job_openings_cargo_grupo` — `USING btree (cargo_grupo_id)`
- `job_requisitions.idx_job_requisitions_status` — `USING btree (status)`
- `kph_intelligence_scores.idx_kis_modulo` — `USING btree (modulo)`
- `kph_learning_proposals.idx_klp_modulo_sev_pending` — `USING btree (modulo, severidade) WHERE (status = 'pending'::text)`
- `kph_alerts.idx_kph_alerts_created` — `USING btree (created_at DESC)`
- `kph_alerts.idx_kph_alerts_entidade_id` — `USING btree (entidade_id)`
- `kph_alerts.idx_kph_alerts_prioridade` — `USING btree (prioridade)`
- `kph_alerts.idx_kph_alerts_resolvido` — `USING btree (resolvido)`
- `kph_insights.idx_kph_insights_aprovado` — `USING btree (aprovado)`
- `kph_insights.idx_kph_insights_modulo` — `USING btree (modulo)`
- `kph_insights.idx_kph_insights_semana` — `USING btree (semana DESC)`
- `kph_learning_proposals.idx_kph_learning_proposals_created_at` — `USING btree (created_at DESC)`
- `kph_learning_proposals.idx_kph_learning_proposals_modulo_status` — `USING btree (modulo, status)`
- `dre_manutencao_detalhada.idx_manutencao_mes` — `USING btree (mes_ano)`
- `menu_items.idx_menu_items_ativo` — `USING btree (ativo) WHERE (ativo = true)`
- `menu_items.idx_menu_items_brand` — `USING btree (brand_id)`
- `menu_items.idx_menu_items_categoria` — `USING btree (categoria)`
- `menu_items.idx_menu_items_unit` — `USING btree (unit_id) WHERE (unit_id IS NOT NULL)`
- `manutencao_aprovacoes.idx_mnt_aprov_chamado` — `USING btree (chamado_id)`
- `manutencao_aprovacoes.idx_mnt_aprov_status` — `USING btree (unit_id, aprovado)`
- `manutencao_aprovacoes.idx_mnt_aprov_unit` — `USING btree (unit_id, data_solicitacao DESC)`
- `manutencao_chamados.idx_mnt_chamados_categoria` — `USING btree (unit_id, categoria)`
- `manutencao_chamados.idx_mnt_chamados_status` — `USING btree (unit_id, status)`
- `manutencao_chamados.idx_mnt_chamados_unit` — `USING btree (unit_id, data_solicitacao DESC)`
- `manutencao_parcelas.idx_mnt_parcelas_aprov` — `USING btree (aprovacao_id, numero)`
- `manutencao_parcelas.idx_mnt_parcelas_competencia` — `USING btree (competencia, pago)`
- `movimentacoes_rh.idx_movimentacoes_rh_data` — `USING btree (data_movimentacao DESC)`
- `movimentacoes_rh.idx_movimentacoes_rh_employee` — `USING btree (employee_id)`
- `movimentacoes_rh.idx_movimentacoes_rh_tipo` — `USING btree (tipo)`
- `movimentacoes_rh.idx_movimentacoes_rh_unidade` — `USING btree (unidade_id)`
- `notifications.idx_notifications_user_created` — `USING btree (user_id, created_at DESC)`
- `notifications.idx_notifications_user_lida` — `USING btree (user_id, lida, created_at DESC)`
- `orkestri_achados.idx_oa_auditor` — `USING btree (auditor)`
- `orkestri_achados.idx_oa_created` — `USING btree (created_at DESC)`
- `orkestri_achados.idx_oa_marca` — `USING btree (marca)`
- `orkestri_achados.idx_oa_severidade` — `USING btree (severidade)`
- `orkestri_achados.idx_oa_status` — `USING btree (status)`
- `orkestri_achados.idx_oa_unit_status` — `USING btree (unit_id, status)`
- `onboarding_checklist.idx_ob_checklist_run` — `USING btree (run_id)`
- `onboarding_runs.idx_ob_runs_employee` — `USING btree (employee_id)`
- `onboarding_runs.idx_ob_runs_unit` — `USING btree (unit_id)`
- `onboarding_tarefas.idx_ob_tarefas_template` — `USING btree (template_id, ordem)`
- `onboarding_templates.idx_ob_templates_unit` — `USING btree (unit_id)`
- `overtime_records.idx_overtime_employee_periodo` — `USING btree (employee_id, periodo)`
- `page_views.idx_page_views_path` — `USING btree (path)`
- `page_views.idx_page_views_user` — `USING btree (user_id)`
- `page_views.idx_page_views_visited` — `USING btree (visited_at DESC)`
- `punch_adjustment_requests.idx_par_employee_data` — `USING btree (employee_id, data_referencia)`
- `punch_adjustment_requests.idx_par_status` — `USING btree (status)`
- `payslips.idx_payslips_employee` — `USING btree (employee_id, competencia DESC)`
- `payslips.idx_payslips_employee_code` — `USING btree (employee_code)`
- `pdi_metas.idx_pdi_metas_pdi` — `USING btree (pdi_id)`
- `pdis.idx_pdis_employee` — `USING btree (employee_id)`
- `pdis.idx_pdis_unit` — `USING btree (unit_id)`
- `performance_reviews.idx_perf_reviews_employee` — `USING btree (employee_id)`
- `performance_reviews.idx_perf_reviews_template` — `USING btree (template_id)`
- `performance_templates.idx_perf_templates_brand` — `USING btree (brand_id)`
- `performance_reviews.idx_performance_reviews_avaliador` — `USING btree (avaliador_id)`
- `performance_reviews.idx_performance_reviews_data` — `USING btree (data_avaliacao DESC)`
- `performance_reviews.idx_performance_reviews_employee` — `USING btree (employee_id)`
- `performance_reviews.idx_performance_reviews_periodo` — `USING btree (periodo)`
- `performance_reviews.idx_performance_reviews_status` — `USING btree (status)`
- `performance_reviews.idx_performance_reviews_template` — `USING btree (template_id)`
- `performance_templates.idx_performance_templates_ativo` — `USING btree (ativo)`
- `performance_templates.idx_performance_templates_brand` — `USING btree (brand_id)`
- `performance_templates.idx_performance_templates_funcao` — `USING btree (funcao)`
- `performance_templates.idx_performance_templates_unit` — `USING btree (unit_id)`
- `payroll_fechamento_linha.idx_pfl_employee` — `USING btree (employee_id)`
- `payroll_fechamento_linha.idx_pfl_periodo` — `USING btree (periodo_id)`
- `payroll_fechamento_periodo.idx_pfp_unit_comp` — `USING btree (unit_id, competencia)`
- `candidate_pipeline.idx_pipeline_autor_id` — `USING btree (autor_id)`
- `candidate_pipeline.idx_pipeline_candidate` — `USING btree (candidate_id)`
- `candidate_pipeline.idx_pipeline_created_at` — `USING btree (created_at DESC)`
- `candidate_pipeline.idx_pipeline_etapa` — `USING btree (etapa)`
- `candidate_pipeline.idx_pipeline_para_status` — `USING btree (para_status)`
- `produtos_relatorio.idx_pr_categoria` — `USING btree (unit_id, desc_gerencial)`
- `produtos_relatorio.idx_pr_unit_mes` — `USING btree (unit_id, ano_lancamento, mes_lancamento)`
- `dre_prestadores.idx_prestadores_mes` — `USING btree (mes_ano)`
- `ingredient_price_history.idx_price_history_ingredient` — `USING btree (ingredient_id, created_at DESC)`
- `lorean_produtos_dia.idx_produtos_dia_wd` — `USING btree (workday_id_fk)`
- `time_clock_punches.idx_punches_employee` — `USING btree (employee_id, timestamp_punch DESC)`
- `purchase_invoice_items.idx_purchase_invoice_items_codigo` — `USING btree (ingredient_codigo)`
- `purchase_invoice_items.idx_purchase_invoice_items_ingredient` — `USING btree (ingredient_id) WHERE (ingredient_id IS NOT NULL)`
- `purchase_invoice_items.idx_purchase_invoice_items_invoice` — `USING btree (purchase_invoice_id)`
- `purchase_invoices.idx_purchase_invoices_data_emissao` — `USING btree (data_emissao DESC)`
- `purchase_invoices.idx_purchase_invoices_mes_referencia` — `USING btree (mes_referencia)`
- `purchase_invoices.idx_purchase_invoices_unit` — `USING btree (unit_id)`
- `purchase_order_items.idx_purchase_order_items_order` — `USING btree (order_id)`
- `purchase_orders.idx_purchase_orders_brand` — `USING btree (brand_id)`
- `purchase_orders.idx_purchase_orders_data_pedido` — `USING btree (data_pedido DESC)`
- `purchase_orders.idx_purchase_orders_status` — `USING btree (status)`
- `purchase_orders.idx_purchase_orders_unit` — `USING btree (unit_id)`
- `quadro_ideal.idx_quadro_ideal_unit_vigente` — `USING btree (unit_id) WHERE (vigente_ate IS NULL)`
- `quadro_ideal.idx_quadro_unit_cargo_ativo` — `USING btree (unit_id, cargo_id) WHERE ((vigente_ate IS NULL) AND (cargo_id IS NOT NULL))`
- `interview_questions.idx_questions_job_order` — `USING btree (job_opening_id, order_num)`
- `recebimento_itens.idx_recebimento_itens_recebimento` — `USING btree (recebimento_id)`
- `recebimentos.idx_recebimentos_pedido` — `USING btree (pedido_id)`
- `recebimentos.idx_recebimentos_status` — `USING btree (pedido_id, status)`
- `recebimentos.idx_recebimentos_unit` — `USING btree (unit_id, created_at DESC)`
- `recipe_items.idx_recipe_items_ingredient` — `USING btree (ingredient_id) WHERE (ingredient_id IS NOT NULL)`
- `recipe_items.idx_recipe_items_menu` — `USING btree (menu_item_id)`
- `recipe_notes.idx_recipe_notes_menu` — `USING btree (menu_item_id, created_at DESC)`
- `interview_responses.idx_responses_candidate` — `USING btree (candidate_id)`
- `reunioes_1on1.idx_reunioes_colaborador` — `USING btree (colaborador_id)`
- `reunioes_1on1.idx_reunioes_data` — `USING btree (data_reuniao DESC)`
- `reunioes_1on1.idx_reunioes_gestor` — `USING btree (gestor_id)`
- `roadmap_items.idx_roadmap_sprint` — `USING btree (sprint)`
- `roadmap_items.idx_roadmap_status` — `USING btree (status)`
- `score_events.idx_score_events_employee` — `USING btree (employee_id, created_at DESC)`
- `shifts.idx_shifts_employee_data` — `USING btree (employee_id, data)`
- `shifts.idx_shifts_unit_data` — `USING btree (unit_id, data)`
- `suppliers.idx_suppliers_ativo` — `USING btree (ativo)`
- `suppliers.idx_suppliers_brand` — `USING btree (brand_id)`
- `suppliers.idx_suppliers_unit` — `USING btree (unit_id)`
- `target_notes.idx_target_notes_target` — `USING btree (target_id, created_at DESC)`
- `theo_tickets.idx_theo_tickets_employee` — `USING btree (employee_id)`
- `theo_tickets.idx_theo_tickets_status` — `USING btree (status)`
- `time_records.idx_time_records_employee_periodo` — `USING btree (employee_id, periodo)`
- `titulo_override.idx_titulo_override_titulo` — `USING btree (titulo_id)`
- `training_records.idx_training_records_emp` — `USING btree (employee_id)`
- `training_records.idx_training_records_employee` — `USING btree (employee_id)`
- `training_records.idx_training_records_status` — `USING btree (status)`
- `training_records.idx_training_records_template` — `USING btree (template_id)`
- `training_records.idx_training_records_tmpl` — `USING btree (template_id)`
- `training_records.idx_training_records_validade` — `USING btree (validade_ate)`
- `training_templates.idx_training_templates_brand` — `USING btree (brand_id)`
- `training_templates.idx_training_templates_funcao` — `USING btree (funcao)`
- `training_templates.idx_training_templates_unit` — `USING btree (unit_id)`
- `training_templates.idx_training_tmpl_brand` — `USING btree (brand_id)`
- `units.idx_units_brand` — `USING btree (brand_id)`
- `user_roles.idx_user_roles_brand` — `USING btree (brand_id)`
- `user_roles.idx_user_roles_unit` — `USING btree (unit_id)`
- `user_roles.idx_user_roles_user` — `USING btree (user_id)`
- `vacations.idx_vacations_employee` — `USING btree (employee_id)`
- `vacations.idx_vacations_status` — `USING btree (status)`
- `vendas_consolidado_ambiente.idx_vcamb_periodo` — `USING btree (periodo_id)`
- `vendas_consolidado_dia_semana.idx_vcdia_periodo` — `USING btree (periodo_id, ordem)`
- `vendas_consolidado_funcionarios.idx_vcfunc_periodo` — `USING btree (periodo_id, bruto DESC)`
- `vendas_consolidado_mensal.idx_vcmensal_periodo` — `USING btree (periodo_id, ordem)`
- `vendas_consolidado_periodo.idx_vcp_unit` — `USING btree (unit_id, data_inicio DESC)`
- `vendas_consolidado_produtos.idx_vcprod_periodo` — `USING btree (periodo_id, valor_liquido DESC)`
- `vendas_consolidado_resumo.idx_vcr_periodo` — `USING btree (periodo_id)`
- `vendas_consolidado_turno.idx_vcturno_periodo` — `USING btree (periodo_id)`
- `transport_vouchers.idx_vt_employee_periodo` — `USING btree (employee_id, periodo)`
- `warnings.idx_warnings_employee` — `USING btree (employee_id, data DESC)`
- `ingredients.ingredients_group_codigo_uniq` — `USING btree (group_id, codigo) WHERE (codigo IS NOT NULL)`
- `payroll_dominio_cadastro.ix_dom_cad_cpf` — `USING btree (cpf)`
- `payroll_dominio_cadastro.ix_dom_cad_emp` — `USING btree (employee_id)`
- `payroll_dominio_cadastro.ix_dom_cad_norm` — `USING btree (nome_norm)`
- `payroll_extrato_dominio_colaborador.ix_extrato_colab_comp` — `USING btree (competencia)`
- `payroll_extrato_dominio_colaborador.ix_extrato_colab_cpf` — `USING btree (cpf)`
- `payroll_extrato_dominio_colaborador.ix_extrato_colab_emp` — `USING btree (employee_id)`
- `payroll_extrato_dominio_linha.ix_extrato_linha_comp` — `USING btree (competencia, rubrica_codigo)`
- `payroll_extrato_dominio_linha.ix_extrato_linha_emp` — `USING btree (employee_id)`
- `job_descriptions.job_descriptions_brand_id_idx` — `USING btree (brand_id)`
- `job_descriptions.job_descriptions_cargo_idx` — `USING btree (cargo)`
- `learning_machine_reports.lm_reports_week_idx` — `USING btree (year DESC, week_number DESC)`
- `lorean_cancelamentos.lorean_cancelamentos_workday` — `USING btree (workday_id_fk)`
- `lorean_horarios.lorean_horarios_workday` — `USING btree (workday_id_fk)`
- `lorean_usuarios.lorean_usuarios_workday` — `USING btree (workday_id_fk)`
- `menu_items.menu_items_unit_codigo_uniq` — `USING btree (unit_id, codigo) WHERE (codigo IS NOT NULL)`
- `orquestrador_jobs.orquestrador_jobs_created_at_idx` — `USING btree (created_at DESC)`
- `orquestrador_jobs.orquestrador_jobs_type_idx` — `USING btree (type)`
- `pdi_metas.pdi_metas_pdi` — `USING btree (pdi_id)`
- `pdis.pdis_employee` — `USING btree (employee_id)`
- `price_quote_items.price_quote_items_quote_idx` — `USING btree (quote_id)`
- `price_quotes.price_quotes_unit_idx` — `USING btree (unit_id, periodo)`
- `quality_checklists.quality_checklists_unit_idx` — `USING btree (unit_id)`
- `recipe_items.recipe_items_menu_item_idx` — `USING btree (menu_item_id)`
- `relatorio_produtos.relatorio_produtos_calcula_cmv_idx` — `USING btree (calcula_cmv)`
- `relatorio_produtos.relatorio_produtos_desc_gerencial_idx` — `USING btree (desc_gerencial)`
- `relatorio_produtos.relatorio_produtos_mes_lancamento_ano_lancamento_idx` — `USING btree (mes_lancamento, ano_lancamento)`
- `relatorio_produtos.relatorio_produtos_unit_id_idx` — `USING btree (unit_id)`
- `reservations.reservations_unit_data_idx` — `USING btree (unit_id, data)`
- `reunioes_1on1.reunioes_colaborador` — `USING btree (colaborador_id)`
- `reunioes_1on1.reunioes_data` — `USING btree (data_reuniao)`
- `reunioes_1on1.reunioes_gestor` — `USING btree (gestor_id)`
- `cargo_salarios.uq_cargo_salario` — `USING btree (cargo_id, COALESCE(nivel, 0), COALESCE(unit_id, '00000000-0000-0000-0000-000000000000'::uuid))`

## Foreign keys
- `Comments_member_id_fkey`: `Comments(member_id)` → `public.Team_Members(id)`
- `Comments_task_id_fkey`: `Comments(task_id)` → `public.Tasks(id)`
- `Task_Assignees_member_id_fkey`: `Task_Assignees(member_id)` → `public.Team_Members(id)`
- `Task_Assignees_task_id_fkey`: `Task_Assignees(task_id)` → `public.Tasks(id)`
- `Tasks_project_id_fkey`: `Tasks(project_id)` → `public.Projects(id)`
- `absences_employee_id_fkey`: `absences(employee_id)` → `public.employees(id)`
- `access_requests_approver_id_fkey`: `access_requests(approver_id)` → `public.employees(id)`
- `access_requests_employee_id_fkey`: `access_requests(employee_id)` → `public.employees(id)`
- `action_plan_tasks_plan_id_fkey`: `action_plan_tasks(plan_id)` → `public.action_plans(id)`
- `action_plans_employee_id_fkey`: `action_plans(employee_id)` → `public.employees(id)`
- `action_plans_responsavel_id_fkey`: `action_plans(responsavel_id)` → `public.employees(id)`
- `action_plans_unit_id_fkey`: `action_plans(unit_id)` → `public.units(id)`
- `agent_prompt_versions_ativado_por_fkey`: `agent_prompt_versions(ativado_por)` → `auth.users(id)`
- `attendance_summaries_employee_id_fkey`: `attendance_summaries(employee_id)` → `public.employees(id)`
- `attendance_summaries_unit_id_fkey`: `attendance_summaries(unit_id)` → `public.units(id)`
- `audit_log_user_id_fkey`: `audit_log(user_id)` → `auth.users(id)`
- `avaliacao_ciclos_created_by_fkey`: `avaliacao_ciclos(created_by)` → `auth.users(id)`
- `avaliacao_ciclos_template_id_fkey`: `avaliacao_ciclos(template_id)` → `public.performance_templates(id)`
- `avaliacao_ciclos_unit_id_fkey`: `avaliacao_ciclos(unit_id)` → `public.units(id)`
- `avaliacao_participantes_avaliado_id_fkey`: `avaliacao_participantes(avaliado_id)` → `public.employees(id)`
- `avaliacao_participantes_avaliador_id_fkey`: `avaliacao_participantes(avaliador_id)` → `public.employees(id)`
- `avaliacao_participantes_ciclo_id_fkey`: `avaliacao_participantes(ciclo_id)` → `public.avaliacao_ciclos(id)`
- `avaliacao_participantes_review_id_fkey`: `avaliacao_participantes(review_id)` → `public.performance_reviews(id)`
- `brand_links_brand_id_fkey`: `brand_links(brand_id)` → `public.brands(id)`
- `brand_targets_brand_id_fkey`: `brand_targets(brand_id)` → `public.brands(id)`
- `brand_targets_created_by_fkey`: `brand_targets(created_by)` → `auth.users(id)`
- `brand_targets_unit_id_fkey`: `brand_targets(unit_id)` → `public.units(id)`
- `brands_group_id_fkey`: `brands(group_id)` → `public.groups(id)`
- `buckets_project_id_fkey`: `buckets(project_id)` → `public.projects(id)`
- `campaigns_brand_id_fkey`: `campaigns(brand_id)` → `public.brands(id)`
- `campaigns_created_by_fkey`: `campaigns(created_by)` → `auth.users(id)`
- `campaigns_unit_id_fkey`: `campaigns(unit_id)` → `public.units(id)`
- `candidate_agendamentos_candidate_id_fkey`: `candidate_agendamentos(candidate_id)` → `public.candidates(id)`
- `candidate_agendamentos_unit_id_fkey`: `candidate_agendamentos(unit_id)` → `public.units(id)`
- `candidate_avaliacao_candidate_id_fkey`: `candidate_avaliacao(candidate_id)` → `public.candidates(id)`
- `candidate_feedback_operacional_agendamento_id_fkey`: `candidate_feedback_operacional(agendamento_id)` → `public.candidate_agendamentos(id)`
- `candidate_feedback_operacional_candidate_id_fkey`: `candidate_feedback_operacional(candidate_id)` → `public.candidates(id)`
- `candidate_pipeline_autor_id_fkey`: `candidate_pipeline(autor_id)` → `public.employees(id)`
- `candidate_pipeline_candidate_id_fkey`: `candidate_pipeline(candidate_id)` → `public.candidates(id)`
- `candidate_pipeline_responsavel_id_fkey`: `candidate_pipeline(responsavel_id)` → `public.employees(id)`
- `candidates_cargo_id_fkey`: `candidates(cargo_id)` → `public.cargos(id)`
- `candidates_entrevistador_id_fkey`: `candidates(entrevistador_id)` → `public.employees(id)`
- `candidates_job_opening_id_fkey`: `candidates(job_opening_id)` → `public.job_openings(id)`
- `candidates_origem_id_fkey`: `candidates(origem_id)` → `public.origens_candidato(id)`
- `candidates_responsavel_id_fkey`: `candidates(responsavel_id)` → `public.employees(id)`
- `candidates_unit_id_fkey`: `candidates(unit_id)` → `public.units(id)`
- `cargo_salarios_cargo_id_fkey`: `cargo_salarios(cargo_id)` → `public.cargos(id)`
- `cargo_salarios_unit_id_fkey`: `cargo_salarios(unit_id)` → `public.units(id)`
- `cargos_reporta_a_cargo_id_fkey`: `cargos(reporta_a_cargo_id)` → `public.cargos(id)`
- `checklist_records_checklist_id_fkey`: `checklist_records(checklist_id)` → `public.quality_checklists(id)`
- `checklist_records_responsavel_id_fkey`: `checklist_records(responsavel_id)` → `auth.users(id)`
- `checklist_records_unit_id_fkey`: `checklist_records(unit_id)` → `public.units(id)`
- `client_interactions_client_id_fkey`: `client_interactions(client_id)` → `public.clients(id)`
- `client_interactions_created_by_fkey`: `client_interactions(created_by)` → `auth.users(id)`
- `clients_brand_id_fkey`: `clients(brand_id)` → `public.brands(id)`
- `clients_created_by_fkey`: `clients(created_by)` → `auth.users(id)`
- `clients_unit_id_fkey`: `clients(unit_id)` → `public.units(id)`
- `climate_questions_survey_id_fkey`: `climate_questions(survey_id)` → `public.climate_surveys(id)`
- `climate_responses_employee_id_fkey`: `climate_responses(employee_id)` → `public.employees(id)`
- `climate_responses_question_id_fkey`: `climate_responses(question_id)` → `public.climate_questions(id)`
- `climate_responses_survey_id_fkey`: `climate_responses(survey_id)` → `public.climate_surveys(id)`
- `climate_survey_questions_survey_id_fkey`: `climate_survey_questions(survey_id)` → `public.climate_surveys(id)`
- `climate_survey_responses_question_id_fkey`: `climate_survey_responses(question_id)` → `public.climate_survey_questions(id)`
- `climate_survey_responses_survey_id_fkey`: `climate_survey_responses(survey_id)` → `public.climate_surveys(id)`
- `climate_surveys_unit_id_fkey`: `climate_surveys(unit_id)` → `public.units(id)`
- `comments_member_id_fkey`: `comments(member_id)` → `public.team_members(id)`
- `comments_task_id_fkey`: `comments(task_id)` → `public.tasks(id)`
- `contatos_kph_candidate_id_fkey`: `contatos_kph(candidate_id)` → `public.candidates(id)`
- `contatos_kph_employee_id_fkey`: `contatos_kph(employee_id)` → `public.employees(id)`
- `contractor_payments_contractor_id_fkey`: `contractor_payments(contractor_id)` → `public.contractors(id)`
- `contractor_payments_unit_id_fkey`: `contractor_payments(unit_id)` → `public.units(id)`
- `contractor_vacations_contractor_id_fkey`: `contractor_vacations(contractor_id)` → `public.contractors(id)`
- `contractor_vacations_unit_id_fkey`: `contractor_vacations(unit_id)` → `public.units(id)`
- `contractors_unit_id_fkey`: `contractors(unit_id)` → `public.units(id)`
- `contratos_arquivos_contrato_id_fkey`: `contratos_arquivos(contrato_id)` → `public.contratos(id)`
- `dependents_employee_id_fkey`: `dependents(employee_id)` → `public.employees(id)`
- `dho_tracking_employee_id_fkey`: `dho_tracking(employee_id)` → `public.employees(id)`
- `dho_tracking_unit_id_fkey`: `dho_tracking(unit_id)` → `public.units(id)`
- `disc_profiles_employee_id_fkey`: `disc_profiles(employee_id)` → `public.employees(id)`
- `disciplinary_actions_employee_id_fkey`: `disciplinary_actions(employee_id)` → `public.employees(id)`
- `disciplinary_actions_unit_id_fkey`: `disciplinary_actions(unit_id)` → `public.units(id)`
- `documents_employee_id_fkey`: `documents(employee_id)` → `public.employees(id)`
- `documents_unit_id_fkey`: `documents(unit_id)` → `public.units(id)`
- `employee_auth_employee_id_fkey`: `employee_auth(employee_id)` → `public.employees(id)`
- `employee_availability_employee_id_fkey`: `employee_availability(employee_id)` → `public.employees(id)`
- `employee_availability_unit_id_fkey`: `employee_availability(unit_id)` → `public.units(id)`
- `employee_benefits_employee_id_fkey`: `employee_benefits(employee_id)` → `public.employees(id)`
- `employee_benefits_unit_id_fkey`: `employee_benefits(unit_id)` → `public.units(id)`
- `employee_codigos_dominio_employee_id_fkey`: `employee_codigos_dominio(employee_id)` → `public.employees(id)`
- `employee_codigos_dominio_unit_id_fkey`: `employee_codigos_dominio(unit_id)` → `public.units(id)`
- `employee_documents_employee_id_fkey`: `employee_documents(employee_id)` → `public.employees(id)`
- `employee_documents_uploaded_by_fkey`: `employee_documents(uploaded_by)` → `auth.users(id)`
- `employees_manager_id_fkey`: `employees(manager_id)` → `public.employees(id)`
- `employees_role_id_fkey`: `employees(role_id)` → `public.roles(id)`
- `employees_unit_id_fkey`: `employees(unit_id)` → `public.units(id)`
- `employees_user_id_fkey`: `employees(user_id)` → `auth.users(id)`
- `event_attachments_event_id_fkey`: `event_attachments(event_id)` → `public.events(id)`
- `event_attachments_uploaded_by_fkey`: `event_attachments(uploaded_by)` → `auth.users(id)`
- `event_infra_items_event_id_fkey`: `event_infra_items(event_id)` → `public.events(id)`
- `event_menu_items_event_id_fkey`: `event_menu_items(event_id)` → `public.events(id)`
- `event_staff_employee_id_fkey`: `event_staff(employee_id)` → `public.employees(id)`
- `event_staff_event_id_fkey`: `event_staff(event_id)` → `public.events(id)`
- `event_status_log_changed_by_fkey`: `event_status_log(changed_by)` → `auth.users(id)`
- `event_status_log_event_id_fkey`: `event_status_log(event_id)` → `public.events(id)`
- `events_approved_by_fkey`: `events(approved_by)` → `auth.users(id)`
- `events_brand_id_fkey`: `events(brand_id)` → `public.brands(id)`
- `events_created_by_fkey`: `events(created_by)` → `auth.users(id)`
- `events_group_id_fkey`: `events(group_id)` → `public.groups(id)`
- `events_responsavel_interno_fkey`: `events(responsavel_interno)` → `auth.users(id)`
- `events_unit_id_fkey`: `events(unit_id)` → `public.units(id)`
- `feedback_user_id_fkey`: `feedback(user_id)` → `auth.users(id)`
- `feedbacks_de_employee_id_fkey`: `feedbacks(de_employee_id)` → `public.employees(id)`
- `feedbacks_para_employee_id_fkey`: `feedbacks(para_employee_id)` → `public.employees(id)`
- `feedbacks_unit_id_fkey`: `feedbacks(unit_id)` → `public.units(id)`
- `gorjeta_cargo_pontos_unit_id_fkey`: `gorjeta_cargo_pontos(unit_id)` → `public.units(id)`
- `gorjeta_dias_employee_id_fkey`: `gorjeta_dias(employee_id)` → `public.employees(id)`
- `gorjeta_dias_periodo_id_fkey`: `gorjeta_dias(periodo_id)` → `public.gorjeta_periodos(id)`
- `gorjeta_dias_unit_id_fkey`: `gorjeta_dias(unit_id)` → `public.units(id)`
- `gorjeta_distribuicao_colaborador_id_fkey`: `gorjeta_distribuicao(colaborador_id)` → `public.employees(id)`
- `gorjeta_distribuicao_employee_id_fkey`: `gorjeta_distribuicao(employee_id)` → `public.employees(id)`
- `gorjeta_distribuicao_unit_id_fkey`: `gorjeta_distribuicao(unit_id)` → `public.units(id)`
- `gorjeta_periodos_unit_id_fkey`: `gorjeta_periodos(unit_id)` → `public.units(id)`
- `groups_parent_id_fkey`: `groups(parent_id)` → `public.groups(id)`
- `hos_approvals_run_id_fkey`: `hos_approvals(run_id)` → `public.hos_runs(id)`
- `hos_approvals_user_id_fkey`: `hos_approvals(user_id)` → `auth.users(id)`
- `hos_jobs_unit_id_fkey`: `hos_jobs(unit_id)` → `public.units(id)`
- `hos_runs_employee_id_fkey`: `hos_runs(employee_id)` → `public.employees(id)`
- `hos_runs_job_id_fkey`: `hos_runs(job_id)` → `public.hos_jobs(id)`
- `hour_bank_employee_id_fkey`: `hour_bank(employee_id)` → `public.employees(id)`
- `hour_bank_unit_id_fkey`: `hour_bank(unit_id)` → `public.units(id)`
- `hr_policies_unit_id_fkey`: `hr_policies(unit_id)` → `public.units(id)`
- `import_logs_imported_by_fkey`: `import_logs(imported_by)` → `auth.users(id)`
- `import_logs_unit_id_fkey`: `import_logs(unit_id)` → `public.units(id)`
- `ingredient_price_history_changed_by_fkey`: `ingredient_price_history(changed_by)` → `auth.users(id)`
- `ingredient_price_history_ingredient_id_fkey`: `ingredient_price_history(ingredient_id)` → `public.ingredients(id)`
- `ingredient_stock_ingredient_id_fkey`: `ingredient_stock(ingredient_id)` → `public.ingredients(id)`
- `ingredients_fornecedor_id_fkey`: `ingredients(fornecedor_id)` → `public.suppliers(id)`
- `ingredients_group_id_fkey`: `ingredients(group_id)` → `public.groups(id)`
- `ingredients_menu_item_id_fkey`: `ingredients(menu_item_id)` → `public.menu_items(id)`
- `interview_questions_job_opening_id_fkey`: `interview_questions(job_opening_id)` → `public.job_openings(id)`
- `interview_responses_candidate_id_fkey`: `interview_responses(candidate_id)` → `public.candidates(id)`
- `interview_responses_question_id_fkey`: `interview_responses(question_id)` → `public.interview_questions(id)`
- `interviews_candidate_id_fkey`: `interviews(candidate_id)` → `public.candidates(id)`
- `interviews_entrevistador_id_fkey`: `interviews(entrevistador_id)` → `public.employees(id)`
- `interviews_job_opening_id_fkey`: `interviews(job_opening_id)` → `public.job_openings(id)`
- `job_descriptions_brand_id_fkey`: `job_descriptions(brand_id)` → `public.brands(id)`
- `job_descriptions_cargo_id_fkey`: `job_descriptions(cargo_id)` → `public.cargos(id)`
- `job_descriptions_created_by_fkey`: `job_descriptions(created_by)` → `auth.users(id)`
- `job_opening_logs_opening_id_fkey`: `job_opening_logs(opening_id)` → `public.job_openings(id)`
- `job_openings_brand_id_fkey`: `job_openings(brand_id)` → `public.brands(id)`
- `job_openings_cargo_grupo_id_fkey`: `job_openings(cargo_grupo_id)` → `public.cargo_grupos(id)`
- `job_openings_created_by_fkey`: `job_openings(created_by)` → `auth.users(id)`
- `job_openings_entrevistador_id_fkey`: `job_openings(entrevistador_id)` → `public.employees(id)`
- `job_openings_responsavel_id_fkey`: `job_openings(responsavel_id)` → `public.employees(id)`
- `job_openings_substituido_id_fkey`: `job_openings(substituido_id)` → `public.employees(id)`
- `job_openings_unit_id_fkey`: `job_openings(unit_id)` → `public.units(id)`
- `lorean_ambientes_workday_id_fk_fkey`: `lorean_ambientes(workday_id_fk)` → `public.lorean_workdays(id)`
- `lorean_caixas_workday_id_fk_fkey`: `lorean_caixas(workday_id_fk)` → `public.lorean_workdays(id)`
- `lorean_cancelamentos_detalhe_workday_id_fk_fkey`: `lorean_cancelamentos_detalhe(workday_id_fk)` → `public.lorean_workdays(id)`
- `lorean_cancelamentos_workday_id_fk_fkey`: `lorean_cancelamentos(workday_id_fk)` → `public.lorean_workdays(id)`
- `lorean_descontos_detalhe_workday_id_fk_fkey`: `lorean_descontos_detalhe(workday_id_fk)` → `public.lorean_workdays(id)`
- `lorean_descontos_workday_id_fk_fkey`: `lorean_descontos(workday_id_fk)` → `public.lorean_workdays(id)`
- `lorean_grupos_workday_id_fk_fkey`: `lorean_grupos(workday_id_fk)` → `public.lorean_workdays(id)`
- `lorean_horarios_workday_id_fk_fkey`: `lorean_horarios(workday_id_fk)` → `public.lorean_workdays(id)`
- `lorean_pagamentos_workday_id_fk_fkey`: `lorean_pagamentos(workday_id_fk)` → `public.lorean_workdays(id)`
- `lorean_produtos_dia_workday_id_fk_fkey`: `lorean_produtos_dia(workday_id_fk)` → `public.lorean_workdays(id)`
- `lorean_turnos_workday_id_fk_fkey`: `lorean_turnos(workday_id_fk)` → `public.lorean_workdays(id)`
- `lorean_usuarios_workday_id_fk_fkey`: `lorean_usuarios(workday_id_fk)` → `public.lorean_workdays(id)`
- `lorean_workdays_unit_id_fkey`: `lorean_workdays(unit_id)` → `public.units(id)`
- `manutencao_aprovacoes_chamado_id_fkey`: `manutencao_aprovacoes(chamado_id)` → `public.manutencao_chamados(id)`
- `manutencao_parcelas_aprovacao_id_fkey`: `manutencao_parcelas(aprovacao_id)` → `public.manutencao_aprovacoes(id)`
- `menu_items_brand_id_fkey`: `menu_items(brand_id)` → `public.brands(id)`
- `menu_items_unit_id_fkey`: `menu_items(unit_id)` → `public.units(id)`
- `movimentacoes_rh_employee_id_fkey`: `movimentacoes_rh(employee_id)` → `public.employees(id)`
- `movimentacoes_rh_registrado_por_fkey`: `movimentacoes_rh(registrado_por)` → `auth.users(id)`
- `movimentacoes_rh_unidade_destino_id_fkey`: `movimentacoes_rh(unidade_destino_id)` → `public.units(id)`
- `movimentacoes_rh_unidade_id_fkey`: `movimentacoes_rh(unidade_id)` → `public.units(id)`
- `notifications_user_id_fkey`: `notifications(user_id)` → `auth.users(id)`
- `occupational_health_employee_id_fkey`: `occupational_health(employee_id)` → `public.employees(id)`
- `occupational_health_unit_id_fkey`: `occupational_health(unit_id)` → `public.units(id)`
- `onboarding_checklist_concluido_por_fkey`: `onboarding_checklist(concluido_por)` → `auth.users(id)`
- `onboarding_checklist_run_id_fkey`: `onboarding_checklist(run_id)` → `public.onboarding_runs(id)`
- `onboarding_checklist_tarefa_id_fkey`: `onboarding_checklist(tarefa_id)` → `public.onboarding_tarefas(id)`
- `onboarding_runs_employee_id_fkey`: `onboarding_runs(employee_id)` → `public.employees(id)`
- `onboarding_runs_template_id_fkey`: `onboarding_runs(template_id)` → `public.onboarding_templates(id)`
- `onboarding_runs_unit_id_fkey`: `onboarding_runs(unit_id)` → `public.units(id)`
- `onboarding_tarefas_template_id_fkey`: `onboarding_tarefas(template_id)` → `public.onboarding_templates(id)`
- `onboarding_templates_unit_id_fkey`: `onboarding_templates(unit_id)` → `public.units(id)`
- `overtime_records_approved_by_fkey`: `overtime_records(approved_by)` → `auth.users(id)`
- `overtime_records_employee_id_fkey`: `overtime_records(employee_id)` → `public.employees(id)`
- `overtime_records_unit_id_fkey`: `overtime_records(unit_id)` → `public.units(id)`
- `page_views_user_id_fkey`: `page_views(user_id)` → `auth.users(id)`
- `payroll_dominio_cadastro_cod_empresa_fkey`: `payroll_dominio_cadastro(cod_empresa)` → `public.payroll_dominio_empresa(cod_empresa)`
- `payroll_dominio_cadastro_employee_id_fkey`: `payroll_dominio_cadastro(employee_id)` → `public.employees(id)`
- `payroll_extrato_dominio_colaborador_employee_id_fkey`: `payroll_extrato_dominio_colaborador(employee_id)` → `public.employees(id)`
- `payroll_extrato_dominio_linha_employee_id_fkey`: `payroll_extrato_dominio_linha(employee_id)` → `public.employees(id)`
- `payroll_fechamento_linha_employee_id_fkey`: `payroll_fechamento_linha(employee_id)` → `public.employees(id)`
- `payroll_fechamento_linha_periodo_id_fkey`: `payroll_fechamento_linha(periodo_id)` → `public.payroll_fechamento_periodo(id)`
- `payroll_fechamento_linha_rubrica_id_fkey`: `payroll_fechamento_linha(rubrica_id)` → `public.payroll_rubricas(id)`
- `payroll_fechamento_periodo_gerado_por_fkey`: `payroll_fechamento_periodo(gerado_por)` → `public.employees(id)`
- `payroll_fechamento_periodo_unit_id_fkey`: `payroll_fechamento_periodo(unit_id)` → `public.units(id)`
- `payslips_employee_id_fkey`: `payslips(employee_id)` → `public.employees(id)`
- `payslips_unit_id_fkey`: `payslips(unit_id)` → `public.units(id)`
- `pdi_metas_pdi_id_fkey`: `pdi_metas(pdi_id)` → `public.pdis(id)`
- `pdis_avaliacao_id_fkey`: `pdis(avaliacao_id)` → `public.performance_reviews(id)`
- `pdis_created_by_fkey`: `pdis(created_by)` → `auth.users(id)`
- `pdis_criado_por_fkey`: `pdis(criado_por)` → `auth.users(id)`
- `pdis_employee_id_fkey`: `pdis(employee_id)` → `public.employees(id)`
- `pdis_unit_id_fkey`: `pdis(unit_id)` → `public.units(id)`
- `performance_reviews_avaliador_id_fkey`: `performance_reviews(avaliador_id)` → `auth.users(id)`
- `performance_reviews_employee_id_fkey`: `performance_reviews(employee_id)` → `public.employees(id)`
- `performance_reviews_template_id_fkey`: `performance_reviews(template_id)` → `public.performance_templates(id)`
- `performance_templates_brand_id_fkey`: `performance_templates(brand_id)` → `public.brands(id)`
- `performance_templates_created_by_fkey`: `performance_templates(created_by)` → `auth.users(id)`
- `performance_templates_unit_id_fkey`: `performance_templates(unit_id)` → `public.units(id)`
- `plan_members_member_id_fkey`: `plan_members(member_id)` → `public.team_members(id)`
- `plan_members_plan_id_fkey`: `plan_members(plan_id)` → `public.projects(id)`
- `ponto_mensal_employee_id_fkey`: `ponto_mensal(employee_id)` → `public.employees(id)`
- `ponto_mensal_unit_id_fkey`: `ponto_mensal(unit_id)` → `public.units(id)`
- `price_quote_items_quote_id_fkey`: `price_quote_items(quote_id)` → `public.price_quotes(id)`
- `price_quotes_created_by_fkey`: `price_quotes(created_by)` → `auth.users(id)`
- `price_quotes_supplier_id_fkey`: `price_quotes(supplier_id)` → `public.suppliers(id)`
- `price_quotes_unit_id_fkey`: `price_quotes(unit_id)` → `public.units(id)`
- `profiles_id_fkey`: `profiles(id)` → `auth.users(id)`
- `project_invites_created_by_fkey`: `project_invites(created_by)` → `auth.users(id)`
- `project_invites_project_id_fkey`: `project_invites(project_id)` → `public.projects(id)`
- `project_members_invited_by_fkey`: `project_members(invited_by)` → `auth.users(id)`
- `project_members_project_id_fkey`: `project_members(project_id)` → `public.projects(id)`
- `project_members_user_id_fkey`: `project_members(user_id)` → `auth.users(id)`
- `projects_owner_id_fkey`: `projects(owner_id)` → `auth.users(id)`
- `punch_adjustment_requests_aprovado_por_fkey`: `punch_adjustment_requests(aprovado_por)` → `auth.users(id)`
- `punch_adjustment_requests_employee_id_fkey`: `punch_adjustment_requests(employee_id)` → `public.employees(id)`
- `purchase_invoice_items_ingredient_id_fkey`: `purchase_invoice_items(ingredient_id)` → `public.ingredients(id)`
- `purchase_invoice_items_purchase_invoice_id_fkey`: `purchase_invoice_items(purchase_invoice_id)` → `public.purchase_invoices(id)`
- `purchase_invoices_unit_id_fkey`: `purchase_invoices(unit_id)` → `public.units(id)`
- `purchase_order_items_order_id_fkey`: `purchase_order_items(order_id)` → `public.purchase_orders(id)`
- `purchase_orders_brand_id_fkey`: `purchase_orders(brand_id)` → `public.brands(id)`
- `purchase_orders_created_by_fkey`: `purchase_orders(created_by)` → `auth.users(id)`
- `purchase_orders_supplier_id_fkey`: `purchase_orders(supplier_id)` → `public.suppliers(id)`
- `purchase_orders_unit_id_fkey`: `purchase_orders(unit_id)` → `public.units(id)`
- `quadro_ideal_cargo_grupo_id_fkey`: `quadro_ideal(cargo_grupo_id)` → `public.cargo_grupos(id)`
- `quadro_ideal_cargo_id_fkey`: `quadro_ideal(cargo_id)` → `public.cargos(id)`
- `quadro_ideal_reporta_a_cargo_id_fkey`: `quadro_ideal(reporta_a_cargo_id)` → `public.cargos(id)`
- `quadro_ideal_unit_id_fkey`: `quadro_ideal(unit_id)` → `public.units(id)`
- `quality_checklists_unit_id_fkey`: `quality_checklists(unit_id)` → `public.units(id)`
- `recebimento_itens_pedido_item_id_fkey`: `recebimento_itens(pedido_item_id)` → `public.purchase_order_items(id)`
- `recebimento_itens_recebimento_id_fkey`: `recebimento_itens(recebimento_id)` → `public.recebimentos(id)`
- `recebimentos_pedido_id_fkey`: `recebimentos(pedido_id)` → `public.purchase_orders(id)`
- `recipe_items_ingredient_id_fkey`: `recipe_items(ingredient_id)` → `public.ingredients(id)`
- `recipe_items_menu_item_id_fkey`: `recipe_items(menu_item_id)` → `public.menu_items(id)`
- `recipe_notes_created_by_fkey`: `recipe_notes(created_by)` → `auth.users(id)`
- `recipe_notes_menu_item_id_fkey`: `recipe_notes(menu_item_id)` → `public.menu_items(id)`
- `relatorio_produtos_unit_id_fkey`: `relatorio_produtos(unit_id)` → `public.units(id)`
- `reservations_confirmado_por_fkey`: `reservations(confirmado_por)` → `auth.users(id)`
- `reservations_created_by_fkey`: `reservations(created_by)` → `auth.users(id)`
- `reservations_unit_id_fkey`: `reservations(unit_id)` → `public.units(id)`
- `reuniao_action_items_responsavel_id_fkey`: `reuniao_action_items(responsavel_id)` → `public.employees(id)`
- `reuniao_action_items_reuniao_id_fkey`: `reuniao_action_items(reuniao_id)` → `public.reunioes_1on1(id)`
- `reunioes_1on1_colaborador_id_fkey`: `reunioes_1on1(colaborador_id)` → `public.employees(id)`
- `reunioes_1on1_created_by_fkey`: `reunioes_1on1(created_by)` → `auth.users(id)`
- `reunioes_1on1_gestor_id_fkey`: `reunioes_1on1(gestor_id)` → `public.employees(id)`
- `reunioes_1on1_unit_id_fkey`: `reunioes_1on1(unit_id)` → `public.units(id)`
- `score_events_employee_id_fkey`: `score_events(employee_id)` → `public.employees(id)`
- `shifts_employee_id_fkey`: `shifts(employee_id)` → `public.employees(id)`
- `shifts_unit_id_fkey`: `shifts(unit_id)` → `public.units(id)`
- `sick_leaves_employee_id_fkey`: `sick_leaves(employee_id)` → `public.employees(id)`
- `sick_leaves_unit_id_fkey`: `sick_leaves(unit_id)` → `public.units(id)`
- `suppliers_brand_id_fkey`: `suppliers(brand_id)` → `public.brands(id)`
- `suppliers_unit_id_fkey`: `suppliers(unit_id)` → `public.units(id)`
- `target_notes_created_by_fkey`: `target_notes(created_by)` → `auth.users(id)`
- `target_notes_target_id_fkey`: `target_notes(target_id)` → `public.brand_targets(id)`
- `task_assignees_member_id_fkey`: `task_assignees(member_id)` → `public.team_members(id)`
- `task_assignees_task_id_fkey`: `task_assignees(task_id)` → `public.tasks(id)`
- `tasks_bucket_id_fkey`: `tasks(bucket_id)` → `public.buckets(id)`
- `tasks_project_id_fkey`: `tasks(project_id)` → `public.projects(id)`
- `terminations_employee_id_fkey`: `terminations(employee_id)` → `public.employees(id)`
- `terminations_unit_id_fkey`: `terminations(unit_id)` → `public.units(id)`
- `theo_tickets_employee_id_fkey`: `theo_tickets(employee_id)` → `public.employees(id)`
- `time_bank_balance_employee_id_fkey`: `time_bank_balance(employee_id)` → `public.employees(id)`
- `time_clock_punches_aprovado_por_fkey`: `time_clock_punches(aprovado_por)` → `public.employees(id)`
- `time_clock_punches_employee_id_fkey`: `time_clock_punches(employee_id)` → `public.employees(id)`
- `time_records_employee_id_fkey`: `time_records(employee_id)` → `public.employees(id)`
- `time_records_unit_id_fkey`: `time_records(unit_id)` → `public.units(id)`
- `training_participants_employee_id_fkey`: `training_participants(employee_id)` → `public.employees(id)`
- `training_participants_training_id_fkey`: `training_participants(training_id)` → `public.trainings(id)`
- `training_records_created_by_fkey`: `training_records(created_by)` → `auth.users(id)`
- `training_records_employee_id_fkey`: `training_records(employee_id)` → `public.employees(id)`
- `training_records_template_id_fkey`: `training_records(template_id)` → `public.training_templates(id)`
- `training_templates_brand_id_fkey`: `training_templates(brand_id)` → `public.brands(id)`
- `training_templates_created_by_fkey`: `training_templates(created_by)` → `auth.users(id)`
- `training_templates_unit_id_fkey`: `training_templates(unit_id)` → `public.units(id)`
- `trainings_unit_id_fkey`: `trainings(unit_id)` → `public.units(id)`
- `transport_vouchers_employee_id_fkey`: `transport_vouchers(employee_id)` → `public.employees(id)`
- `transport_vouchers_unit_id_fkey`: `transport_vouchers(unit_id)` → `public.units(id)`
- `uniforms_employee_id_fkey`: `uniforms(employee_id)` → `public.employees(id)`
- `uniforms_unit_id_fkey`: `uniforms(unit_id)` → `public.units(id)`
- `units_brand_id_fkey`: `units(brand_id)` → `public.brands(id)`
- `user_roles_brand_id_fkey`: `user_roles(brand_id)` → `public.brands(id)`
- `user_roles_group_id_fkey`: `user_roles(group_id)` → `public.groups(id)`
- `user_roles_role_id_fkey`: `user_roles(role_id)` → `public.roles(id)`
- `user_roles_unit_id_fkey`: `user_roles(unit_id)` → `public.units(id)`
- `user_roles_user_id_fkey`: `user_roles(user_id)` → `auth.users(id)`
- `vacation_schedules_employee_id_fkey`: `vacation_schedules(employee_id)` → `public.employees(id)`
- `vacation_schedules_unit_id_fkey`: `vacation_schedules(unit_id)` → `public.units(id)`
- `vacations_created_by_fkey`: `vacations(created_by)` → `auth.users(id)`
- `vacations_employee_id_fkey`: `vacations(employee_id)` → `public.employees(id)`
- `vacations_unit_id_fkey`: `vacations(unit_id)` → `public.units(id)`
- `vendas_consolidado_ambiente_periodo_id_fkey`: `vendas_consolidado_ambiente(periodo_id)` → `public.vendas_consolidado_periodo(id)`
- `vendas_consolidado_dia_semana_periodo_id_fkey`: `vendas_consolidado_dia_semana(periodo_id)` → `public.vendas_consolidado_periodo(id)`
- `vendas_consolidado_funcionarios_periodo_id_fkey`: `vendas_consolidado_funcionarios(periodo_id)` → `public.vendas_consolidado_periodo(id)`
- `vendas_consolidado_mensal_periodo_id_fkey`: `vendas_consolidado_mensal(periodo_id)` → `public.vendas_consolidado_periodo(id)`
- `vendas_consolidado_produtos_periodo_id_fkey`: `vendas_consolidado_produtos(periodo_id)` → `public.vendas_consolidado_periodo(id)`
- `vendas_consolidado_resumo_periodo_id_fkey`: `vendas_consolidado_resumo(periodo_id)` → `public.vendas_consolidado_periodo(id)`
- `vendas_consolidado_turno_periodo_id_fkey`: `vendas_consolidado_turno(periodo_id)` → `public.vendas_consolidado_periodo(id)`
- `warnings_employee_id_fkey`: `warnings(employee_id)` → `public.employees(id)`
- `work_schedules_employee_id_fkey`: `work_schedules(employee_id)` → `public.employees(id)`
- `work_schedules_unit_id_fkey`: `work_schedules(unit_id)` → `public.units(id)`

## Políticas RLS
- `hos_jobs.Admin vê jobs` — `USING ((EXISTS ( SELECT 1 FROM public.user_roles ur WHERE ((ur.user_id = auth.uid()) AND (ur.role_id = ANY (ARRAY['0580a0a6-48c9-4170-b74d-84fd23e815fc'::uuid, '086f0247-6407-4cdf-9c12-6e12ca2dbaf7'::uuid, 'ba89b7b1-cea2-4622-b2f3-2623817d08aa'::uuid]))))))`
- `hos_runs.Admin vê runs` — `USING ((EXISTS ( SELECT 1 FROM public.user_roles ur WHERE ((ur.user_id = auth.uid()) AND (ur.role_id = ANY (ARRAY['0580a0a6-48c9-4170-b74d-84fd23e815fc'::uuid, '086f0247-6407-4cdf-9c12-6e12ca2dbaf7'::uuid, 'ba89b7b1-cea2-4622-b2f3-2623817d08aa'::uuid]))))))`
- `hos_runs.Admins podem atualizar execucoes` — `FOR UPDATE TO authenticated USING ((public.kph_has_role_for_unit(NULL::uuid) OR public.kph_is_founder())) WITH CHECK ((public.kph_has_role_for_unit(NULL::uuid) OR public.kph_is_founder()))`
- `hos_insights.Admins podem inserir insights` — `FOR INSERT TO authenticated WITH CHECK ((public.kph_has_role_for_unit(NULL::uuid) OR public.kph_is_founder()))`
- `hos_insights.Admins podem ver insights` — `FOR SELECT TO authenticated USING ((public.kph_has_role_for_unit(NULL::uuid) OR public.kph_is_founder()))`
- `job_requisitions.Allow anonymous inserts` — `FOR INSERT TO anon WITH CHECK (true)`
- `job_requisitions.Allow authenticated reads` — `FOR SELECT TO authenticated USING (true)`
- `hos_approvals.Founder aprova` — `USING ((EXISTS ( SELECT 1 FROM public.user_roles ur WHERE ((ur.user_id = auth.uid()) AND (ur.role_id = '0580a0a6-48c9-4170-b74d-84fd23e815fc'::uuid)))))`
- `job_requisitions.Permitir edicao` — `FOR UPDATE USING (true)`
- `job_requisitions.Permitir exclusao` — `FOR DELETE USING (true)`
- `job_requisitions.Permitir leitura` — `FOR SELECT USING (true)`
- `absences.absences_all` — `USING ((EXISTS ( SELECT 1 FROM public.employees e WHERE ((e.id = absences.employee_id) AND public.kph_has_role_for_unit(e.unit_id)))))`
- `reuniao_action_items.action_items_access` — `USING ((reuniao_id IN ( SELECT reunioes_1on1.id FROM public.reunioes_1on1 WHERE (reunioes_1on1.unit_id IN ( SELECT user_roles.unit_id FROM public.user_roles WHERE (user_roles.user_id = auth.uid()))))))`
- `reuniao_action_items.action_items_read` — `FOR SELECT USING ((reuniao_id IN ( SELECT reunioes_1on1.id FROM public.reunioes_1on1)))`
- `reuniao_action_items.action_items_write` — `USING (((reuniao_id IN ( SELECT r.id FROM (public.reunioes_1on1 r JOIN public.employees eg ON (((eg.id = r.gestor_id) AND (eg.user_id = auth.uid())))))) OR (public.get_my_tier() = ANY (ARRAY['T3'::text, 'T4'::text]))))`
- `candidate_agendamentos.agendamentos_all` — `USING (true) WITH CHECK (true)`
- `agent_conversations.agent_conversations_deny_anon` — `TO anon USING (false)`
- `agent_conversations.agent_conversations_select` — `FOR SELECT TO authenticated USING (((public.get_my_tier() = ANY (ARRAY['T2A'::text, 'T2B'::text, 'T3'::text, 'T4'::text])) OR (operator_id = auth.uid())))`
- `agent_conversations.agent_conversations_update` — `FOR UPDATE TO authenticated USING (((public.get_my_tier() = ANY (ARRAY['T2A'::text, 'T2B'::text, 'T3'::text, 'T4'::text])) OR (operator_id = auth.uid())))`
- `dre_contratos_fixos.allow_all` — `USING (true) WITH CHECK (true)`
- `dre_kpis_mensais.allow_all` — `USING (true) WITH CHECK (true)`
- `dre_linhas_detalhadas.allow_all` — `USING (true)`
- `dre_manutencao_detalhada.allow_all` — `USING (true) WITH CHECK (true)`
- `dre_pessoal_detalhado.allow_all` — `USING (true) WITH CHECK (true)`
- `dre_prestadores.allow_all` — `USING (true) WITH CHECK (true)`
- `climate_questions.anon_all_climate_questions` — `TO authenticated, anon USING (true) WITH CHECK (true)`
- `climate_responses.anon_all_climate_responses` — `TO authenticated, anon USING (true) WITH CHECK (true)`
- `climate_surveys.anon_all_climate_surveys` — `TO authenticated, anon USING (true) WITH CHECK (true)`
- `punch_adjustment_requests.anon_all_punch_adj` — `TO authenticated, anon USING (true) WITH CHECK (true)`
- `access_requests.anyone_insert` — `FOR INSERT TO authenticated WITH CHECK (true)`
- `access_requests.approver_update` — `FOR UPDATE TO authenticated USING ((((public.get_my_tier() = 'T2A'::text) AND (approver_tier = 'T2A'::text)) OR ((public.get_my_tier() = 'T3'::text) AND (approver_tier = 'T3'::text) AND (public.get_my_dept() = 'pessoas'::text)) OR (public.get_my_tier() = 'T4'::text)))`
- `audit_log.audit_insert_service` — `FOR INSERT TO service_role WITH CHECK (true)`
- `audit_log.audit_select` — `FOR SELECT TO authenticated USING (public.kph_is_founder_or_cfo())`
- `agent_runs.authenticated insert agent_runs` — `FOR INSERT TO authenticated WITH CHECK (true)`
- `orkestri_achados.authenticated insert orkestri_achados` — `FOR INSERT TO authenticated WITH CHECK (true)`
- `orquestrador_jobs.authenticated insert orquestrador_jobs` — `FOR INSERT TO authenticated WITH CHECK (true)`
- `agent_runs.authenticated read agent_runs` — `FOR SELECT TO authenticated USING (true)`
- `learning_machine_reports.authenticated read learning_machine_reports` — `FOR SELECT TO authenticated USING (true)`
- `orkestri_achados.authenticated read orkestri_achados` — `FOR SELECT TO authenticated USING (true)`
- `orquestrador_jobs.authenticated read orquestrador_jobs` — `FOR SELECT TO authenticated USING (true)`
- `learning_machine_reports.authenticated update learning_machine_reports` — `FOR UPDATE TO authenticated USING (true)`
- `learning_machine_reports.authenticated upsert learning_machine_reports` — `FOR INSERT TO authenticated WITH CHECK (true)`
- `avaliacao_ciclos.av_ciclos_read` — `FOR SELECT USING ((public.get_my_tier() = ANY (ARRAY['T3'::text, 'T4'::text])))`
- `avaliacao_ciclos.av_ciclos_write` — `USING ((public.get_my_tier() = ANY (ARRAY['T3'::text, 'T4'::text])))`
- `avaliacao_participantes.av_part_read` — `FOR SELECT USING (((avaliado_id IN ( SELECT employees.id FROM public.employees WHERE (employees.user_id = auth.uid()))) OR (avaliador_id IN ( SELECT employees.id FROM public.employees WHERE (employees.user_id = auth.uid()))) OR (public.get_my_tier() = ANY (ARRAY['T3'::text, 'T4'::text]))))`
- `avaliacao_participantes.av_part_write` — `USING ((public.get_my_tier() = ANY (ARRAY['T3'::text, 'T4'::text])))`
- `brand_links.brand_links_select` — `FOR SELECT USING (public.kph_has_role_for_brand(brand_id))`
- `brand_links.brand_links_write` — `USING (public.kph_is_founder_or_cfo())`
- `brands.brands_delete` — `FOR DELETE TO authenticated USING (public.kph_is_founder())`
- `brands.brands_insert` — `FOR INSERT TO authenticated WITH CHECK (public.kph_is_founder())`
- `brands.brands_select` — `FOR SELECT TO authenticated USING (public.kph_has_role_for_brand(id))`
- `brands.brands_update` — `FOR UPDATE TO authenticated USING ((public.kph_is_founder() OR (EXISTS ( SELECT 1 FROM (public.user_roles ur JOIN public.roles r ON ((r.id = ur.role_id))) WHERE ((ur.user_id = auth.uid()) AND (ur.brand_id = brands.id) AND (r.name = ANY (ARRAY['founder'::text, 'gm'::text]))))))) WITH CHECK ((public.kph_is_founder() OR (EXISTS ( SELECT 1 FROM (public.user_roles ur JOIN public.roles r ON ((r.id = ur.role_id))) WHERE ((ur.user_id = auth.uid()) AND (ur.brand_id = brands.id) AND (r.name = ANY (ARRAY['founder'::text, 'gm'::text])))))))`
- `brand_targets.bt_delete` — `FOR DELETE USING (public.kph_is_founder())`
- `brand_targets.bt_insert` — `FOR INSERT WITH CHECK (public.kph_has_role_for_brand(brand_id))`
- `brand_targets.bt_select` — `FOR SELECT USING (public.kph_has_role_for_brand(brand_id))`
- `brand_targets.bt_update` — `FOR UPDATE USING (public.kph_has_role_for_brand(brand_id)) WITH CHECK (public.kph_has_role_for_brand(brand_id))`
- `campaigns.campaigns_delete` — `FOR DELETE USING (public.kph_is_founder())`
- `campaigns.campaigns_insert` — `FOR INSERT WITH CHECK ((((brand_id IS NOT NULL) AND public.kph_has_role_for_brand(brand_id)) OR ((unit_id IS NOT NULL) AND public.kph_has_role_for_unit(unit_id))))`
- `campaigns.campaigns_select` — `FOR SELECT USING ((((brand_id IS NOT NULL) AND public.kph_has_role_for_brand(brand_id)) OR ((unit_id IS NOT NULL) AND public.kph_has_role_for_unit(unit_id)) OR public.kph_is_founder()))`
- `campaigns.campaigns_update` — `FOR UPDATE USING ((((brand_id IS NOT NULL) AND public.kph_has_role_for_brand(brand_id)) OR ((unit_id IS NOT NULL) AND public.kph_has_role_for_unit(unit_id))))`
- `candidate_pipeline.candidate_pipeline_read` — `FOR SELECT USING ((candidate_id IN ( SELECT candidates.id FROM public.candidates)))`
- `candidate_pipeline.candidate_pipeline_write` — `USING ((public.get_my_tier() = ANY (ARRAY['T3'::text, 'T4'::text])))`
- `candidates.candidates_delete` — `FOR DELETE USING (public.kph_is_founder())`
- `candidates.candidates_insert` — `FOR INSERT WITH CHECK ((EXISTS ( SELECT 1 FROM public.job_openings j WHERE ((j.id = candidates.job_opening_id) AND (((j.brand_id IS NOT NULL) AND public.kph_has_role_for_brand(j.brand_id)) OR ((j.unit_id IS NOT NULL) AND public.kph_has_role_for_unit(j.unit_id)))))))`
- `candidates.candidates_read` — `FOR SELECT USING ((public.get_my_tier() = ANY (ARRAY['T3'::text, 'T4'::text])))`
- `candidates.candidates_select` — `FOR SELECT TO authenticated USING ((EXISTS ( SELECT 1 FROM (public.user_roles ur JOIN public.roles r ON ((r.id = ur.role_id))) WHERE ((ur.user_id = auth.uid()) AND (r.name = ANY (ARRAY['founder'::text, 'gm'::text, 'pessoas'::text]))))))`
- `candidates.candidates_select_admin` — `FOR SELECT USING ((EXISTS ( SELECT 1 FROM public.job_openings j WHERE ((j.id = candidates.job_opening_id) AND (((j.brand_id IS NOT NULL) AND public.kph_has_role_for_brand(j.brand_id)) OR ((j.unit_id IS NOT NULL) AND public.kph_has_role_for_unit(j.unit_id)) OR public.kph_is_founder())))))`
- `candidates.candidates_select_public` — `FOR SELECT USING (true)`
- `candidates.candidates_update` — `FOR UPDATE USING (true)`
- `candidates.candidates_write` — `USING ((public.get_my_tier() = ANY (ARRAY['T3'::text, 'T4'::text])))`
- `candidatos_maya.candidatos_maya_select` — `FOR SELECT TO authenticated USING ((EXISTS ( SELECT 1 FROM (public.user_roles ur JOIN public.roles r ON ((r.id = ur.role_id))) WHERE ((ur.user_id = auth.uid()) AND (r.name = ANY (ARRAY['founder'::text, 'gm'::text, 'pessoas'::text]))))))`
- `cargo_grupos.cargo_grupos_select` — `FOR SELECT USING (true)`
- `candidate_avaliacao.cav_all` — `USING (true) WITH CHECK (true)`
- `cct_versions.cct_select` — `FOR SELECT TO authenticated USING (true)`
- `onboarding_checklist.checklist_access` — `USING ((run_id IN ( SELECT onboarding_runs.id FROM public.onboarding_runs WHERE (onboarding_runs.unit_id IN ( SELECT user_roles.unit_id FROM public.user_roles WHERE (user_roles.user_id = auth.uid()))))))`
- `avaliacao_participantes.ciclo_unit_access` — `USING ((ciclo_id IN ( SELECT avaliacao_ciclos.id FROM public.avaliacao_ciclos WHERE (avaliacao_ciclos.unit_id IN ( SELECT user_roles.unit_id FROM public.user_roles WHERE (user_roles.user_id = auth.uid()))))))`
- `client_interactions.client_interactions_delete` — `FOR DELETE USING (public.kph_is_founder())`
- `client_interactions.client_interactions_insert` — `FOR INSERT WITH CHECK ((EXISTS ( SELECT 1 FROM public.clients c WHERE ((c.id = client_interactions.client_id) AND public.kph_has_role_for_unit(c.unit_id)))))`
- `client_interactions.client_interactions_select` — `FOR SELECT USING ((EXISTS ( SELECT 1 FROM public.clients c WHERE ((c.id = client_interactions.client_id) AND public.kph_has_role_for_unit(c.unit_id)))))`
- `client_interactions.client_interactions_update` — `FOR UPDATE USING ((EXISTS ( SELECT 1 FROM public.clients c WHERE ((c.id = client_interactions.client_id) AND public.kph_has_role_for_unit(c.unit_id))))) WITH CHECK ((EXISTS ( SELECT 1 FROM public.clients c WHERE ((c.id = client_interactions.client_id) AND public.kph_has_role_for_unit(c.unit_id)))))`
- `clients.clients_delete` — `FOR DELETE USING (public.kph_is_founder())`
- `clients.clients_insert` — `FOR INSERT WITH CHECK (public.kph_has_role_for_unit(unit_id))`
- `clients.clients_select` — `FOR SELECT USING (public.kph_has_role_for_unit(unit_id))`
- `clients.clients_update` — `FOR UPDATE USING (public.kph_has_role_for_unit(unit_id)) WITH CHECK (public.kph_has_role_for_unit(unit_id))`
- `contratos_arquivos.contratos_arq_manage` — `TO service_role USING (true) WITH CHECK (true)`
- `contratos_arquivos.contratos_arq_read` — `FOR SELECT TO authenticated, anon USING (true)`
- `contratos.contratos_manage` — `TO service_role USING (true) WITH CHECK (true)`
- `contratos.contratos_read` — `FOR SELECT TO authenticated, anon USING (true)`
- `access_requests.deny_anon` — `TO anon USING (false)`
- `dependents.dependents_all` — `USING ((EXISTS ( SELECT 1 FROM public.employees e WHERE ((e.id = dependents.employee_id) AND public.kph_has_role_for_unit(e.unit_id)))))`
- `dependents.dependents_select` — `FOR SELECT USING ((EXISTS ( SELECT 1 FROM public.employees e WHERE ((e.id = dependents.employee_id) AND public.kph_has_role_for_unit(e.unit_id)))))`
- `documents.documents_delete` — `FOR DELETE USING (public.kph_is_founder())`
- `documents.documents_insert` — `FOR INSERT WITH CHECK (public.kph_has_role_for_unit(unit_id))`
- `documents.documents_select` — `FOR SELECT USING (public.kph_has_role_for_unit(unit_id))`
- `documents.documents_update` — `FOR UPDATE USING (public.kph_has_role_for_unit(unit_id))`
- `dre_despesa_detalhada.dre_despesa_manage` — `TO service_role USING (true) WITH CHECK (true)`
- `dre_despesa_detalhada.dre_despesa_read` — `FOR SELECT TO authenticated, anon USING (true)`
- `dre_faturamento_historico.dre_fat_manage` — `TO service_role USING (true) WITH CHECK (true)`
- `dre_faturamento_historico.dre_fat_read` — `FOR SELECT TO authenticated, anon USING (true)`
- `dre_folha.dre_folha_manage` — `TO service_role USING (true) WITH CHECK (true)`
- `dre_folha.dre_folha_read` — `FOR SELECT TO authenticated, anon USING (true)`
- `dre_gorjeta_mensal.dre_gorjeta_manage` — `TO service_role USING (true) WITH CHECK (true)`
- `dre_gorjeta_mensal.dre_gorjeta_read` — `FOR SELECT TO authenticated, anon USING (true)`
- `dre_indicadores.dre_indicadores_manage` — `TO service_role USING (true) WITH CHECK (true)`
- `dre_indicadores.dre_indicadores_read` — `FOR SELECT TO authenticated, anon USING (true)`
- `dre_mensal.dre_mensal_manage` — `TO service_role USING (true) WITH CHECK (true)`
- `dre_mensal.dre_mensal_read` — `FOR SELECT TO authenticated, anon USING (true)`
- `dre_receita_detalhada.dre_receita_manage` — `TO service_role USING (true) WITH CHECK (true)`
- `dre_receita_detalhada.dre_receita_read` — `FOR SELECT TO authenticated, anon USING (true)`
- `employee_documents.emp_docs_delete` — `FOR DELETE USING (public.kph_is_founder())`
- `employee_documents.emp_docs_insert` — `FOR INSERT WITH CHECK ((EXISTS ( SELECT 1 FROM public.employees e WHERE ((e.id = employee_documents.employee_id) AND public.kph_has_role_for_unit(e.unit_id)))))`
- `employee_documents.emp_docs_select` — `FOR SELECT USING ((EXISTS ( SELECT 1 FROM public.employees e WHERE ((e.id = employee_documents.employee_id) AND ((e.user_id = auth.uid()) OR public.kph_has_role_for_unit(e.unit_id))))))`
- `employee_documents.emp_docs_update` — `FOR UPDATE USING ((EXISTS ( SELECT 1 FROM public.employees e WHERE ((e.id = employee_documents.employee_id) AND public.kph_has_role_for_unit(e.unit_id)))))`
- `employee_auth.employee_auth_delete` — `FOR DELETE USING (public.kph_is_founder())`
- `employee_auth.employee_auth_insert` — `FOR INSERT WITH CHECK ((EXISTS ( SELECT 1 FROM public.employees e WHERE ((e.id = employee_auth.employee_id) AND public.kph_has_role_for_unit(e.unit_id)))))`
- `employee_auth.employee_auth_login` — `FOR SELECT USING (true)`
- `employee_auth.employee_auth_select` — `FOR SELECT USING ((EXISTS ( SELECT 1 FROM public.employees e WHERE ((e.id = employee_auth.employee_id) AND public.kph_has_role_for_unit(e.unit_id)))))`
- `employee_auth.employee_auth_update` — `FOR UPDATE USING ((EXISTS ( SELECT 1 FROM public.employees e WHERE ((e.id = employee_auth.employee_id) AND public.kph_has_role_for_unit(e.unit_id)))))`
- `employee_availability.employee_availability_all` — `USING (public.kph_has_role_for_unit(unit_id)) WITH CHECK (public.kph_has_role_for_unit(unit_id))`
- `employee_availability.employee_availability_select` — `FOR SELECT USING (public.kph_has_role_for_unit(unit_id))`
- `employees.employees_delete` — `FOR DELETE TO authenticated USING ((public.get_my_tier() = 'T4'::text))`
- `employees.employees_insert` — `FOR INSERT TO authenticated WITH CHECK ((public.get_my_tier() = ANY (ARRAY['T3'::text, 'T4'::text])))`
- `employees.employees_select` — `FOR SELECT TO authenticated USING (((public.get_my_tier() = ANY (ARRAY['T3'::text, 'T4'::text])) OR ((public.get_my_tier() = ANY (ARRAY['T2A'::text, 'T2B'::text])) AND (unit_id = public.get_my_unit())) OR (user_id = auth.uid())))`
- `employees.employees_self_select` — `FOR SELECT TO authenticated USING ((user_id = auth.uid()))`
- `employees.employees_update` — `FOR UPDATE TO authenticated USING (((public.get_my_tier() = ANY (ARRAY['T3'::text, 'T4'::text])) OR ((public.get_my_tier() = ANY (ARRAY['T2A'::text, 'T2B'::text])) AND (unit_id = public.get_my_unit()))))`
- `event_attachments.event_attachments_select` — `FOR SELECT USING ((EXISTS ( SELECT 1 FROM public.events e WHERE ((e.id = event_attachments.event_id) AND public.kph_has_role_for_brand(e.brand_id)))))`
- `event_attachments.event_attachments_write` — `USING ((EXISTS ( SELECT 1 FROM public.events e WHERE ((e.id = event_attachments.event_id) AND public.kph_can_write_event_brand(e.brand_id))))) WITH CHECK ((EXISTS ( SELECT 1 FROM public.events e WHERE ((e.id = event_attachments.event_id) AND public.kph_can_write_event_brand(e.brand_id)))))`
- `event_infra_items.event_infra_items_select` — `FOR SELECT USING ((EXISTS ( SELECT 1 FROM public.events e WHERE ((e.id = event_infra_items.event_id) AND public.kph_has_role_for_brand(e.brand_id)))))`
- `event_infra_items.event_infra_items_write` — `USING ((EXISTS ( SELECT 1 FROM public.events e WHERE ((e.id = event_infra_items.event_id) AND public.kph_can_write_event_brand(e.brand_id))))) WITH CHECK ((EXISTS ( SELECT 1 FROM public.events e WHERE ((e.id = event_infra_items.event_id) AND public.kph_can_write_event_brand(e.brand_id)))))`
- `event_menu_items.event_menu_items_select` — `FOR SELECT USING ((EXISTS ( SELECT 1 FROM public.events e WHERE ((e.id = event_menu_items.event_id) AND public.kph_has_role_for_brand(e.brand_id)))))`
- `event_menu_items.event_menu_items_write` — `USING ((EXISTS ( SELECT 1 FROM public.events e WHERE ((e.id = event_menu_items.event_id) AND public.kph_can_write_event_brand(e.brand_id))))) WITH CHECK ((EXISTS ( SELECT 1 FROM public.events e WHERE ((e.id = event_menu_items.event_id) AND public.kph_can_write_event_brand(e.brand_id)))))`
- `event_staff.event_staff_select` — `FOR SELECT USING ((EXISTS ( SELECT 1 FROM public.events e WHERE ((e.id = event_staff.event_id) AND public.kph_has_role_for_brand(e.brand_id)))))`
- `event_staff.event_staff_write` — `USING ((EXISTS ( SELECT 1 FROM public.events e WHERE ((e.id = event_staff.event_id) AND public.kph_can_write_event_brand(e.brand_id))))) WITH CHECK ((EXISTS ( SELECT 1 FROM public.events e WHERE ((e.id = event_staff.event_id) AND public.kph_can_write_event_brand(e.brand_id)))))`
- `event_status_log.event_status_log_select` — `FOR SELECT USING ((EXISTS ( SELECT 1 FROM public.events e WHERE ((e.id = event_status_log.event_id) AND public.kph_has_role_for_brand(e.brand_id)))))`
- `event_status_log.event_status_log_write` — `USING ((EXISTS ( SELECT 1 FROM public.events e WHERE ((e.id = event_status_log.event_id) AND public.kph_can_write_event_brand(e.brand_id))))) WITH CHECK ((EXISTS ( SELECT 1 FROM public.events e WHERE ((e.id = event_status_log.event_id) AND public.kph_can_write_event_brand(e.brand_id)))))`
- `events.events_delete` — `FOR DELETE USING (public.kph_can_delete_event_brand(brand_id))`
- `events.events_insert` — `FOR INSERT WITH CHECK (public.kph_can_write_event_brand(brand_id))`
- `events.events_select` — `FOR SELECT USING (public.kph_has_role_for_brand(brand_id))`
- `events.events_update` — `FOR UPDATE USING (public.kph_can_write_event_brand(brand_id))`
- `candidate_feedback_operacional.feedback_op_all` — `USING (true) WITH CHECK (true)`
- `feedbacks.feedbacks_insert` — `FOR INSERT WITH CHECK (((de_employee_id IN ( SELECT employees.id FROM public.employees WHERE (employees.user_id = auth.uid()))) OR (public.get_my_tier() = ANY (ARRAY['T3'::text, 'T4'::text]))))`
- `feedbacks.feedbacks_read` — `FOR SELECT USING (((para_employee_id IN ( SELECT employees.id FROM public.employees WHERE (employees.user_id = auth.uid()))) OR (de_employee_id IN ( SELECT employees.id FROM public.employees WHERE (employees.user_id = auth.uid()))) OR (public.get_my_tier() = ANY (ARRAY['T3'::text, 'T4'::text]))))`
- `gorjeta_distribuicao.gorjeta_distribuicao_delete` — `FOR DELETE TO authenticated USING ((public.get_my_tier() = ANY (ARRAY['T3'::text, 'T4'::text])))`
- `gorjeta_distribuicao.gorjeta_distribuicao_insert` — `FOR INSERT TO authenticated WITH CHECK ((public.get_my_tier() = ANY (ARRAY['T2A'::text, 'T2B'::text, 'T3'::text, 'T4'::text])))`
- `gorjeta_distribuicao.gorjeta_distribuicao_select` — `FOR SELECT TO authenticated USING (((public.get_my_tier() = ANY (ARRAY['T3'::text, 'T4'::text])) OR ((public.get_my_tier() = ANY (ARRAY['T2A'::text, 'T2B'::text])) AND (unit_id = public.get_my_unit())) OR (employee_id IN ( SELECT employees.id FROM public.employees WHERE (employees.user_id = auth.uid())))))`
- `gorjeta_distribuicao.gorjeta_distribuicao_update` — `FOR UPDATE TO authenticated USING ((public.get_my_tier() = ANY (ARRAY['T2A'::text, 'T2B'::text, 'T3'::text, 'T4'::text])))`
- `gorjeta_periodos.gorjeta_periodos_insert` — `FOR INSERT TO authenticated WITH CHECK ((public.get_my_tier() = ANY (ARRAY['T2A'::text, 'T2B'::text, 'T3'::text, 'T4'::text])))`
- `gorjeta_periodos.gorjeta_periodos_select` — `FOR SELECT TO authenticated USING (((public.get_my_tier() = ANY (ARRAY['T3'::text, 'T4'::text])) OR ((public.get_my_tier() = ANY (ARRAY['T2A'::text, 'T2B'::text])) AND (unit_id = public.get_my_unit()))))`
- `gorjeta_periodos.gorjeta_periodos_update` — `FOR UPDATE TO authenticated USING ((public.get_my_tier() = ANY (ARRAY['T2A'::text, 'T2B'::text, 'T3'::text, 'T4'::text])))`
- `groups.groups_delete` — `FOR DELETE TO authenticated USING (public.kph_is_founder())`
- `groups.groups_insert` — `FOR INSERT TO authenticated WITH CHECK (public.kph_is_founder())`
- `groups.groups_select` — `FOR SELECT TO authenticated USING (public.kph_has_role_for_group(id))`
- `groups.groups_update` — `FOR UPDATE TO authenticated USING (public.kph_is_founder()) WITH CHECK (public.kph_is_founder())`
- `hos_jobs.hos_jobs_read_t3` — `FOR SELECT USING ((public.get_my_tier() = ANY (ARRAY['T3'::text, 'T4'::text])))`
- `hos_jobs.hos_jobs_write_t4` — `USING ((public.get_my_tier() = 'T4'::text))`
- `import_logs.import_logs_insert` — `FOR INSERT WITH CHECK (public.kph_has_role_for_unit(unit_id))`
- `import_logs.import_logs_select` — `FOR SELECT USING ((public.kph_is_founder_or_cfo() OR public.kph_has_role_for_unit(unit_id)))`
- `ingredients.ingredients_delete` — `FOR DELETE USING (public.kph_is_founder())`
- `ingredients.ingredients_insert` — `FOR INSERT WITH CHECK (public.kph_has_role_for_group(group_id))`
- `ingredients.ingredients_select` — `FOR SELECT USING (public.kph_has_role_for_group(group_id))`
- `ingredients.ingredients_update` — `FOR UPDATE USING (public.kph_has_role_for_group(group_id)) WITH CHECK (public.kph_has_role_for_group(group_id))`
- `orkestri_leads.insert convidados` — `FOR INSERT TO anon WITH CHECK (true)`
- `gorjeta_cargo_pontos.insert gorjeta_cargo_pontos` — `FOR INSERT WITH CHECK (public.kph_has_role_for_unit(unit_id))`
- `gorjeta_dias.insert gorjeta_dias` — `FOR INSERT WITH CHECK (public.kph_has_role_for_unit(unit_id))`
- `job_opening_logs.insert job_opening_logs` — `FOR INSERT WITH CHECK ((EXISTS ( SELECT 1 FROM public.job_openings jo WHERE ((jo.id = job_opening_logs.opening_id) AND public.kph_has_role_for_unit(jo.unit_id)))))`
- `orkestri_leads.insert livre para convidados` — `FOR INSERT TO anon WITH CHECK (true)`
- `feedback.insert_feedback` — `FOR INSERT TO authenticated WITH CHECK ((user_id = auth.uid()))`
- `page_views.insert_own` — `FOR INSERT TO authenticated WITH CHECK ((user_id = auth.uid()))`
- `interviews.interviews_read` — `FOR SELECT USING ((public.get_my_tier() = ANY (ARRAY['T3'::text, 'T4'::text])))`
- `interviews.interviews_write` — `USING ((public.get_my_tier() = ANY (ARRAY['T3'::text, 'T4'::text])))`
- `project_invites.invites_own` — `USING ((auth.uid() = created_by))`
- `job_descriptions.job_descriptions_delete` — `FOR DELETE TO authenticated USING ((public.get_my_tier() = ANY (ARRAY['T3'::text, 'T4'::text])))`
- `job_descriptions.job_descriptions_insert` — `FOR INSERT TO authenticated WITH CHECK ((public.get_my_tier() = ANY (ARRAY['T3'::text, 'T4'::text])))`
- `job_descriptions.job_descriptions_select` — `FOR SELECT TO authenticated USING ((public.get_my_tier() = ANY (ARRAY['T2A'::text, 'T2B'::text, 'T3'::text, 'T4'::text])))`
- `job_descriptions.job_descriptions_update` — `FOR UPDATE TO authenticated USING ((public.get_my_tier() = ANY (ARRAY['T2A'::text, 'T2B'::text, 'T3'::text, 'T4'::text])))`
- `job_openings.job_openings_delete` — `FOR DELETE TO authenticated USING ((public.get_my_tier() = ANY (ARRAY['T3'::text, 'T4'::text])))`
- `job_openings.job_openings_insert` — `FOR INSERT TO authenticated WITH CHECK ((public.get_my_tier() = ANY (ARRAY['T2A'::text, 'T2B'::text, 'T3'::text, 'T4'::text])))`
- `job_openings.job_openings_select` — `FOR SELECT TO authenticated USING (((public.get_my_tier() = ANY (ARRAY['T3'::text, 'T4'::text])) OR ((public.get_my_tier() = ANY (ARRAY['T2A'::text, 'T2B'::text])) AND (unit_id = public.get_my_unit()))))`
- `job_openings.job_openings_update` — `FOR UPDATE TO authenticated USING ((public.get_my_tier() = ANY (ARRAY['T2A'::text, 'T2B'::text, 'T3'::text, 'T4'::text])))`
- `kph_alerts.kph_alerts_manage` — `USING (public.kph_is_founder_or_cfo()) WITH CHECK (public.kph_is_founder_or_cfo())`
- `kph_alerts.kph_alerts_select` — `FOR SELECT USING ((public.kph_is_founder_or_cfo() OR (entidade_id IN ( SELECT user_roles.unit_id FROM public.user_roles WHERE (user_roles.user_id = auth.uid())))))`
- `kph_insights.kph_insights_manage` — `USING (public.kph_is_founder_or_cfo()) WITH CHECK (public.kph_is_founder_or_cfo())`
- `kph_insights.kph_insights_select` — `FOR SELECT USING (public.kph_is_founder_or_cfo())`
- `kph_intelligence_scores.kph_intelligence_scores_manage` — `USING (public.kph_is_founder_or_cfo()) WITH CHECK (public.kph_is_founder_or_cfo())`
- `kph_intelligence_scores.kph_intelligence_scores_select` — `FOR SELECT USING (public.kph_is_founder_or_cfo())`
- `kph_learning_proposals.kph_learning_proposals_select` — `FOR SELECT TO authenticated USING (true)`
- `kph_learning_proposals.kph_learning_proposals_update_founder` — `FOR UPDATE TO authenticated USING (public.kph_is_founder()) WITH CHECK ((status = ANY (ARRAY['approved'::text, 'dismissed'::text])))`
- `orkestri_leads.leitura admin` — `FOR SELECT TO anon USING (true)`
- `orkestri_leads.leitura livre para admin` — `FOR SELECT TO anon USING (true)`
- `roadmap_items.manage_roadmap` — `USING (public.kph_is_founder_or_cfo()) WITH CHECK (public.kph_is_founder_or_cfo())`
- `mapa_conta_dre.mapa_conta_dre_manage` — `TO service_role USING (true) WITH CHECK (true)`
- `mapa_conta_dre.mapa_conta_dre_read` — `FOR SELECT TO authenticated, anon USING (true)`
- `project_members.members_own` — `USING (((auth.uid() = user_id) OR (auth.uid() = invited_by)))`
- `menu_items.menu_items_modify` — `USING (public.kph_has_role_for_brand(brand_id)) WITH CHECK (public.kph_has_role_for_brand(brand_id))`
- `menu_items.menu_items_select` — `FOR SELECT USING (public.kph_has_role_for_brand(brand_id))`
- `movimentacoes_rh.movimentacoes_read_t3` — `FOR SELECT USING ((public.get_my_tier() = ANY (ARRAY['T3'::text, 'T4'::text])))`
- `movimentacoes_rh.movimentacoes_write_t4` — `USING ((public.get_my_tier() = 'T4'::text))`
- `notifications.notif_select_own` — `FOR SELECT USING ((user_id = auth.uid()))`
- `notifications.notif_update_own` — `FOR UPDATE USING ((user_id = auth.uid())) WITH CHECK ((user_id = auth.uid()))`
- `notifications.notifications_own` — `USING ((auth.uid() = user_id))`
- `onboarding_checklist.ob_checklist_read` — `FOR SELECT USING (((run_id IN ( SELECT r.id FROM (public.onboarding_runs r JOIN public.employees e ON ((e.id = r.employee_id))) WHERE (e.user_id = auth.uid()))) OR (public.get_my_tier() = ANY (ARRAY['T3'::text, 'T4'::text]))))`
- `onboarding_checklist.ob_checklist_write` — `USING ((public.get_my_tier() = ANY (ARRAY['T3'::text, 'T4'::text])))`
- `onboarding_runs.ob_runs_read` — `FOR SELECT USING (((employee_id IN ( SELECT employees.id FROM public.employees WHERE (employees.user_id = auth.uid()))) OR (public.get_my_tier() = ANY (ARRAY['T3'::text, 'T4'::text]))))`
- `onboarding_runs.ob_runs_write` — `USING ((public.get_my_tier() = ANY (ARRAY['T3'::text, 'T4'::text])))`
- `onboarding_tarefas.ob_tarefas_read` — `FOR SELECT USING (true)`
- `onboarding_tarefas.ob_tarefas_write` — `USING ((public.get_my_tier() = ANY (ARRAY['T3'::text, 'T4'::text])))`
- `onboarding_templates.ob_templates_read` — `FOR SELECT USING ((public.get_my_tier() = ANY (ARRAY['T3'::text, 'T4'::text])))`
- `onboarding_templates.ob_templates_write` — `USING ((public.get_my_tier() = ANY (ARRAY['T3'::text, 'T4'::text])))`
- `origens_candidato.origens_candidato_select` — `FOR SELECT USING (true)`
- `overtime_records.overtime_delete` — `FOR DELETE USING (public.kph_is_founder())`
- `overtime_records.overtime_insert` — `FOR INSERT WITH CHECK (public.kph_has_role_for_unit(unit_id))`
- `overtime_records.overtime_select` — `FOR SELECT USING ((EXISTS ( SELECT 1 FROM public.employees e WHERE ((e.id = overtime_records.employee_id) AND public.kph_has_role_for_unit(e.unit_id)))))`
- `overtime_records.overtime_update` — `FOR UPDATE USING (public.kph_has_role_for_unit(unit_id))`
- `candidate_agendamentos.p_cand_agend_all` — `USING (true) WITH CHECK (true)`
- `candidate_feedback_operacional.p_cand_feedback_op_all` — `USING (true) WITH CHECK (true)`
- `payroll_rubricas.payroll_rubricas_read` — `FOR SELECT USING ((public.get_my_tier() = ANY (ARRAY['T3'::text, 'T4'::text, 'T5'::text, 'T6'::text])))`
- `payroll_rubricas.payroll_rubricas_write` — `USING ((public.get_my_tier() = ANY (ARRAY['T4'::text, 'T5'::text, 'T6'::text])))`
- `payslips.payslips_delete` — `FOR DELETE USING (public.kph_is_founder())`
- `payslips.payslips_insert` — `FOR INSERT WITH CHECK ((EXISTS ( SELECT 1 FROM public.employees e WHERE ((e.id = payslips.employee_id) AND public.kph_has_role_for_unit(e.unit_id)))))`
- `payslips.payslips_select` — `FOR SELECT USING ((EXISTS ( SELECT 1 FROM public.employees e WHERE ((e.id = payslips.employee_id) AND public.kph_has_role_for_unit(e.unit_id)))))`
- `payslips.payslips_update` — `FOR UPDATE USING ((EXISTS ( SELECT 1 FROM public.employees e WHERE ((e.id = payslips.employee_id) AND public.kph_has_role_for_unit(e.unit_id)))))`
- `pdi_metas.pdi_metas_access` — `USING ((pdi_id IN ( SELECT pdis.id FROM public.pdis WHERE (pdis.unit_id IN ( SELECT user_roles.unit_id FROM public.user_roles WHERE (user_roles.user_id = auth.uid()))))))`
- `pdi_metas.pdi_metas_select` — `FOR SELECT USING ((pdi_id IN ( SELECT pdis.id FROM public.pdis)))`
- `pdi_metas.pdi_metas_write_t3` — `USING ((public.get_my_tier() = ANY (ARRAY['T3'::text, 'T4'::text])))`
- `pdis.pdis_select_own` — `FOR SELECT USING (((employee_id IN ( SELECT employees.id FROM public.employees WHERE (employees.user_id = auth.uid()))) OR (public.get_my_tier() = ANY (ARRAY['T3'::text, 'T4'::text]))))`
- `pdis.pdis_write_t3` — `USING ((public.get_my_tier() = ANY (ARRAY['T3'::text, 'T4'::text])))`
- `performance_reviews.perf_reviews_read` — `FOR SELECT USING (((employee_id IN ( SELECT employees.id FROM public.employees WHERE (employees.user_id = auth.uid()))) OR (public.get_my_tier() = ANY (ARRAY['T3'::text, 'T4'::text]))))`
- `performance_reviews.perf_reviews_write` — `USING ((public.get_my_tier() = ANY (ARRAY['T3'::text, 'T4'::text])))`
- `performance_templates.perf_templates_read` — `FOR SELECT USING ((public.get_my_tier() = ANY (ARRAY['T3'::text, 'T4'::text])))`
- `performance_templates.perf_templates_write` — `USING ((public.get_my_tier() = 'T4'::text))`
- `payroll_fechamento_linha.pfl_read` — `FOR SELECT USING ((public.get_my_tier() = ANY (ARRAY['T3'::text, 'T4'::text, 'T5'::text, 'T6'::text])))`
- `payroll_fechamento_linha.pfl_write` — `USING ((public.get_my_tier() = ANY (ARRAY['T4'::text, 'T5'::text, 'T6'::text])))`
- `payroll_fechamento_periodo.pfp_read` — `FOR SELECT USING ((public.get_my_tier() = ANY (ARRAY['T3'::text, 'T4'::text, 'T5'::text, 'T6'::text])))`
- `payroll_fechamento_periodo.pfp_write` — `USING ((public.get_my_tier() = ANY (ARRAY['T4'::text, 'T5'::text, 'T6'::text])))`
- `purchase_orders.po_delete` — `FOR DELETE USING (public.kph_is_founder())`
- `purchase_orders.po_insert` — `FOR INSERT WITH CHECK (public.kph_has_role_for_unit(unit_id))`
- `purchase_order_items.po_items_delete` — `FOR DELETE USING (public.kph_is_founder())`
- `purchase_order_items.po_items_insert` — `FOR INSERT WITH CHECK ((EXISTS ( SELECT 1 FROM public.purchase_orders po WHERE ((po.id = purchase_order_items.order_id) AND public.kph_has_role_for_unit(po.unit_id)))))`
- `purchase_order_items.po_items_select` — `FOR SELECT USING ((EXISTS ( SELECT 1 FROM public.purchase_orders po WHERE ((po.id = purchase_order_items.order_id) AND public.kph_has_role_for_unit(po.unit_id)))))`
- `purchase_order_items.po_items_update` — `FOR UPDATE USING ((EXISTS ( SELECT 1 FROM public.purchase_orders po WHERE ((po.id = purchase_order_items.order_id) AND public.kph_has_role_for_unit(po.unit_id))))) WITH CHECK ((EXISTS ( SELECT 1 FROM public.purchase_orders po WHERE ((po.id = purchase_order_items.order_id) AND public.kph_has_role_for_unit(po.unit_id)))))`
- `purchase_orders.po_select` — `FOR SELECT USING (public.kph_has_role_for_unit(unit_id))`
- `purchase_orders.po_update` — `FOR UPDATE USING (public.kph_has_role_for_unit(unit_id)) WITH CHECK (public.kph_has_role_for_unit(unit_id))`
- `performance_reviews.pr_delete` — `FOR DELETE USING (public.kph_is_founder())`
- `performance_reviews.pr_insert` — `FOR INSERT WITH CHECK ((EXISTS ( SELECT 1 FROM public.employees e WHERE ((e.id = performance_reviews.employee_id) AND public.kph_has_role_for_unit(e.unit_id)))))`
- `performance_reviews.pr_select` — `FOR SELECT USING ((EXISTS ( SELECT 1 FROM public.employees e WHERE ((e.id = performance_reviews.employee_id) AND public.kph_has_role_for_unit(e.unit_id)))))`
- `performance_reviews.pr_update` — `FOR UPDATE USING ((EXISTS ( SELECT 1 FROM public.employees e WHERE ((e.id = performance_reviews.employee_id) AND public.kph_has_role_for_unit(e.unit_id))))) WITH CHECK ((EXISTS ( SELECT 1 FROM public.employees e WHERE ((e.id = performance_reviews.employee_id) AND public.kph_has_role_for_unit(e.unit_id)))))`
- `ingredient_price_history.price_history_select` — `FOR SELECT USING ((EXISTS ( SELECT 1 FROM public.ingredients i WHERE ((i.id = ingredient_price_history.ingredient_id) AND public.kph_has_role_for_group(i.group_id)))))`
- `produtos_relatorio.produtos_manage` — `TO service_role USING (true) WITH CHECK (true)`
- `produtos_relatorio.produtos_read` — `FOR SELECT TO authenticated, anon USING (true)`
- `profiles.profiles_own` — `USING ((auth.uid() = id))`
- `agent_prompt_versions.prompt_versions_read_t3` — `FOR SELECT USING ((public.get_my_tier() = ANY (ARRAY['T3'::text, 'T4'::text])))`
- `agent_prompt_versions.prompt_versions_write_t4` — `USING ((public.get_my_tier() = 'T4'::text))`
- `performance_templates.pt_delete` — `FOR DELETE USING (public.kph_is_founder())`
- `performance_templates.pt_insert` — `FOR INSERT WITH CHECK (public.kph_has_role_for_brand(brand_id))`
- `performance_templates.pt_select` — `FOR SELECT USING (public.kph_has_role_for_brand(brand_id))`
- `performance_templates.pt_update` — `FOR UPDATE USING (public.kph_has_role_for_brand(brand_id)) WITH CHECK (public.kph_has_role_for_brand(brand_id))`
- `time_clock_punches.punches_delete` — `FOR DELETE TO authenticated USING ((public.get_my_tier() = ANY (ARRAY['T3'::text, 'T4'::text])))`
- `time_clock_punches.punches_insert` — `FOR INSERT TO authenticated WITH CHECK (((public.get_my_tier() = ANY (ARRAY['T3'::text, 'T4'::text])) OR ((public.get_my_tier() = ANY (ARRAY['T2A'::text, 'T2B'::text])) AND (employee_id IN ( SELECT employees.id FROM public.employees WHERE (employees.unit_id = public.get_my_unit())))) OR (employee_id IN ( SELECT employees.id FROM public.employees WHERE (employees.user_id = auth.uid())))))`
- `time_clock_punches.punches_select` — `FOR SELECT TO authenticated USING (((public.get_my_tier() = ANY (ARRAY['T3'::text, 'T4'::text])) OR ((public.get_my_tier() = ANY (ARRAY['T2A'::text, 'T2B'::text])) AND (employee_id IN ( SELECT employees.id FROM public.employees WHERE (employees.unit_id = public.get_my_unit())))) OR (employee_id IN ( SELECT employees.id FROM public.employees WHERE (employees.user_id = auth.uid())))))`
- `time_clock_punches.punches_self_select` — `FOR SELECT TO authenticated USING ((employee_id IN ( SELECT employees.id FROM public.employees WHERE (employees.user_id = auth.uid()))))`
- `time_clock_punches.punches_update` — `FOR UPDATE TO authenticated USING ((public.get_my_tier() = ANY (ARRAY['T2A'::text, 'T2B'::text, 'T3'::text, 'T4'::text])))`
- `purchase_invoice_items.purchase_invoice_items_delete` — `FOR DELETE USING (public.kph_is_founder())`
- `purchase_invoice_items.purchase_invoice_items_insert` — `FOR INSERT WITH CHECK ((EXISTS ( SELECT 1 FROM public.purchase_invoices pi WHERE ((pi.id = purchase_invoice_items.purchase_invoice_id) AND public.kph_has_role_for_unit(pi.unit_id)))))`
- `purchase_invoice_items.purchase_invoice_items_select` — `FOR SELECT USING ((EXISTS ( SELECT 1 FROM public.purchase_invoices pi WHERE ((pi.id = purchase_invoice_items.purchase_invoice_id) AND public.kph_has_role_for_unit(pi.unit_id)))))`
- `purchase_invoice_items.purchase_invoice_items_update` — `FOR UPDATE USING ((EXISTS ( SELECT 1 FROM public.purchase_invoices pi WHERE ((pi.id = purchase_invoice_items.purchase_invoice_id) AND public.kph_has_role_for_unit(pi.unit_id))))) WITH CHECK ((EXISTS ( SELECT 1 FROM public.purchase_invoices pi WHERE ((pi.id = purchase_invoice_items.purchase_invoice_id) AND public.kph_has_role_for_unit(pi.unit_id)))))`
- `purchase_invoices.purchase_invoices_delete` — `FOR DELETE USING (public.kph_is_founder())`
- `purchase_invoices.purchase_invoices_insert` — `FOR INSERT WITH CHECK (public.kph_has_role_for_unit(unit_id))`
- `purchase_invoices.purchase_invoices_select` — `FOR SELECT USING (public.kph_has_role_for_unit(unit_id))`
- `purchase_invoices.purchase_invoices_update` — `FOR UPDATE USING (public.kph_has_role_for_unit(unit_id)) WITH CHECK (public.kph_has_role_for_unit(unit_id))`
- `quadro_ideal.quadro_ideal_insert` — `FOR INSERT WITH CHECK (true)`
- `quadro_ideal.quadro_ideal_select` — `FOR SELECT USING (true)`
- `quadro_ideal.quadro_ideal_update` — `FOR UPDATE USING (true)`
- `interview_questions.questions_delete` — `FOR DELETE USING (public.kph_is_founder())`
- `interview_questions.questions_insert` — `FOR INSERT WITH CHECK ((EXISTS ( SELECT 1 FROM public.job_openings j WHERE ((j.id = interview_questions.job_opening_id) AND (((j.brand_id IS NOT NULL) AND public.kph_has_role_for_brand(j.brand_id)) OR ((j.unit_id IS NOT NULL) AND public.kph_has_role_for_unit(j.unit_id)))))))`
- `interview_questions.questions_select` — `FOR SELECT USING (true)`
- `interview_questions.questions_update` — `FOR UPDATE USING ((EXISTS ( SELECT 1 FROM public.job_openings j WHERE ((j.id = interview_questions.job_opening_id) AND (((j.brand_id IS NOT NULL) AND public.kph_has_role_for_brand(j.brand_id)) OR ((j.unit_id IS NOT NULL) AND public.kph_has_role_for_unit(j.unit_id)))))))`
- `interview_responses.responses_delete` — `FOR DELETE USING (public.kph_is_founder())`
- `interview_responses.responses_insert` — `FOR INSERT WITH CHECK (true)`
- `interview_responses.responses_select` — `FOR SELECT USING (true)`
- `interview_responses.responses_update` — `FOR UPDATE USING (true)`
- `reunioes_1on1.reunioes_read` — `FOR SELECT USING (((gestor_id IN ( SELECT employees.id FROM public.employees WHERE (employees.user_id = auth.uid()))) OR (colaborador_id IN ( SELECT employees.id FROM public.employees WHERE (employees.user_id = auth.uid()))) OR (public.get_my_tier() = ANY (ARRAY['T3'::text, 'T4'::text]))))`
- `reunioes_1on1.reunioes_write_t2` — `USING (((gestor_id IN ( SELECT employees.id FROM public.employees WHERE (employees.user_id = auth.uid()))) OR (public.get_my_tier() = ANY (ARRAY['T3'::text, 'T4'::text]))))`
- `recipe_items.ri_delete` — `FOR DELETE USING ((menu_item_id IN ( SELECT menu_items.id FROM public.menu_items WHERE public.kph_has_role_for_brand(menu_items.brand_id))))`
- `recipe_items.ri_insert` — `FOR INSERT WITH CHECK ((menu_item_id IN ( SELECT menu_items.id FROM public.menu_items WHERE public.kph_has_role_for_brand(menu_items.brand_id))))`
- `recipe_items.ri_modify` — `USING ((menu_item_id IN ( SELECT menu_items.id FROM public.menu_items WHERE public.kph_has_role_for_brand(menu_items.brand_id)))) WITH CHECK ((menu_item_id IN ( SELECT menu_items.id FROM public.menu_items WHERE public.kph_has_role_for_brand(menu_items.brand_id))))`
- `recipe_items.ri_select` — `FOR SELECT USING ((menu_item_id IN ( SELECT menu_items.id FROM public.menu_items WHERE public.kph_has_role_for_brand(menu_items.brand_id))))`
- `recipe_items.ri_update` — `FOR UPDATE USING ((menu_item_id IN ( SELECT menu_items.id FROM public.menu_items WHERE public.kph_has_role_for_brand(menu_items.brand_id)))) WITH CHECK ((menu_item_id IN ( SELECT menu_items.id FROM public.menu_items WHERE public.kph_has_role_for_brand(menu_items.brand_id))))`
- `recipe_notes.rn_delete` — `FOR DELETE USING (public.kph_is_founder())`
- `recipe_notes.rn_insert` — `FOR INSERT WITH CHECK ((menu_item_id IN ( SELECT menu_items.id FROM public.menu_items WHERE public.kph_has_role_for_brand(menu_items.brand_id))))`
- `recipe_notes.rn_select` — `FOR SELECT USING ((menu_item_id IN ( SELECT menu_items.id FROM public.menu_items WHERE public.kph_has_role_for_brand(menu_items.brand_id))))`
- `roles.roles_mutate` — `TO authenticated USING (public.kph_is_founder()) WITH CHECK (public.kph_is_founder())`
- `roles.roles_select` — `FOR SELECT TO authenticated USING (true)`
- `score_events.score_insert` — `FOR INSERT WITH CHECK ((EXISTS ( SELECT 1 FROM public.employees e WHERE ((e.id = score_events.employee_id) AND public.kph_has_role_for_unit(e.unit_id)))))`
- `score_events.score_select` — `FOR SELECT USING ((EXISTS ( SELECT 1 FROM public.employees e WHERE ((e.id = score_events.employee_id) AND public.kph_has_role_for_unit(e.unit_id)))))`
- `gorjeta_cargo_pontos.select gorjeta_cargo_pontos` — `FOR SELECT USING (((unit_id IS NULL) OR public.kph_has_role_for_unit(unit_id)))`
- `gorjeta_dias.select gorjeta_dias` — `FOR SELECT USING (public.kph_has_role_for_unit(unit_id))`
- `job_opening_logs.select job_opening_logs` — `FOR SELECT USING ((EXISTS ( SELECT 1 FROM public.job_openings jo WHERE ((jo.id = job_opening_logs.opening_id) AND public.kph_has_role_for_unit(jo.unit_id)))))`
- `feedback.select_feedback` — `FOR SELECT USING (((user_id = auth.uid()) OR public.kph_is_founder_or_cfo()))`
- `page_views.select_own` — `FOR SELECT USING (((user_id = auth.uid()) OR public.kph_is_founder_or_cfo()))`
- `roadmap_items.select_roadmap` — `FOR SELECT TO authenticated USING (true)`
- `orquestrador_jobs.service update orquestrador_jobs` — `FOR UPDATE TO authenticated USING (true)`
- `orkestri_achados.service upsert orkestri_achados` — `FOR UPDATE TO authenticated USING (true)`
- `dre_linhas_detalhadas.service_role_all` — `TO service_role USING (true)`
- `documents.service_role_full_access` — `USING (true) WITH CHECK (true)`
- `shifts.shifts_all` — `USING (public.kph_has_role_for_unit(unit_id))`
- `shifts.shifts_select` — `FOR SELECT USING (public.kph_has_role_for_unit(unit_id))`
- `suppliers.suppliers_delete` — `FOR DELETE USING (public.kph_is_founder())`
- `suppliers.suppliers_insert` — `FOR INSERT WITH CHECK (public.kph_has_role_for_unit(unit_id))`
- `suppliers.suppliers_select` — `FOR SELECT USING (public.kph_has_role_for_unit(unit_id))`
- `suppliers.suppliers_update` — `FOR UPDATE USING (public.kph_has_role_for_unit(unit_id)) WITH CHECK (public.kph_has_role_for_unit(unit_id))`
- `attendance_summaries.t1_own` — `FOR SELECT USING ((employee_id = ( SELECT employees.id FROM public.employees WHERE (employees.user_id = auth.uid()))))`
- `employee_benefits.t1_own` — `FOR SELECT USING ((employee_id = ( SELECT employees.id FROM public.employees WHERE (employees.user_id = auth.uid()))))`
- `hour_bank.t1_own` — `FOR SELECT USING ((employee_id = ( SELECT employees.id FROM public.employees WHERE (employees.user_id = auth.uid()))))`
- `occupational_health.t1_own` — `FOR SELECT USING ((employee_id = ( SELECT employees.id FROM public.employees WHERE (employees.user_id = auth.uid()))))`
- `payslips.t1_own` — `FOR SELECT USING ((employee_id = ( SELECT employees.id FROM public.employees WHERE (employees.user_id = auth.uid()))))`
- `sick_leaves.t1_own` — `FOR SELECT USING ((employee_id = ( SELECT employees.id FROM public.employees WHERE (employees.user_id = auth.uid()))))`
- `vacation_schedules.t1_own` — `FOR SELECT USING ((employee_id = ( SELECT employees.id FROM public.employees WHERE (employees.user_id = auth.uid()))))`
- `work_schedules.t1_own` — `FOR SELECT USING ((employee_id = ( SELECT employees.id FROM public.employees WHERE (employees.user_id = auth.uid()))))`
- `document_templates.t2a_read` — `FOR SELECT USING ((public.get_my_tier() = ANY (ARRAY['T2A'::text, 'T2B'::text, 'T3'::text, 'T4'::text])))`
- `hr_policies.t2a_read` — `FOR SELECT USING (((public.get_my_tier() = ANY (ARRAY['T2A'::text, 'T2B'::text])) AND (unit_id = public.get_my_unit())))`
- `access_requests.t2a_see_pending` — `FOR SELECT TO authenticated USING (((public.get_my_tier() = 'T2A'::text) AND (approver_tier = 'T2A'::text) AND (( SELECT employees.unit_id FROM public.employees WHERE (employees.id = access_requests.employee_id)) = public.get_my_unit())))`
- `attendance_summaries.t3_dept` — `USING ((public.get_my_tier() = 'T3'::text))`
- `dho_tracking.t3_dept` — `USING ((public.get_my_tier() = 'T3'::text))`
- `disc_profiles.t3_dept` — `USING ((public.get_my_tier() = 'T3'::text))`
- `disciplinary_actions.t3_dept` — `USING ((public.get_my_tier() = 'T3'::text))`
- `employee_benefits.t3_dept` — `USING ((public.get_my_tier() = 'T3'::text))`
- `hour_bank.t3_dept` — `USING ((public.get_my_tier() = 'T3'::text))`
- `hr_policies.t3_dept` — `USING ((public.get_my_tier() = 'T3'::text))`
- `job_openings.t3_dept` — `USING ((public.get_my_tier() = 'T3'::text))`
- `occupational_health.t3_dept` — `USING (((public.get_my_tier() = 'T3'::text) AND (public.get_my_dept() = 'pessoas'::text)))`
- `payslips.t3_dept` — `USING (((public.get_my_tier() = 'T3'::text) AND (public.get_my_dept() = 'pessoas'::text)))`
- `sick_leaves.t3_dept` — `USING ((public.get_my_tier() = 'T3'::text))`
- `terminations.t3_dept` — `USING ((public.get_my_tier() = 'T3'::text))`
- `uniforms.t3_dept` — `USING ((public.get_my_tier() = 'T3'::text))`
- `vacation_schedules.t3_dept` — `USING ((public.get_my_tier() = 'T3'::text))`
- `work_schedules.t3_dept` — `USING ((public.get_my_tier() = 'T3'::text))`
- `access_requests.t3_see_pending` — `FOR SELECT TO authenticated USING (((public.get_my_tier() = 'T3'::text) AND (approver_tier = 'T3'::text) AND (public.get_my_dept() = 'pessoas'::text)))`
- `contractor_payments.t3_view` — `FOR SELECT USING ((public.get_my_tier() = ANY (ARRAY['T3'::text, 'T4'::text])))`
- `contractor_vacations.t3_view` — `FOR SELECT USING ((public.get_my_tier() = ANY (ARRAY['T3'::text, 'T4'::text])))`
- `contractors.t3_view` — `FOR SELECT USING ((public.get_my_tier() = ANY (ARRAY['T3'::text, 'T4'::text])))`
- `access_requests.t4_master` — `TO authenticated USING ((public.get_my_tier() = 'T4'::text))`
- `attendance_summaries.t4_master` — `USING ((public.get_my_tier() = 'T4'::text))`
- `contractor_payments.t4_master` — `USING ((public.get_my_tier() = 'T4'::text))`
- `contractor_vacations.t4_master` — `USING ((public.get_my_tier() = 'T4'::text))`
- `contractors.t4_master` — `USING ((public.get_my_tier() = 'T4'::text))`
- `dho_tracking.t4_master` — `USING ((public.get_my_tier() = 'T4'::text))`
- `disc_profiles.t4_master` — `USING ((public.get_my_tier() = 'T4'::text))`
- `disciplinary_actions.t4_master` — `USING ((public.get_my_tier() = 'T4'::text))`
- `document_templates.t4_master` — `USING ((public.get_my_tier() = 'T4'::text))`
- `employee_benefits.t4_master` — `USING ((public.get_my_tier() = 'T4'::text))`
- `hour_bank.t4_master` — `USING ((public.get_my_tier() = 'T4'::text))`
- `hr_policies.t4_master` — `USING ((public.get_my_tier() = 'T4'::text))`
- `job_openings.t4_master` — `USING ((public.get_my_tier() = 'T4'::text))`
- `occupational_health.t4_master` — `USING ((public.get_my_tier() = 'T4'::text))`
- `payslips.t4_master` — `USING ((public.get_my_tier() = 'T4'::text))`
- `sick_leaves.t4_master` — `USING ((public.get_my_tier() = 'T4'::text))`
- `terminations.t4_master` — `USING ((public.get_my_tier() = 'T4'::text))`
- `uniforms.t4_master` — `USING ((public.get_my_tier() = 'T4'::text))`
- `vacation_schedules.t4_master` — `USING ((public.get_my_tier() = 'T4'::text))`
- `work_schedules.t4_master` — `USING ((public.get_my_tier() = 'T4'::text))`
- `theo_tickets.theo_tickets_select` — `FOR SELECT TO authenticated USING ((public.kph_is_founder() OR (EXISTS ( SELECT 1 FROM public.employees e WHERE ((e.id = theo_tickets.employee_id) AND public.kph_has_role_for_unit(e.unit_id))))))`
- `time_records.time_records_delete` — `FOR DELETE USING (public.kph_is_founder())`
- `time_records.time_records_insert` — `FOR INSERT WITH CHECK (public.kph_has_role_for_unit(unit_id))`
- `time_records.time_records_select` — `FOR SELECT USING ((EXISTS ( SELECT 1 FROM public.employees e WHERE ((e.id = time_records.employee_id) AND public.kph_has_role_for_unit(e.unit_id)))))`
- `time_records.time_records_update` — `FOR UPDATE USING (public.kph_has_role_for_unit(unit_id))`
- `titulo_override.titulo_override_manage` — `TO service_role USING (true) WITH CHECK (true)`
- `titulo_override.titulo_override_read` — `FOR SELECT TO authenticated, anon USING (true)`
- `target_notes.tn_delete` — `FOR DELETE USING (public.kph_is_founder())`
- `target_notes.tn_insert` — `FOR INSERT WITH CHECK ((target_id IN ( SELECT brand_targets.id FROM public.brand_targets WHERE public.kph_has_role_for_brand(brand_targets.brand_id))))`
- `target_notes.tn_select` — `FOR SELECT USING ((target_id IN ( SELECT brand_targets.id FROM public.brand_targets WHERE public.kph_has_role_for_brand(brand_targets.brand_id))))`
- `training_records.tr_delete` — `FOR DELETE USING (public.kph_is_founder())`
- `training_records.tr_insert` — `FOR INSERT WITH CHECK ((EXISTS ( SELECT 1 FROM public.employees e WHERE ((e.id = training_records.employee_id) AND public.kph_has_role_for_unit(e.unit_id)))))`
- `training_records.tr_select` — `FOR SELECT USING ((EXISTS ( SELECT 1 FROM public.employees e WHERE ((e.id = training_records.employee_id) AND public.kph_has_role_for_unit(e.unit_id)))))`
- `training_records.tr_update` — `FOR UPDATE USING ((EXISTS ( SELECT 1 FROM public.employees e WHERE ((e.id = training_records.employee_id) AND public.kph_has_role_for_unit(e.unit_id))))) WITH CHECK ((EXISTS ( SELECT 1 FROM public.employees e WHERE ((e.id = training_records.employee_id) AND public.kph_has_role_for_unit(e.unit_id)))))`
- `training_records.training_records_read` — `FOR SELECT USING (((employee_id IN ( SELECT employees.id FROM public.employees WHERE (employees.user_id = auth.uid()))) OR (public.get_my_tier() = ANY (ARRAY['T3'::text, 'T4'::text]))))`
- `training_records.training_records_write` — `USING ((public.get_my_tier() = ANY (ARRAY['T3'::text, 'T4'::text])))`
- `training_templates.training_templates_read` — `FOR SELECT USING (true)`
- `training_templates.training_templates_write` — `USING ((public.get_my_tier() = ANY (ARRAY['T3'::text, 'T4'::text])))`
- `training_templates.tt_delete` — `FOR DELETE USING (public.kph_is_founder())`
- `training_templates.tt_insert` — `FOR INSERT WITH CHECK (public.kph_has_role_for_brand(brand_id))`
- `training_templates.tt_select` — `FOR SELECT USING (public.kph_has_role_for_brand(brand_id))`
- `training_templates.tt_update` — `FOR UPDATE USING (public.kph_has_role_for_brand(brand_id)) WITH CHECK (public.kph_has_role_for_brand(brand_id))`
- `price_quote_items.unit members can delete quote items` — `FOR DELETE USING ((EXISTS ( SELECT 1 FROM public.price_quotes q WHERE ((q.id = price_quote_items.quote_id) AND public.kph_has_role_for_unit(q.unit_id)))))`
- `ponto_mensal.unit members can insert ponto_mensal` — `FOR INSERT WITH CHECK (public.kph_has_role_for_unit(unit_id))`
- `price_quote_items.unit members can insert quote items` — `FOR INSERT WITH CHECK ((EXISTS ( SELECT 1 FROM public.price_quotes q WHERE ((q.id = price_quote_items.quote_id) AND public.kph_has_role_for_unit(q.unit_id)))))`
- `price_quotes.unit members can insert quotes` — `FOR INSERT WITH CHECK (public.kph_has_role_for_unit(unit_id))`
- `checklist_records.unit members can insert records` — `FOR INSERT WITH CHECK (public.kph_has_role_for_unit(unit_id))`
- `reservations.unit members can insert reservations` — `FOR INSERT WITH CHECK (public.kph_has_role_for_unit(unit_id))`
- `quality_checklists.unit members can manage checklists` — `USING (public.kph_has_role_for_unit(unit_id)) WITH CHECK (public.kph_has_role_for_unit(unit_id))`
- `ponto_mensal.unit members can select ponto_mensal` — `FOR SELECT USING (public.kph_has_role_for_unit(unit_id))`
- `price_quote_items.unit members can select quote items` — `FOR SELECT USING ((EXISTS ( SELECT 1 FROM public.price_quotes q WHERE ((q.id = price_quote_items.quote_id) AND public.kph_has_role_for_unit(q.unit_id)))))`
- `price_quotes.unit members can select quotes` — `FOR SELECT USING (public.kph_has_role_for_unit(unit_id))`
- `checklist_records.unit members can select records` — `FOR SELECT USING (public.kph_has_role_for_unit(unit_id))`
- `reservations.unit members can select reservations` — `FOR SELECT USING (public.kph_has_role_for_unit(unit_id))`
- `ponto_mensal.unit members can update ponto_mensal` — `FOR UPDATE USING (public.kph_has_role_for_unit(unit_id)) WITH CHECK (public.kph_has_role_for_unit(unit_id))`
- `price_quote_items.unit members can update quote items` — `FOR UPDATE USING ((EXISTS ( SELECT 1 FROM public.price_quotes q WHERE ((q.id = price_quote_items.quote_id) AND public.kph_has_role_for_unit(q.unit_id)))))`
- `price_quotes.unit members can update quotes` — `FOR UPDATE USING (public.kph_has_role_for_unit(unit_id)) WITH CHECK (public.kph_has_role_for_unit(unit_id))`
- `reservations.unit members can update reservations` — `FOR UPDATE USING (public.kph_has_role_for_unit(unit_id)) WITH CHECK (public.kph_has_role_for_unit(unit_id))`
- `avaliacao_ciclos.unit_access` — `USING ((unit_id IN ( SELECT user_roles.unit_id FROM public.user_roles WHERE (user_roles.user_id = auth.uid()))))`
- `feedbacks.unit_access` — `USING ((unit_id IN ( SELECT user_roles.unit_id FROM public.user_roles WHERE (user_roles.user_id = auth.uid()))))`
- `pdis.unit_access` — `USING ((unit_id IN ( SELECT user_roles.unit_id FROM public.user_roles WHERE (user_roles.user_id = auth.uid()))))`
- `reunioes_1on1.unit_access` — `USING ((unit_id IN ( SELECT user_roles.unit_id FROM public.user_roles WHERE (user_roles.user_id = auth.uid()))))`
- `onboarding_runs.unit_access_runs` — `USING ((unit_id IN ( SELECT user_roles.unit_id FROM public.user_roles WHERE (user_roles.user_id = auth.uid()))))`
- `onboarding_templates.unit_access_templates` — `USING ((unit_id IN ( SELECT user_roles.unit_id FROM public.user_roles WHERE (user_roles.user_id = auth.uid()))))`
- `units.units_delete` — `FOR DELETE TO authenticated USING (public.kph_is_founder())`
- `units.units_insert` — `FOR INSERT TO authenticated WITH CHECK (public.kph_is_founder())`
- `units.units_select` — `FOR SELECT TO authenticated USING (public.kph_has_role_for_unit(id))`
- `units.units_update` — `FOR UPDATE TO authenticated USING ((public.kph_is_founder() OR (EXISTS ( SELECT 1 FROM (public.user_roles ur JOIN public.roles r ON ((r.id = ur.role_id))) WHERE ((ur.user_id = auth.uid()) AND (ur.unit_id = units.id) AND (r.name = ANY (ARRAY['founder'::text, 'gm'::text]))))))) WITH CHECK ((public.kph_is_founder() OR (EXISTS ( SELECT 1 FROM (public.user_roles ur JOIN public.roles r ON ((r.id = ur.role_id))) WHERE ((ur.user_id = auth.uid()) AND (ur.unit_id = units.id) AND (r.name = ANY (ARRAY['founder'::text, 'gm'::text])))))))`
- `gorjeta_cargo_pontos.update gorjeta_cargo_pontos` — `FOR UPDATE USING (public.kph_has_role_for_unit(unit_id))`
- `feedback.update_status` — `FOR UPDATE USING (public.kph_is_founder_or_cfo()) WITH CHECK (public.kph_is_founder_or_cfo())`
- `user_roles.user_roles_delete` — `FOR DELETE TO authenticated USING (public.kph_is_founder())`
- `user_roles.user_roles_insert` — `FOR INSERT TO authenticated WITH CHECK (public.kph_is_founder())`
- `user_roles.user_roles_select` — `FOR SELECT TO authenticated USING (((user_id = auth.uid()) OR public.kph_is_founder()))`
- `user_roles.user_roles_update` — `FOR UPDATE TO authenticated USING (public.kph_is_founder()) WITH CHECK (public.kph_is_founder())`
- `vacations.vacations_delete` — `FOR DELETE USING (public.kph_is_founder())`
- `vacations.vacations_insert` — `FOR INSERT WITH CHECK (public.kph_has_role_for_unit(unit_id))`
- `vacations.vacations_select` — `FOR SELECT USING (public.kph_has_role_for_unit(unit_id))`
- `vacations.vacations_update` — `FOR UPDATE USING (public.kph_has_role_for_unit(unit_id))`
- `vendas_consolidado_periodo.vcp_manage` — `TO service_role USING (true) WITH CHECK (true)`
- `vendas_consolidado_periodo.vcp_read` — `FOR SELECT TO authenticated, anon USING (true)`
- `vendas_consolidado_produtos.vcprod_manage` — `TO service_role USING (true) WITH CHECK (true)`
- `vendas_consolidado_produtos.vcprod_read` — `FOR SELECT TO authenticated, anon USING (true)`
- `vendas_consolidado_ambiente.vendas_consolidado_ambiente_manage` — `TO service_role USING (true) WITH CHECK (true)`
- `vendas_consolidado_ambiente.vendas_consolidado_ambiente_read` — `FOR SELECT TO authenticated, anon USING (true)`
- `vendas_consolidado_dia_semana.vendas_consolidado_dia_semana_manage` — `TO service_role USING (true) WITH CHECK (true)`
- `vendas_consolidado_dia_semana.vendas_consolidado_dia_semana_read` — `FOR SELECT TO authenticated, anon USING (true)`
- `vendas_consolidado_funcionarios.vendas_consolidado_funcionarios_manage` — `TO service_role USING (true) WITH CHECK (true)`
- `vendas_consolidado_funcionarios.vendas_consolidado_funcionarios_read` — `FOR SELECT TO authenticated, anon USING (true)`
- `vendas_consolidado_mensal.vendas_consolidado_mensal_manage` — `TO service_role USING (true) WITH CHECK (true)`
- `vendas_consolidado_mensal.vendas_consolidado_mensal_read` — `FOR SELECT TO authenticated, anon USING (true)`
- `vendas_consolidado_resumo.vendas_consolidado_resumo_manage` — `TO service_role USING (true) WITH CHECK (true)`
- `vendas_consolidado_resumo.vendas_consolidado_resumo_read` — `FOR SELECT TO authenticated, anon USING (true)`
- `vendas_consolidado_turno.vendas_consolidado_turno_manage` — `TO service_role USING (true) WITH CHECK (true)`
- `vendas_consolidado_turno.vendas_consolidado_turno_read` — `FOR SELECT TO authenticated, anon USING (true)`
- `transport_vouchers.vt_delete` — `FOR DELETE USING (public.kph_is_founder())`
- `transport_vouchers.vt_insert` — `FOR INSERT WITH CHECK (public.kph_has_role_for_unit(unit_id))`
- `transport_vouchers.vt_select` — `FOR SELECT USING ((EXISTS ( SELECT 1 FROM public.employees e WHERE ((e.id = transport_vouchers.employee_id) AND public.kph_has_role_for_unit(e.unit_id)))))`
- `transport_vouchers.vt_update` — `FOR UPDATE USING (public.kph_has_role_for_unit(unit_id))`
- `warnings.warnings_all` — `USING ((EXISTS ( SELECT 1 FROM public.employees e WHERE ((e.id = warnings.employee_id) AND public.kph_has_role_for_unit(e.unit_id)))))`
<!-- AUTO-GENERATED:END -->
