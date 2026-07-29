# Estrutura das tabelas

Este catálogo é gerado exclusivamente de `database/schema.sql`. “Obrigatória” significa que a coluna possui `NOT NULL`; uma coluna opcional ainda pode estar sujeita a regras de aplicação ou constraints. Descrições de finalidade são inferências conservadoras baseadas apenas no nome e devem ser confirmadas com a equipe de negócio.

Para atualizar:

```powershell
node scripts/documentar-schema.js
```

<!-- AUTO-GENERATED:START -->
_Inventário automático: 228 tabelas no schema `public`._

## candidate_avaliacao

### Finalidade

Descrição inferida pela estrutura: armazena registros relacionados a `candidate avaliacao`. A finalidade de negócio exata deve ser confirmada com a equipe responsável.

### Colunas

| Coluna | Tipo | Obrigatória | Padrão | Observação |
|---|---|---|---|---|
| id | uuid | Sim | gen_random_uuid() | — |
| candidate_id | uuid | Sim | — | — |
| aderencia_skills | numeric(3,1) | Não | — | — |
| experiencia | numeric(3,1) | Não | — | — |
| entrevista_tec | numeric(3,1) | Não | — | — |
| entrevista_comp | numeric(3,1) | Não | — | — |
| aderencia_ia_sugerida | boolean | Não | false | — |
| experiencia_ia_sugerida | boolean | Não | false | — |
| nota_final | numeric(3,1) | Não | GENERATED ALWAYS AS (((((COALESCE(aderencia_skills, (0)::numeric) + COALESCE(experiencia, (0)::numeric)) + COALESCE(entrevista_tec, (0)::numeric)) + COALESCE(entrevista_comp, (0)::numeric)) / (4)::numeric)) STORED | Coluna gerada |
| avaliador_id | uuid | Não | — | — |
| created_at | timestamp with time zone | Não | now() | — |
| updated_at | timestamp with time zone | Não | now() | — |

### Chave primária
- `CONSTRAINT candidate_avaliacao_pkey PRIMARY KEY (id)`

### Relacionamentos
- `candidate_avaliacao_candidate_id_fkey`: `candidate_id` → `public.candidates(id)` (ON DELETE CASCADE)

### Constraints
- `CONSTRAINT candidate_avaliacao_aderencia_skills_check CHECK (((aderencia_skills >= (0)::numeric) AND (aderencia_skills <= (10)::numeric)))`
- `CONSTRAINT candidate_avaliacao_entrevista_comp_check CHECK (((entrevista_comp >= (0)::numeric) AND (entrevista_comp <= (10)::numeric)))`
- `CONSTRAINT candidate_avaliacao_entrevista_tec_check CHECK (((entrevista_tec >= (0)::numeric) AND (entrevista_tec <= (10)::numeric)))`
- `CONSTRAINT candidate_avaliacao_experiencia_check CHECK (((experiencia >= (0)::numeric) AND (experiencia <= (10)::numeric)))`
- `CONSTRAINT candidate_avaliacao_candidate_id_key UNIQUE (candidate_id)`

### Índices

Nenhum índice adicional identificado.

### Triggers

Nenhum trigger associado.

### Políticas RLS

RLS: **habilitada**.
- `cav_all`: `USING (true) WITH CHECK (true)`

## candidate_feedback_operacional

### Finalidade

Descrição inferida pela estrutura: armazena registros relacionados a `candidate feedback operacional`. A finalidade de negócio exata deve ser confirmada com a equipe responsável.

### Colunas

| Coluna | Tipo | Obrigatória | Padrão | Observação |
|---|---|---|---|---|
| id | uuid | Sim | gen_random_uuid() | — |
| candidate_id | uuid | Sim | — | — |
| agendamento_id | uuid | Não | — | — |
| postura_apresentacao | numeric(3,1) | Não | — | — |
| ritmo_sob_pressao | numeric(3,1) | Não | — | — |
| dominio_tecnico | numeric(3,1) | Não | — | — |
| higiene_seguranca | numeric(3,1) | Não | — | — |
| trabalho_em_equipe | numeric(3,1) | Não | — | — |
| nota_final | numeric(4,2) | Não | GENERATED ALWAYS AS ((((((COALESCE(postura_apresentacao, (0)::numeric) + COALESCE(ritmo_sob_pressao, (0)::numeric)) + COALESCE(dominio_tecnico, (0)::numeric)) + COALESCE(higiene_seguranca, (0)::numeric)) + COALESCE(trabalho_em_equipe, (0)::numeric)) / 5.0)) STORED | Coluna gerada |
| parecer | text | Não | — | — |
| avaliador_id | uuid | Não | — | — |
| created_at | timestamp with time zone | Sim | now() | — |
| updated_at | timestamp with time zone | Sim | now() | — |

### Chave primária
- `CONSTRAINT candidate_feedback_operacional_pkey PRIMARY KEY (id)`

### Relacionamentos
- `candidate_feedback_operacional_agendamento_id_fkey`: `agendamento_id` → `public.candidate_agendamentos(id)`
- `candidate_feedback_operacional_candidate_id_fkey`: `candidate_id` → `public.candidates(id)` (ON DELETE CASCADE)

### Constraints
- `CONSTRAINT cand_feedback_op_unique UNIQUE (candidate_id)`

### Índices

Nenhum índice adicional identificado.

### Triggers

Nenhum trigger associado.

### Políticas RLS

RLS: **habilitada**.
- `feedback_op_all`: `USING (true) WITH CHECK (true)`
- `p_cand_feedback_op_all`: `USING (true) WITH CHECK (true)`

## cargo_salarios

### Finalidade

Descrição inferida pela estrutura: armazena registros relacionados a `cargo salarios`. A finalidade de negócio exata deve ser confirmada com a equipe responsável.

### Colunas

| Coluna | Tipo | Obrigatória | Padrão | Observação |
|---|---|---|---|---|
| id | uuid | Sim | gen_random_uuid() | — |
| cargo_id | uuid | Sim | — | — |
| nivel | integer | Não | — | — |
| unit_id | uuid | Não | — | — |
| salario_min | numeric(10,2) | Não | — | — |
| salario_ref | numeric(10,2) | Não | — | — |
| salario_max | numeric(10,2) | Não | — | — |
| observacao | text | Não | — | — |
| created_at | timestamp with time zone | Sim | now() | — |
| updated_at | timestamp with time zone | Sim | now() | — |

### Chave primária
- `CONSTRAINT cargo_salarios_pkey PRIMARY KEY (id)`

### Relacionamentos
- `cargo_salarios_cargo_id_fkey`: `cargo_id` → `public.cargos(id)` (ON DELETE CASCADE)
- `cargo_salarios_unit_id_fkey`: `unit_id` → `public.units(id)` (ON DELETE CASCADE)

### Constraints
- `CONSTRAINT chk_faixa CHECK (((salario_min IS NULL) OR (salario_max IS NULL) OR (salario_min <= salario_max)))`
- `CONSTRAINT chk_nivel_valido CHECK (((nivel IS NULL) OR ((nivel >= 1) AND (nivel <= 3))))`

### Índices
- `uq_cargo_salario`: `USING btree (cargo_id, COALESCE(nivel, 0), COALESCE(unit_id, '00000000-0000-0000-0000-000000000000'::uuid))`

### Triggers

Nenhum trigger associado.

### Políticas RLS

RLS: **habilitada**.

Nenhuma política associada.

## Comments

### Finalidade

Descrição inferida pela estrutura: armazena registros relacionados a `Comments`. A finalidade de negócio exata deve ser confirmada com a equipe responsável.

### Colunas

| Coluna | Tipo | Obrigatória | Padrão | Observação |
|---|---|---|---|---|
| id | uuid | Sim | gen_random_uuid() | — |
| task_id | uuid | Sim | — | — |
| member_id | uuid | Sim | — | — |
| content | text | Sim | — | — |
| created_at | timestamp with time zone | Sim | timezone('utc'::text, now()) | — |

### Chave primária

Não identificada no dump.

### Relacionamentos
- `Comments_member_id_fkey`: `member_id` → `public.Team_Members(id)` (ON DELETE CASCADE)
- `Comments_task_id_fkey`: `task_id` → `public.Tasks(id)` (ON DELETE CASCADE)

### Constraints

Nenhuma constraint adicional identificada.

### Índices

Nenhum índice adicional identificado.

### Triggers

Nenhum trigger associado.

### Políticas RLS

RLS: **habilitada**.

Nenhuma política associada.

## Projects

### Finalidade

Descrição inferida pela estrutura: armazena registros relacionados a `Projects`. A finalidade de negócio exata deve ser confirmada com a equipe responsável.

### Colunas

| Coluna | Tipo | Obrigatória | Padrão | Observação |
|---|---|---|---|---|
| id | uuid | Sim | gen_random_uuid() | — |
| name | text | Sim | — | — |
| description | text | Não | — | — |
| created_at | timestamp with time zone | Sim | timezone('utc'::text, now()) | — |

### Chave primária
- `CONSTRAINT Projects_pkey PRIMARY KEY (id)`

### Relacionamentos

Nenhuma chave estrangeira identificada.

### Constraints

Nenhuma constraint adicional identificada.

### Índices

Nenhum índice adicional identificado.

### Triggers

Nenhum trigger associado.

### Políticas RLS

RLS: **habilitada**.

Nenhuma política associada.

## Task_Assignees

### Finalidade

Descrição inferida pela estrutura: armazena registros relacionados a `Task Assignees`. A finalidade de negócio exata deve ser confirmada com a equipe responsável.

### Colunas

| Coluna | Tipo | Obrigatória | Padrão | Observação |
|---|---|---|---|---|
| task_id | uuid | Sim | — | — |
| member_id | uuid | Sim | — | — |

### Chave primária
- `CONSTRAINT Task_Assignees_pkey PRIMARY KEY (task_id, member_id)`

### Relacionamentos
- `Task_Assignees_member_id_fkey`: `member_id` → `public.Team_Members(id)` (ON DELETE CASCADE)
- `Task_Assignees_task_id_fkey`: `task_id` → `public.Tasks(id)` (ON DELETE CASCADE)

### Constraints

Nenhuma constraint adicional identificada.

### Índices

Nenhum índice adicional identificado.

### Triggers

Nenhum trigger associado.

### Políticas RLS

RLS: **habilitada**.

Nenhuma política associada.

## Tasks

### Finalidade

Descrição inferida pela estrutura: armazena registros relacionados a `Tasks`. A finalidade de negócio exata deve ser confirmada com a equipe responsável.

### Colunas

| Coluna | Tipo | Obrigatória | Padrão | Observação |
|---|---|---|---|---|
| id | uuid | Sim | gen_random_uuid() | — |
| project_id | uuid | Sim | — | — |
| title | text | Sim | — | — |
| description | text | Não | — | — |
| due_date | date | Não | — | — |
| status | text | Sim | 'pendente'::text | — |

### Chave primária
- `CONSTRAINT Tasks_pkey PRIMARY KEY (id)`

### Relacionamentos
- `Tasks_project_id_fkey`: `project_id` → `public.Projects(id)` (ON DELETE CASCADE)

### Constraints
- `CONSTRAINT "Tasks_status_check" CHECK ((status = ANY (ARRAY['pendente'::text, 'concluído'::text])))`

### Índices

Nenhum índice adicional identificado.

### Triggers

Nenhum trigger associado.

### Políticas RLS

RLS: **habilitada**.

Nenhuma política associada.

## Team_Members

### Finalidade

Descrição inferida pela estrutura: armazena registros relacionados a `Team Members`. A finalidade de negócio exata deve ser confirmada com a equipe responsável.

### Colunas

| Coluna | Tipo | Obrigatória | Padrão | Observação |
|---|---|---|---|---|
| id | uuid | Sim | gen_random_uuid() | — |
| name | text | Sim | — | — |
| role | text | Sim | — | — |

### Chave primária
- `CONSTRAINT Team_Members_pkey PRIMARY KEY (id)`

### Relacionamentos

Nenhuma chave estrangeira identificada.

### Constraints

Nenhuma constraint adicional identificada.

### Índices

Nenhum índice adicional identificado.

### Triggers

Nenhum trigger associado.

### Políticas RLS

RLS: **habilitada**.

Nenhuma política associada.

## absences

### Finalidade

Descrição inferida pela estrutura: armazena registros relacionados a `absences`. A finalidade de negócio exata deve ser confirmada com a equipe responsável.

### Colunas

| Coluna | Tipo | Obrigatória | Padrão | Observação |
|---|---|---|---|---|
| id | uuid | Sim | gen_random_uuid() | — |
| employee_id | uuid | Sim | — | — |
| data | date | Sim | — | — |
| tipo | text | Sim | — | — |
| motivo | text | Não | — | — |
| score_impact | integer | Não | 0 | — |
| atestado_path | text | Não | — | — |
| created_at | timestamp with time zone | Não | now() | — |

### Chave primária
- `CONSTRAINT absences_pkey PRIMARY KEY (id)`

### Relacionamentos
- `absences_employee_id_fkey`: `employee_id` → `public.employees(id)` (ON DELETE CASCADE)

### Constraints

Nenhuma constraint adicional identificada.

### Índices
- `idx_absences_employee`: `USING btree (employee_id, data DESC)`

### Triggers

Nenhum trigger associado.

### Políticas RLS

RLS: **habilitada**.
- `absences_all`: `USING ((EXISTS ( SELECT 1 FROM public.employees e WHERE ((e.id = absences.employee_id) AND public.kph_has_role_for_unit(e.unit_id)))))`

## access_requests

### Finalidade

Descrição inferida pela estrutura: armazena registros relacionados a `access requests`. A finalidade de negócio exata deve ser confirmada com a equipe responsável.

### Colunas

| Coluna | Tipo | Obrigatória | Padrão | Observação |
|---|---|---|---|---|
| id | uuid | Sim | gen_random_uuid() | — |
| employee_id | uuid | Não | — | — |
| email | text | Sim | — | — |
| cpf | text | Sim | — | — |
| status | text | Sim | 'pending'::text | — |
| approver_tier | text | Sim | — | — |
| approver_id | uuid | Não | — | — |
| approved_at | timestamp with time zone | Não | — | — |
| rejected_reason | text | Não | — | — |
| created_at | timestamp with time zone | Não | now() | — |

### Chave primária
- `CONSTRAINT access_requests_pkey PRIMARY KEY (id)`

### Relacionamentos
- `access_requests_approver_id_fkey`: `approver_id` → `public.employees(id)`
- `access_requests_employee_id_fkey`: `employee_id` → `public.employees(id)` (ON DELETE CASCADE)

### Constraints
- `CONSTRAINT access_requests_approver_tier_check CHECK ((approver_tier = ANY (ARRAY['T2A'::text, 'T3'::text, 'T4'::text, 'T5'::text, 'T6'::text])))`
- `CONSTRAINT access_requests_status_check CHECK ((status = ANY (ARRAY['pending'::text, 'approved'::text, 'rejected'::text])))`

### Índices
- `access_requests_employee_idx`: `USING btree (employee_id)`
- `access_requests_status_idx`: `USING btree (status, approver_tier)`

### Triggers

Nenhum trigger associado.

### Políticas RLS

RLS: **habilitada**.
- `anyone_insert`: `FOR INSERT TO authenticated WITH CHECK (true)`
- `approver_update`: `FOR UPDATE TO authenticated USING ((((public.get_my_tier() = 'T2A'::text) AND (approver_tier = 'T2A'::text)) OR ((public.get_my_tier() = 'T3'::text) AND (approver_tier = 'T3'::text) AND (public.get_my_dept() = 'pessoas'::text)) OR (public.get_my_tier() = 'T4'::text)))`
- `deny_anon`: `TO anon USING (false)`
- `t2a_see_pending`: `FOR SELECT TO authenticated USING (((public.get_my_tier() = 'T2A'::text) AND (approver_tier = 'T2A'::text) AND (( SELECT employees.unit_id FROM public.employees WHERE (employees.id = access_requests.employee_id)) = public.get_my_unit())))`
- `t3_see_pending`: `FOR SELECT TO authenticated USING (((public.get_my_tier() = 'T3'::text) AND (approver_tier = 'T3'::text) AND (public.get_my_dept() = 'pessoas'::text)))`
- `t4_master`: `TO authenticated USING ((public.get_my_tier() = 'T4'::text))`

## action_plan_tasks

### Finalidade

Descrição inferida pela estrutura: armazena registros relacionados a `action plan tasks`. A finalidade de negócio exata deve ser confirmada com a equipe responsável.

### Colunas

| Coluna | Tipo | Obrigatória | Padrão | Observação |
|---|---|---|---|---|
| id | uuid | Sim | gen_random_uuid() | — |
| plan_id | uuid | Não | — | — |
| descricao | text | Sim | — | — |
| responsavel_id | uuid | Não | — | — |
| prazo | date | Não | — | — |
| status | text | Não | 'pendente'::text | — |
| created_at | timestamp with time zone | Não | now() | — |

### Chave primária
- `CONSTRAINT action_plan_tasks_pkey PRIMARY KEY (id)`

### Relacionamentos
- `action_plan_tasks_plan_id_fkey`: `plan_id` → `public.action_plans(id)` (ON DELETE CASCADE)

### Constraints

Nenhuma constraint adicional identificada.

### Índices

Nenhum índice adicional identificado.

### Triggers

Nenhum trigger associado.

### Políticas RLS

RLS: **habilitada**.

Nenhuma política associada.

## action_plans

### Finalidade

Descrição inferida pela estrutura: armazena registros relacionados a `action plans`. A finalidade de negócio exata deve ser confirmada com a equipe responsável.

### Colunas

| Coluna | Tipo | Obrigatória | Padrão | Observação |
|---|---|---|---|---|
| id | uuid | Sim | gen_random_uuid() | — |
| unit_id | uuid | Não | — | — |
| employee_id | uuid | Não | — | — |
| titulo | text | Sim | — | — |
| descricao | text | Não | — | — |
| origem | text | Não | — | — |
| origem_id | uuid | Não | — | — |
| status | text | Não | 'aberto'::text | — |
| prazo | date | Não | — | — |
| responsavel_id | uuid | Não | — | — |
| created_by | uuid | Não | — | — |
| created_at | timestamp with time zone | Não | now() | — |
| updated_at | timestamp with time zone | Não | now() | — |

### Chave primária
- `CONSTRAINT action_plans_pkey PRIMARY KEY (id)`

### Relacionamentos
- `action_plans_employee_id_fkey`: `employee_id` → `public.employees(id)`
- `action_plans_responsavel_id_fkey`: `responsavel_id` → `public.employees(id)`
- `action_plans_unit_id_fkey`: `unit_id` → `public.units(id)`

### Constraints

Nenhuma constraint adicional identificada.

### Índices

Nenhum índice adicional identificado.

### Triggers

Nenhum trigger associado.

### Políticas RLS

RLS: **habilitada**.

Nenhuma política associada.

## agent_conversations

### Finalidade

Descrição inferida pela estrutura: armazena registros relacionados a `agent conversations`. A finalidade de negócio exata deve ser confirmada com a equipe responsável.

### Colunas

| Coluna | Tipo | Obrigatória | Padrão | Observação |
|---|---|---|---|---|
| id | uuid | Sim | gen_random_uuid() | — |
| agent | text | Sim | — | — |
| phone | text | Sim | — | — |
| messages | jsonb | Sim | '[]'::jsonb | — |
| last_activity | timestamp with time zone | Não | now() | — |
| created_at | timestamp with time zone | Não | now() | — |
| status | text | Não | 'ativa'::text | — |
| operator_id | uuid | Não | — | — |
| operator_name | text | Não | — | — |
| session_type | text | Sim | 'whatsapp'::text | — |

### Chave primária
- `CONSTRAINT Comments_pkey PRIMARY KEY (id)`
- `CONSTRAINT agent_conversations_pkey PRIMARY KEY (id)`

### Relacionamentos

Nenhuma chave estrangeira identificada.

### Constraints
- `CONSTRAINT agent_conversations_session_type_check CHECK ((session_type = ANY (ARRAY['whatsapp'::text, 'web'::text])))`

### Índices
- `agent_conversations_agent_phone`: `USING btree (agent, phone)`
- `idx_agent_conversations_agent_status`: `USING btree (agent, status, last_activity DESC)`
- `idx_agent_conversations_last_activity`: `USING btree (last_activity DESC)`

### Triggers

Nenhum trigger associado.

### Políticas RLS

RLS: **habilitada**.
- `agent_conversations_deny_anon`: `TO anon USING (false)`
- `agent_conversations_select`: `FOR SELECT TO authenticated USING (((public.get_my_tier() = ANY (ARRAY['T2A'::text, 'T2B'::text, 'T3'::text, 'T4'::text])) OR (operator_id = auth.uid())))`
- `agent_conversations_update`: `FOR UPDATE TO authenticated USING (((public.get_my_tier() = ANY (ARRAY['T2A'::text, 'T2B'::text, 'T3'::text, 'T4'::text])) OR (operator_id = auth.uid())))`

## agent_metrics

### Finalidade

Descrição inferida pela estrutura: armazena registros relacionados a `agent metrics`. A finalidade de negócio exata deve ser confirmada com a equipe responsável.

### Colunas

| Coluna | Tipo | Obrigatória | Padrão | Observação |
|---|---|---|---|---|
| id | uuid | Sim | gen_random_uuid() | — |
| agent | text | Sim | — | — |
| phone_last4 | text | Não | — | — |
| input_tokens | integer | Não | — | — |
| output_tokens | integer | Não | — | — |
| cost_usd | numeric(10,6) | Não | — | — |
| latency_ms | integer | Não | — | — |
| intencao | text | Não | — | — |
| created_at | timestamp with time zone | Não | now() | — |

### Chave primária
- `CONSTRAINT agent_metrics_pkey PRIMARY KEY (id)`

### Relacionamentos

Nenhuma chave estrangeira identificada.

### Constraints

Nenhuma constraint adicional identificada.

### Índices
- `agent_metrics_agent_created`: `USING btree (agent, created_at DESC)`

### Triggers

Nenhum trigger associado.

### Políticas RLS

RLS: **habilitada**.

Nenhuma política associada.

## agent_prompt_versions

### Finalidade

Descrição inferida pela estrutura: armazena registros relacionados a `agent prompt versions`. A finalidade de negócio exata deve ser confirmada com a equipe responsável.

### Colunas

| Coluna | Tipo | Obrigatória | Padrão | Observação |
|---|---|---|---|---|
| id | uuid | Sim | gen_random_uuid() | — |
| agent | text | Sim | — | — |
| version | text | Sim | — | — |
| system_prompt | text | Sim | — | — |
| ativado_em | timestamp with time zone | Sim | now() | — |
| ativado_por | uuid | Não | — | — |
| nota | text | Não | — | — |
| ativo | boolean | Sim | false | — |
| created_at | timestamp with time zone | Sim | now() | — |

### Chave primária
- `CONSTRAINT agent_prompt_versions_pkey PRIMARY KEY (id)`

### Relacionamentos
- `agent_prompt_versions_ativado_por_fkey`: `ativado_por` → `auth.users(id)` (ON DELETE SET NULL)

### Constraints
- `CONSTRAINT agent_prompt_versions_agent_check CHECK ((agent = ANY (ARRAY['maya'::text, 'theo'::text])))`

### Índices
- `idx_agent_prompt_versions_agent`: `USING btree (agent)`
- `idx_agent_prompt_versions_ativo`: `USING btree (agent, ativo)`

### Triggers

Nenhum trigger associado.

### Políticas RLS

RLS: **habilitada**.
- `prompt_versions_read_t3`: `FOR SELECT USING ((public.get_my_tier() = ANY (ARRAY['T3'::text, 'T4'::text])))`
- `prompt_versions_write_t4`: `USING ((public.get_my_tier() = 'T4'::text))`

## agent_runs

### Finalidade

Descrição inferida pela estrutura: armazena registros relacionados a `agent runs`. A finalidade de negócio exata deve ser confirmada com a equipe responsável.

### Colunas

| Coluna | Tipo | Obrigatória | Padrão | Observação |
|---|---|---|---|---|
| id | uuid | Sim | gen_random_uuid() | — |
| agent_name | text | Sim | — | — |
| category | text | Sim | — | — |
| triggered_by | text | Não | — | — |
| status | text | Sim | 'completed'::text | — |
| duration_seconds | integer | Não | — | — |
| output_summary | text | Não | — | — |
| week_number | integer | Sim | — | — |
| year | integer | Sim | — | — |
| created_at | timestamp with time zone | Não | now() | — |

### Chave primária
- `CONSTRAINT agent_runs_pkey PRIMARY KEY (id)`

### Relacionamentos

Nenhuma chave estrangeira identificada.

### Constraints
- `CONSTRAINT agent_runs_status_check CHECK ((status = ANY (ARRAY['completed'::text, 'failed'::text, 'skipped'::text])))`

### Índices
- `agent_runs_agent_name_idx`: `USING btree (agent_name)`
- `agent_runs_created_at_idx`: `USING btree (created_at DESC)`
- `agent_runs_week_idx`: `USING btree (year, week_number)`

### Triggers

Nenhum trigger associado.

### Políticas RLS

RLS: **habilitada**.
- `authenticated insert agent_runs`: `FOR INSERT TO authenticated WITH CHECK (true)`
- `authenticated read agent_runs`: `FOR SELECT TO authenticated USING (true)`

## attendance_summaries

### Finalidade

Descrição inferida pela estrutura: armazena registros relacionados a `attendance summaries`. A finalidade de negócio exata deve ser confirmada com a equipe responsável.

### Colunas

| Coluna | Tipo | Obrigatória | Padrão | Observação |
|---|---|---|---|---|
| id | uuid | Sim | gen_random_uuid() | — |
| unit_id | uuid | Não | — | — |
| employee_id | uuid | Não | — | — |
| nome | text | Não | — | — |
| departamento | text | Não | — | — |
| cargo | text | Não | — | — |
| periodo_inicio | date | Sim | — | — |
| periodo_fim | date | Sim | — | — |
| horas_trabalhadas_min | integer | Sim | 0 | — |
| adicional_noturno_min | integer | Sim | 0 | — |
| documento_ref | text | Não | — | — |
| created_at | timestamp with time zone | Sim | now() | — |

### Chave primária
- `CONSTRAINT attendance_summaries_pkey PRIMARY KEY (id)`

### Relacionamentos
- `attendance_summaries_employee_id_fkey`: `employee_id` → `public.employees(id)`
- `attendance_summaries_unit_id_fkey`: `unit_id` → `public.units(id)`

### Constraints
- `CONSTRAINT attendance_summaries_employee_id_periodo_inicio_periodo_fim_key UNIQUE (employee_id, periodo_inicio, periodo_fim)`

### Índices

Nenhum índice adicional identificado.

### Triggers

Nenhum trigger associado.

### Políticas RLS

RLS: **habilitada**.
- `t1_own`: `FOR SELECT USING ((employee_id = ( SELECT employees.id FROM public.employees WHERE (employees.user_id = auth.uid()))))`
- `t3_dept`: `USING ((public.get_my_tier() = 'T3'::text))`
- `t4_master`: `USING ((public.get_my_tier() = 'T4'::text))`

## audit_log

### Finalidade

Descrição inferida pela estrutura: armazena registros relacionados a `audit log`. A finalidade de negócio exata deve ser confirmada com a equipe responsável.

### Colunas

| Coluna | Tipo | Obrigatória | Padrão | Observação |
|---|---|---|---|---|
| id | uuid | Sim | gen_random_uuid() | — |
| user_id | uuid | Não | — | — |
| action | text | Sim | — | — |
| resource | text | Sim | — | — |
| resource_id | text | Não | — | — |
| old_data | jsonb | Não | — | — |
| new_data | jsonb | Não | — | — |
| ip_address | text | Não | — | — |
| created_at | timestamp with time zone | Não | now() | — |

### Chave primária
- `CONSTRAINT audit_log_pkey PRIMARY KEY (id)`

### Relacionamentos
- `audit_log_user_id_fkey`: `user_id` → `auth.users(id)`

### Constraints

Nenhuma constraint adicional identificada.

### Índices
- `idx_audit_resource`: `USING btree (resource, resource_id)`
- `idx_audit_user`: `USING btree (user_id, created_at DESC)`

### Triggers

Nenhum trigger associado.

### Políticas RLS

RLS: **habilitada**.
- `audit_insert_service`: `FOR INSERT TO service_role WITH CHECK (true)`
- `audit_select`: `FOR SELECT TO authenticated USING (public.kph_is_founder_or_cfo())`

## auditoria_nutricional

### Finalidade

Descrição inferida pela estrutura: armazena registros relacionados a `auditoria nutricional`. A finalidade de negócio exata deve ser confirmada com a equipe responsável.

### Colunas

| Coluna | Tipo | Obrigatória | Padrão | Observação |
|---|---|---|---|---|
| id | integer | Sim | — | — |
| data_inspecao | date | Sim | — | — |
| nota | numeric | Não | — | — |
| status | text | Não | — | — |
| local | text | Não | — | — |
| tipo_inspecao | text | Não | — | — |
| criado_em | timestamp with time zone | Não | now() | — |

### Chave primária
- `CONSTRAINT auditoria_nutricional_pkey PRIMARY KEY (id)`

### Relacionamentos

Nenhuma chave estrangeira identificada.

### Constraints

Nenhuma constraint adicional identificada.

### Índices

Nenhum índice adicional identificado.

### Triggers

Nenhum trigger associado.

### Políticas RLS

RLS: **não habilitada no dump**.

Nenhuma política associada.

## avaliacao_ciclos

### Finalidade

Descrição inferida pela estrutura: armazena registros relacionados a `avaliacao ciclos`. A finalidade de negócio exata deve ser confirmada com a equipe responsável.

### Colunas

| Coluna | Tipo | Obrigatória | Padrão | Observação |
|---|---|---|---|---|
| id | uuid | Sim | gen_random_uuid() | — |
| unit_id | uuid | Sim | — | — |
| nome | text | Sim | — | — |
| template_id | uuid | Não | — | — |
| status | text | Sim | 'aberto'::text | — |
| data_inicio | date | Sim | — | — |
| data_fim | date | Sim | — | — |
| created_by | uuid | Não | — | — |
| created_at | timestamp with time zone | Não | now() | — |

### Chave primária
- `CONSTRAINT avaliacao_ciclos_pkey PRIMARY KEY (id)`

### Relacionamentos
- `avaliacao_ciclos_created_by_fkey`: `created_by` → `auth.users(id)`
- `avaliacao_ciclos_template_id_fkey`: `template_id` → `public.performance_templates(id)`
- `avaliacao_ciclos_unit_id_fkey`: `unit_id` → `public.units(id)`

### Constraints
- `CONSTRAINT avaliacao_ciclos_status_check CHECK ((status = ANY (ARRAY['aberto'::text, 'em_andamento'::text, 'encerrado'::text])))`

### Índices
- `idx_av_ciclos_unit`: `USING btree (unit_id)`

### Triggers

Nenhum trigger associado.

### Políticas RLS

RLS: **habilitada**.
- `av_ciclos_read`: `FOR SELECT USING ((public.get_my_tier() = ANY (ARRAY['T3'::text, 'T4'::text])))`
- `av_ciclos_write`: `USING ((public.get_my_tier() = ANY (ARRAY['T3'::text, 'T4'::text])))`
- `unit_access`: `USING ((unit_id IN ( SELECT user_roles.unit_id FROM public.user_roles WHERE (user_roles.user_id = auth.uid()))))`

## avaliacao_participantes

### Finalidade

Descrição inferida pela estrutura: armazena registros relacionados a `avaliacao participantes`. A finalidade de negócio exata deve ser confirmada com a equipe responsável.

### Colunas

| Coluna | Tipo | Obrigatória | Padrão | Observação |
|---|---|---|---|---|
| id | uuid | Sim | gen_random_uuid() | — |
| ciclo_id | uuid | Sim | — | — |
| avaliado_id | uuid | Sim | — | — |
| avaliador_id | uuid | Sim | — | — |
| tipo_avaliador | text | Sim | — | — |
| status | text | Não | 'pendente'::text | — |
| review_id | uuid | Não | — | — |

### Chave primária
- `CONSTRAINT avaliacao_participantes_pkey PRIMARY KEY (id)`

### Relacionamentos
- `avaliacao_participantes_avaliado_id_fkey`: `avaliado_id` → `public.employees(id)`
- `avaliacao_participantes_avaliador_id_fkey`: `avaliador_id` → `public.employees(id)`
- `avaliacao_participantes_ciclo_id_fkey`: `ciclo_id` → `public.avaliacao_ciclos(id)` (ON DELETE CASCADE)
- `avaliacao_participantes_review_id_fkey`: `review_id` → `public.performance_reviews(id)`

### Constraints
- `CONSTRAINT avaliacao_participantes_status_check CHECK ((status = ANY (ARRAY['pendente'::text, 'concluido'::text])))`
- `CONSTRAINT avaliacao_participantes_tipo_avaliador_check CHECK ((tipo_avaliador = ANY (ARRAY['autoavaliacao'::text, 'par'::text, 'gestor'::text, 'liderado'::text])))`
- `CONSTRAINT avaliacao_unica UNIQUE (ciclo_id, avaliado_id, avaliador_id)`

### Índices
- `idx_av_part_avaliado`: `USING btree (avaliado_id)`
- `idx_av_part_ciclo`: `USING btree (ciclo_id)`

### Triggers

Nenhum trigger associado.

### Políticas RLS

RLS: **habilitada**.
- `av_part_read`: `FOR SELECT USING (((avaliado_id IN ( SELECT employees.id FROM public.employees WHERE (employees.user_id = auth.uid()))) OR (avaliador_id IN ( SELECT employees.id FROM public.employees WHERE (employees.user_id = auth.uid()))) OR (public.get_my_tier() = ANY (ARRAY['T3'::text, 'T4'::text]))))`
- `av_part_write`: `USING ((public.get_my_tier() = ANY (ARRAY['T3'::text, 'T4'::text])))`
- `ciclo_unit_access`: `USING ((ciclo_id IN ( SELECT avaliacao_ciclos.id FROM public.avaliacao_ciclos WHERE (avaliacao_ciclos.unit_id IN ( SELECT user_roles.unit_id FROM public.user_roles WHERE (user_roles.user_id = auth.uid()))))))`

## brand_links

### Finalidade

Descrição inferida pela estrutura: armazena registros relacionados a `brand links`. A finalidade de negócio exata deve ser confirmada com a equipe responsável.

### Colunas

| Coluna | Tipo | Obrigatória | Padrão | Observação |
|---|---|---|---|---|
| id | uuid | Sim | gen_random_uuid() | — |
| brand_id | uuid | Sim | — | — |
| kind | text | Sim | — | — |
| url | text | Sim | — | — |
| label | text | Não | — | — |
| ordem | integer | Não | 0 | — |
| created_at | timestamp with time zone | Não | now() | — |

### Chave primária
- `CONSTRAINT brand_links_pkey PRIMARY KEY (id)`

### Relacionamentos
- `brand_links_brand_id_fkey`: `brand_id` → `public.brands(id)` (ON DELETE CASCADE)

### Constraints

Nenhuma constraint adicional identificada.

### Índices
- `idx_brand_links_brand`: `USING btree (brand_id, ordem)`

### Triggers

Nenhum trigger associado.

### Políticas RLS

RLS: **habilitada**.
- `brand_links_select`: `FOR SELECT USING (public.kph_has_role_for_brand(brand_id))`
- `brand_links_write`: `USING (public.kph_is_founder_or_cfo())`

## brand_targets

### Finalidade

Descrição inferida pela estrutura: armazena registros relacionados a `brand targets`. A finalidade de negócio exata deve ser confirmada com a equipe responsável.

### Colunas

| Coluna | Tipo | Obrigatória | Padrão | Observação |
|---|---|---|---|---|
| id | uuid | Sim | gen_random_uuid() | — |
| brand_id | uuid | Sim | — | — |
| unit_id | uuid | Não | — | — |
| periodo | text | Sim | — | — |
| receita_meta | numeric(12,2) | Não | — | — |
| cmv_meta_pct | numeric(5,2) | Não | — | — |
| prime_cost_meta_pct | numeric(5,2) | Não | — | — |
| ticket_medio_meta | numeric(10,2) | Não | — | — |
| nps_meta | numeric(5,2) | Não | — | — |
| headcount_meta | integer | Não | — | — |
| eventos_meta | integer | Não | — | — |
| created_by | uuid | Não | — | — |
| created_at | timestamp with time zone | Não | now() | — |
| updated_at | timestamp with time zone | Não | now() | — |

### Chave primária
- `CONSTRAINT brand_targets_pkey PRIMARY KEY (id)`

### Relacionamentos
- `brand_targets_brand_id_fkey`: `brand_id` → `public.brands(id)`
- `brand_targets_created_by_fkey`: `created_by` → `auth.users(id)`
- `brand_targets_unit_id_fkey`: `unit_id` → `public.units(id)`

### Constraints
- `CONSTRAINT brand_targets_brand_id_periodo_key UNIQUE (brand_id, periodo)`

### Índices
- `idx_brand_targets_brand`: `USING btree (brand_id)`
- `idx_brand_targets_periodo`: `USING btree (periodo)`
- `idx_brand_targets_unit`: `USING btree (unit_id)`

### Triggers
- `trg_brand_targets_updated_at`: `BEFORE UPDATE FOR EACH ROW EXECUTE FUNCTION public.update_updated_at_column()`

### Políticas RLS

RLS: **habilitada**.
- `bt_delete`: `FOR DELETE USING (public.kph_is_founder())`
- `bt_insert`: `FOR INSERT WITH CHECK (public.kph_has_role_for_brand(brand_id))`
- `bt_select`: `FOR SELECT USING (public.kph_has_role_for_brand(brand_id))`
- `bt_update`: `FOR UPDATE USING (public.kph_has_role_for_brand(brand_id)) WITH CHECK (public.kph_has_role_for_brand(brand_id))`

## brands

### Finalidade

Descrição inferida pela estrutura: armazena registros relacionados a `brands`. A finalidade de negócio exata deve ser confirmada com a equipe responsável.

### Colunas

| Coluna | Tipo | Obrigatória | Padrão | Observação |
|---|---|---|---|---|
| id | uuid | Sim | gen_random_uuid() | — |
| group_id | uuid | Não | — | — |
| name | text | Sim | — | — |
| slug | text | Sim | — | — |
| color | text | Não | '#D4A574'::text | — |
| active | boolean | Não | true | — |
| created_at | timestamp with time zone | Não | now() | — |

### Chave primária
- `CONSTRAINT brands_pkey PRIMARY KEY (id)`

### Relacionamentos
- `brands_group_id_fkey`: `group_id` → `public.groups(id)` (ON DELETE CASCADE)

### Constraints
- `CONSTRAINT brands_slug_key UNIQUE (slug)`

### Índices
- `idx_brands_group`: `USING btree (group_id)`

### Triggers

Nenhum trigger associado.

### Políticas RLS

RLS: **habilitada**.
- `brands_delete`: `FOR DELETE TO authenticated USING (public.kph_is_founder())`
- `brands_insert`: `FOR INSERT TO authenticated WITH CHECK (public.kph_is_founder())`
- `brands_select`: `FOR SELECT TO authenticated USING (public.kph_has_role_for_brand(id))`
- `brands_update`: `FOR UPDATE TO authenticated USING ((public.kph_is_founder() OR (EXISTS ( SELECT 1 FROM (public.user_roles ur JOIN public.roles r ON ((r.id = ur.role_id))) WHERE ((ur.user_id = auth.uid()) AND (ur.brand_id = brands.id) AND (r.name = ANY (ARRAY['founder'::text, 'gm'::text]))))))) WITH CHECK ((public.kph_is_founder() OR (EXISTS ( SELECT 1 FROM (public.user_roles ur JOIN public.roles r ON ((r.id = ur.role_id))) WHERE ((ur.user_id = auth.uid()) AND (ur.brand_id = brands.id) AND (r.name = ANY (ARRAY['founder'::text, 'gm'::text])))))))`

## buckets

### Finalidade

Descrição inferida pela estrutura: armazena registros relacionados a `buckets`. A finalidade de negócio exata deve ser confirmada com a equipe responsável.

### Colunas

| Coluna | Tipo | Obrigatória | Padrão | Observação |
|---|---|---|---|---|
| id | uuid | Sim | gen_random_uuid() | — |
| project_id | uuid | Sim | — | — |
| name | text | Sim | — | — |
| created_at | timestamp with time zone | Sim | timezone('utc'::text, now()) | — |

### Chave primária
- `CONSTRAINT buckets_pkey PRIMARY KEY (id)`

### Relacionamentos
- `buckets_project_id_fkey`: `project_id` → `public.projects(id)` (ON DELETE CASCADE)

### Constraints

Nenhuma constraint adicional identificada.

### Índices

Nenhum índice adicional identificado.

### Triggers

Nenhum trigger associado.

### Políticas RLS

RLS: **não habilitada no dump**.

Nenhuma política associada.

## campaigns

### Finalidade

Descrição inferida pela estrutura: armazena registros relacionados a `campaigns`. A finalidade de negócio exata deve ser confirmada com a equipe responsável.

### Colunas

| Coluna | Tipo | Obrigatória | Padrão | Observação |
|---|---|---|---|---|
| id | uuid | Sim | gen_random_uuid() | — |
| brand_id | uuid | Não | — | — |
| unit_id | uuid | Não | — | — |
| title | text | Sim | — | — |
| description | text | Não | — | — |
| image_url | text | Não | — | — |
| category | text | Sim | — | — |
| target | text | Sim | 'all'::text | — |
| target_value | text | Não | — | — |
| active | boolean | Não | true | — |
| starts_at | date | Não | — | — |
| ends_at | date | Não | — | — |
| created_by | uuid | Não | — | — |
| created_at | timestamp with time zone | Não | now() | — |

### Chave primária
- `CONSTRAINT campaigns_pkey PRIMARY KEY (id)`

### Relacionamentos
- `campaigns_brand_id_fkey`: `brand_id` → `public.brands(id)`
- `campaigns_created_by_fkey`: `created_by` → `auth.users(id)`
- `campaigns_unit_id_fkey`: `unit_id` → `public.units(id)`

### Constraints
- `CONSTRAINT campaigns_category_check CHECK ((category = ANY (ARRAY['saude'::text, 'evento'::text, 'comunicado'::text])))`
- `CONSTRAINT campaigns_target_check CHECK ((target = ANY (ARRAY['all'::text, 'department'::text])))`

### Índices
- `idx_campaigns_active`: `USING btree (active, starts_at, ends_at)`
- `idx_campaigns_brand`: `USING btree (brand_id)`

### Triggers

Nenhum trigger associado.

### Políticas RLS

RLS: **habilitada**.
- `campaigns_delete`: `FOR DELETE USING (public.kph_is_founder())`
- `campaigns_insert`: `FOR INSERT WITH CHECK ((((brand_id IS NOT NULL) AND public.kph_has_role_for_brand(brand_id)) OR ((unit_id IS NOT NULL) AND public.kph_has_role_for_unit(unit_id))))`
- `campaigns_select`: `FOR SELECT USING ((((brand_id IS NOT NULL) AND public.kph_has_role_for_brand(brand_id)) OR ((unit_id IS NOT NULL) AND public.kph_has_role_for_unit(unit_id)) OR public.kph_is_founder()))`
- `campaigns_update`: `FOR UPDATE USING ((((brand_id IS NOT NULL) AND public.kph_has_role_for_brand(brand_id)) OR ((unit_id IS NOT NULL) AND public.kph_has_role_for_unit(unit_id))))`

## candidate_agendamentos

### Finalidade

Descrição inferida pela estrutura: armazena registros relacionados a `candidate agendamentos`. A finalidade de negócio exata deve ser confirmada com a equipe responsável.

### Colunas

| Coluna | Tipo | Obrigatória | Padrão | Observação |
|---|---|---|---|---|
| id | uuid | Sim | gen_random_uuid() | — |
| candidate_id | uuid | Sim | — | — |
| tipo | text | Sim | — | — |
| data_hora | timestamp with time zone | Sim | — | — |
| duracao_min | integer | Sim | 30 | — |
| modalidade | text | Não | — | — |
| local | text | Não | — | — |
| unit_id | uuid | Não | — | — |
| responsavel_id | uuid | Não | — | — |
| status | text | Sim | 'agendado'::text | — |
| observacoes | text | Não | — | — |
| google_event_id | text | Não | — | — |
| google_meet_link | text | Não | — | — |
| transcricao_drive_id | text | Não | — | — |
| resumo_ia | text | Não | — | — |
| created_at | timestamp with time zone | Sim | now() | — |
| updated_at | timestamp with time zone | Sim | now() | — |

### Chave primária
- `CONSTRAINT candidate_agendamentos_pkey PRIMARY KEY (id)`

### Relacionamentos
- `candidate_agendamentos_candidate_id_fkey`: `candidate_id` → `public.candidates(id)` (ON DELETE CASCADE)
- `candidate_agendamentos_unit_id_fkey`: `unit_id` → `public.units(id)`

### Constraints
- `CONSTRAINT candidate_agendamentos_modalidade_check CHECK ((modalidade = ANY (ARRAY['presencial'::text, 'video'::text, 'telefone'::text])))`
- `CONSTRAINT candidate_agendamentos_status_check CHECK ((status = ANY (ARRAY['agendado'::text, 'realizado'::text, 'cancelado'::text, 'nao_compareceu'::text])))`
- `CONSTRAINT candidate_agendamentos_tipo_check CHECK ((tipo = ANY (ARRAY['entrevista'::text, 'teste_pratico'::text])))`

### Índices
- `idx_agendamentos_candidate_tipo`: `USING btree (candidate_id, tipo)`
- `idx_agendamentos_data_hora`: `USING btree (data_hora)`
- `idx_cand_agend_cand_tipo`: `USING btree (candidate_id, tipo)`
- `idx_cand_agend_data`: `USING btree (data_hora)`

### Triggers

Nenhum trigger associado.

### Políticas RLS

RLS: **habilitada**.
- `agendamentos_all`: `USING (true) WITH CHECK (true)`
- `p_cand_agend_all`: `USING (true) WITH CHECK (true)`

## candidate_pipeline

### Finalidade

Descrição inferida pela estrutura: armazena registros relacionados a `candidate pipeline`. A finalidade de negócio exata deve ser confirmada com a equipe responsável.

### Colunas

| Coluna | Tipo | Obrigatória | Padrão | Observação |
|---|---|---|---|---|
| id | uuid | Sim | gen_random_uuid() | — |
| candidate_id | uuid | Sim | — | — |
| etapa | text | Não | — | — |
| status | text | Não | 'pendente'::text | — |
| responsavel_id | uuid | Não | — | — |
| data_agendamento | timestamp with time zone | Não | — | — |
| feedback | text | Não | — | — |
| created_at | timestamp with time zone | Sim | now() | — |
| de_status | text | Não | — | — |
| para_status | text | Não | — | — |
| motivo | text | Não | — | — |
| autor_id | uuid | Não | — | — |

### Chave primária
- `CONSTRAINT candidate_pipeline_pkey PRIMARY KEY (id)`

### Relacionamentos
- `candidate_pipeline_autor_id_fkey`: `autor_id` → `public.employees(id)` (ON DELETE SET NULL)
- `candidate_pipeline_candidate_id_fkey`: `candidate_id` → `public.candidates(id)` (ON DELETE CASCADE)
- `candidate_pipeline_responsavel_id_fkey`: `responsavel_id` → `public.employees(id)` (ON DELETE SET NULL)

### Constraints
- `CONSTRAINT candidate_pipeline_de_status_check CHECK (((de_status IS NULL) OR (de_status = ANY (ARRAY['novo'::text, 'triagem'::text, 'agendamento'::text, 'entrevista'::text, 'avaliacao_administrativa'::text, 'entrevista_diretoria'::text, 'agendamento_teste'::text, 'feedback_operacional'::text, 'decisao'::text, 'aprovado'::text, 'contratado'::text, 'banco_talentos'::text, 'reprovado'::text, 'desistiu'::text]))))`
- `CONSTRAINT candidate_pipeline_para_status_check CHECK (((para_status IS NULL) OR (para_status = ANY (ARRAY['novo'::text, 'triagem'::text, 'agendamento'::text, 'entrevista'::text, 'avaliacao_administrativa'::text, 'entrevista_diretoria'::text, 'agendamento_teste'::text, 'feedback_operacional'::text, 'decisao'::text, 'aprovado'::text, 'contratado'::text, 'banco_talentos'::text, 'reprovado'::text, 'desistiu'::text]))))`
- `CONSTRAINT candidate_pipeline_status_check CHECK (((status IS NULL) OR (status = ANY (ARRAY['pendente'::text, 'aprovado'::text, 'reprovado'::text]))))`

### Índices
- `idx_pipeline_autor_id`: `USING btree (autor_id)`
- `idx_pipeline_candidate`: `USING btree (candidate_id)`
- `idx_pipeline_created_at`: `USING btree (created_at DESC)`
- `idx_pipeline_etapa`: `USING btree (etapa)`
- `idx_pipeline_para_status`: `USING btree (para_status)`

### Triggers

Nenhum trigger associado.

### Políticas RLS

RLS: **habilitada**.
- `candidate_pipeline_read`: `FOR SELECT USING ((candidate_id IN ( SELECT candidates.id FROM public.candidates)))`
- `candidate_pipeline_write`: `USING ((public.get_my_tier() = ANY (ARRAY['T3'::text, 'T4'::text])))`

## candidates

### Finalidade

Descrição inferida pela estrutura: armazena registros relacionados a `candidates`. A finalidade de negócio exata deve ser confirmada com a equipe responsável.

### Colunas

| Coluna | Tipo | Obrigatória | Padrão | Observação |
|---|---|---|---|---|
| id | uuid | Sim | gen_random_uuid() | — |
| job_opening_id | uuid | Não | — | — |
| full_name | text | Sim | — | — |
| email | text | Não | — | — |
| phone | text | Não | — | — |
| access_code | text | Sim | (gen_random_uuid())::text | — |
| status | text | Sim | 'novo'::text | — |
| interview_status | text | Sim | 'pendente'::text | — |
| created_at | timestamp with time zone | Não | now() | — |
| unit_id | uuid | Não | — | — |
| origem | text | Sim | 'manual'::text | — |
| area_interesse | text | Não | — | — |
| nota_maya | numeric(3,1) | Não | — | — |
| conversa_id | uuid | Não | — | — |
| disc_profile | text | Não | — | — |
| updated_at | timestamp with time zone | Sim | now() | — |
| responsavel_id | uuid | Não | — | — |
| entrevistador_id | uuid | Não | — | — |
| observacoes | text | Não | — | — |
| welcome_message_sid | text | Não | — | — |
| welcome_delivery_status | text | Não | — | — |
| welcome_sent_at | timestamp with time zone | Não | — | — |
| welcome_error_code | text | Não | — | — |
| origem_id | uuid | Não | — | — |
| cidade | text | Não | — | — |
| escolaridade_nivel | text | Não | — | — |
| pretensao_salarial | numeric(10,2) | Não | — | — |
| disponibilidade_inicio | date | Não | — | — |
| turnos_disponiveis | text[] | Não | '{}'::text[] | — |
| bairro | text | Não | — | — |
| cv_storage_path | text | Não | — | — |
| experiencias | jsonb | Não | '[]'::jsonb | — |
| formacoes | jsonb | Não | '[]'::jsonb | — |
| idiomas | jsonb | Não | '[]'::jsonb | — |
| habilidades | text[] | Não | '{}'::text[] | — |
| cargo_id | uuid | Não | — | — |
| requer_entrevista_diretoria | boolean | Não | — | — |

### Chave primária
- `CONSTRAINT candidates_pkey PRIMARY KEY (id)`

### Relacionamentos
- `candidates_cargo_id_fkey`: `cargo_id` → `public.cargos(id)`
- `candidates_entrevistador_id_fkey`: `entrevistador_id` → `public.employees(id)`
- `candidates_job_opening_id_fkey`: `job_opening_id` → `public.job_openings(id)` (ON DELETE CASCADE)
- `candidates_origem_id_fkey`: `origem_id` → `public.origens_candidato(id)`
- `candidates_responsavel_id_fkey`: `responsavel_id` → `public.employees(id)`
- `candidates_unit_id_fkey`: `unit_id` → `public.units(id)` (ON DELETE SET NULL)

### Constraints
- `CONSTRAINT candidates_escolaridade_nivel_check CHECK (((escolaridade_nivel IS NULL) OR (escolaridade_nivel = ANY (ARRAY['analfabeto'::text, 'fundamental_5_incompleto'::text, 'fundamental_5_completo'::text, 'fundamental_6_9'::text, 'fundamental_completo'::text, 'medio_incompleto'::text, 'medio_completo'::text, 'superior_incompleto'::text, 'superior_completo'::text, 'pos_graduacao'::text]))))`
- `CONSTRAINT candidates_interview_status_check CHECK ((interview_status = ANY (ARRAY['pendente'::text, 'em_andamento'::text, 'concluido'::text])))`
- `CONSTRAINT candidates_origem_check CHECK (((origem IS NULL) OR (origem = ANY (ARRAY['maya'::text, 'portal'::text, 'indicacao_colaborador'::text, 'indicacao'::text, 'linkedin'::text, 'indeed'::text, 'catho'::text, 'vagas_com_br'::text, 'infojobs'::text, 'instagram'::text, 'mutirao'::text, 'busca_ativa'::text, 'banco_talentos_reativado'::text, 'escola'::text, 'sindicato'::text, 'abordagem'::text, 'manual'::text, 'outro'::text, 'maya_whatsapp'::text, 'portal_kph'::text]))))`
- `CONSTRAINT candidates_status_check CHECK ((status = ANY (ARRAY['novo'::text, 'triagem'::text, 'agendamento'::text, 'entrevista'::text, 'avaliacao_administrativa'::text, 'entrevista_diretoria'::text, 'agendamento_teste'::text, 'feedback_operacional'::text, 'decisao'::text, 'aprovado'::text, 'contratado'::text, 'reprovado'::text, 'desistiu'::text, 'banco_talentos'::text])))`
- `CONSTRAINT candidates_access_code_key UNIQUE (access_code)`

### Índices
- `candidates_phone_unique`: `USING btree (phone)`
- `idx_candidates_access_code`: `USING btree (access_code)`
- `idx_candidates_cidade`: `USING btree (cidade) WHERE (cidade IS NOT NULL)`
- `idx_candidates_escolaridade`: `USING btree (escolaridade_nivel) WHERE (escolaridade_nivel IS NOT NULL)`
- `idx_candidates_job_opening`: `USING btree (job_opening_id)`
- `idx_candidates_opening`: `USING btree (job_opening_id)`
- `idx_candidates_origem`: `USING btree (origem)`
- `idx_candidates_pretensao`: `USING btree (pretensao_salarial) WHERE (pretensao_salarial IS NOT NULL)`
- `idx_candidates_status`: `USING btree (status)`
- `idx_candidates_unit`: `USING btree (unit_id)`
- `idx_candidates_welcome_sid`: `USING btree (welcome_message_sid) WHERE (welcome_message_sid IS NOT NULL)`

### Triggers
- `candidates_updated_at`: `BEFORE UPDATE FOR EACH ROW EXECUTE FUNCTION public.set_updated_at()`

### Políticas RLS

RLS: **habilitada**.
- `candidates_delete`: `FOR DELETE USING (public.kph_is_founder())`
- `candidates_insert`: `FOR INSERT WITH CHECK ((EXISTS ( SELECT 1 FROM public.job_openings j WHERE ((j.id = candidates.job_opening_id) AND (((j.brand_id IS NOT NULL) AND public.kph_has_role_for_brand(j.brand_id)) OR ((j.unit_id IS NOT NULL) AND public.kph_has_role_for_unit(j.unit_id)))))))`
- `candidates_read`: `FOR SELECT USING ((public.get_my_tier() = ANY (ARRAY['T3'::text, 'T4'::text])))`
- `candidates_select`: `FOR SELECT TO authenticated USING ((EXISTS ( SELECT 1 FROM (public.user_roles ur JOIN public.roles r ON ((r.id = ur.role_id))) WHERE ((ur.user_id = auth.uid()) AND (r.name = ANY (ARRAY['founder'::text, 'gm'::text, 'pessoas'::text]))))))`
- `candidates_select_admin`: `FOR SELECT USING ((EXISTS ( SELECT 1 FROM public.job_openings j WHERE ((j.id = candidates.job_opening_id) AND (((j.brand_id IS NOT NULL) AND public.kph_has_role_for_brand(j.brand_id)) OR ((j.unit_id IS NOT NULL) AND public.kph_has_role_for_unit(j.unit_id)) OR public.kph_is_founder())))))`
- `candidates_select_public`: `FOR SELECT USING (true)`
- `candidates_update`: `FOR UPDATE USING (true)`
- `candidates_write`: `USING ((public.get_my_tier() = ANY (ARRAY['T3'::text, 'T4'::text])))`

## candidatos_maya

### Finalidade

Descrição inferida pela estrutura: armazena registros relacionados a `candidatos maya`. A finalidade de negócio exata deve ser confirmada com a equipe responsável.

### Colunas

| Coluna | Tipo | Obrigatória | Padrão | Observação |
|---|---|---|---|---|
| id | uuid | Sim | gen_random_uuid() | — |
| nome | text | Sim | — | — |
| telefone | text | Sim | — | — |
| area_interesse | text | Não | — | — |
| cargo_interesse | text | Não | — | — |
| status | text | Sim | 'novo'::text | — |
| source | text | Sim | 'whatsapp'::text | — |
| created_at | timestamp with time zone | Não | now() | — |
| updated_at | timestamp with time zone | Não | now() | — |

### Chave primária
- `CONSTRAINT candidatos_maya_pkey PRIMARY KEY (id)`

### Relacionamentos

Nenhuma chave estrangeira identificada.

### Constraints
- `CONSTRAINT candidatos_maya_status_check CHECK ((status = ANY (ARRAY['novo'::text, 'triagem'::text, 'entrevista'::text, 'aprovado'::text, 'reprovado'::text, 'desistiu'::text])))`

### Índices
- `idx_candidatos_maya_status`: `USING btree (status)`
- `idx_candidatos_maya_telefone`: `USING btree (telefone)`

### Triggers

Nenhum trigger associado.

### Políticas RLS

RLS: **habilitada**.
- `candidatos_maya_select`: `FOR SELECT TO authenticated USING ((EXISTS ( SELECT 1 FROM (public.user_roles ur JOIN public.roles r ON ((r.id = ur.role_id))) WHERE ((ur.user_id = auth.uid()) AND (r.name = ANY (ARRAY['founder'::text, 'gm'::text, 'pessoas'::text]))))))`

## cargo_grupos

### Finalidade

Descrição inferida pela estrutura: armazena registros relacionados a `cargo grupos`. A finalidade de negócio exata deve ser confirmada com a equipe responsável.

### Colunas

| Coluna | Tipo | Obrigatória | Padrão | Observação |
|---|---|---|---|---|
| id | uuid | Sim | gen_random_uuid() | — |
| nome | text | Sim | — | — |
| sla_dias_uteis | integer | Sim | — | — |
| descricao | text | Não | — | — |
| ativo | boolean | Sim | true | — |
| created_at | timestamp with time zone | Sim | now() | — |

### Chave primária
- `CONSTRAINT cargo_grupos_pkey PRIMARY KEY (id)`

### Relacionamentos

Nenhuma chave estrangeira identificada.

### Constraints
- `CONSTRAINT cargo_grupos_sla_dias_uteis_check CHECK ((sla_dias_uteis > 0))`
- `CONSTRAINT cargo_grupos_nome_key UNIQUE (nome)`

### Índices

Nenhum índice adicional identificado.

### Triggers

Nenhum trigger associado.

### Políticas RLS

RLS: **habilitada**.
- `cargo_grupos_select`: `FOR SELECT USING (true)`

## cargos

### Finalidade

Descrição inferida pela estrutura: armazena registros relacionados a `cargos`. A finalidade de negócio exata deve ser confirmada com a equipe responsável.

### Colunas

| Coluna | Tipo | Obrigatória | Padrão | Observação |
|---|---|---|---|---|
| id | uuid | Sim | gen_random_uuid() | — |
| nome | text | Sim | — | — |
| setor | text | Sim | — | — |
| grupo | text | Sim | — | — |
| tem_nivel | boolean | Sim | false | — |
| sinonimos | text[] | Sim | '{}'::text[] | — |
| ativo | boolean | Sim | true | — |
| created_at | timestamp with time zone | Sim | now() | — |
| reporta_a_cargo_id | uuid | Não | — | — |
| ordem_hierarquia | integer | Não | — | — |
| requer_entrevista_diretoria | boolean | Sim | false | — |

### Chave primária
- `CONSTRAINT cargos_pkey PRIMARY KEY (id)`

### Relacionamentos
- `cargos_reporta_a_cargo_id_fkey`: `reporta_a_cargo_id` → `public.cargos(id)`

### Constraints
- `CONSTRAINT cargos_grupo_chk CHECK ((grupo = ANY (ARRAY['Operacional'::text, 'Tático'::text, 'Estratégico'::text, 'Executivo-Liderança'::text])))`
- `CONSTRAINT cargos_setor_chk CHECK ((setor = ANY (ARRAY['Gerência'::text, 'Bar'::text, 'Salão'::text, 'Limpeza'::text, 'Cozinha'::text, 'Estoque'::text])))`
- `CONSTRAINT cargos_nome_unique UNIQUE (nome)`

### Índices

Nenhum índice adicional identificado.

### Triggers

Nenhum trigger associado.

### Políticas RLS

RLS: **habilitada**.

Nenhuma política associada.

## cct_versions

### Finalidade

Descrição inferida pela estrutura: armazena registros relacionados a `cct versions`. A finalidade de negócio exata deve ser confirmada com a equipe responsável.

### Colunas

| Coluna | Tipo | Obrigatória | Padrão | Observação |
|---|---|---|---|---|
| id | uuid | Sim | gen_random_uuid() | — |
| sindicato | text | Sim | — | — |
| vigencia_inicio | date | Sim | — | — |
| vigencia_fim | date | Sim | — | — |
| piso_salarial | numeric(10,2) | Não | — | — |
| adicional_noturno_pct | numeric(5,2) | Não | 20 | — |
| hora_extra_50_pct | numeric(5,2) | Não | 50 | — |
| hora_extra_100_pct | numeric(5,2) | Não | 100 | — |
| gorjeta_percentual | numeric(5,2) | Não | — | — |
| dsr_sobre_gorjeta | boolean | Não | true | — |
| dados_completos | jsonb | Não | — | — |
| ativo | boolean | Não | true | — |
| created_at | timestamp with time zone | Não | now() | — |

### Chave primária
- `CONSTRAINT cct_versions_pkey PRIMARY KEY (id)`

### Relacionamentos

Nenhuma chave estrangeira identificada.

### Constraints

Nenhuma constraint adicional identificada.

### Índices

Nenhum índice adicional identificado.

### Triggers

Nenhum trigger associado.

### Políticas RLS

RLS: **habilitada**.
- `cct_select`: `FOR SELECT TO authenticated USING (true)`

## checklist_records

### Finalidade

Descrição inferida pela estrutura: armazena registros relacionados a `checklist records`. A finalidade de negócio exata deve ser confirmada com a equipe responsável.

### Colunas

| Coluna | Tipo | Obrigatória | Padrão | Observação |
|---|---|---|---|---|
| id | uuid | Sim | gen_random_uuid() | — |
| checklist_id | uuid | Sim | — | — |
| unit_id | uuid | Sim | — | — |
| data | date | Sim | CURRENT_DATE | — |
| turno | public.checklist_turno | Sim | — | — |
| responsavel_id | uuid | Não | — | — |
| respostas | jsonb | Sim | '{}'::jsonb | — |
| score_pct | integer | Não | — | — |
| observacoes | text | Não | — | — |
| created_at | timestamp with time zone | Sim | now() | — |

### Chave primária
- `CONSTRAINT checklist_records_pkey PRIMARY KEY (id)`

### Relacionamentos
- `checklist_records_checklist_id_fkey`: `checklist_id` → `public.quality_checklists(id)` (ON DELETE CASCADE)
- `checklist_records_responsavel_id_fkey`: `responsavel_id` → `auth.users(id)`
- `checklist_records_unit_id_fkey`: `unit_id` → `public.units(id)` (ON DELETE CASCADE)

### Constraints

Nenhuma constraint adicional identificada.

### Índices
- `checklist_records_checklist_idx`: `USING btree (checklist_id)`
- `checklist_records_unit_data_idx`: `USING btree (unit_id, data)`

### Triggers

Nenhum trigger associado.

### Políticas RLS

RLS: **habilitada**.
- `unit members can insert records`: `FOR INSERT WITH CHECK (public.kph_has_role_for_unit(unit_id))`
- `unit members can select records`: `FOR SELECT USING (public.kph_has_role_for_unit(unit_id))`

## client_interactions

### Finalidade

Descrição inferida pela estrutura: armazena registros relacionados a `client interactions`. A finalidade de negócio exata deve ser confirmada com a equipe responsável.

### Colunas

| Coluna | Tipo | Obrigatória | Padrão | Observação |
|---|---|---|---|---|
| id | uuid | Sim | gen_random_uuid() | — |
| client_id | uuid | Sim | — | — |
| tipo | text | Sim | — | — |
| descricao | text | Não | — | — |
| data | timestamp with time zone | Sim | now() | — |
| created_by | uuid | Não | — | — |
| created_at | timestamp with time zone | Não | now() | — |

### Chave primária
- `CONSTRAINT client_interactions_pkey PRIMARY KEY (id)`

### Relacionamentos
- `client_interactions_client_id_fkey`: `client_id` → `public.clients(id)` (ON DELETE CASCADE)
- `client_interactions_created_by_fkey`: `created_by` → `auth.users(id)`

### Constraints
- `CONSTRAINT client_interactions_tipo_check CHECK ((tipo = ANY (ARRAY['ligacao'::text, 'email'::text, 'whatsapp'::text, 'reuniao'::text, 'visita'::text, 'outro'::text])))`

### Índices
- `idx_client_interactions_cli`: `USING btree (client_id, data DESC)`

### Triggers

Nenhum trigger associado.

### Políticas RLS

RLS: **habilitada**.
- `client_interactions_delete`: `FOR DELETE USING (public.kph_is_founder())`
- `client_interactions_insert`: `FOR INSERT WITH CHECK ((EXISTS ( SELECT 1 FROM public.clients c WHERE ((c.id = client_interactions.client_id) AND public.kph_has_role_for_unit(c.unit_id)))))`
- `client_interactions_select`: `FOR SELECT USING ((EXISTS ( SELECT 1 FROM public.clients c WHERE ((c.id = client_interactions.client_id) AND public.kph_has_role_for_unit(c.unit_id)))))`
- `client_interactions_update`: `FOR UPDATE USING ((EXISTS ( SELECT 1 FROM public.clients c WHERE ((c.id = client_interactions.client_id) AND public.kph_has_role_for_unit(c.unit_id))))) WITH CHECK ((EXISTS ( SELECT 1 FROM public.clients c WHERE ((c.id = client_interactions.client_id) AND public.kph_has_role_for_unit(c.unit_id)))))`

## clients

### Finalidade

Descrição inferida pela estrutura: armazena registros relacionados a `clients`. A finalidade de negócio exata deve ser confirmada com a equipe responsável.

### Colunas

| Coluna | Tipo | Obrigatória | Padrão | Observação |
|---|---|---|---|---|
| id | uuid | Sim | gen_random_uuid() | — |
| brand_id | uuid | Sim | — | — |
| unit_id | uuid | Sim | — | — |
| nome | text | Sim | — | — |
| email | text | Não | — | — |
| telefone | text | Não | — | — |
| empresa | text | Não | — | — |
| origem | text | Não | — | — |
| observacoes | text | Não | — | — |
| ativo | boolean | Não | true | — |
| created_by | uuid | Não | — | — |
| created_at | timestamp with time zone | Não | now() | — |
| updated_at | timestamp with time zone | Não | now() | — |

### Chave primária
- `CONSTRAINT clients_pkey PRIMARY KEY (id)`

### Relacionamentos
- `clients_brand_id_fkey`: `brand_id` → `public.brands(id)`
- `clients_created_by_fkey`: `created_by` → `auth.users(id)`
- `clients_unit_id_fkey`: `unit_id` → `public.units(id)`

### Constraints
- `CONSTRAINT clients_origem_check CHECK (((origem IS NULL) OR (origem = ANY (ARRAY['indicacao'::text, 'site'::text, 'instagram'::text, 'whatsapp'::text, 'evento'::text, 'outro'::text]))))`

### Índices
- `idx_clients_ativo`: `USING btree (ativo)`
- `idx_clients_brand`: `USING btree (brand_id)`
- `idx_clients_created_at`: `USING btree (created_at DESC)`
- `idx_clients_origem`: `USING btree (origem)`
- `idx_clients_unit`: `USING btree (unit_id)`

### Triggers
- `trg_clients_updated_at`: `BEFORE UPDATE FOR EACH ROW EXECUTE FUNCTION public.update_updated_at_column()`

### Políticas RLS

RLS: **habilitada**.
- `clients_delete`: `FOR DELETE USING (public.kph_is_founder())`
- `clients_insert`: `FOR INSERT WITH CHECK (public.kph_has_role_for_unit(unit_id))`
- `clients_select`: `FOR SELECT USING (public.kph_has_role_for_unit(unit_id))`
- `clients_update`: `FOR UPDATE USING (public.kph_has_role_for_unit(unit_id)) WITH CHECK (public.kph_has_role_for_unit(unit_id))`

## climate_questions

### Finalidade

Descrição inferida pela estrutura: armazena registros relacionados a `climate questions`. A finalidade de negócio exata deve ser confirmada com a equipe responsável.

### Colunas

| Coluna | Tipo | Obrigatória | Padrão | Observação |
|---|---|---|---|---|
| id | uuid | Sim | gen_random_uuid() | — |
| survey_id | uuid | Sim | — | — |
| ordem | integer | Sim | 1 | — |
| texto | text | Sim | — | — |
| tipo | text | Sim | 'escala'::text | — |
| created_at | timestamp with time zone | Não | now() | — |

### Chave primária
- `CONSTRAINT climate_questions_pkey PRIMARY KEY (id)`

### Relacionamentos
- `climate_questions_survey_id_fkey`: `survey_id` → `public.climate_surveys(id)` (ON DELETE CASCADE)

### Constraints
- `CONSTRAINT climate_questions_tipo_check CHECK ((tipo = ANY (ARRAY['escala'::text, 'texto_livre'::text])))`

### Índices

Nenhum índice adicional identificado.

### Triggers

Nenhum trigger associado.

### Políticas RLS

RLS: **habilitada**.
- `anon_all_climate_questions`: `TO authenticated, anon USING (true) WITH CHECK (true)`

## climate_responses

### Finalidade

Descrição inferida pela estrutura: armazena registros relacionados a `climate responses`. A finalidade de negócio exata deve ser confirmada com a equipe responsável.

### Colunas

| Coluna | Tipo | Obrigatória | Padrão | Observação |
|---|---|---|---|---|
| id | uuid | Sim | gen_random_uuid() | — |
| survey_id | uuid | Sim | — | — |
| question_id | uuid | Sim | — | — |
| employee_id | uuid | Sim | — | — |
| valor_escala | integer | Não | — | — |
| texto_livre | text | Não | — | — |
| respondido_em | timestamp with time zone | Não | now() | — |

### Chave primária
- `CONSTRAINT climate_responses_pkey PRIMARY KEY (id)`

### Relacionamentos
- `climate_responses_employee_id_fkey`: `employee_id` → `public.employees(id)`
- `climate_responses_question_id_fkey`: `question_id` → `public.climate_questions(id)`
- `climate_responses_survey_id_fkey`: `survey_id` → `public.climate_surveys(id)`

### Constraints
- `CONSTRAINT climate_responses_valor_escala_check CHECK (((valor_escala >= 1) AND (valor_escala <= 5)))`
- `CONSTRAINT climate_responses_question_id_employee_id_key UNIQUE (question_id, employee_id)`

### Índices

Nenhum índice adicional identificado.

### Triggers

Nenhum trigger associado.

### Políticas RLS

RLS: **habilitada**.
- `anon_all_climate_responses`: `TO authenticated, anon USING (true) WITH CHECK (true)`

## climate_survey_questions

### Finalidade

Descrição inferida pela estrutura: armazena registros relacionados a `climate survey questions`. A finalidade de negócio exata deve ser confirmada com a equipe responsável.

### Colunas

| Coluna | Tipo | Obrigatória | Padrão | Observação |
|---|---|---|---|---|
| id | uuid | Sim | gen_random_uuid() | — |
| survey_id | uuid | Não | — | — |
| ordem | integer | Não | — | — |
| pergunta | text | Sim | — | — |
| tipo | text | Não | 'escala'::text | — |
| opcoes | jsonb | Não | — | — |
| created_at | timestamp with time zone | Não | now() | — |

### Chave primária
- `CONSTRAINT climate_survey_questions_pkey PRIMARY KEY (id)`

### Relacionamentos
- `climate_survey_questions_survey_id_fkey`: `survey_id` → `public.climate_surveys(id)` (ON DELETE CASCADE)

### Constraints

Nenhuma constraint adicional identificada.

### Índices

Nenhum índice adicional identificado.

### Triggers

Nenhum trigger associado.

### Políticas RLS

RLS: **habilitada**.

Nenhuma política associada.

## climate_survey_responses

### Finalidade

Descrição inferida pela estrutura: armazena registros relacionados a `climate survey responses`. A finalidade de negócio exata deve ser confirmada com a equipe responsável.

### Colunas

| Coluna | Tipo | Obrigatória | Padrão | Observação |
|---|---|---|---|---|
| id | uuid | Sim | gen_random_uuid() | — |
| survey_id | uuid | Não | — | — |
| question_id | uuid | Não | — | — |
| employee_id | uuid | Não | — | — |
| resposta | text | Não | — | — |
| nota | integer | Não | — | — |
| created_at | timestamp with time zone | Não | now() | — |

### Chave primária
- `CONSTRAINT climate_survey_responses_pkey PRIMARY KEY (id)`

### Relacionamentos
- `climate_survey_responses_question_id_fkey`: `question_id` → `public.climate_survey_questions(id)`
- `climate_survey_responses_survey_id_fkey`: `survey_id` → `public.climate_surveys(id)`

### Constraints

Nenhuma constraint adicional identificada.

### Índices

Nenhum índice adicional identificado.

### Triggers

Nenhum trigger associado.

### Políticas RLS

RLS: **habilitada**.

Nenhuma política associada.

## climate_surveys

### Finalidade

Descrição inferida pela estrutura: armazena registros relacionados a `climate surveys`. A finalidade de negócio exata deve ser confirmada com a equipe responsável.

### Colunas

| Coluna | Tipo | Obrigatória | Padrão | Observação |
|---|---|---|---|---|
| id | uuid | Sim | gen_random_uuid() | — |
| unit_id | uuid | Não | — | — |
| titulo | text | Sim | — | — |
| descricao | text | Não | — | — |
| status | text | Não | 'rascunho'::text | — |
| data_inicio | date | Não | — | — |
| data_fim | date | Não | — | — |
| anonimo | boolean | Não | true | — |
| created_by | uuid | Não | — | — |
| created_at | timestamp with time zone | Não | now() | — |

### Chave primária
- `CONSTRAINT climate_surveys_pkey PRIMARY KEY (id)`

### Relacionamentos
- `climate_surveys_unit_id_fkey`: `unit_id` → `public.units(id)`

### Constraints

Nenhuma constraint adicional identificada.

### Índices

Nenhum índice adicional identificado.

### Triggers

Nenhum trigger associado.

### Políticas RLS

RLS: **habilitada**.
- `anon_all_climate_surveys`: `TO authenticated, anon USING (true) WITH CHECK (true)`

## comments

### Finalidade

Descrição inferida pela estrutura: armazena registros relacionados a `comments`. A finalidade de negócio exata deve ser confirmada com a equipe responsável.

### Colunas

| Coluna | Tipo | Obrigatória | Padrão | Observação |
|---|---|---|---|---|
| id | uuid | Sim | gen_random_uuid() | — |
| task_id | uuid | Sim | — | — |
| member_id | uuid | Sim | — | — |
| content | text | Sim | — | — |
| created_at | timestamp with time zone | Sim | timezone('utc'::text, now()) | — |

### Chave primária
- `CONSTRAINT comments_pkey PRIMARY KEY (id)`

### Relacionamentos
- `comments_member_id_fkey`: `member_id` → `public.team_members(id)` (ON DELETE CASCADE)
- `comments_task_id_fkey`: `task_id` → `public.tasks(id)` (ON DELETE CASCADE)

### Constraints

Nenhuma constraint adicional identificada.

### Índices

Nenhum índice adicional identificado.

### Triggers

Nenhum trigger associado.

### Políticas RLS

RLS: **não habilitada no dump**.

Nenhuma política associada.

## contatos_kph

### Finalidade

Descrição inferida pela estrutura: armazena registros relacionados a `contatos kph`. A finalidade de negócio exata deve ser confirmada com a equipe responsável.

### Colunas

| Coluna | Tipo | Obrigatória | Padrão | Observação |
|---|---|---|---|---|
| id | uuid | Sim | gen_random_uuid() | — |
| telefone | text | Sim | — | — |
| nome | text | Não | — | — |
| tipo | text | Não | 'externo'::text | — |
| area_interesse | text | Não | — | — |
| primeiro_contato | timestamp with time zone | Não | now() | — |
| ultimo_contato | timestamp with time zone | Não | now() | — |
| total_conversas | integer | Não | 1 | — |
| agentes_usados | text[] | Não | '{}'::text[] | — |
| employee_id | uuid | Não | — | — |
| candidate_id | uuid | Não | — | — |
| created_at | timestamp with time zone | Não | now() | — |
| updated_at | timestamp with time zone | Não | now() | — |

### Chave primária
- `CONSTRAINT contatos_kph_pkey PRIMARY KEY (id)`

### Relacionamentos
- `contatos_kph_candidate_id_fkey`: `candidate_id` → `public.candidates(id)`
- `contatos_kph_employee_id_fkey`: `employee_id` → `public.employees(id)`

### Constraints
- `CONSTRAINT contatos_kph_tipo_check CHECK ((tipo = ANY (ARRAY['candidato'::text, 'colaborador'::text, 'externo'::text])))`
- `CONSTRAINT contatos_kph_telefone_key UNIQUE (telefone)`

### Índices
- `idx_contatos_kph_candidate`: `USING btree (candidate_id)`
- `idx_contatos_kph_employee`: `USING btree (employee_id)`
- `idx_contatos_kph_telefone`: `USING btree (telefone)`
- `idx_contatos_kph_tipo`: `USING btree (tipo)`

### Triggers

Nenhum trigger associado.

### Políticas RLS

RLS: **não habilitada no dump**.

Nenhuma política associada.

## contractor_payments

### Finalidade

Descrição inferida pela estrutura: armazena registros relacionados a `contractor payments`. A finalidade de negócio exata deve ser confirmada com a equipe responsável.

### Colunas

| Coluna | Tipo | Obrigatória | Padrão | Observação |
|---|---|---|---|---|
| id | uuid | Sim | gen_random_uuid() | — |
| unit_id | uuid | Não | — | — |
| contractor_id | uuid | Não | — | — |
| competencia | date | Sim | — | — |
| valor_bruto | numeric(10,2) | Não | — | — |
| valor_cash | numeric(10,2) | Não | 0 | — |
| desconto | numeric(10,2) | Não | 0 | — |
| valor_nota | numeric(10,2) | Não | — | — |
| gorjeta_1q | numeric(10,2) | Não | 0 | — |
| gorjeta_2q | numeric(10,2) | Não | 0 | — |
| pgto_15 | numeric(10,2) | Não | — | — |
| pgto_30 | numeric(10,2) | Não | — | — |
| observacao | text | Não | — | — |
| created_at | timestamp with time zone | Não | now() | — |

### Chave primária
- `CONSTRAINT contractor_payments_pkey PRIMARY KEY (id)`

### Relacionamentos
- `contractor_payments_contractor_id_fkey`: `contractor_id` → `public.contractors(id)`
- `contractor_payments_unit_id_fkey`: `unit_id` → `public.units(id)`

### Constraints
- `CONSTRAINT contractor_payments_contractor_id_unit_id_competencia_key UNIQUE (contractor_id, unit_id, competencia)`

### Índices

Nenhum índice adicional identificado.

### Triggers

Nenhum trigger associado.

### Políticas RLS

RLS: **habilitada**.
- `t3_view`: `FOR SELECT USING ((public.get_my_tier() = ANY (ARRAY['T3'::text, 'T4'::text])))`
- `t4_master`: `USING ((public.get_my_tier() = 'T4'::text))`

## contractor_vacations

### Finalidade

Descrição inferida pela estrutura: armazena registros relacionados a `contractor vacations`. A finalidade de negócio exata deve ser confirmada com a equipe responsável.

### Colunas

| Coluna | Tipo | Obrigatória | Padrão | Observação |
|---|---|---|---|---|
| id | uuid | Sim | gen_random_uuid() | — |
| unit_id | uuid | Não | — | — |
| contractor_id | uuid | Não | — | — |
| data_inicio | date | Não | — | — |
| data_termino | date | Não | — | — |
| total_dias | integer | Não | — | — |
| observacao | text | Não | — | — |
| created_at | timestamp with time zone | Não | now() | — |

### Chave primária
- `CONSTRAINT contractor_vacations_pkey PRIMARY KEY (id)`

### Relacionamentos
- `contractor_vacations_contractor_id_fkey`: `contractor_id` → `public.contractors(id)`
- `contractor_vacations_unit_id_fkey`: `unit_id` → `public.units(id)`

### Constraints

Nenhuma constraint adicional identificada.

### Índices

Nenhum índice adicional identificado.

### Triggers

Nenhum trigger associado.

### Políticas RLS

RLS: **habilitada**.
- `t3_view`: `FOR SELECT USING ((public.get_my_tier() = ANY (ARRAY['T3'::text, 'T4'::text])))`
- `t4_master`: `USING ((public.get_my_tier() = 'T4'::text))`

## contractors

### Finalidade

Descrição inferida pela estrutura: armazena registros relacionados a `contractors`. A finalidade de negócio exata deve ser confirmada com a equipe responsável.

### Colunas

| Coluna | Tipo | Obrigatória | Padrão | Observação |
|---|---|---|---|---|
| id | uuid | Sim | gen_random_uuid() | — |
| unit_id | uuid | Não | — | — |
| cnpj | text | Não | — | — |
| responsavel | text | Sim | — | — |
| valor_mensal | numeric(10,2) | Não | — | — |
| valor_nota | numeric(10,2) | Não | — | — |
| setor | text | Não | — | — |
| observacao | text | Não | — | — |
| ativo | boolean | Não | true | — |
| email | text | Não | — | — |
| telefone | text | Não | — | — |
| banco | text | Não | — | — |
| banco_codigo | text | Não | — | — |
| agencia | text | Não | — | — |
| conta | text | Não | — | — |
| cpf_responsavel | text | Não | — | — |
| data_nascimento_responsavel | date | Não | — | — |
| endereco | text | Não | — | — |
| data_inicio_contrato | date | Não | — | — |
| data_fim_contrato | date | Não | — | — |
| created_at | timestamp with time zone | Não | now() | — |

### Chave primária
- `CONSTRAINT contractors_pkey PRIMARY KEY (id)`

### Relacionamentos
- `contractors_unit_id_fkey`: `unit_id` → `public.units(id)`

### Constraints
- `CONSTRAINT contractors_cnpj_key UNIQUE (cnpj)`

### Índices
- `contractors_responsavel_sem_cnpj`: `USING btree (responsavel) WHERE (cnpj IS NULL)`

### Triggers

Nenhum trigger associado.

### Políticas RLS

RLS: **habilitada**.
- `t3_view`: `FOR SELECT USING ((public.get_my_tier() = ANY (ARRAY['T3'::text, 'T4'::text])))`
- `t4_master`: `USING ((public.get_my_tier() = 'T4'::text))`

## contratos

### Finalidade

Descrição inferida pela estrutura: armazena registros relacionados a `contratos`. A finalidade de negócio exata deve ser confirmada com a equipe responsável.

### Colunas

| Coluna | Tipo | Obrigatória | Padrão | Observação |
|---|---|---|---|---|
| id | uuid | Sim | gen_random_uuid() | — |
| unit_id | uuid | Não | — | — |
| titulo | text | Sim | — | — |
| categoria | text | Sim | — | — |
| contraparte | text | Sim | — | — |
| contraparte_doc | text | Não | — | — |
| responsavel | text | Não | — | — |
| valor | numeric(14,2) | Não | 0 | — |
| recorrencia | text | Não | — | — |
| data_inicio | date | Não | — | — |
| data_fim | date | Não | — | — |
| vigencia_indeterminada | boolean | Não | false | — |
| renovacao_automatica | boolean | Não | false | — |
| aviso_previo_dias | integer | Não | 0 | — |
| indice_reajuste | text | Não | — | — |
| data_proximo_reajuste | date | Não | — | — |
| multa_rescisoria | text | Não | — | — |
| status_manual | text | Não | — | — |
| tags | text[] | Não | — | — |
| observacoes | text | Não | — | — |
| created_at | timestamp with time zone | Não | now() | — |
| updated_at | timestamp with time zone | Não | now() | — |

### Chave primária
- `CONSTRAINT contratos_pkey PRIMARY KEY (id)`

### Relacionamentos

Nenhuma chave estrangeira identificada.

### Constraints

Nenhuma constraint adicional identificada.

### Índices
- `idx_contratos_fim`: `USING btree (data_fim)`
- `idx_contratos_unit`: `USING btree (unit_id)`

### Triggers

Nenhum trigger associado.

### Políticas RLS

RLS: **habilitada**.
- `contratos_manage`: `TO service_role USING (true) WITH CHECK (true)`
- `contratos_read`: `FOR SELECT TO authenticated, anon USING (true)`

## contratos_arquivos

### Finalidade

Descrição inferida pela estrutura: armazena registros relacionados a `contratos arquivos`. A finalidade de negócio exata deve ser confirmada com a equipe responsável.

### Colunas

| Coluna | Tipo | Obrigatória | Padrão | Observação |
|---|---|---|---|---|
| id | uuid | Sim | gen_random_uuid() | — |
| contrato_id | uuid | Sim | — | — |
| tipo | text | Sim | 'principal'::text | — |
| nome | text | Sim | — | — |
| storage_path | text | Sim | — | — |
| tamanho_bytes | bigint | Não | — | — |
| content_type | text | Não | 'application/pdf'::text | — |
| uploaded_at | timestamp with time zone | Não | now() | — |

### Chave primária
- `CONSTRAINT contratos_arquivos_pkey PRIMARY KEY (id)`

### Relacionamentos
- `contratos_arquivos_contrato_id_fkey`: `contrato_id` → `public.contratos(id)` (ON DELETE CASCADE)

### Constraints

Nenhuma constraint adicional identificada.

### Índices
- `idx_arquivos_contrato`: `USING btree (contrato_id)`

### Triggers

Nenhum trigger associado.

### Políticas RLS

RLS: **habilitada**.
- `contratos_arq_manage`: `TO service_role USING (true) WITH CHECK (true)`
- `contratos_arq_read`: `FOR SELECT TO authenticated, anon USING (true)`

## dependents

### Finalidade

Descrição inferida pela estrutura: armazena registros relacionados a `dependents`. A finalidade de negócio exata deve ser confirmada com a equipe responsável.

### Colunas

| Coluna | Tipo | Obrigatória | Padrão | Observação |
|---|---|---|---|---|
| id | uuid | Sim | gen_random_uuid() | — |
| employee_id | uuid | Sim | — | — |
| nome | text | Sim | — | — |
| cpf | text | Não | — | — |
| data_nascimento | date | Não | — | — |
| parentesco | text | Sim | — | — |
| ordem | integer | Não | 1 | — |
| created_at | timestamp with time zone | Não | now() | — |

### Chave primária
- `CONSTRAINT dependents_pkey PRIMARY KEY (id)`

### Relacionamentos
- `dependents_employee_id_fkey`: `employee_id` → `public.employees(id)` (ON DELETE CASCADE)

### Constraints

Nenhuma constraint adicional identificada.

### Índices
- `idx_dependents_employee`: `USING btree (employee_id)`

### Triggers

Nenhum trigger associado.

### Políticas RLS

RLS: **habilitada**.
- `dependents_all`: `USING ((EXISTS ( SELECT 1 FROM public.employees e WHERE ((e.id = dependents.employee_id) AND public.kph_has_role_for_unit(e.unit_id)))))`
- `dependents_select`: `FOR SELECT USING ((EXISTS ( SELECT 1 FROM public.employees e WHERE ((e.id = dependents.employee_id) AND public.kph_has_role_for_unit(e.unit_id)))))`

## dho_tracking

### Finalidade

Descrição inferida pela estrutura: armazena registros relacionados a `dho tracking`. A finalidade de negócio exata deve ser confirmada com a equipe responsável.

### Colunas

| Coluna | Tipo | Obrigatória | Padrão | Observação |
|---|---|---|---|---|
| id | uuid | Sim | gen_random_uuid() | — |
| unit_id | uuid | Não | — | — |
| employee_id | uuid | Não | — | — |
| nome | text | Não | — | — |
| tipo | text | Não | — | — |
| competencia | date | Não | — | — |
| score | numeric(5,2) | Não | — | — |
| descricao | text | Não | — | — |
| created_at | timestamp with time zone | Não | now() | — |

### Chave primária
- `CONSTRAINT dho_tracking_pkey PRIMARY KEY (id)`

### Relacionamentos
- `dho_tracking_employee_id_fkey`: `employee_id` → `public.employees(id)`
- `dho_tracking_unit_id_fkey`: `unit_id` → `public.units(id)`

### Constraints

Nenhuma constraint adicional identificada.

### Índices

Nenhum índice adicional identificado.

### Triggers

Nenhum trigger associado.

### Políticas RLS

RLS: **habilitada**.
- `t3_dept`: `USING ((public.get_my_tier() = 'T3'::text))`
- `t4_master`: `USING ((public.get_my_tier() = 'T4'::text))`

## disc_profiles

### Finalidade

Descrição inferida pela estrutura: armazena registros relacionados a `disc profiles`. A finalidade de negócio exata deve ser confirmada com a equipe responsável.

### Colunas

| Coluna | Tipo | Obrigatória | Padrão | Observação |
|---|---|---|---|---|
| id | uuid | Sim | gen_random_uuid() | — |
| employee_id | uuid | Não | — | — |
| nome | text | Não | — | — |
| perfil | text | Não | — | — |
| descricao | text | Não | — | — |
| data_avaliacao | date | Não | — | — |
| documento_ref | text | Não | — | — |
| created_at | timestamp with time zone | Não | now() | — |

### Chave primária
- `CONSTRAINT disc_profiles_pkey PRIMARY KEY (id)`

### Relacionamentos
- `disc_profiles_employee_id_fkey`: `employee_id` → `public.employees(id)`

### Constraints

Nenhuma constraint adicional identificada.

### Índices

Nenhum índice adicional identificado.

### Triggers

Nenhum trigger associado.

### Políticas RLS

RLS: **habilitada**.
- `t3_dept`: `USING ((public.get_my_tier() = 'T3'::text))`
- `t4_master`: `USING ((public.get_my_tier() = 'T4'::text))`

## disciplinary_actions

### Finalidade

Descrição inferida pela estrutura: armazena registros relacionados a `disciplinary actions`. A finalidade de negócio exata deve ser confirmada com a equipe responsável.

### Colunas

| Coluna | Tipo | Obrigatória | Padrão | Observação |
|---|---|---|---|---|
| id | uuid | Sim | gen_random_uuid() | — |
| unit_id | uuid | Não | — | — |
| employee_id | uuid | Não | — | — |
| nome | text | Não | — | — |
| tipo | text | Não | — | — |
| data | date | Não | — | — |
| motivo | text | Não | — | — |
| documento_ref | text | Não | — | — |
| created_at | timestamp with time zone | Não | now() | — |

### Chave primária
- `CONSTRAINT disciplinary_actions_pkey PRIMARY KEY (id)`

### Relacionamentos
- `disciplinary_actions_employee_id_fkey`: `employee_id` → `public.employees(id)`
- `disciplinary_actions_unit_id_fkey`: `unit_id` → `public.units(id)`

### Constraints

Nenhuma constraint adicional identificada.

### Índices

Nenhum índice adicional identificado.

### Triggers

Nenhum trigger associado.

### Políticas RLS

RLS: **habilitada**.
- `t3_dept`: `USING ((public.get_my_tier() = 'T3'::text))`
- `t4_master`: `USING ((public.get_my_tier() = 'T4'::text))`

## document_templates

### Finalidade

Descrição inferida pela estrutura: armazena registros relacionados a `document templates`. A finalidade de negócio exata deve ser confirmada com a equipe responsável.

### Colunas

| Coluna | Tipo | Obrigatória | Padrão | Observação |
|---|---|---|---|---|
| id | uuid | Sim | gen_random_uuid() | — |
| nome | text | Sim | — | — |
| tipo | text | Não | — | — |
| unidade | text | Não | — | — |
| ativo | boolean | Não | true | — |
| created_at | timestamp with time zone | Não | now() | — |

### Chave primária
- `CONSTRAINT document_templates_pkey PRIMARY KEY (id)`

### Relacionamentos

Nenhuma chave estrangeira identificada.

### Constraints
- `CONSTRAINT document_templates_nome_unidade_key UNIQUE (nome, unidade)`

### Índices

Nenhum índice adicional identificado.

### Triggers

Nenhum trigger associado.

### Políticas RLS

RLS: **habilitada**.
- `t2a_read`: `FOR SELECT USING ((public.get_my_tier() = ANY (ARRAY['T2A'::text, 'T2B'::text, 'T3'::text, 'T4'::text])))`
- `t4_master`: `USING ((public.get_my_tier() = 'T4'::text))`

## documents

### Finalidade

Descrição inferida pela estrutura: armazena registros relacionados a `documents`. A finalidade de negócio exata deve ser confirmada com a equipe responsável.

### Colunas

| Coluna | Tipo | Obrigatória | Padrão | Observação |
|---|---|---|---|---|
| id | uuid | Sim | gen_random_uuid() | — |
| employee_id | uuid | Não | — | — |
| unit_id | uuid | Não | — | — |
| name | text | Sim | — | — |
| type | text | Sim | 'outro'::text | — |
| storage_path | text | Sim | — | — |
| notes | text | Não | — | — |
| uploaded_at | timestamp with time zone | Não | now() | — |

### Chave primária
- `CONSTRAINT documents_pkey PRIMARY KEY (id)`

### Relacionamentos
- `documents_employee_id_fkey`: `employee_id` → `public.employees(id)` (ON DELETE CASCADE)
- `documents_unit_id_fkey`: `unit_id` → `public.units(id)`

### Constraints
- `CONSTRAINT documents_type_check CHECK ((type = ANY (ARRAY['rg_cnh'::text, 'cpf'::text, 'residencia'::text, 'foto_3x4'::text, 'ctps'::text, 'exame_admissional'::text, 'dados_bancarios'::text, 'certidao_filhos'::text, 'atestado'::text, 'declaracao_ir'::text, 'outro'::text, 'RG'::text, 'CPF'::text, 'CTPS'::text, 'contrato'::text, 'exame'::text, 'relatorio_folha'::text])))`

### Índices
- `documents_employee_id_idx`: `USING btree (employee_id)`
- `idx_documents_employee`: `USING btree (employee_id)`
- `idx_documents_type`: `USING btree (type)`

### Triggers

Nenhum trigger associado.

### Políticas RLS

RLS: **habilitada**.
- `documents_delete`: `FOR DELETE USING (public.kph_is_founder())`
- `documents_insert`: `FOR INSERT WITH CHECK (public.kph_has_role_for_unit(unit_id))`
- `documents_select`: `FOR SELECT USING (public.kph_has_role_for_unit(unit_id))`
- `documents_update`: `FOR UPDATE USING (public.kph_has_role_for_unit(unit_id))`
- `service_role_full_access`: `USING (true) WITH CHECK (true)`

## dre_contratos_fixos

### Finalidade

Descrição inferida pela estrutura: armazena registros relacionados a `dre contratos fixos`. A finalidade de negócio exata deve ser confirmada com a equipe responsável.

### Colunas

| Coluna | Tipo | Obrigatória | Padrão | Observação |
|---|---|---|---|---|
| id | bigint | Sim | — | — |
| razao_social | text | Sim | — | — |
| descricao | text | Não | — | — |
| valor_mensal | numeric | Sim | — | — |
| codigo_contabil | text | Não | — | — |
| tipo | text | Não | — | — |
| unit_id | uuid | Não | — | — |

### Chave primária
- `CONSTRAINT dre_contratos_fixos_pkey PRIMARY KEY (id)`

### Relacionamentos

Nenhuma chave estrangeira identificada.

### Constraints

Nenhuma constraint adicional identificada.

### Índices
- `idx_dre_contratos_unit_id`: `USING btree (unit_id)`

### Triggers

Nenhum trigger associado.

### Políticas RLS

RLS: **habilitada**.
- `allow_all`: `USING (true) WITH CHECK (true)`

## dre_despesa_detalhada

### Finalidade

Descrição inferida pela estrutura: armazena registros relacionados a `dre despesa detalhada`. A finalidade de negócio exata deve ser confirmada com a equipe responsável.

### Colunas

| Coluna | Tipo | Obrigatória | Padrão | Observação |
|---|---|---|---|---|
| id | integer | Sim | — | — |
| mes_ano | character varying(7) | Sim | — | — |
| data_competencia | date | Não | — | — |
| descricao | text | Não | — | — |
| categoria | character varying(100) | Não | — | — |
| valor | numeric | Sim | — | — |
| classificacao_dre | character varying(100) | Não | — | — |
| tipo_despesa | character varying(60) | Não | — | — |
| criado_em | timestamp with time zone | Não | now() | — |
| unit_id | uuid | Não | — | — |

### Chave primária
- `CONSTRAINT dre_despesa_detalhada_pkey PRIMARY KEY (id)`

### Relacionamentos

Nenhuma chave estrangeira identificada.

### Constraints

Nenhuma constraint adicional identificada.

### Índices
- `idx_dre_despesa_cls`: `USING btree (classificacao_dre)`
- `idx_dre_despesa_det_unit_id`: `USING btree (unit_id)`
- `idx_dre_despesa_mes`: `USING btree (mes_ano)`
- `idx_dre_despesa_tipo`: `USING btree (tipo_despesa)`

### Triggers

Nenhum trigger associado.

### Políticas RLS

RLS: **habilitada**.
- `dre_despesa_manage`: `TO service_role USING (true) WITH CHECK (true)`
- `dre_despesa_read`: `FOR SELECT TO authenticated, anon USING (true)`

## dre_faturamento_historico

### Finalidade

Descrição inferida pela estrutura: armazena registros relacionados a `dre faturamento historico`. A finalidade de negócio exata deve ser confirmada com a equipe responsável.

### Colunas

| Coluna | Tipo | Obrigatória | Padrão | Observação |
|---|---|---|---|---|
| id | integer | Sim | — | — |
| mes_num | smallint | Sim | — | — |
| categoria | character varying(20) | Sim | — | — |
| rec_2022 | numeric | Não | — | — |
| rec_2023 | numeric | Não | — | — |
| rec_2024 | numeric | Não | — | — |
| rec_2025 | numeric | Não | — | — |
| rec_2026_bd | numeric | Não | — | — |
| clientes_bd | integer | Não | — | — |
| ticket_bd | numeric | Não | — | — |
| criado_em | timestamp with time zone | Não | now() | — |
| unit_id | uuid | Não | — | — |

### Chave primária
- `CONSTRAINT dre_faturamento_historico_pkey PRIMARY KEY (id)`

### Relacionamentos

Nenhuma chave estrangeira identificada.

### Constraints
- `CONSTRAINT dre_faturamento_historico_categoria_check CHECK (((categoria)::text = ANY ((ARRAY['restaurante'::character varying, 'eventos'::character varying, 'total'::character varying])::text[])))`
- `CONSTRAINT dre_faturamento_historico_mes_num_check CHECK (((mes_num >= 1) AND (mes_num <= 12)))`
- `CONSTRAINT dre_faturamento_historico_mes_num_categoria_unit_id_key UNIQUE (mes_num, categoria, unit_id)`

### Índices
- `idx_dre_historico_unit_id`: `USING btree (unit_id)`

### Triggers

Nenhum trigger associado.

### Políticas RLS

RLS: **habilitada**.
- `dre_fat_manage`: `TO service_role USING (true) WITH CHECK (true)`
- `dre_fat_read`: `FOR SELECT TO authenticated, anon USING (true)`

## dre_folha

### Finalidade

Descrição inferida pela estrutura: armazena registros relacionados a `dre folha`. A finalidade de negócio exata deve ser confirmada com a equipe responsável.

### Colunas

| Coluna | Tipo | Obrigatória | Padrão | Observação |
|---|---|---|---|---|
| id | integer | Sim | — | — |
| tipo | character varying(10) | Sim | — | — |
| nome | character varying(120) | Não | — | — |
| funcao | character varying(80) | Sim | — | — |
| divisao | character varying(40) | Sim | — | — |
| admissao | date | Não | — | — |
| salario | numeric | Sim | — | — |
| custo_total | numeric | Sim | — | — |
| is_vaga | boolean | Sim | false | — |
| criado_em | timestamp with time zone | Não | now() | — |
| unit_id | uuid | Não | — | — |
| competencia | text | Não | — | — |

### Chave primária
- `CONSTRAINT dre_folha_pkey PRIMARY KEY (id)`

### Relacionamentos

Nenhuma chave estrangeira identificada.

### Constraints

Nenhuma constraint adicional identificada.

### Índices
- `idx_dre_folha_competencia`: `USING btree (unit_id, competencia)`
- `idx_dre_folha_unit_id`: `USING btree (unit_id)`

### Triggers

Nenhum trigger associado.

### Políticas RLS

RLS: **habilitada**.
- `dre_folha_manage`: `TO service_role USING (true) WITH CHECK (true)`
- `dre_folha_read`: `FOR SELECT TO authenticated, anon USING (true)`

## dre_gorjeta_mensal

### Finalidade

Descrição inferida pela estrutura: armazena registros relacionados a `dre gorjeta mensal`. A finalidade de negócio exata deve ser confirmada com a equipe responsável.

### Colunas

| Coluna | Tipo | Obrigatória | Padrão | Observação |
|---|---|---|---|---|
| id | integer | Sim | — | — |
| mes_ano | character varying(7) | Sim | — | — |
| gorjeta_recebida | numeric | Não | — | — |
| gorjeta_paga | numeric | Não | — | — |
| retencao | numeric | Não | — | — |
| ferias | numeric | Não | — | — |
| decimo_terceiro | numeric | Não | — | — |
| fgts | numeric | Não | — | — |
| inss | numeric | Não | — | — |
| encargos_total | numeric | Não | — | — |
| criado_em | timestamp with time zone | Não | now() | — |
| unit_id | uuid | Não | — | — |

### Chave primária
- `CONSTRAINT dre_gorjeta_mensal_pkey PRIMARY KEY (id)`

### Relacionamentos

Nenhuma chave estrangeira identificada.

### Constraints
- `CONSTRAINT dre_gorjeta_mensal_mes_ano_unit_id_key UNIQUE (mes_ano, unit_id)`

### Índices
- `idx_dre_gorjeta_unit_id`: `USING btree (unit_id)`

### Triggers

Nenhum trigger associado.

### Políticas RLS

RLS: **habilitada**.
- `dre_gorjeta_manage`: `TO service_role USING (true) WITH CHECK (true)`
- `dre_gorjeta_read`: `FOR SELECT TO authenticated, anon USING (true)`

## dre_indicadores

### Finalidade

Descrição inferida pela estrutura: armazena registros relacionados a `dre indicadores`. A finalidade de negócio exata deve ser confirmada com a equipe responsável.

### Colunas

| Coluna | Tipo | Obrigatória | Padrão | Observação |
|---|---|---|---|---|
| id | integer | Sim | — | — |
| mes_ano | character varying(7) | Sim | — | — |
| tipo | character varying(20) | Sim | — | — |
| indicador | character varying(40) | Sim | — | — |
| valor | numeric | Não | — | — |
| criado_em | timestamp with time zone | Não | now() | — |
| unit_id | uuid | Não | — | — |

### Chave primária
- `CONSTRAINT dre_indicadores_pkey PRIMARY KEY (id)`

### Relacionamentos

Nenhuma chave estrangeira identificada.

### Constraints
- `CONSTRAINT dre_indicadores_tipo_check CHECK (((tipo)::text = ANY ((ARRAY['orcado'::character varying, 'realizado'::character varying])::text[])))`
- `CONSTRAINT dre_indicadores_mes_ano_tipo_indicador_unit_key UNIQUE (mes_ano, tipo, indicador, unit_id)`

### Índices
- `idx_dre_indicadores_unit_id`: `USING btree (unit_id)`

### Triggers

Nenhum trigger associado.

### Políticas RLS

RLS: **habilitada**.
- `dre_indicadores_manage`: `TO service_role USING (true) WITH CHECK (true)`
- `dre_indicadores_read`: `FOR SELECT TO authenticated, anon USING (true)`

## dre_kpis_mensais

### Finalidade

Descrição inferida pela estrutura: armazena registros relacionados a `dre kpis mensais`. A finalidade de negócio exata deve ser confirmada com a equipe responsável.

### Colunas

| Coluna | Tipo | Obrigatória | Padrão | Observação |
|---|---|---|---|---|
| mes_ano | text | Sim | — | — |
| clientes | integer | Não | — | — |
| ticket_medio | numeric | Não | — | — |
| gorjetas_recebidas | numeric | Não | — | — |
| icms | numeric | Não | — | — |
| cofins | numeric | Não | — | — |
| pis | numeric | Não | — | — |
| iss | numeric | Não | — | — |
| unit_id | uuid | Sim | — | — |

### Chave primária
- `CONSTRAINT dre_kpis_mensais_pkey PRIMARY KEY (mes_ano, unit_id)`

### Relacionamentos

Nenhuma chave estrangeira identificada.

### Constraints

Nenhuma constraint adicional identificada.

### Índices
- `idx_dre_kpis_unit_id`: `USING btree (unit_id)`

### Triggers

Nenhum trigger associado.

### Políticas RLS

RLS: **habilitada**.
- `allow_all`: `USING (true) WITH CHECK (true)`

## dre_linhas_detalhadas

### Finalidade

Descrição inferida pela estrutura: armazena registros relacionados a `dre linhas detalhadas`. A finalidade de negócio exata deve ser confirmada com a equipe responsável.

### Colunas

| Coluna | Tipo | Obrigatória | Padrão | Observação |
|---|---|---|---|---|
| id | bigint | Sim | — | — |
| mes_ano | character varying | Sim | — | — |
| tipo | character varying | Sim | — | — |
| grupo | character varying | Sim | — | — |
| descricao | character varying | Sim | — | — |
| conta | character varying | Não | — | — |
| custo_tipo | character varying | Não | — | — |
| valor | numeric | Não | — | — |
| av_percentual | numeric | Não | — | — |
| criado_em | timestamp without time zone | Não | now() | — |
| unit_id | uuid | Não | — | — |

### Chave primária
- `CONSTRAINT dre_linhas_detalhadas_pkey PRIMARY KEY (id)`

### Relacionamentos

Nenhuma chave estrangeira identificada.

### Constraints

Nenhuma constraint adicional identificada.

### Índices
- `idx_dre_linhas_det_unit_id`: `USING btree (unit_id)`

### Triggers

Nenhum trigger associado.

### Políticas RLS

RLS: **habilitada**.
- `allow_all`: `USING (true)`
- `service_role_all`: `TO service_role USING (true)`

## dre_manutencao_detalhada

### Finalidade

Descrição inferida pela estrutura: armazena registros relacionados a `dre manutencao detalhada`. A finalidade de negócio exata deve ser confirmada com a equipe responsável.

### Colunas

| Coluna | Tipo | Obrigatória | Padrão | Observação |
|---|---|---|---|---|
| id | bigint | Sim | — | — |
| mes_ano | text | Não | — | — |
| fornecedor | text | Sim | — | — |
| categoria | text | Sim | — | — |
| valor | numeric | Sim | — | — |
| unit_id | uuid | Não | — | — |

### Chave primária
- `CONSTRAINT dre_manutencao_detalhada_pkey PRIMARY KEY (id)`

### Relacionamentos

Nenhuma chave estrangeira identificada.

### Constraints

Nenhuma constraint adicional identificada.

### Índices
- `idx_dre_manutencao_det_unit_id`: `USING btree (unit_id)`
- `idx_manutencao_mes`: `USING btree (mes_ano)`

### Triggers

Nenhum trigger associado.

### Políticas RLS

RLS: **habilitada**.
- `allow_all`: `USING (true) WITH CHECK (true)`

## dre_mensal

### Finalidade

Descrição inferida pela estrutura: armazena registros relacionados a `dre mensal`. A finalidade de negócio exata deve ser confirmada com a equipe responsável.

### Colunas

| Coluna | Tipo | Obrigatória | Padrão | Observação |
|---|---|---|---|---|
| id | integer | Sim | — | — |
| mes_ano | character varying(7) | Sim | — | — |
| tipo | character varying(20) | Sim | — | — |
| receita_bruta | numeric | Não | — | — |
| cmv | numeric | Não | — | — |
| pessoal | numeric | Não | — | — |
| ocupacao | numeric | Não | — | — |
| utilidades | numeric | Não | — | — |
| operacao | numeric | Não | — | — |
| manutencao | numeric | Não | — | — |
| administrativa | numeric | Não | — | — |
| marketing | numeric | Não | — | — |
| taxa_cartao | numeric | Não | — | — |
| impostos | numeric | Não | — | — |
| ebitda | numeric | Não | — | — |
| resultado_liquido | numeric | Não | — | — |
| clientes | integer | Não | — | — |
| ticket_medio | numeric | Não | — | — |
| criado_em | timestamp with time zone | Não | now() | — |
| unit_id | uuid | Não | — | — |

### Chave primária
- `CONSTRAINT dre_mensal_pkey PRIMARY KEY (id)`

### Relacionamentos

Nenhuma chave estrangeira identificada.

### Constraints
- `CONSTRAINT dre_mensal_tipo_check CHECK (((tipo)::text = ANY ((ARRAY['orcado'::character varying, 'realizado'::character varying])::text[])))`
- `CONSTRAINT dre_mensal_mes_ano_tipo_unit_key UNIQUE (mes_ano, tipo, unit_id)`

### Índices
- `idx_dre_mensal_unit_id`: `USING btree (unit_id)`

### Triggers

Nenhum trigger associado.

### Políticas RLS

RLS: **habilitada**.
- `dre_mensal_manage`: `TO service_role USING (true) WITH CHECK (true)`
- `dre_mensal_read`: `FOR SELECT TO authenticated, anon USING (true)`

## dre_pessoal_detalhado

### Finalidade

Descrição inferida pela estrutura: armazena registros relacionados a `dre pessoal detalhado`. A finalidade de negócio exata deve ser confirmada com a equipe responsável.

### Colunas

| Coluna | Tipo | Obrigatória | Padrão | Observação |
|---|---|---|---|---|
| id | bigint | Sim | — | — |
| mes_ano | text | Sim | — | — |
| categoria | text | Sim | — | — |
| valor | numeric | Não | — | — |
| unit_id | uuid | Não | — | — |

### Chave primária
- `CONSTRAINT dre_pessoal_detalhado_pkey PRIMARY KEY (id)`

### Relacionamentos

Nenhuma chave estrangeira identificada.

### Constraints
- `CONSTRAINT dre_pessoal_detalhado_mes_ano_categoria_unit_id_key UNIQUE (mes_ano, categoria, unit_id)`

### Índices
- `idx_dre_pessoal_det_unit_id`: `USING btree (unit_id)`

### Triggers

Nenhum trigger associado.

### Políticas RLS

RLS: **habilitada**.
- `allow_all`: `USING (true) WITH CHECK (true)`

## dre_prestadores

### Finalidade

Descrição inferida pela estrutura: armazena registros relacionados a `dre prestadores`. A finalidade de negócio exata deve ser confirmada com a equipe responsável.

### Colunas

| Coluna | Tipo | Obrigatória | Padrão | Observação |
|---|---|---|---|---|
| id | bigint | Sim | — | — |
| mes_ano | text | Sim | — | — |
| nome | text | Sim | — | — |
| grupo | text | Sim | — | — |
| valor | numeric | Sim | — | — |
| unit_id | uuid | Não | — | — |

### Chave primária
- `CONSTRAINT dre_prestadores_pkey PRIMARY KEY (id)`

### Relacionamentos

Nenhuma chave estrangeira identificada.

### Constraints
- `CONSTRAINT dre_prestadores_mes_ano_nome_grupo_unit_id_key UNIQUE (mes_ano, nome, grupo, unit_id)`

### Índices
- `idx_dre_prestadores_unit_id`: `USING btree (unit_id)`
- `idx_prestadores_mes`: `USING btree (mes_ano)`

### Triggers

Nenhum trigger associado.

### Políticas RLS

RLS: **habilitada**.
- `allow_all`: `USING (true) WITH CHECK (true)`

## dre_receita_detalhada

### Finalidade

Descrição inferida pela estrutura: armazena registros relacionados a `dre receita detalhada`. A finalidade de negócio exata deve ser confirmada com a equipe responsável.

### Colunas

| Coluna | Tipo | Obrigatória | Padrão | Observação |
|---|---|---|---|---|
| id | integer | Sim | — | — |
| mes_ano | character varying(7) | Sim | — | — |
| bandeira | character varying(50) | Sim | — | — |
| classificacao | character varying(60) | Sim | — | — |
| grupo | character varying(40) | Sim | — | — |
| valor | numeric | Sim | — | — |
| criado_em | timestamp with time zone | Não | now() | — |
| unit_id | uuid | Não | — | — |

### Chave primária
- `CONSTRAINT dre_receita_detalhada_pkey PRIMARY KEY (id)`

### Relacionamentos

Nenhuma chave estrangeira identificada.

### Constraints
- `CONSTRAINT dre_receita_detalhada_mes_ano_bandeira_unit_id_key UNIQUE (mes_ano, bandeira, unit_id)`

### Índices
- `idx_dre_receita_det_unit_id`: `USING btree (unit_id)`

### Triggers

Nenhum trigger associado.

### Políticas RLS

RLS: **habilitada**.
- `dre_receita_manage`: `TO service_role USING (true) WITH CHECK (true)`
- `dre_receita_read`: `FOR SELECT TO authenticated, anon USING (true)`

## employee_auth

### Finalidade

Descrição inferida pela estrutura: armazena registros relacionados a `employee auth`. A finalidade de negócio exata deve ser confirmada com a equipe responsável.

### Colunas

| Coluna | Tipo | Obrigatória | Padrão | Observação |
|---|---|---|---|---|
| id | uuid | Sim | gen_random_uuid() | — |
| employee_id | uuid | Sim | — | — |
| cpf | text | Sim | — | — |
| password_hash | text | Sim | — | — |
| is_active | boolean | Sim | true | — |
| last_login | timestamp with time zone | Não | — | — |
| created_at | timestamp with time zone | Não | now() | — |
| updated_at | timestamp with time zone | Não | now() | — |

### Chave primária
- `CONSTRAINT employee_auth_pkey PRIMARY KEY (id)`

### Relacionamentos
- `employee_auth_employee_id_fkey`: `employee_id` → `public.employees(id)`

### Constraints
- `CONSTRAINT employee_auth_cpf_key UNIQUE (cpf)`

### Índices
- `idx_employee_auth_cpf`: `USING btree (cpf)`
- `idx_employee_auth_employee`: `USING btree (employee_id)`

### Triggers

Nenhum trigger associado.

### Políticas RLS

RLS: **habilitada**.
- `employee_auth_delete`: `FOR DELETE USING (public.kph_is_founder())`
- `employee_auth_insert`: `FOR INSERT WITH CHECK ((EXISTS ( SELECT 1 FROM public.employees e WHERE ((e.id = employee_auth.employee_id) AND public.kph_has_role_for_unit(e.unit_id)))))`
- `employee_auth_login`: `FOR SELECT USING (true)`
- `employee_auth_select`: `FOR SELECT USING ((EXISTS ( SELECT 1 FROM public.employees e WHERE ((e.id = employee_auth.employee_id) AND public.kph_has_role_for_unit(e.unit_id)))))`
- `employee_auth_update`: `FOR UPDATE USING ((EXISTS ( SELECT 1 FROM public.employees e WHERE ((e.id = employee_auth.employee_id) AND public.kph_has_role_for_unit(e.unit_id)))))`

## employee_availability

### Finalidade

Descrição inferida pela estrutura: armazena registros relacionados a `employee availability`. A finalidade de negócio exata deve ser confirmada com a equipe responsável.

### Colunas

| Coluna | Tipo | Obrigatória | Padrão | Observação |
|---|---|---|---|---|
| id | uuid | Sim | gen_random_uuid() | — |
| employee_id | uuid | Sim | — | — |
| unit_id | uuid | Sim | — | — |
| data | date | Sim | — | — |
| disponivel | boolean | Sim | false | — |
| motivo | text | Não | — | — |
| created_at | timestamp with time zone | Sim | now() | — |

### Chave primária
- `CONSTRAINT employee_availability_pkey PRIMARY KEY (id)`

### Relacionamentos
- `employee_availability_employee_id_fkey`: `employee_id` → `public.employees(id)` (ON DELETE CASCADE)
- `employee_availability_unit_id_fkey`: `unit_id` → `public.units(id)` (ON DELETE CASCADE)

### Constraints
- `CONSTRAINT employee_availability_employee_id_data_key UNIQUE (employee_id, data)`

### Índices
- `employee_availability_unit_data_idx`: `USING btree (unit_id, data)`

### Triggers

Nenhum trigger associado.

### Políticas RLS

RLS: **habilitada**.
- `employee_availability_all`: `USING (public.kph_has_role_for_unit(unit_id)) WITH CHECK (public.kph_has_role_for_unit(unit_id))`
- `employee_availability_select`: `FOR SELECT USING (public.kph_has_role_for_unit(unit_id))`

## employee_benefits

### Finalidade

Descrição inferida pela estrutura: armazena registros relacionados a `employee benefits`. A finalidade de negócio exata deve ser confirmada com a equipe responsável.

### Colunas

| Coluna | Tipo | Obrigatória | Padrão | Observação |
|---|---|---|---|---|
| id | uuid | Sim | gen_random_uuid() | — |
| unit_id | uuid | Não | — | — |
| employee_id | uuid | Não | — | — |
| tipo | text | Não | — | — |
| valor | numeric(10,2) | Não | — | — |
| competencia | date | Não | — | — |
| detalhes | jsonb | Não | — | — |
| created_at | timestamp with time zone | Não | now() | — |

### Chave primária
- `CONSTRAINT employee_benefits_pkey PRIMARY KEY (id)`

### Relacionamentos
- `employee_benefits_employee_id_fkey`: `employee_id` → `public.employees(id)`
- `employee_benefits_unit_id_fkey`: `unit_id` → `public.units(id)`

### Constraints
- `CONSTRAINT employee_benefits_employee_id_tipo_competencia_key UNIQUE (employee_id, tipo, competencia)`

### Índices

Nenhum índice adicional identificado.

### Triggers

Nenhum trigger associado.

### Políticas RLS

RLS: **habilitada**.
- `t1_own`: `FOR SELECT USING ((employee_id = ( SELECT employees.id FROM public.employees WHERE (employees.user_id = auth.uid()))))`
- `t3_dept`: `USING ((public.get_my_tier() = 'T3'::text))`
- `t4_master`: `USING ((public.get_my_tier() = 'T4'::text))`

## employee_codigos_dominio

### Finalidade

Descrição inferida pela estrutura: armazena registros relacionados a `employee codigos dominio`. A finalidade de negócio exata deve ser confirmada com a equipe responsável.

### Colunas

| Coluna | Tipo | Obrigatória | Padrão | Observação |
|---|---|---|---|---|
| employee_id | uuid | Sim | — | — |
| unit_id | uuid | Sim | — | — |
| cod_folha | text | Sim | — | — |
| ativo | boolean | Sim | true | — |
| created_at | timestamp with time zone | Sim | now() | — |

### Chave primária
- `CONSTRAINT employee_codigos_dominio_pkey PRIMARY KEY (employee_id, unit_id)`

### Relacionamentos
- `employee_codigos_dominio_employee_id_fkey`: `employee_id` → `public.employees(id)` (ON DELETE CASCADE)
- `employee_codigos_dominio_unit_id_fkey`: `unit_id` → `public.units(id)` (ON DELETE CASCADE)

### Constraints

Nenhuma constraint adicional identificada.

### Índices
- `idx_ecd_folha`: `USING btree (cod_folha)`
- `idx_ecd_unit`: `USING btree (unit_id)`

### Triggers

Nenhum trigger associado.

### Políticas RLS

RLS: **não habilitada no dump**.

Nenhuma política associada.

## employee_documents

### Finalidade

Descrição inferida pela estrutura: armazena registros relacionados a `employee documents`. A finalidade de negócio exata deve ser confirmada com a equipe responsável.

### Colunas

| Coluna | Tipo | Obrigatória | Padrão | Observação |
|---|---|---|---|---|
| id | uuid | Sim | gen_random_uuid() | — |
| employee_id | uuid | Sim | — | — |
| tipo | text | Sim | — | — |
| nome | text | Sim | — | — |
| descricao | text | Não | — | — |
| file_path | text | Sim | ''::text | — |
| file_size | bigint | Não | — | — |
| mime_type | text | Não | — | — |
| data_emissao | date | Não | — | — |
| data_validade | date | Não | — | — |
| observacoes | text | Não | — | — |
| uploaded_by | uuid | Não | — | — |
| created_at | timestamp with time zone | Não | now() | — |
| updated_at | timestamp with time zone | Não | now() | — |

### Chave primária
- `CONSTRAINT employee_documents_pkey PRIMARY KEY (id)`

### Relacionamentos
- `employee_documents_employee_id_fkey`: `employee_id` → `public.employees(id)` (ON DELETE CASCADE)
- `employee_documents_uploaded_by_fkey`: `uploaded_by` → `auth.users(id)` (ON DELETE SET NULL)

### Constraints
- `CONSTRAINT employee_documents_tipo_check CHECK ((tipo = ANY (ARRAY['rg'::text, 'cpf'::text, 'ctps'::text, 'pis_pasep'::text, 'titulo_eleitor'::text, 'comprovante_residencia'::text, 'foto_3x4'::text, 'aso_admissional'::text, 'reservista'::text, 'certidao_nascimento'::text, 'certidao_casamento'::text, 'cnh'::text, 'outros'::text])))`

### Índices
- `idx_emp_docs_employee`: `USING btree (employee_id)`
- `idx_emp_docs_tipo`: `USING btree (tipo)`
- `idx_emp_docs_validade`: `USING btree (data_validade) WHERE (data_validade IS NOT NULL)`

### Triggers

Nenhum trigger associado.

### Políticas RLS

RLS: **habilitada**.
- `emp_docs_delete`: `FOR DELETE USING (public.kph_is_founder())`
- `emp_docs_insert`: `FOR INSERT WITH CHECK ((EXISTS ( SELECT 1 FROM public.employees e WHERE ((e.id = employee_documents.employee_id) AND public.kph_has_role_for_unit(e.unit_id)))))`
- `emp_docs_select`: `FOR SELECT USING ((EXISTS ( SELECT 1 FROM public.employees e WHERE ((e.id = employee_documents.employee_id) AND ((e.user_id = auth.uid()) OR public.kph_has_role_for_unit(e.unit_id))))))`
- `emp_docs_update`: `FOR UPDATE USING ((EXISTS ( SELECT 1 FROM public.employees e WHERE ((e.id = employee_documents.employee_id) AND public.kph_has_role_for_unit(e.unit_id)))))`

## employees

### Finalidade

Descrição inferida pela estrutura: armazena registros relacionados a `employees`. A finalidade de negócio exata deve ser confirmada com a equipe responsável.

### Colunas

| Coluna | Tipo | Obrigatória | Padrão | Observação |
|---|---|---|---|---|
| id | uuid | Sim | gen_random_uuid() | — |
| unit_id | uuid | Sim | — | — |
| user_id | uuid | Não | — | — |
| nome | text | Sim | — | — |
| sobrenome | text | Sim | — | — |
| cpf | text | Não | — | — |
| ctps | text | Não | — | — |
| funcao | text | Sim | — | — |
| salario_base | numeric(10,2) | Sim | 0 | — |
| data_admissao | date | Sim | — | — |
| data_demissao | date | Não | — | — |
| ativo | boolean | Não | true | — |
| banco | text | Não | — | — |
| agencia | text | Não | — | — |
| conta | text | Não | — | — |
| tipo_conta | text | Não | — | — |
| pix | text | Não | — | — |
| created_at | timestamp with time zone | Não | now() | — |
| updated_at | timestamp with time zone | Não | now() | — |
| rg | text | Não | — | — |
| rg_orgao | text | Não | — | — |
| rg_uf | character(2) | Não | — | — |
| pis | text | Não | — | — |
| ctps_serie | text | Não | — | — |
| ctps_uf | character(2) | Não | — | — |
| titulo_eleitor | text | Não | — | — |
| reservista | text | Não | — | — |
| rua | text | Não | — | — |
| numero | text | Não | — | — |
| complemento | text | Não | — | — |
| bairro | text | Não | — | — |
| cidade | text | Não | — | — |
| estado | character(2) | Não | — | — |
| cep | text | Não | — | — |
| escolaridade | text | Não | — | — |
| raca | text | Não | — | — |
| genero | text | Não | — | — |
| nome_mae | text | Não | — | — |
| nome_pai | text | Não | — | — |
| departamento | text | Não | — | — |
| employee_code | text | Não | — | — |
| esocial_code | text | Não | — | — |
| nome_social | text | Não | — | — |
| data_nascimento | date | Não | — | — |
| cidade_nascimento | text | Não | — | — |
| uf_nascimento | character(2) | Não | — | — |
| pais_nascimento | text | Não | 'Brasil'::text | — |
| estado_civil | text | Não | — | — |
| tipo_contrato | text | Não | — | — |
| jornada | text | Não | — | — |
| telefone | text | Não | — | — |
| email | text | Não | — | — |
| contato_emergencia_nome | text | Não | — | — |
| contato_emergencia_tel | text | Não | — | — |
| photo_url | text | Não | — | — |
| ctps_expedicao | date | Não | — | — |
| zona_eleitoral | text | Não | — | — |
| secao_eleitoral | text | Não | — | — |
| rne | text | Não | — | — |
| rne_orgao | text | Não | — | — |
| rne_expedicao | date | Não | — | — |
| status_rh | text | Não | 'ativo'::text | — |
| score | integer | Sim | 100 | — |
| manager_id | uuid | Não | — | — |
| mise_ativo | boolean | Não | false | — |
| role_id | uuid | Não | — | — |
| tier | text | Não | — | — |
| observacao | text | Não | — | — |
| push_token | text | Não | — | — |
| push_token_updated_at | timestamp with time zone | Não | — | — |

### Chave primária
- `CONSTRAINT employees_pkey PRIMARY KEY (id)`

### Relacionamentos
- `employees_manager_id_fkey`: `manager_id` → `public.employees(id)`
- `employees_role_id_fkey`: `role_id` → `public.roles(id)` (ON DELETE SET NULL)
- `employees_unit_id_fkey`: `unit_id` → `public.units(id)` (ON DELETE CASCADE)
- `employees_user_id_fkey`: `user_id` → `auth.users(id)`

### Constraints
- `CONSTRAINT employees_status_rh_check CHECK ((status_rh = ANY (ARRAY['ativo'::text, 'inativo'::text, 'ferias'::text, 'afastado'::text])))`
- `CONSTRAINT employees_tier_check CHECK ((tier = ANY (ARRAY['T1'::text, 'T2A'::text, 'T2B'::text, 'T3'::text, 'T4'::text, 'T5'::text, 'T6'::text])))`
- `CONSTRAINT employees_tipo_contrato_check CHECK ((tipo_contrato = ANY (ARRAY['CLT'::text, 'PJ'::text, 'temporario'::text, 'estagiario'::text])))`
- `CONSTRAINT employees_cpf_key UNIQUE (cpf)`

### Índices
- `employees_manager`: `USING btree (manager_id)`
- `idx_employees_employee_code`: `USING btree (employee_code)`
- `idx_employees_score`: `USING btree (score DESC)`
- `idx_employees_status_rh`: `USING btree (status_rh)`
- `idx_employees_unit`: `USING btree (unit_id)`

### Triggers
- `trg_sync_employee_tier`: `BEFORE INSERT OR UPDATE OF role_id FOR EACH ROW EXECUTE FUNCTION public._sync_employee_tier()`

### Políticas RLS

RLS: **habilitada**.
- `employees_delete`: `FOR DELETE TO authenticated USING ((public.get_my_tier() = 'T4'::text))`
- `employees_insert`: `FOR INSERT TO authenticated WITH CHECK ((public.get_my_tier() = ANY (ARRAY['T3'::text, 'T4'::text])))`
- `employees_select`: `FOR SELECT TO authenticated USING (((public.get_my_tier() = ANY (ARRAY['T3'::text, 'T4'::text])) OR ((public.get_my_tier() = ANY (ARRAY['T2A'::text, 'T2B'::text])) AND (unit_id = public.get_my_unit())) OR (user_id = auth.uid())))`
- `employees_self_select`: `FOR SELECT TO authenticated USING ((user_id = auth.uid()))`
- `employees_update`: `FOR UPDATE TO authenticated USING (((public.get_my_tier() = ANY (ARRAY['T3'::text, 'T4'::text])) OR ((public.get_my_tier() = ANY (ARRAY['T2A'::text, 'T2B'::text])) AND (unit_id = public.get_my_unit()))))`

## event_attachments

### Finalidade

Descrição inferida pela estrutura: armazena registros relacionados a `event attachments`. A finalidade de negócio exata deve ser confirmada com a equipe responsável.

### Colunas

| Coluna | Tipo | Obrigatória | Padrão | Observação |
|---|---|---|---|---|
| id | uuid | Sim | gen_random_uuid() | — |
| event_id | uuid | Sim | — | — |
| nome | text | Sim | — | — |
| tipo | text | Não | — | — |
| storage_path | text | Sim | — | — |
| tamanho_bytes | bigint | Não | — | — |
| uploaded_by | uuid | Não | — | — |
| created_at | timestamp with time zone | Não | now() | — |

### Chave primária
- `CONSTRAINT event_attachments_pkey PRIMARY KEY (id)`

### Relacionamentos
- `event_attachments_event_id_fkey`: `event_id` → `public.events(id)` (ON DELETE CASCADE)
- `event_attachments_uploaded_by_fkey`: `uploaded_by` → `auth.users(id)`

### Constraints

Nenhuma constraint adicional identificada.

### Índices
- `idx_event_attachments_event_id`: `USING btree (event_id)`

### Triggers

Nenhum trigger associado.

### Políticas RLS

RLS: **habilitada**.
- `event_attachments_select`: `FOR SELECT USING ((EXISTS ( SELECT 1 FROM public.events e WHERE ((e.id = event_attachments.event_id) AND public.kph_has_role_for_brand(e.brand_id)))))`
- `event_attachments_write`: `USING ((EXISTS ( SELECT 1 FROM public.events e WHERE ((e.id = event_attachments.event_id) AND public.kph_can_write_event_brand(e.brand_id))))) WITH CHECK ((EXISTS ( SELECT 1 FROM public.events e WHERE ((e.id = event_attachments.event_id) AND public.kph_can_write_event_brand(e.brand_id)))))`

## event_infra_items

### Finalidade

Descrição inferida pela estrutura: armazena registros relacionados a `event infra items`. A finalidade de negócio exata deve ser confirmada com a equipe responsável.

### Colunas

| Coluna | Tipo | Obrigatória | Padrão | Observação |
|---|---|---|---|---|
| id | uuid | Sim | gen_random_uuid() | — |
| event_id | uuid | Sim | — | — |
| categoria | text | Sim | — | — |
| item | text | Sim | — | — |
| quantidade | integer | Não | 1 | — |
| responsavel | text | Não | — | — |
| status | text | Não | 'pendente'::text | — |
| observacoes | text | Não | — | — |
| sort_order | integer | Não | 0 | — |
| created_at | timestamp with time zone | Não | now() | — |

### Chave primária
- `CONSTRAINT event_infra_items_pkey PRIMARY KEY (id)`

### Relacionamentos
- `event_infra_items_event_id_fkey`: `event_id` → `public.events(id)` (ON DELETE CASCADE)

### Constraints

Nenhuma constraint adicional identificada.

### Índices
- `idx_event_infra_items_event_id`: `USING btree (event_id)`

### Triggers

Nenhum trigger associado.

### Políticas RLS

RLS: **habilitada**.
- `event_infra_items_select`: `FOR SELECT USING ((EXISTS ( SELECT 1 FROM public.events e WHERE ((e.id = event_infra_items.event_id) AND public.kph_has_role_for_brand(e.brand_id)))))`
- `event_infra_items_write`: `USING ((EXISTS ( SELECT 1 FROM public.events e WHERE ((e.id = event_infra_items.event_id) AND public.kph_can_write_event_brand(e.brand_id))))) WITH CHECK ((EXISTS ( SELECT 1 FROM public.events e WHERE ((e.id = event_infra_items.event_id) AND public.kph_can_write_event_brand(e.brand_id)))))`

## event_menu_items

### Finalidade

Descrição inferida pela estrutura: armazena registros relacionados a `event menu items`. A finalidade de negócio exata deve ser confirmada com a equipe responsável.

### Colunas

| Coluna | Tipo | Obrigatória | Padrão | Observação |
|---|---|---|---|---|
| id | uuid | Sim | gen_random_uuid() | — |
| event_id | uuid | Sim | — | — |
| categoria | public.menu_item_category | Sim | — | — |
| nome | text | Sim | — | — |
| descricao | text | Não | — | — |
| quantidade | integer | Não | — | — |
| unidade | text | Não | — | — |
| preco_unitario | numeric(10,2) | Não | — | — |
| observacoes | text | Não | — | — |
| sort_order | integer | Não | 0 | — |
| created_at | timestamp with time zone | Não | now() | — |

### Chave primária
- `CONSTRAINT event_menu_items_pkey PRIMARY KEY (id)`

### Relacionamentos
- `event_menu_items_event_id_fkey`: `event_id` → `public.events(id)` (ON DELETE CASCADE)

### Constraints

Nenhuma constraint adicional identificada.

### Índices
- `idx_event_menu_items_event_id`: `USING btree (event_id)`

### Triggers

Nenhum trigger associado.

### Políticas RLS

RLS: **habilitada**.
- `event_menu_items_select`: `FOR SELECT USING ((EXISTS ( SELECT 1 FROM public.events e WHERE ((e.id = event_menu_items.event_id) AND public.kph_has_role_for_brand(e.brand_id)))))`
- `event_menu_items_write`: `USING ((EXISTS ( SELECT 1 FROM public.events e WHERE ((e.id = event_menu_items.event_id) AND public.kph_can_write_event_brand(e.brand_id))))) WITH CHECK ((EXISTS ( SELECT 1 FROM public.events e WHERE ((e.id = event_menu_items.event_id) AND public.kph_can_write_event_brand(e.brand_id)))))`

## event_staff

### Finalidade

Descrição inferida pela estrutura: armazena registros relacionados a `event staff`. A finalidade de negócio exata deve ser confirmada com a equipe responsável.

### Colunas

| Coluna | Tipo | Obrigatória | Padrão | Observação |
|---|---|---|---|---|
| id | uuid | Sim | gen_random_uuid() | — |
| event_id | uuid | Sim | — | — |
| employee_id | uuid | Não | — | — |
| nome_externo | text | Não | — | — |
| funcao | text | Sim | — | — |
| horario_entrada | time without time zone | Não | — | — |
| horario_saida | time without time zone | Não | — | — |
| observacoes | text | Não | — | — |
| confirmado | boolean | Não | false | — |
| created_at | timestamp with time zone | Não | now() | — |

### Chave primária
- `CONSTRAINT event_staff_pkey PRIMARY KEY (id)`

### Relacionamentos
- `event_staff_employee_id_fkey`: `employee_id` → `public.employees(id)`
- `event_staff_event_id_fkey`: `event_id` → `public.events(id)` (ON DELETE CASCADE)

### Constraints

Nenhuma constraint adicional identificada.

### Índices
- `idx_event_staff_event_id`: `USING btree (event_id)`

### Triggers

Nenhum trigger associado.

### Políticas RLS

RLS: **habilitada**.
- `event_staff_select`: `FOR SELECT USING ((EXISTS ( SELECT 1 FROM public.events e WHERE ((e.id = event_staff.event_id) AND public.kph_has_role_for_brand(e.brand_id)))))`
- `event_staff_write`: `USING ((EXISTS ( SELECT 1 FROM public.events e WHERE ((e.id = event_staff.event_id) AND public.kph_can_write_event_brand(e.brand_id))))) WITH CHECK ((EXISTS ( SELECT 1 FROM public.events e WHERE ((e.id = event_staff.event_id) AND public.kph_can_write_event_brand(e.brand_id)))))`

## event_status_log

### Finalidade

Descrição inferida pela estrutura: armazena registros relacionados a `event status log`. A finalidade de negócio exata deve ser confirmada com a equipe responsável.

### Colunas

| Coluna | Tipo | Obrigatória | Padrão | Observação |
|---|---|---|---|---|
| id | uuid | Sim | gen_random_uuid() | — |
| event_id | uuid | Sim | — | — |
| status_anterior | public.event_status | Não | — | — |
| status_novo | public.event_status | Sim | — | — |
| changed_by | uuid | Não | — | — |
| motivo | text | Não | — | — |
| created_at | timestamp with time zone | Não | now() | — |

### Chave primária
- `CONSTRAINT event_status_log_pkey PRIMARY KEY (id)`

### Relacionamentos
- `event_status_log_changed_by_fkey`: `changed_by` → `auth.users(id)`
- `event_status_log_event_id_fkey`: `event_id` → `public.events(id)` (ON DELETE CASCADE)

### Constraints

Nenhuma constraint adicional identificada.

### Índices
- `idx_event_status_log_event_id`: `USING btree (event_id, created_at DESC)`

### Triggers

Nenhum trigger associado.

### Políticas RLS

RLS: **habilitada**.
- `event_status_log_select`: `FOR SELECT USING ((EXISTS ( SELECT 1 FROM public.events e WHERE ((e.id = event_status_log.event_id) AND public.kph_has_role_for_brand(e.brand_id)))))`
- `event_status_log_write`: `USING ((EXISTS ( SELECT 1 FROM public.events e WHERE ((e.id = event_status_log.event_id) AND public.kph_can_write_event_brand(e.brand_id))))) WITH CHECK ((EXISTS ( SELECT 1 FROM public.events e WHERE ((e.id = event_status_log.event_id) AND public.kph_can_write_event_brand(e.brand_id)))))`

## events

### Finalidade

Descrição inferida pela estrutura: armazena registros relacionados a `events`. A finalidade de negócio exata deve ser confirmada com a equipe responsável.

### Colunas

| Coluna | Tipo | Obrigatória | Padrão | Observação |
|---|---|---|---|---|
| id | uuid | Sim | gen_random_uuid() | — |
| group_id | uuid | Sim | — | — |
| brand_id | uuid | Sim | — | — |
| unit_id | uuid | Não | — | — |
| nome | text | Sim | — | — |
| tipo | text | Não | — | — |
| data_inicio | timestamp with time zone | Sim | — | — |
| data_fim | timestamp with time zone | Não | — | — |
| num_convidados | integer | Não | — | — |
| responsavel_interno | uuid | Não | — | — |
| contato_cliente | text | Não | — | — |
| telefone_cliente | text | Não | — | — |
| email_cliente | text | Não | — | — |
| empresa_cliente | text | Não | — | — |
| observacoes | text | Não | — | — |
| status | public.event_status | Sim | 'rascunho'::public.event_status | — |
| valor_total | numeric(12,2) | Não | — | — |
| valor_sinal | numeric(12,2) | Não | — | — |
| valor_sinal_pago | boolean | Não | false | — |
| created_by | uuid | Não | — | — |
| approved_by | uuid | Não | — | — |
| approved_at | timestamp with time zone | Não | — | — |
| created_at | timestamp with time zone | Não | now() | — |
| updated_at | timestamp with time zone | Não | now() | — |
| tema | text | Não | — | — |
| hora_inicio | time without time zone | Não | — | — |
| hora_termino | time without time zone | Não | — | — |
| situacao_pagamento | text | Não | — | — |
| responsavel_comercial | text | Não | — | — |
| responsavel_operacional | text | Não | — | — |
| briefing_cliente | text | Não | — | — |
| espacos | text | Não | — | — |
| acesso_entrada | text | Não | — | — |
| acesso_obs | text | Não | — | — |
| mobiliario | text | Não | — | — |
| mobiliario_obs | text | Não | — | — |
| fotografia | text | Não | — | — |
| valet | text | Não | — | — |
| artistico | text | Não | — | — |
| gerador | text | Não | — | — |
| ambulancia | text | Não | — | — |
| menores | text | Não | — | — |
| montagem | text | Não | — | — |
| montagem_descricao | text | Não | — | — |
| brigada | jsonb | Não | — | — |
| menu_bar | jsonb | Não | — | — |
| menu_cozinha | jsonb | Não | — | — |
| campo_livre | text | Não | — | — |
| tempos_movimentos | text | Não | — | — |
| layout_anexos | text | Não | — | — |
| criado_por | text | Não | — | — |

### Chave primária
- `CONSTRAINT events_pkey PRIMARY KEY (id)`

### Relacionamentos
- `events_approved_by_fkey`: `approved_by` → `auth.users(id)`
- `events_brand_id_fkey`: `brand_id` → `public.brands(id)`
- `events_created_by_fkey`: `created_by` → `auth.users(id)`
- `events_group_id_fkey`: `group_id` → `public.groups(id)`
- `events_responsavel_interno_fkey`: `responsavel_interno` → `auth.users(id)`
- `events_unit_id_fkey`: `unit_id` → `public.units(id)`

### Constraints

Nenhuma constraint adicional identificada.

### Índices
- `idx_events_brand_id`: `USING btree (brand_id)`
- `idx_events_data_inicio`: `USING btree (data_inicio DESC)`
- `idx_events_status`: `USING btree (status)`
- `idx_events_unit_id`: `USING btree (unit_id)`

### Triggers
- `trg_events_updated_at`: `BEFORE UPDATE FOR EACH ROW EXECUTE FUNCTION public.events_set_updated_at()`

### Políticas RLS

RLS: **habilitada**.
- `events_delete`: `FOR DELETE USING (public.kph_can_delete_event_brand(brand_id))`
- `events_insert`: `FOR INSERT WITH CHECK (public.kph_can_write_event_brand(brand_id))`
- `events_select`: `FOR SELECT USING (public.kph_has_role_for_brand(brand_id))`
- `events_update`: `FOR UPDATE USING (public.kph_can_write_event_brand(brand_id))`

## feedback

### Finalidade

Descrição inferida pela estrutura: armazena registros relacionados a `feedback`. A finalidade de negócio exata deve ser confirmada com a equipe responsável.

### Colunas

| Coluna | Tipo | Obrigatória | Padrão | Observação |
|---|---|---|---|---|
| id | uuid | Sim | gen_random_uuid() | — |
| user_id | uuid | Não | — | — |
| type | text | Sim | — | — |
| module | text | Sim | — | — |
| description | text | Sim | — | — |
| priority | text | Sim | 'medium'::text | — |
| status | text | Sim | 'open'::text | — |
| created_at | timestamp with time zone | Sim | now() | — |

### Chave primária
- `CONSTRAINT feedback_pkey PRIMARY KEY (id)`

### Relacionamentos
- `feedback_user_id_fkey`: `user_id` → `auth.users(id)` (ON DELETE SET NULL)

### Constraints
- `CONSTRAINT feedback_priority_check CHECK ((priority = ANY (ARRAY['low'::text, 'medium'::text, 'high'::text])))`
- `CONSTRAINT feedback_status_check CHECK ((status = ANY (ARRAY['open'::text, 'triaged'::text, 'resolved'::text])))`
- `CONSTRAINT feedback_type_check CHECK ((type = ANY (ARRAY['bug'::text, 'suggestion'::text, 'other'::text])))`

### Índices
- `idx_feedback_created`: `USING btree (created_at DESC)`
- `idx_feedback_status`: `USING btree (status)`
- `idx_feedback_user`: `USING btree (user_id)`

### Triggers

Nenhum trigger associado.

### Políticas RLS

RLS: **habilitada**.
- `insert_feedback`: `FOR INSERT TO authenticated WITH CHECK ((user_id = auth.uid()))`
- `select_feedback`: `FOR SELECT USING (((user_id = auth.uid()) OR public.kph_is_founder_or_cfo()))`
- `update_status`: `FOR UPDATE USING (public.kph_is_founder_or_cfo()) WITH CHECK (public.kph_is_founder_or_cfo())`

## feedbacks

### Finalidade

Descrição inferida pela estrutura: armazena registros relacionados a `feedbacks`. A finalidade de negócio exata deve ser confirmada com a equipe responsável.

### Colunas

| Coluna | Tipo | Obrigatória | Padrão | Observação |
|---|---|---|---|---|
| id | uuid | Sim | gen_random_uuid() | — |
| unit_id | uuid | Sim | — | — |
| de_employee_id | uuid | Sim | — | — |
| para_employee_id | uuid | Sim | — | — |
| tipo | text | Sim | — | — |
| categoria | text | Sim | — | — |
| mensagem | text | Sim | — | — |
| anonimo | boolean | Não | false | — |
| created_at | timestamp with time zone | Não | now() | — |

### Chave primária
- `CONSTRAINT feedbacks_pkey PRIMARY KEY (id)`

### Relacionamentos
- `feedbacks_de_employee_id_fkey`: `de_employee_id` → `public.employees(id)`
- `feedbacks_para_employee_id_fkey`: `para_employee_id` → `public.employees(id)`
- `feedbacks_unit_id_fkey`: `unit_id` → `public.units(id)`

### Constraints
- `CONSTRAINT feedback_nao_proprio CHECK ((de_employee_id <> para_employee_id))`
- `CONSTRAINT feedbacks_categoria_check CHECK ((categoria = ANY (ARRAY['atendimento'::text, 'trabalho_em_equipe'::text, 'lideranca'::text, 'pontualidade'::text, 'tecnico'::text, 'comportamento'::text, 'outro'::text])))`
- `CONSTRAINT feedbacks_tipo_check CHECK ((tipo = ANY (ARRAY['positivo'::text, 'desenvolvimento'::text])))`

### Índices
- `feedbacks_para_employee`: `USING btree (para_employee_id)`
- `feedbacks_unit`: `USING btree (unit_id)`
- `idx_feedbacks_de`: `USING btree (de_employee_id)`
- `idx_feedbacks_para`: `USING btree (para_employee_id)`
- `idx_feedbacks_unit`: `USING btree (unit_id)`

### Triggers

Nenhum trigger associado.

### Políticas RLS

RLS: **habilitada**.
- `feedbacks_insert`: `FOR INSERT WITH CHECK (((de_employee_id IN ( SELECT employees.id FROM public.employees WHERE (employees.user_id = auth.uid()))) OR (public.get_my_tier() = ANY (ARRAY['T3'::text, 'T4'::text]))))`
- `feedbacks_read`: `FOR SELECT USING (((para_employee_id IN ( SELECT employees.id FROM public.employees WHERE (employees.user_id = auth.uid()))) OR (de_employee_id IN ( SELECT employees.id FROM public.employees WHERE (employees.user_id = auth.uid()))) OR (public.get_my_tier() = ANY (ARRAY['T3'::text, 'T4'::text]))))`
- `unit_access`: `USING ((unit_id IN ( SELECT user_roles.unit_id FROM public.user_roles WHERE (user_roles.user_id = auth.uid()))))`

## gorjeta_cargo_pontos

### Finalidade

Descrição inferida pela estrutura: armazena registros relacionados a `gorjeta cargo pontos`. A finalidade de negócio exata deve ser confirmada com a equipe responsável.

### Colunas

| Coluna | Tipo | Obrigatória | Padrão | Observação |
|---|---|---|---|---|
| id | uuid | Sim | gen_random_uuid() | — |
| unit_id | uuid | Não | — | — |
| cargo | text | Sim | — | — |
| pontos | integer | Sim | — | — |
| ativo | boolean | Sim | true | — |
| created_at | timestamp with time zone | Sim | now() | — |
| updated_at | timestamp with time zone | Sim | now() | — |

### Chave primária
- `CONSTRAINT gorjeta_cargo_pontos_pkey PRIMARY KEY (id)`

### Relacionamentos
- `gorjeta_cargo_pontos_unit_id_fkey`: `unit_id` → `public.units(id)` (ON DELETE CASCADE)

### Constraints
- `CONSTRAINT gorjeta_cargo_pontos_pontos_check CHECK ((pontos >= 0))`
- `CONSTRAINT gorjeta_cargo_pontos_unit_id_cargo_key UNIQUE (unit_id, cargo)`

### Índices

Nenhum índice adicional identificado.

### Triggers
- `trg_gorjeta_cargo_pontos_updated_at`: `BEFORE UPDATE FOR EACH ROW EXECUTE FUNCTION public.fn_set_updated_at()`

### Políticas RLS

RLS: **habilitada**.
- `insert gorjeta_cargo_pontos`: `FOR INSERT WITH CHECK (public.kph_has_role_for_unit(unit_id))`
- `select gorjeta_cargo_pontos`: `FOR SELECT USING (((unit_id IS NULL) OR public.kph_has_role_for_unit(unit_id)))`
- `update gorjeta_cargo_pontos`: `FOR UPDATE USING (public.kph_has_role_for_unit(unit_id))`

## gorjeta_dias

### Finalidade

Descrição inferida pela estrutura: armazena registros relacionados a `gorjeta dias`. A finalidade de negócio exata deve ser confirmada com a equipe responsável.

### Colunas

| Coluna | Tipo | Obrigatória | Padrão | Observação |
|---|---|---|---|---|
| id | uuid | Sim | gen_random_uuid() | — |
| unit_id | uuid | Não | — | — |
| employee_id | uuid | Não | — | — |
| periodo_id | uuid | Não | — | — |
| data | date | Sim | — | — |
| cargo | text | Sim | — | — |
| pontos | integer | Sim | 0 | — |
| presente | boolean | Sim | true | — |
| valor_calculado | numeric(10,2) | Sim | 0 | — |
| created_at | timestamp with time zone | Sim | now() | — |

### Chave primária
- `CONSTRAINT gorjeta_dias_pkey PRIMARY KEY (id)`

### Relacionamentos
- `gorjeta_dias_employee_id_fkey`: `employee_id` → `public.employees(id)` (ON DELETE CASCADE)
- `gorjeta_dias_periodo_id_fkey`: `periodo_id` → `public.gorjeta_periodos(id)` (ON DELETE CASCADE)
- `gorjeta_dias_unit_id_fkey`: `unit_id` → `public.units(id)` (ON DELETE CASCADE)

### Constraints
- `CONSTRAINT gorjeta_dias_pontos_check CHECK ((pontos >= 0))`
- `CONSTRAINT gorjeta_dias_unit_id_employee_id_data_key UNIQUE (unit_id, employee_id, data)`

### Índices
- `idx_gorjeta_dias_employee`: `USING btree (employee_id)`
- `idx_gorjeta_dias_periodo`: `USING btree (periodo_id)`
- `idx_gorjeta_dias_unit_data`: `USING btree (unit_id, data)`

### Triggers

Nenhum trigger associado.

### Políticas RLS

RLS: **habilitada**.
- `insert gorjeta_dias`: `FOR INSERT WITH CHECK (public.kph_has_role_for_unit(unit_id))`
- `select gorjeta_dias`: `FOR SELECT USING (public.kph_has_role_for_unit(unit_id))`

## gorjeta_distribuicao

### Finalidade

Descrição inferida pela estrutura: armazena registros relacionados a `gorjeta distribuicao`. A finalidade de negócio exata deve ser confirmada com a equipe responsável.

### Colunas

| Coluna | Tipo | Obrigatória | Padrão | Observação |
|---|---|---|---|---|
| id | uuid | Sim | gen_random_uuid() | — |
| unit_id | uuid | Sim | — | — |
| mes | smallint | Sim | — | — |
| ano | smallint | Sim | — | — |
| employee_id | uuid | Sim | — | — |
| nome | text | Sim | — | — |
| cargo | text | Sim | — | — |
| dias_trabalhados | integer | Sim | — | — |
| pontuacao | numeric(10,4) | Sim | — | — |
| percentual | numeric(10,8) | Sim | 0 | — |
| valor_bruto | numeric(12,2) | Sim | 0 | — |
| valor_liquido | numeric(12,2) | Sim | 0 | — |
| recibo_gerado_at | timestamp with time zone | Não | — | — |
| created_at | timestamp with time zone | Sim | now() | — |
| updated_at | timestamp with time zone | Sim | now() | — |
| recibo_url | text | Não | — | — |
| periodo | text | Não | — | — |
| colaborador_id | uuid | Não | — | — |

### Chave primária
- `CONSTRAINT gorjeta_distribuicao_pkey PRIMARY KEY (id)`

### Relacionamentos
- `gorjeta_distribuicao_colaborador_id_fkey`: `colaborador_id` → `public.employees(id)`
- `gorjeta_distribuicao_employee_id_fkey`: `employee_id` → `public.employees(id)` (ON DELETE CASCADE)
- `gorjeta_distribuicao_unit_id_fkey`: `unit_id` → `public.units(id)` (ON DELETE CASCADE)

### Constraints
- `CONSTRAINT gorjeta_distribuicao_ano_check CHECK ((ano >= 2024))`
- `CONSTRAINT gorjeta_distribuicao_mes_check CHECK (((mes >= 1) AND (mes <= 12)))`
- `CONSTRAINT gorjeta_distribuicao_periodo_emp_uq UNIQUE (unit_id, periodo, employee_id)`

### Índices
- `gorjeta_distribuicao_employee_idx`: `USING btree (employee_id)`
- `gorjeta_distribuicao_unit_period_idx`: `USING btree (unit_id, mes, ano)`
- `idx_gorjeta_periodo_emp`: `USING btree (unit_id, periodo)`
- `idx_gorjeta_recibo_pendente`: `USING btree (unit_id, mes, ano) WHERE (recibo_gerado_at IS NULL)`

### Triggers

Nenhum trigger associado.

### Políticas RLS

RLS: **habilitada**.
- `gorjeta_distribuicao_delete`: `FOR DELETE TO authenticated USING ((public.get_my_tier() = ANY (ARRAY['T3'::text, 'T4'::text])))`
- `gorjeta_distribuicao_insert`: `FOR INSERT TO authenticated WITH CHECK ((public.get_my_tier() = ANY (ARRAY['T2A'::text, 'T2B'::text, 'T3'::text, 'T4'::text])))`
- `gorjeta_distribuicao_select`: `FOR SELECT TO authenticated USING (((public.get_my_tier() = ANY (ARRAY['T3'::text, 'T4'::text])) OR ((public.get_my_tier() = ANY (ARRAY['T2A'::text, 'T2B'::text])) AND (unit_id = public.get_my_unit())) OR (employee_id IN ( SELECT employees.id FROM public.employees WHERE (employees.user_id = auth.uid())))))`
- `gorjeta_distribuicao_update`: `FOR UPDATE TO authenticated USING ((public.get_my_tier() = ANY (ARRAY['T2A'::text, 'T2B'::text, 'T3'::text, 'T4'::text])))`

## gorjeta_periodos

### Finalidade

Descrição inferida pela estrutura: armazena registros relacionados a `gorjeta periodos`. A finalidade de negócio exata deve ser confirmada com a equipe responsável.

### Colunas

| Coluna | Tipo | Obrigatória | Padrão | Observação |
|---|---|---|---|---|
| id | uuid | Sim | gen_random_uuid() | — |
| unit_id | uuid | Não | — | — |
| data | date | Sim | — | — |
| receita_bruta | numeric(12,2) | Sim | — | — |
| imposto_pct | numeric(5,2) | Sim | 20.00 | — |
| receita_liquida | numeric(12,2) | Não | GENERATED ALWAYS AS (round((receita_bruta * ((1)::numeric - (imposto_pct / 100.0))), 2)) STORED | Coluna gerada |
| total_pontos | integer | Sim | — | — |
| valor_ponto | numeric(10,4) | Não | GENERATED ALWAYS AS (round(((receita_bruta * ((1)::numeric - (imposto_pct / 100.0))) / (total_pontos)::numeric), 4)) STORED | Coluna gerada |
| fonte | text | Sim | 'manual'::text | — |
| created_at | timestamp with time zone | Sim | now() | — |
| updated_at | timestamp with time zone | Sim | now() | — |

### Chave primária
- `CONSTRAINT gorjeta_periodos_pkey PRIMARY KEY (id)`

### Relacionamentos
- `gorjeta_periodos_unit_id_fkey`: `unit_id` → `public.units(id)` (ON DELETE CASCADE)

### Constraints
- `CONSTRAINT gorjeta_periodos_fonte_check CHECK ((fonte = ANY (ARRAY['manual'::text, 'lorean'::text, 'import'::text])))`
- `CONSTRAINT gorjeta_periodos_imposto_pct_check CHECK (((imposto_pct >= (0)::numeric) AND (imposto_pct <= (100)::numeric)))`
- `CONSTRAINT gorjeta_periodos_receita_bruta_check CHECK ((receita_bruta >= (0)::numeric))`
- `CONSTRAINT gorjeta_periodos_total_pontos_check CHECK ((total_pontos > 0))`
- `CONSTRAINT gorjeta_periodos_unit_id_data_key UNIQUE (unit_id, data)`

### Índices
- `idx_gorjeta_periodos_unit_data`: `USING btree (unit_id, data)`

### Triggers
- `trg_gorjeta_periodos_updated_at`: `BEFORE UPDATE FOR EACH ROW EXECUTE FUNCTION public.fn_set_updated_at()`

### Políticas RLS

RLS: **habilitada**.
- `gorjeta_periodos_insert`: `FOR INSERT TO authenticated WITH CHECK ((public.get_my_tier() = ANY (ARRAY['T2A'::text, 'T2B'::text, 'T3'::text, 'T4'::text])))`
- `gorjeta_periodos_select`: `FOR SELECT TO authenticated USING (((public.get_my_tier() = ANY (ARRAY['T3'::text, 'T4'::text])) OR ((public.get_my_tier() = ANY (ARRAY['T2A'::text, 'T2B'::text])) AND (unit_id = public.get_my_unit()))))`
- `gorjeta_periodos_update`: `FOR UPDATE TO authenticated USING ((public.get_my_tier() = ANY (ARRAY['T2A'::text, 'T2B'::text, 'T3'::text, 'T4'::text])))`

## groups

### Finalidade

Descrição inferida pela estrutura: armazena registros relacionados a `groups`. A finalidade de negócio exata deve ser confirmada com a equipe responsável.

### Colunas

| Coluna | Tipo | Obrigatória | Padrão | Observação |
|---|---|---|---|---|
| id | uuid | Sim | gen_random_uuid() | — |
| name | text | Sim | — | — |
| slug | text | Sim | — | — |
| created_at | timestamp with time zone | Não | now() | — |
| icone | text | Não | — | — |
| parent_id | uuid | Não | — | — |

### Chave primária
- `CONSTRAINT groups_pkey PRIMARY KEY (id)`

### Relacionamentos
- `groups_parent_id_fkey`: `parent_id` → `public.groups(id)`

### Constraints
- `CONSTRAINT groups_slug_key UNIQUE (slug)`

### Índices

Nenhum índice adicional identificado.

### Triggers

Nenhum trigger associado.

### Políticas RLS

RLS: **habilitada**.
- `groups_delete`: `FOR DELETE TO authenticated USING (public.kph_is_founder())`
- `groups_insert`: `FOR INSERT TO authenticated WITH CHECK (public.kph_is_founder())`
- `groups_select`: `FOR SELECT TO authenticated USING (public.kph_has_role_for_group(id))`
- `groups_update`: `FOR UPDATE TO authenticated USING (public.kph_is_founder()) WITH CHECK (public.kph_is_founder())`

## hos_approvals

### Finalidade

Descrição inferida pela estrutura: armazena registros relacionados a `hos approvals`. A finalidade de negócio exata deve ser confirmada com a equipe responsável.

### Colunas

| Coluna | Tipo | Obrigatória | Padrão | Observação |
|---|---|---|---|---|
| id | uuid | Sim | gen_random_uuid() | — |
| run_id | uuid | Não | — | — |
| user_id | uuid | Não | — | — |
| decision | text | Sim | — | — |
| feedback | text | Não | — | — |
| created_at | timestamp with time zone | Não | now() | — |

### Chave primária
- `CONSTRAINT hos_approvals_pkey PRIMARY KEY (id)`

### Relacionamentos
- `hos_approvals_run_id_fkey`: `run_id` → `public.hos_runs(id)`
- `hos_approvals_user_id_fkey`: `user_id` → `auth.users(id)`

### Constraints
- `CONSTRAINT hos_approvals_decision_check CHECK ((decision = ANY (ARRAY['approve'::text, 'reject'::text])))`

### Índices

Nenhum índice adicional identificado.

### Triggers

Nenhum trigger associado.

### Políticas RLS

RLS: **habilitada**.
- `Founder aprova`: `USING ((EXISTS ( SELECT 1 FROM public.user_roles ur WHERE ((ur.user_id = auth.uid()) AND (ur.role_id = '0580a0a6-48c9-4170-b74d-84fd23e815fc'::uuid)))))`

## hos_insights

### Finalidade

Descrição inferida pela estrutura: armazena registros relacionados a `hos insights`. A finalidade de negócio exata deve ser confirmada com a equipe responsável.

### Colunas

| Coluna | Tipo | Obrigatória | Padrão | Observação |
|---|---|---|---|---|
| id | uuid | Sim | gen_random_uuid() | — |
| period_start | timestamp with time zone | Sim | — | — |
| period_end | timestamp with time zone | Sim | — | — |
| report_md | text | Sim | — | — |
| metrics | jsonb | Sim | '{}'::jsonb | — |
| created_at | timestamp with time zone | Sim | now() | — |

### Chave primária
- `CONSTRAINT hos_insights_pkey PRIMARY KEY (id)`

### Relacionamentos

Nenhuma chave estrangeira identificada.

### Constraints

Nenhuma constraint adicional identificada.

### Índices
- `idx_hos_insights_created_at`: `USING btree (created_at DESC)`

### Triggers

Nenhum trigger associado.

### Políticas RLS

RLS: **habilitada**.
- `Admins podem inserir insights`: `FOR INSERT TO authenticated WITH CHECK ((public.kph_has_role_for_unit(NULL::uuid) OR public.kph_is_founder()))`
- `Admins podem ver insights`: `FOR SELECT TO authenticated USING ((public.kph_has_role_for_unit(NULL::uuid) OR public.kph_is_founder()))`

## hos_jobs

### Finalidade

Descrição inferida pela estrutura: armazena registros relacionados a `hos jobs`. A finalidade de negócio exata deve ser confirmada com a equipe responsável.

### Colunas

| Coluna | Tipo | Obrigatória | Padrão | Observação |
|---|---|---|---|---|
| id | uuid | Sim | gen_random_uuid() | — |
| name | text | Sim | — | — |
| slug | text | Sim | — | — |
| description | text | Não | — | — |
| is_active | boolean | Não | true | — |
| created_at | timestamp with time zone | Não | now() | — |
| auto_approve | boolean | Sim | false | — |
| unit_id | uuid | Não | — | — |
| funcao | text | Não | — | — |
| descricao | text | Não | — | — |

### Chave primária
- `CONSTRAINT hos_jobs_pkey PRIMARY KEY (id)`

### Relacionamentos
- `hos_jobs_unit_id_fkey`: `unit_id` → `public.units(id)` (ON DELETE CASCADE)

### Constraints
- `CONSTRAINT hos_jobs_slug_key UNIQUE (slug)`

### Índices
- `idx_hos_jobs_unit`: `USING btree (unit_id)`

### Triggers

Nenhum trigger associado.

### Políticas RLS

RLS: **habilitada**.
- `Admin vê jobs`: `USING ((EXISTS ( SELECT 1 FROM public.user_roles ur WHERE ((ur.user_id = auth.uid()) AND (ur.role_id = ANY (ARRAY['0580a0a6-48c9-4170-b74d-84fd23e815fc'::uuid, '086f0247-6407-4cdf-9c12-6e12ca2dbaf7'::uuid, 'ba89b7b1-cea2-4622-b2f3-2623817d08aa'::uuid]))))))`
- `hos_jobs_read_t3`: `FOR SELECT USING ((public.get_my_tier() = ANY (ARRAY['T3'::text, 'T4'::text])))`
- `hos_jobs_write_t4`: `USING ((public.get_my_tier() = 'T4'::text))`

## hos_runs

### Finalidade

Descrição inferida pela estrutura: armazena registros relacionados a `hos runs`. A finalidade de negócio exata deve ser confirmada com a equipe responsável.

### Colunas

| Coluna | Tipo | Obrigatória | Padrão | Observação |
|---|---|---|---|---|
| id | uuid | Sim | gen_random_uuid() | — |
| job_id | uuid | Não | — | — |
| status | text | Sim | 'pending'::text | — |
| triggered_by | text | Sim | 'webhook'::text | — |
| payload | jsonb | Não | '{}'::jsonb | — |
| logs | jsonb | Não | '[]'::jsonb | — |
| created_at | timestamp with time zone | Não | now() | — |
| updated_at | timestamp with time zone | Não | now() | — |
| archived_at | timestamp with time zone | Não | — | — |
| deployment_id | text | Não | — | — |
| title | text | Não | — | — |
| employee_id | uuid | Não | — | — |
| result_data | jsonb | Não | — | — |

### Chave primária
- `CONSTRAINT hos_runs_pkey PRIMARY KEY (id)`

### Relacionamentos
- `hos_runs_employee_id_fkey`: `employee_id` → `public.employees(id)`
- `hos_runs_job_id_fkey`: `job_id` → `public.hos_jobs(id)`

### Constraints
- `CONSTRAINT hos_runs_status_check CHECK ((status = ANY (ARRAY['pending'::text, 'running'::text, 'awaiting_approval'::text, 'approved'::text, 'rejected'::text, 'failed'::text])))`
- `CONSTRAINT hos_runs_triggered_by_check CHECK ((triggered_by = ANY (ARRAY['webhook'::text, 'cron'::text, 'discord'::text, 'manual'::text])))`

### Índices
- `hos_runs_active_idx`: `USING btree (created_at DESC) WHERE (archived_at IS NULL)`
- `hos_runs_deployment_id_job_idx`: `USING btree (deployment_id, job_id) WHERE (deployment_id IS NOT NULL)`
- `hos_runs_employee_id_idx`: `USING btree (employee_id)`

### Triggers
- `runs_updated_at`: `BEFORE UPDATE FOR EACH ROW EXECUTE FUNCTION public.update_updated_at()`

### Políticas RLS

RLS: **habilitada**.
- `Admin vê runs`: `USING ((EXISTS ( SELECT 1 FROM public.user_roles ur WHERE ((ur.user_id = auth.uid()) AND (ur.role_id = ANY (ARRAY['0580a0a6-48c9-4170-b74d-84fd23e815fc'::uuid, '086f0247-6407-4cdf-9c12-6e12ca2dbaf7'::uuid, 'ba89b7b1-cea2-4622-b2f3-2623817d08aa'::uuid]))))))`
- `Admins podem atualizar execucoes`: `FOR UPDATE TO authenticated USING ((public.kph_has_role_for_unit(NULL::uuid) OR public.kph_is_founder())) WITH CHECK ((public.kph_has_role_for_unit(NULL::uuid) OR public.kph_is_founder()))`

## hour_bank

### Finalidade

Descrição inferida pela estrutura: armazena registros relacionados a `hour bank`. A finalidade de negócio exata deve ser confirmada com a equipe responsável.

### Colunas

| Coluna | Tipo | Obrigatória | Padrão | Observação |
|---|---|---|---|---|
| id | uuid | Sim | gen_random_uuid() | — |
| unit_id | uuid | Não | — | — |
| employee_id | uuid | Não | — | — |
| nome | text | Não | — | — |
| competencia | date | Não | — | — |
| horas_extras | numeric(6,2) | Não | — | — |
| horas_debito | numeric(6,2) | Não | — | — |
| saldo | numeric(6,2) | Não | — | — |
| created_at | timestamp with time zone | Não | now() | — |

### Chave primária
- `CONSTRAINT hour_bank_pkey PRIMARY KEY (id)`

### Relacionamentos
- `hour_bank_employee_id_fkey`: `employee_id` → `public.employees(id)`
- `hour_bank_unit_id_fkey`: `unit_id` → `public.units(id)`

### Constraints
- `CONSTRAINT hour_bank_employee_id_competencia_key UNIQUE (employee_id, competencia)`

### Índices

Nenhum índice adicional identificado.

### Triggers

Nenhum trigger associado.

### Políticas RLS

RLS: **habilitada**.
- `t1_own`: `FOR SELECT USING ((employee_id = ( SELECT employees.id FROM public.employees WHERE (employees.user_id = auth.uid()))))`
- `t3_dept`: `USING ((public.get_my_tier() = 'T3'::text))`
- `t4_master`: `USING ((public.get_my_tier() = 'T4'::text))`

## hr_policies

### Finalidade

Descrição inferida pela estrutura: armazena registros relacionados a `hr policies`. A finalidade de negócio exata deve ser confirmada com a equipe responsável.

### Colunas

| Coluna | Tipo | Obrigatória | Padrão | Observação |
|---|---|---|---|---|
| id | uuid | Sim | gen_random_uuid() | — |
| unit_id | uuid | Não | — | — |
| nome | text | Sim | — | — |
| tipo | text | Não | — | — |
| descricao | text | Não | — | — |
| valor | numeric(10,2) | Não | — | — |
| dia_pagamento | integer | Não | — | — |
| condicoes | text | Não | — | — |
| ativo | boolean | Não | true | — |
| created_at | timestamp with time zone | Não | now() | — |

### Chave primária
- `CONSTRAINT hr_policies_pkey PRIMARY KEY (id)`

### Relacionamentos
- `hr_policies_unit_id_fkey`: `unit_id` → `public.units(id)`

### Constraints

Nenhuma constraint adicional identificada.

### Índices

Nenhum índice adicional identificado.

### Triggers

Nenhum trigger associado.

### Políticas RLS

RLS: **habilitada**.
- `t2a_read`: `FOR SELECT USING (((public.get_my_tier() = ANY (ARRAY['T2A'::text, 'T2B'::text])) AND (unit_id = public.get_my_unit())))`
- `t3_dept`: `USING ((public.get_my_tier() = 'T3'::text))`
- `t4_master`: `USING ((public.get_my_tier() = 'T4'::text))`

## import_logs

### Finalidade

Descrição inferida pela estrutura: armazena registros relacionados a `import logs`. A finalidade de negócio exata deve ser confirmada com a equipe responsável.

### Colunas

| Coluna | Tipo | Obrigatória | Padrão | Observação |
|---|---|---|---|---|
| id | uuid | Sim | gen_random_uuid() | — |
| unit_id | uuid | Não | — | — |
| periodo | text | Sim | — | — |
| tipo | text | Não | 'ponto'::text | — |
| total_linhas | integer | Não | 0 | — |
| importados | integer | Não | 0 | — |
| nao_encontrados | integer | Não | 0 | — |
| erros | integer | Não | 0 | — |
| detalhes | jsonb | Não | — | — |
| imported_by | uuid | Não | — | — |
| imported_at | timestamp with time zone | Não | now() | — |

### Chave primária
- `CONSTRAINT import_logs_pkey PRIMARY KEY (id)`

### Relacionamentos
- `import_logs_imported_by_fkey`: `imported_by` → `auth.users(id)`
- `import_logs_unit_id_fkey`: `unit_id` → `public.units(id)`

### Constraints
- `CONSTRAINT import_logs_tipo_check CHECK ((tipo = ANY (ARRAY['ponto'::text, 'holerites'::text, 'gorjetas'::text, 'vt'::text, 'purchase_invoices'::text])))`

### Índices

Nenhum índice adicional identificado.

### Triggers

Nenhum trigger associado.

### Políticas RLS

RLS: **habilitada**.
- `import_logs_insert`: `FOR INSERT WITH CHECK (public.kph_has_role_for_unit(unit_id))`
- `import_logs_select`: `FOR SELECT USING ((public.kph_is_founder_or_cfo() OR public.kph_has_role_for_unit(unit_id)))`

## ingredient_price_history

### Finalidade

Descrição inferida pela estrutura: armazena registros relacionados a `ingredient price history`. A finalidade de negócio exata deve ser confirmada com a equipe responsável.

### Colunas

| Coluna | Tipo | Obrigatória | Padrão | Observação |
|---|---|---|---|---|
| id | uuid | Sim | gen_random_uuid() | — |
| ingredient_id | uuid | Sim | — | — |
| custo_anterior | numeric(12,4) | Não | — | — |
| custo_novo | numeric(12,4) | Sim | — | — |
| motivo | text | Não | — | — |
| changed_by | uuid | Não | — | — |
| created_at | timestamp with time zone | Não | now() | — |

### Chave primária
- `CONSTRAINT ingredient_price_history_pkey PRIMARY KEY (id)`

### Relacionamentos
- `ingredient_price_history_changed_by_fkey`: `changed_by` → `auth.users(id)` (ON DELETE SET NULL)
- `ingredient_price_history_ingredient_id_fkey`: `ingredient_id` → `public.ingredients(id)` (ON DELETE CASCADE)

### Constraints

Nenhuma constraint adicional identificada.

### Índices
- `idx_price_history_ingredient`: `USING btree (ingredient_id, created_at DESC)`

### Triggers

Nenhum trigger associado.

### Políticas RLS

RLS: **habilitada**.
- `price_history_select`: `FOR SELECT USING ((EXISTS ( SELECT 1 FROM public.ingredients i WHERE ((i.id = ingredient_price_history.ingredient_id) AND public.kph_has_role_for_group(i.group_id)))))`

## ingredient_stock

### Finalidade

Descrição inferida pela estrutura: armazena registros relacionados a `ingredient stock`. A finalidade de negócio exata deve ser confirmada com a equipe responsável.

### Colunas

| Coluna | Tipo | Obrigatória | Padrão | Observação |
|---|---|---|---|---|
| id | uuid | Sim | gen_random_uuid() | — |
| ingredient_id | uuid | Sim | — | — |
| unit_id | uuid | Sim | — | — |
| estoque_minimo | numeric | Sim | 0 | — |
| estoque_real | numeric | Sim | 0 | — |
| updated_at | timestamp with time zone | Sim | now() | — |

### Chave primária
- `CONSTRAINT ingredient_stock_pkey PRIMARY KEY (id)`

### Relacionamentos
- `ingredient_stock_ingredient_id_fkey`: `ingredient_id` → `public.ingredients(id)` (ON DELETE CASCADE)

### Constraints
- `CONSTRAINT ingredient_stock_ingredient_id_unit_id_key UNIQUE (ingredient_id, unit_id)`

### Índices
- `idx_ingredient_stock_unit`: `USING btree (unit_id, ingredient_id)`

### Triggers

Nenhum trigger associado.

### Políticas RLS

RLS: **habilitada**.

Nenhuma política associada.

## ingredients

### Finalidade

Descrição inferida pela estrutura: armazena registros relacionados a `ingredients`. A finalidade de negócio exata deve ser confirmada com a equipe responsável.

### Colunas

| Coluna | Tipo | Obrigatória | Padrão | Observação |
|---|---|---|---|---|
| id | uuid | Sim | gen_random_uuid() | — |
| group_id | uuid | Sim | — | — |
| codigo | text | Não | — | — |
| nome | text | Sim | — | — |
| categoria | text | Sim | — | — |
| unidade_padrao | text | Sim | — | — |
| custo_padrao | numeric(12,4) | Sim | 0 | — |
| fornecedor_id | uuid | Não | — | — |
| perdas_padrao | numeric(5,2) | Não | 0 | — |
| observacoes | text | Não | — | — |
| ativo | boolean | Não | true | — |
| created_at | timestamp with time zone | Não | now() | — |
| updated_at | timestamp with time zone | Não | now() | — |
| categoria_anvisa | text | Não | — | — |
| menu_item_id | uuid | Não | — | — |

### Chave primária
- `CONSTRAINT ingredients_pkey PRIMARY KEY (id)`

### Relacionamentos
- `ingredients_fornecedor_id_fkey`: `fornecedor_id` → `public.suppliers(id)` (ON DELETE SET NULL)
- `ingredients_group_id_fkey`: `group_id` → `public.groups(id)` (ON DELETE CASCADE)
- `ingredients_menu_item_id_fkey`: `menu_item_id` → `public.menu_items(id)` (ON DELETE SET NULL)

### Constraints
- `CONSTRAINT ingredients_categoria_check CHECK ((categoria = ANY (ARRAY['proteina'::text, 'verdura'::text, 'legume'::text, 'fruta'::text, 'graos'::text, 'laticinios'::text, 'panificacao'::text, 'bebida_alcoolica'::text, 'bebida_nao_alcoolica'::text, 'tempero'::text, 'oleo_gordura'::text, 'descartavel'::text, 'limpeza'::text, 'outro'::text])))`
- `CONSTRAINT ingredients_unidade_padrao_check CHECK ((unidade_padrao = ANY (ARRAY['kg'::text, 'g'::text, 'l'::text, 'ml'::text, 'un'::text, 'cx'::text, 'fardo'::text, 'duzia'::text])))`

### Índices
- `idx_ingredients_ativo`: `USING btree (ativo) WHERE (ativo = true)`
- `idx_ingredients_categoria`: `USING btree (categoria)`
- `idx_ingredients_codigo_group`: `USING btree (group_id, codigo) WHERE (codigo IS NOT NULL)`
- `idx_ingredients_group`: `USING btree (group_id)`
- `ingredients_group_codigo_uniq`: `USING btree (group_id, codigo) WHERE (codigo IS NOT NULL)`

### Triggers
- `trg_ingredient_price_change`: `AFTER UPDATE FOR EACH ROW EXECUTE FUNCTION public.fn_ingredient_price_change()`

### Políticas RLS

RLS: **habilitada**.
- `ingredients_delete`: `FOR DELETE USING (public.kph_is_founder())`
- `ingredients_insert`: `FOR INSERT WITH CHECK (public.kph_has_role_for_group(group_id))`
- `ingredients_select`: `FOR SELECT USING (public.kph_has_role_for_group(group_id))`
- `ingredients_update`: `FOR UPDATE USING (public.kph_has_role_for_group(group_id)) WITH CHECK (public.kph_has_role_for_group(group_id))`

## interview_questions

### Finalidade

Descrição inferida pela estrutura: armazena registros relacionados a `interview questions`. A finalidade de negócio exata deve ser confirmada com a equipe responsável.

### Colunas

| Coluna | Tipo | Obrigatória | Padrão | Observação |
|---|---|---|---|---|
| id | uuid | Sim | gen_random_uuid() | — |
| job_opening_id | uuid | Sim | — | — |
| order_num | integer | Sim | — | — |
| question_text | text | Não | — | — |
| video_url | text | Não | — | — |
| created_at | timestamp with time zone | Não | now() | — |

### Chave primária
- `CONSTRAINT interview_questions_pkey PRIMARY KEY (id)`

### Relacionamentos
- `interview_questions_job_opening_id_fkey`: `job_opening_id` → `public.job_openings(id)` (ON DELETE CASCADE)

### Constraints
- `CONSTRAINT interview_questions_job_opening_id_order_num_key UNIQUE (job_opening_id, order_num)`

### Índices
- `idx_questions_job_order`: `USING btree (job_opening_id, order_num)`

### Triggers

Nenhum trigger associado.

### Políticas RLS

RLS: **habilitada**.
- `questions_delete`: `FOR DELETE USING (public.kph_is_founder())`
- `questions_insert`: `FOR INSERT WITH CHECK ((EXISTS ( SELECT 1 FROM public.job_openings j WHERE ((j.id = interview_questions.job_opening_id) AND (((j.brand_id IS NOT NULL) AND public.kph_has_role_for_brand(j.brand_id)) OR ((j.unit_id IS NOT NULL) AND public.kph_has_role_for_unit(j.unit_id)))))))`
- `questions_select`: `FOR SELECT USING (true)`
- `questions_update`: `FOR UPDATE USING ((EXISTS ( SELECT 1 FROM public.job_openings j WHERE ((j.id = interview_questions.job_opening_id) AND (((j.brand_id IS NOT NULL) AND public.kph_has_role_for_brand(j.brand_id)) OR ((j.unit_id IS NOT NULL) AND public.kph_has_role_for_unit(j.unit_id)))))))`

## interview_responses

### Finalidade

Descrição inferida pela estrutura: armazena registros relacionados a `interview responses`. A finalidade de negócio exata deve ser confirmada com a equipe responsável.

### Colunas

| Coluna | Tipo | Obrigatória | Padrão | Observação |
|---|---|---|---|---|
| id | uuid | Sim | gen_random_uuid() | — |
| candidate_id | uuid | Sim | — | — |
| question_id | uuid | Sim | — | — |
| video_url | text | Não | — | — |
| created_at | timestamp with time zone | Não | now() | — |

### Chave primária
- `CONSTRAINT interview_responses_pkey PRIMARY KEY (id)`

### Relacionamentos
- `interview_responses_candidate_id_fkey`: `candidate_id` → `public.candidates(id)` (ON DELETE CASCADE)
- `interview_responses_question_id_fkey`: `question_id` → `public.interview_questions(id)`

### Constraints
- `CONSTRAINT interview_responses_candidate_id_question_id_key UNIQUE (candidate_id, question_id)`

### Índices
- `idx_responses_candidate`: `USING btree (candidate_id)`

### Triggers

Nenhum trigger associado.

### Políticas RLS

RLS: **habilitada**.
- `responses_delete`: `FOR DELETE USING (public.kph_is_founder())`
- `responses_insert`: `FOR INSERT WITH CHECK (true)`
- `responses_select`: `FOR SELECT USING (true)`
- `responses_update`: `FOR UPDATE USING (true)`

## interviews

### Finalidade

Descrição inferida pela estrutura: armazena registros relacionados a `interviews`. A finalidade de negócio exata deve ser confirmada com a equipe responsável.

### Colunas

| Coluna | Tipo | Obrigatória | Padrão | Observação |
|---|---|---|---|---|
| id | uuid | Sim | gen_random_uuid() | — |
| candidate_id | uuid | Sim | — | — |
| job_opening_id | uuid | Não | — | — |
| entrevistador_id | uuid | Não | — | — |
| data_entrevista | timestamp with time zone | Sim | — | — |
| formato | text | Sim | 'presencial'::text | — |
| status | text | Sim | 'agendada'::text | — |
| feedback | text | Não | — | — |
| nota | numeric(3,1) | Não | — | — |
| created_at | timestamp with time zone | Sim | now() | — |

### Chave primária
- `CONSTRAINT interviews_pkey PRIMARY KEY (id)`

### Relacionamentos
- `interviews_candidate_id_fkey`: `candidate_id` → `public.candidates(id)` (ON DELETE CASCADE)
- `interviews_entrevistador_id_fkey`: `entrevistador_id` → `public.employees(id)` (ON DELETE SET NULL)
- `interviews_job_opening_id_fkey`: `job_opening_id` → `public.job_openings(id)` (ON DELETE SET NULL)

### Constraints
- `CONSTRAINT interviews_formato_check CHECK ((formato = ANY (ARRAY['presencial'::text, 'video'::text, 'telefone'::text])))`
- `CONSTRAINT interviews_nota_check CHECK (((nota >= (0)::numeric) AND (nota <= (10)::numeric)))`
- `CONSTRAINT interviews_status_check CHECK ((status = ANY (ARRAY['agendada'::text, 'realizada'::text, 'cancelada'::text, 'no_show'::text])))`

### Índices
- `idx_interviews_candidate`: `USING btree (candidate_id)`
- `idx_interviews_data`: `USING btree (data_entrevista DESC)`

### Triggers

Nenhum trigger associado.

### Políticas RLS

RLS: **habilitada**.
- `interviews_read`: `FOR SELECT USING ((public.get_my_tier() = ANY (ARRAY['T3'::text, 'T4'::text])))`
- `interviews_write`: `USING ((public.get_my_tier() = ANY (ARRAY['T3'::text, 'T4'::text])))`

## job_descriptions

### Finalidade

Descrição inferida pela estrutura: armazena registros relacionados a `job descriptions`. A finalidade de negócio exata deve ser confirmada com a equipe responsável.

### Colunas

| Coluna | Tipo | Obrigatória | Padrão | Observação |
|---|---|---|---|---|
| id | uuid | Sim | gen_random_uuid() | — |
| cargo | text | Sim | — | — |
| area | text | Sim | — | — |
| responsabilidades | text | Não | — | — |
| requisitos | text | Não | — | — |
| beneficios | text | Não | — | — |
| brand_id | uuid | Não | — | — |
| created_by | uuid | Não | — | — |
| created_at | timestamp with time zone | Sim | now() | — |
| updated_at | timestamp with time zone | Sim | now() | — |
| status | text | Sim | 'draft'::text | — |
| tipo_contrato | text | Sim | 'clt'::text | — |
| modalidade | text | Sim | 'presencial'::text | — |
| reporte_direto | text | Não | — | — |
| objetivo_cargo | text | Não | — | — |
| resp_gestao_operacional | text | Não | — | — |
| resp_gestao_pessoas | text | Não | — | — |
| resp_estoque_custos | text | Não | — | — |
| resp_qualidade_experiencia | text | Não | — | — |
| indicadores_performance | text | Não | — | — |
| req_formacao | text | Não | — | — |
| req_experiencia | text | Não | — | — |
| req_conhecimentos_tecnicos | text | Não | — | — |
| req_competencias_comportamentais | text | Não | — | — |
| responsabilidades_sobre_pessoas | text | Não | — | — |
| condicoes_trabalho | text | Não | — | — |
| indicadores_sucesso | text | Não | — | — |
| cargo_id | uuid | Não | — | — |

### Chave primária
- `CONSTRAINT job_descriptions_pkey PRIMARY KEY (id)`

### Relacionamentos
- `job_descriptions_brand_id_fkey`: `brand_id` → `public.brands(id)` (ON DELETE SET NULL)
- `job_descriptions_cargo_id_fkey`: `cargo_id` → `public.cargos(id)`
- `job_descriptions_created_by_fkey`: `created_by` → `auth.users(id)` (ON DELETE SET NULL)

### Constraints
- `CONSTRAINT job_descriptions_modalidade_check CHECK ((modalidade = ANY (ARRAY['presencial'::text, 'hibrido'::text, 'remoto'::text])))`
- `CONSTRAINT job_descriptions_status_check CHECK ((status = ANY (ARRAY['draft'::text, 'published'::text, 'archived'::text])))`
- `CONSTRAINT job_descriptions_tipo_contrato_check CHECK ((tipo_contrato = ANY (ARRAY['clt'::text, 'pj'::text, 'estagio'::text, 'temporario'::text, 'intermitente'::text])))`

### Índices
- `idx_job_descriptions_brand_status`: `USING btree (brand_id, status, created_at DESC)`
- `job_descriptions_brand_id_idx`: `USING btree (brand_id)`
- `job_descriptions_cargo_idx`: `USING btree (cargo)`

### Triggers

Nenhum trigger associado.

### Políticas RLS

RLS: **habilitada**.
- `job_descriptions_delete`: `FOR DELETE TO authenticated USING ((public.get_my_tier() = ANY (ARRAY['T3'::text, 'T4'::text])))`
- `job_descriptions_insert`: `FOR INSERT TO authenticated WITH CHECK ((public.get_my_tier() = ANY (ARRAY['T3'::text, 'T4'::text])))`
- `job_descriptions_select`: `FOR SELECT TO authenticated USING ((public.get_my_tier() = ANY (ARRAY['T2A'::text, 'T2B'::text, 'T3'::text, 'T4'::text])))`
- `job_descriptions_update`: `FOR UPDATE TO authenticated USING ((public.get_my_tier() = ANY (ARRAY['T2A'::text, 'T2B'::text, 'T3'::text, 'T4'::text])))`

## job_opening_logs

### Finalidade

Descrição inferida pela estrutura: armazena registros relacionados a `job opening logs`. A finalidade de negócio exata deve ser confirmada com a equipe responsável.

### Colunas

| Coluna | Tipo | Obrigatória | Padrão | Observação |
|---|---|---|---|---|
| id | uuid | Sim | gen_random_uuid() | — |
| opening_id | uuid | Não | — | — |
| texto | text | Sim | — | — |
| autor | text | Não | — | — |
| created_at | timestamp with time zone | Sim | now() | — |

### Chave primária
- `CONSTRAINT job_opening_logs_pkey PRIMARY KEY (id)`

### Relacionamentos
- `job_opening_logs_opening_id_fkey`: `opening_id` → `public.job_openings(id)` (ON DELETE CASCADE)

### Constraints

Nenhuma constraint adicional identificada.

### Índices
- `idx_job_opening_logs_opening`: `USING btree (opening_id)`

### Triggers

Nenhum trigger associado.

### Políticas RLS

RLS: **habilitada**.
- `insert job_opening_logs`: `FOR INSERT WITH CHECK ((EXISTS ( SELECT 1 FROM public.job_openings jo WHERE ((jo.id = job_opening_logs.opening_id) AND public.kph_has_role_for_unit(jo.unit_id)))))`
- `select job_opening_logs`: `FOR SELECT USING ((EXISTS ( SELECT 1 FROM public.job_openings jo WHERE ((jo.id = job_opening_logs.opening_id) AND public.kph_has_role_for_unit(jo.unit_id)))))`

## job_openings

### Finalidade

Descrição inferida pela estrutura: armazena registros relacionados a `job openings`. A finalidade de negócio exata deve ser confirmada com a equipe responsável.

### Colunas

| Coluna | Tipo | Obrigatória | Padrão | Observação |
|---|---|---|---|---|
| id | uuid | Sim | gen_random_uuid() | — |
| brand_id | uuid | Não | — | — |
| unit_id | uuid | Não | — | — |
| title | text | Sim | — | — |
| description | text | Não | — | — |
| is_active | boolean | Não | true | — |
| created_by | uuid | Não | — | — |
| created_at | timestamp with time zone | Não | now() | — |
| status | text | Sim | 'aberta'::text | — |
| recrutador | text | Não | — | — |
| sla_dias | integer | Não | 30 | — |
| status_prazo | text | Não | — | — |
| motivo | text | Não | — | — |
| horario | text | Não | — | — |
| salario | numeric(10,2) | Não | — | — |
| fonte_recrutamento | text | Não | — | — |
| data_admissao | date | Não | — | — |
| candidato_aprovado | text | Não | — | — |
| fechamento_previsto | date | Não | — | — |
| observacoes | text | Não | — | — |
| area | text | Não | — | — |
| cargo | text | Não | — | — |
| data_solicitacao | date | Não | — | — |
| observacao | text | Não | — | — |
| responsavel_id | uuid | Não | — | — |
| entrevistador_id | uuid | Não | — | — |
| prioridade | text | Não | 'media'::text | — |
| salario_min | numeric(10,2) | Não | — | — |
| salario_max | numeric(10,2) | Não | — | — |
| must_have | text | Não | — | — |
| nice_to_have | text | Não | — | — |
| cargo_grupo_id | uuid | Não | — | — |
| motivo_estruturado | text | Não | — | — |
| horario_escala | text | Não | — | — |
| forma_contratacao | text | Não | — | — |
| substituido_id | uuid | Não | — | — |
| periodo_exp_dias | integer | Não | 90 | — |
| congelada | boolean | Sim | false | — |
| cancelada | boolean | Sim | false | — |
| motivo_congelamento | text | Não | — | — |
| congelada_em | timestamp with time zone | Não | — | — |
| cancelada_em | timestamp with time zone | Não | — | — |

### Chave primária
- `CONSTRAINT job_openings_pkey PRIMARY KEY (id)`

### Relacionamentos
- `job_openings_brand_id_fkey`: `brand_id` → `public.brands(id)`
- `job_openings_cargo_grupo_id_fkey`: `cargo_grupo_id` → `public.cargo_grupos(id)`
- `job_openings_created_by_fkey`: `created_by` → `auth.users(id)`
- `job_openings_entrevistador_id_fkey`: `entrevistador_id` → `public.employees(id)`
- `job_openings_responsavel_id_fkey`: `responsavel_id` → `public.employees(id)`
- `job_openings_substituido_id_fkey`: `substituido_id` → `public.employees(id)`
- `job_openings_unit_id_fkey`: `unit_id` → `public.units(id)`

### Constraints
- `CONSTRAINT job_openings_forma_contratacao_check CHECK (((forma_contratacao IS NULL) OR (forma_contratacao = ANY (ARRAY['CLT'::text, 'PJ'::text, 'freelance'::text, 'temporario'::text, 'estagio'::text]))))`
- `CONSTRAINT job_openings_motivo_estruturado_check CHECK (((motivo_estruturado IS NULL) OR (motivo_estruturado = ANY (ARRAY['abertura_casa'::text, 'aumento_quadro'::text, 'adequacao_quadro'::text, 'substituicao_desligamento'::text, 'substituicao_promocao'::text, 'substituicao_licenca'::text]))))`
- `CONSTRAINT job_openings_prioridade_check CHECK ((prioridade = ANY (ARRAY['alta'::text, 'media'::text, 'baixa'::text])))`
- `CONSTRAINT job_openings_status_prazo_check CHECK ((status_prazo = ANY (ARRAY['no_prazo'::text, 'atencao'::text, 'atrasado'::text, 'congelada'::text])))`

### Índices
- `idx_job_openings_ativas`: `USING btree (unit_id, status) WHERE ((congelada = false) AND (cancelada = false))`
- `idx_job_openings_cargo_grupo`: `USING btree (cargo_grupo_id)`

### Triggers
- `trg_job_openings_status_prazo`: `BEFORE INSERT OR UPDATE FOR EACH ROW EXECUTE FUNCTION public.fn_recalc_status_prazo()`

### Políticas RLS

RLS: **habilitada**.
- `job_openings_delete`: `FOR DELETE TO authenticated USING ((public.get_my_tier() = ANY (ARRAY['T3'::text, 'T4'::text])))`
- `job_openings_insert`: `FOR INSERT TO authenticated WITH CHECK ((public.get_my_tier() = ANY (ARRAY['T2A'::text, 'T2B'::text, 'T3'::text, 'T4'::text])))`
- `job_openings_select`: `FOR SELECT TO authenticated USING (((public.get_my_tier() = ANY (ARRAY['T3'::text, 'T4'::text])) OR ((public.get_my_tier() = ANY (ARRAY['T2A'::text, 'T2B'::text])) AND (unit_id = public.get_my_unit()))))`
- `job_openings_update`: `FOR UPDATE TO authenticated USING ((public.get_my_tier() = ANY (ARRAY['T2A'::text, 'T2B'::text, 'T3'::text, 'T4'::text])))`
- `t3_dept`: `USING ((public.get_my_tier() = 'T3'::text))`
- `t4_master`: `USING ((public.get_my_tier() = 'T4'::text))`

## job_requisitions

### Finalidade

Descrição inferida pela estrutura: armazena registros relacionados a `job requisitions`. A finalidade de negócio exata deve ser confirmada com a equipe responsável.

### Colunas

| Coluna | Tipo | Obrigatória | Padrão | Observação |
|---|---|---|---|---|
| id | uuid | Sim | gen_random_uuid() | — |
| created_at | timestamp with time zone | Sim | now() | — |
| status | text | Sim | 'pending_hr_review'::text | — |
| area | text | Não | — | — |
| cargo | text | Não | — | — |
| motivo | text | Não | — | — |
| data_limite | date | Não | — | — |
| resumo_responsabilidades | text | Não | — | — |
| desafios_reais | text | Não | — | — |
| hard_skills_obrigatorios | text | Não | — | — |
| hard_skills_desejaveis | text | Não | — | — |
| soft_skills | text | Não | — | — |
| fatores_eliminatorios | text | Não | — | — |
| cenario_pratico | text | Não | — | — |
| gabarito_rh | text | Não | — | — |
| proposta_valor | text | Não | — | — |
| justificativa_vaga | text | Não | — | — |
| nome_solicitante | text | Não | — | — |
| vale_transporte | text | Não | — | — |
| empresa | text | Não | — | — |

### Chave primária
- `CONSTRAINT job_requisitions_pkey PRIMARY KEY (id)`

### Relacionamentos

Nenhuma chave estrangeira identificada.

### Constraints

Nenhuma constraint adicional identificada.

### Índices
- `idx_job_requisitions_status`: `USING btree (status)`

### Triggers

Nenhum trigger associado.

### Políticas RLS

RLS: **habilitada**.
- `Allow anonymous inserts`: `FOR INSERT TO anon WITH CHECK (true)`
- `Allow authenticated reads`: `FOR SELECT TO authenticated USING (true)`
- `Permitir edicao`: `FOR UPDATE USING (true)`
- `Permitir exclusao`: `FOR DELETE USING (true)`
- `Permitir leitura`: `FOR SELECT USING (true)`

## kph_alerts

### Finalidade

Descrição inferida pela estrutura: armazena registros relacionados a `kph alerts`. A finalidade de negócio exata deve ser confirmada com a equipe responsável.

### Colunas

| Coluna | Tipo | Obrigatória | Padrão | Observação |
|---|---|---|---|---|
| id | uuid | Sim | gen_random_uuid() | — |
| tipo | text | Sim | — | — |
| prioridade | text | Sim | — | — |
| mensagem | text | Sim | — | — |
| entidade | text | Não | — | — |
| entidade_id | uuid | Não | — | — |
| enviado_para | text[] | Não | — | — |
| canal | text | Não | 'whatsapp'::text | — |
| enviado_em | timestamp with time zone | Não | — | — |
| lido | boolean | Não | false | — |
| resolvido | boolean | Não | false | — |
| created_at | timestamp with time zone | Sim | now() | — |

### Chave primária
- `CONSTRAINT kph_alerts_pkey PRIMARY KEY (id)`

### Relacionamentos

Nenhuma chave estrangeira identificada.

### Constraints
- `CONSTRAINT kph_alerts_prioridade_check CHECK ((prioridade = ANY (ARRAY['P0'::text, 'P1'::text, 'P2'::text, 'P3'::text])))`

### Índices
- `idx_kph_alerts_created`: `USING btree (created_at DESC)`
- `idx_kph_alerts_entidade_id`: `USING btree (entidade_id)`
- `idx_kph_alerts_prioridade`: `USING btree (prioridade)`
- `idx_kph_alerts_resolvido`: `USING btree (resolvido)`

### Triggers

Nenhum trigger associado.

### Políticas RLS

RLS: **habilitada**.
- `kph_alerts_manage`: `USING (public.kph_is_founder_or_cfo()) WITH CHECK (public.kph_is_founder_or_cfo())`
- `kph_alerts_select`: `FOR SELECT USING ((public.kph_is_founder_or_cfo() OR (entidade_id IN ( SELECT user_roles.unit_id FROM public.user_roles WHERE (user_roles.user_id = auth.uid())))))`

## kph_insights

### Finalidade

Descrição inferida pela estrutura: armazena registros relacionados a `kph insights`. A finalidade de negócio exata deve ser confirmada com a equipe responsável.

### Colunas

| Coluna | Tipo | Obrigatória | Padrão | Observação |
|---|---|---|---|---|
| id | uuid | Sim | gen_random_uuid() | — |
| modulo | text | Sim | — | — |
| semana | date | Sim | — | — |
| insight_text | text | Sim | — | — |
| dados_referencia | jsonb | Não | — | — |
| gerado_por | text | Não | 'claude-sonnet-4-6'::text | — |
| aprovado | boolean | Não | false | — |
| created_at | timestamp with time zone | Sim | now() | — |

### Chave primária
- `CONSTRAINT kph_insights_pkey PRIMARY KEY (id)`

### Relacionamentos

Nenhuma chave estrangeira identificada.

### Constraints
- `CONSTRAINT kph_insights_modulo_check CHECK ((modulo = ANY (ARRAY['wbr'::text, 'metas'::text, 'cross'::text, 'adocao'::text, 'orquestrador'::text, 'geral'::text, 'pessoas'::text, 'financeiro'::text, 'operacao'::text, 'compras'::text, 'comercial'::text, 'marca'::text])))`

### Índices
- `idx_kph_insights_aprovado`: `USING btree (aprovado)`
- `idx_kph_insights_modulo`: `USING btree (modulo)`
- `idx_kph_insights_semana`: `USING btree (semana DESC)`

### Triggers

Nenhum trigger associado.

### Políticas RLS

RLS: **habilitada**.
- `kph_insights_manage`: `USING (public.kph_is_founder_or_cfo()) WITH CHECK (public.kph_is_founder_or_cfo())`
- `kph_insights_select`: `FOR SELECT USING (public.kph_is_founder_or_cfo())`

## kph_intelligence_scores

### Finalidade

Descrição inferida pela estrutura: armazena registros relacionados a `kph intelligence scores`. A finalidade de negócio exata deve ser confirmada com a equipe responsável.

### Colunas

| Coluna | Tipo | Obrigatória | Padrão | Observação |
|---|---|---|---|---|
| id | uuid | Sim | gen_random_uuid() | — |
| semana | date | Sim | — | — |
| score | integer | Sim | — | — |
| cmv_score | integer | Não | — | — |
| ebitda_score | integer | Não | — | — |
| metas_score | integer | Não | — | — |
| adocao_score | integer | Não | — | — |
| bugs_score | integer | Não | — | — |
| breakdown | jsonb | Não | — | — |
| created_at | timestamp with time zone | Sim | now() | — |
| modulo | text | Não | — | — |
| score_oficial | integer | Não | — | — |
| cap_razao | text | Não | — | — |

### Chave primária
- `CONSTRAINT kph_intelligence_scores_pkey PRIMARY KEY (id)`

### Relacionamentos

Nenhuma chave estrangeira identificada.

### Constraints
- `CONSTRAINT kph_intelligence_scores_adocao_score_check CHECK (((adocao_score >= 0) AND (adocao_score <= 100)))`
- `CONSTRAINT kph_intelligence_scores_bugs_score_check CHECK (((bugs_score >= 0) AND (bugs_score <= 100)))`
- `CONSTRAINT kph_intelligence_scores_cmv_score_check CHECK (((cmv_score >= 0) AND (cmv_score <= 100)))`
- `CONSTRAINT kph_intelligence_scores_ebitda_score_check CHECK (((ebitda_score >= 0) AND (ebitda_score <= 100)))`
- `CONSTRAINT kph_intelligence_scores_metas_score_check CHECK (((metas_score >= 0) AND (metas_score <= 100)))`
- `CONSTRAINT kph_intelligence_scores_score_check CHECK (((score >= 0) AND (score <= 100)))`
- `CONSTRAINT kph_intelligence_scores_score_oficial_check CHECK (((score_oficial IS NULL) OR ((score_oficial >= 0) AND (score_oficial <= 100))))`
- `CONSTRAINT kph_intelligence_scores_modulo_semana_key UNIQUE (modulo, semana)`

### Índices
- `idx_intelligence_score_semana`: `USING btree (semana DESC)`
- `idx_kis_modulo`: `USING btree (modulo)`

### Triggers

Nenhum trigger associado.

### Políticas RLS

RLS: **habilitada**.
- `kph_intelligence_scores_manage`: `USING (public.kph_is_founder_or_cfo()) WITH CHECK (public.kph_is_founder_or_cfo())`
- `kph_intelligence_scores_select`: `FOR SELECT USING (public.kph_is_founder_or_cfo())`

## kph_learning_proposals

### Finalidade

Descrição inferida pela estrutura: armazena registros relacionados a `kph learning proposals`. A finalidade de negócio exata deve ser confirmada com a equipe responsável.

### Colunas

| Coluna | Tipo | Obrigatória | Padrão | Observação |
|---|---|---|---|---|
| id | uuid | Sim | gen_random_uuid() | — |
| modulo | text | Sim | — | — |
| tipo | text | Sim | — | — |
| prioridade | text | Sim | — | — |
| titulo | text | Sim | — | — |
| descricao | text | Sim | — | — |
| evidencia | text | Não | — | — |
| impacto_estimado | text | Não | — | — |
| status | text | Sim | 'pending'::text | — |
| created_at | timestamp with time zone | Sim | now() | — |
| executed_at | timestamp with time zone | Não | — | — |
| severidade | text | Não | — | — |

### Chave primária
- `CONSTRAINT kph_learning_proposals_pkey PRIMARY KEY (id)`

### Relacionamentos

Nenhuma chave estrangeira identificada.

### Constraints
- `CONSTRAINT kph_learning_proposals_prioridade_check CHECK ((prioridade = ANY (ARRAY['alta'::text, 'media'::text, 'baixa'::text])))`
- `CONSTRAINT kph_learning_proposals_severidade_check CHECK (((severidade IS NULL) OR (severidade = ANY (ARRAY['CRITICO'::text, 'ALTO'::text, 'MEDIO'::text, 'BAIXO'::text]))))`
- `CONSTRAINT kph_learning_proposals_status_check CHECK ((status = ANY (ARRAY['pending'::text, 'approved'::text, 'dismissed'::text])))`
- `CONSTRAINT kph_learning_proposals_tipo_check CHECK ((tipo = ANY (ARRAY['faq'::text, 'prompt'::text, 'processo'::text, 'integracao'::text])))`

### Índices
- `idx_klp_modulo_sev_pending`: `USING btree (modulo, severidade) WHERE (status = 'pending'::text)`
- `idx_kph_learning_proposals_created_at`: `USING btree (created_at DESC)`
- `idx_kph_learning_proposals_modulo_status`: `USING btree (modulo, status)`

### Triggers

Nenhum trigger associado.

### Políticas RLS

RLS: **habilitada**.
- `kph_learning_proposals_select`: `FOR SELECT TO authenticated USING (true)`
- `kph_learning_proposals_update_founder`: `FOR UPDATE TO authenticated USING (public.kph_is_founder()) WITH CHECK ((status = ANY (ARRAY['approved'::text, 'dismissed'::text])))`

## learning_machine_reports

### Finalidade

Descrição inferida pela estrutura: armazena registros relacionados a `learning machine reports`. A finalidade de negócio exata deve ser confirmada com a equipe responsável.

### Colunas

| Coluna | Tipo | Obrigatória | Padrão | Observação |
|---|---|---|---|---|
| id | uuid | Sim | gen_random_uuid() | — |
| week_number | integer | Sim | — | — |
| year | integer | Sim | — | — |
| total_runs | integer | Sim | 0 | — |
| active_agents | integer | Sim | 0 | — |
| inactive_agents | integer | Sim | 0 | — |
| top_agents | jsonb | Não | — | — |
| dormant_agents | jsonb | Não | — | — |
| missing_agents | jsonb | Não | — | — |
| insights | jsonb | Não | — | — |
| raw_analysis | text | Não | — | — |
| generated_at | timestamp with time zone | Não | now() | — |

### Chave primária
- `CONSTRAINT learning_machine_reports_pkey PRIMARY KEY (id)`

### Relacionamentos

Nenhuma chave estrangeira identificada.

### Constraints
- `CONSTRAINT learning_machine_reports_week_number_year_key UNIQUE (week_number, year)`

### Índices
- `lm_reports_week_idx`: `USING btree (year DESC, week_number DESC)`

### Triggers

Nenhum trigger associado.

### Políticas RLS

RLS: **habilitada**.
- `authenticated read learning_machine_reports`: `FOR SELECT TO authenticated USING (true)`
- `authenticated update learning_machine_reports`: `FOR UPDATE TO authenticated USING (true)`
- `authenticated upsert learning_machine_reports`: `FOR INSERT TO authenticated WITH CHECK (true)`

## lorean_ambientes

### Finalidade

Descrição inferida pela estrutura: armazena registros relacionados a `lorean ambientes`. A finalidade de negócio exata deve ser confirmada com a equipe responsável.

### Colunas

| Coluna | Tipo | Obrigatória | Padrão | Observação |
|---|---|---|---|---|
| id | uuid | Sim | gen_random_uuid() | — |
| workday_id_fk | uuid | Não | — | — |
| ambiente | character varying | Sim | — | — |
| clientes | integer | Não | — | — |
| gorjeta | numeric | Não | — | — |
| produto | numeric | Não | — | — |
| consumo | numeric | Não | — | — |
| criado_em | timestamp with time zone | Não | now() | — |

### Chave primária
- `CONSTRAINT lorean_ambientes_pkey PRIMARY KEY (id)`

### Relacionamentos
- `lorean_ambientes_workday_id_fk_fkey`: `workday_id_fk` → `public.lorean_workdays(id)` (ON DELETE CASCADE)

### Constraints

Nenhuma constraint adicional identificada.

### Índices

Nenhum índice adicional identificado.

### Triggers

Nenhum trigger associado.

### Políticas RLS

RLS: **habilitada**.

Nenhuma política associada.

## lorean_caixas

### Finalidade

Descrição inferida pela estrutura: armazena registros relacionados a `lorean caixas`. A finalidade de negócio exata deve ser confirmada com a equipe responsável.

### Colunas

| Coluna | Tipo | Obrigatória | Padrão | Observação |
|---|---|---|---|---|
| id | uuid | Sim | gen_random_uuid() | — |
| workday_id_fk | uuid | Não | — | — |
| caixa_id | integer | Não | — | — |
| operador | character varying | Não | — | — |
| abertura_at | timestamp with time zone | Não | — | — |
| fechamento_at | timestamp with time zone | Não | — | — |
| total_fechado | numeric | Não | — | — |
| total_recebido | numeric | Não | — | — |
| diferenca | numeric | Não | — | — |
| criado_em | timestamp with time zone | Não | now() | — |

### Chave primária
- `CONSTRAINT lorean_caixas_pkey PRIMARY KEY (id)`

### Relacionamentos
- `lorean_caixas_workday_id_fk_fkey`: `workday_id_fk` → `public.lorean_workdays(id)` (ON DELETE CASCADE)

### Constraints

Nenhuma constraint adicional identificada.

### Índices

Nenhum índice adicional identificado.

### Triggers

Nenhum trigger associado.

### Políticas RLS

RLS: **habilitada**.

Nenhuma política associada.

## lorean_cancelamentos

### Finalidade

Descrição inferida pela estrutura: armazena registros relacionados a `lorean cancelamentos`. A finalidade de negócio exata deve ser confirmada com a equipe responsável.

### Colunas

| Coluna | Tipo | Obrigatória | Padrão | Observação |
|---|---|---|---|---|
| id | uuid | Sim | gen_random_uuid() | — |
| workday_id_fk | uuid | Não | — | — |
| motivo | character varying | Sim | — | — |
| qtd | integer | Não | — | — |
| consumo | numeric | Não | — | — |
| criado_em | timestamp with time zone | Não | now() | — |

### Chave primária
- `CONSTRAINT lorean_cancelamentos_pkey PRIMARY KEY (id)`

### Relacionamentos
- `lorean_cancelamentos_workday_id_fk_fkey`: `workday_id_fk` → `public.lorean_workdays(id)` (ON DELETE CASCADE)

### Constraints

Nenhuma constraint adicional identificada.

### Índices
- `lorean_cancelamentos_workday`: `USING btree (workday_id_fk)`

### Triggers

Nenhum trigger associado.

### Políticas RLS

RLS: **habilitada**.

Nenhuma política associada.

## lorean_cancelamentos_detalhe

### Finalidade

Descrição inferida pela estrutura: armazena registros relacionados a `lorean cancelamentos detalhe`. A finalidade de negócio exata deve ser confirmada com a equipe responsável.

### Colunas

| Coluna | Tipo | Obrigatória | Padrão | Observação |
|---|---|---|---|---|
| id | bigint | Sim | — | — |
| workday_id_fk | uuid | Sim | — | — |
| item | text | Não | — | — |
| usuario | text | Não | — | — |
| motivo | text | Não | — | — |
| qtd | numeric | Não | — | — |
| valor | numeric | Não | — | — |
| created_at | timestamp with time zone | Não | now() | — |

### Chave primária
- `CONSTRAINT lorean_cancelamentos_detalhe_pkey PRIMARY KEY (id)`

### Relacionamentos
- `lorean_cancelamentos_detalhe_workday_id_fk_fkey`: `workday_id_fk` → `public.lorean_workdays(id)` (ON DELETE CASCADE)

### Constraints

Nenhuma constraint adicional identificada.

### Índices
- `idx_cancel_det_wd`: `USING btree (workday_id_fk)`

### Triggers

Nenhum trigger associado.

### Políticas RLS

RLS: **habilitada**.

Nenhuma política associada.

## lorean_descontos

### Finalidade

Descrição inferida pela estrutura: armazena registros relacionados a `lorean descontos`. A finalidade de negócio exata deve ser confirmada com a equipe responsável.

### Colunas

| Coluna | Tipo | Obrigatória | Padrão | Observação |
|---|---|---|---|---|
| id | uuid | Sim | gen_random_uuid() | — |
| workday_id_fk | uuid | Não | — | — |
| motivo | character varying | Sim | — | — |
| qtd | integer | Não | — | — |
| consumo | numeric | Não | — | — |
| criado_em | timestamp with time zone | Não | now() | — |

### Chave primária
- `CONSTRAINT lorean_descontos_pkey PRIMARY KEY (id)`

### Relacionamentos
- `lorean_descontos_workday_id_fk_fkey`: `workday_id_fk` → `public.lorean_workdays(id)` (ON DELETE CASCADE)

### Constraints

Nenhuma constraint adicional identificada.

### Índices

Nenhum índice adicional identificado.

### Triggers

Nenhum trigger associado.

### Políticas RLS

RLS: **habilitada**.

Nenhuma política associada.

## lorean_descontos_detalhe

### Finalidade

Descrição inferida pela estrutura: armazena registros relacionados a `lorean descontos detalhe`. A finalidade de negócio exata deve ser confirmada com a equipe responsável.

### Colunas

| Coluna | Tipo | Obrigatória | Padrão | Observação |
|---|---|---|---|---|
| id | bigint | Sim | — | — |
| workday_id_fk | uuid | Sim | — | — |
| item | text | Não | — | — |
| usuario | text | Não | — | — |
| motivo | text | Não | — | — |
| qtd | numeric | Não | — | — |
| valor | numeric | Não | — | — |
| created_at | timestamp with time zone | Não | now() | — |

### Chave primária
- `CONSTRAINT lorean_descontos_detalhe_pkey PRIMARY KEY (id)`

### Relacionamentos
- `lorean_descontos_detalhe_workday_id_fk_fkey`: `workday_id_fk` → `public.lorean_workdays(id)` (ON DELETE CASCADE)

### Constraints

Nenhuma constraint adicional identificada.

### Índices
- `idx_descontos_det_wd`: `USING btree (workday_id_fk)`

### Triggers

Nenhum trigger associado.

### Políticas RLS

RLS: **habilitada**.

Nenhuma política associada.

## lorean_grupos

### Finalidade

Descrição inferida pela estrutura: armazena registros relacionados a `lorean grupos`. A finalidade de negócio exata deve ser confirmada com a equipe responsável.

### Colunas

| Coluna | Tipo | Obrigatória | Padrão | Observação |
|---|---|---|---|---|
| id | uuid | Sim | gen_random_uuid() | — |
| workday_id_fk | uuid | Não | — | — |
| grupo | character varying | Sim | — | — |
| pct_bruto | numeric | Não | — | — |
| bruto | numeric | Não | — | — |
| desconto | numeric | Não | — | — |
| gorjeta | numeric | Não | — | — |
| consumo | numeric | Não | — | — |
| criado_em | timestamp with time zone | Não | now() | — |

### Chave primária
- `CONSTRAINT lorean_grupos_pkey PRIMARY KEY (id)`

### Relacionamentos
- `lorean_grupos_workday_id_fk_fkey`: `workday_id_fk` → `public.lorean_workdays(id)` (ON DELETE CASCADE)

### Constraints

Nenhuma constraint adicional identificada.

### Índices

Nenhum índice adicional identificado.

### Triggers

Nenhum trigger associado.

### Políticas RLS

RLS: **habilitada**.

Nenhuma política associada.

## lorean_horarios

### Finalidade

Descrição inferida pela estrutura: armazena registros relacionados a `lorean horarios`. A finalidade de negócio exata deve ser confirmada com a equipe responsável.

### Colunas

| Coluna | Tipo | Obrigatória | Padrão | Observação |
|---|---|---|---|---|
| id | uuid | Sim | gen_random_uuid() | — |
| workday_id_fk | uuid | Não | — | — |
| hora | integer | Sim | — | — |
| clientes | integer | Não | — | — |
| gorjeta | numeric | Não | — | — |
| produto | numeric | Não | — | — |
| consumo | numeric | Não | — | — |
| criado_em | timestamp with time zone | Não | now() | — |

### Chave primária
- `CONSTRAINT lorean_horarios_pkey PRIMARY KEY (id)`

### Relacionamentos
- `lorean_horarios_workday_id_fk_fkey`: `workday_id_fk` → `public.lorean_workdays(id)` (ON DELETE CASCADE)

### Constraints

Nenhuma constraint adicional identificada.

### Índices
- `lorean_horarios_workday`: `USING btree (workday_id_fk)`

### Triggers

Nenhum trigger associado.

### Políticas RLS

RLS: **habilitada**.

Nenhuma política associada.

## lorean_import_log

### Finalidade

Descrição inferida pela estrutura: armazena registros relacionados a `lorean import log`. A finalidade de negócio exata deve ser confirmada com a equipe responsável.

### Colunas

| Coluna | Tipo | Obrigatória | Padrão | Observação |
|---|---|---|---|---|
| id | uuid | Sim | gen_random_uuid() | — |
| email_id | character varying | Não | — | — |
| filename | character varying | Não | — | — |
| tipo | character varying | Não | — | — |
| data_referente | date | Não | — | — |
| status | character varying | Não | — | — |
| erro | text | Não | — | — |
| processado_em | timestamp with time zone | Não | now() | — |

### Chave primária
- `CONSTRAINT lorean_import_log_pkey PRIMARY KEY (id)`

### Relacionamentos

Nenhuma chave estrangeira identificada.

### Constraints

Nenhuma constraint adicional identificada.

### Índices

Nenhum índice adicional identificado.

### Triggers

Nenhum trigger associado.

### Políticas RLS

RLS: **habilitada**.

Nenhuma política associada.

## lorean_pagamentos

### Finalidade

Descrição inferida pela estrutura: armazena registros relacionados a `lorean pagamentos`. A finalidade de negócio exata deve ser confirmada com a equipe responsável.

### Colunas

| Coluna | Tipo | Obrigatória | Padrão | Observação |
|---|---|---|---|---|
| id | uuid | Sim | gen_random_uuid() | — |
| workday_id_fk | uuid | Não | — | — |
| forma | character varying | Sim | — | — |
| valor_fechado | numeric | Não | — | — |
| valor_recebido | numeric | Não | — | — |
| diferenca | numeric | Não | — | — |
| criado_em | timestamp with time zone | Não | now() | — |

### Chave primária
- `CONSTRAINT lorean_pagamentos_pkey PRIMARY KEY (id)`

### Relacionamentos
- `lorean_pagamentos_workday_id_fk_fkey`: `workday_id_fk` → `public.lorean_workdays(id)` (ON DELETE CASCADE)

### Constraints

Nenhuma constraint adicional identificada.

### Índices

Nenhum índice adicional identificado.

### Triggers

Nenhum trigger associado.

### Políticas RLS

RLS: **habilitada**.

Nenhuma política associada.

## lorean_produtos_dia

### Finalidade

Descrição inferida pela estrutura: armazena registros relacionados a `lorean produtos dia`. A finalidade de negócio exata deve ser confirmada com a equipe responsável.

### Colunas

| Coluna | Tipo | Obrigatória | Padrão | Observação |
|---|---|---|---|---|
| id | bigint | Sim | — | — |
| workday_id_fk | uuid | Sim | — | — |
| grupo | text | Não | — | — |
| produto | text | Sim | — | — |
| qtd | numeric | Não | — | — |
| cmv_pct | numeric | Não | — | — |
| bruto | numeric | Não | — | — |
| desconto | numeric | Não | — | — |
| gorjeta | numeric | Não | — | — |
| total | numeric | Não | — | — |
| created_at | timestamp with time zone | Não | now() | — |

### Chave primária
- `CONSTRAINT lorean_produtos_dia_pkey PRIMARY KEY (id)`

### Relacionamentos
- `lorean_produtos_dia_workday_id_fk_fkey`: `workday_id_fk` → `public.lorean_workdays(id)` (ON DELETE CASCADE)

### Constraints

Nenhuma constraint adicional identificada.

### Índices
- `idx_produtos_dia_wd`: `USING btree (workday_id_fk)`

### Triggers

Nenhum trigger associado.

### Políticas RLS

RLS: **habilitada**.

Nenhuma política associada.

## lorean_turnos

### Finalidade

Descrição inferida pela estrutura: armazena registros relacionados a `lorean turnos`. A finalidade de negócio exata deve ser confirmada com a equipe responsável.

### Colunas

| Coluna | Tipo | Obrigatória | Padrão | Observação |
|---|---|---|---|---|
| id | uuid | Sim | gen_random_uuid() | — |
| workday_id_fk | uuid | Não | — | — |
| turno | character varying | Sim | — | — |
| clientes | integer | Não | — | — |
| gorjeta | numeric | Não | — | — |
| produto | numeric | Não | — | — |
| consumo | numeric | Não | — | — |
| criado_em | timestamp with time zone | Não | now() | — |

### Chave primária
- `CONSTRAINT lorean_turnos_pkey PRIMARY KEY (id)`

### Relacionamentos
- `lorean_turnos_workday_id_fk_fkey`: `workday_id_fk` → `public.lorean_workdays(id)` (ON DELETE CASCADE)

### Constraints

Nenhuma constraint adicional identificada.

### Índices

Nenhum índice adicional identificado.

### Triggers

Nenhum trigger associado.

### Políticas RLS

RLS: **habilitada**.

Nenhuma política associada.

## lorean_usuarios

### Finalidade

Descrição inferida pela estrutura: armazena registros relacionados a `lorean usuarios`. A finalidade de negócio exata deve ser confirmada com a equipe responsável.

### Colunas

| Coluna | Tipo | Obrigatória | Padrão | Observação |
|---|---|---|---|---|
| id | uuid | Sim | gen_random_uuid() | — |
| workday_id_fk | uuid | Não | — | — |
| usuario | character varying | Sim | — | — |
| qtd | integer | Não | — | — |
| gorjeta | numeric | Não | — | — |
| produto | numeric | Não | — | — |
| consumo | numeric | Não | — | — |
| criado_em | timestamp with time zone | Não | now() | — |

### Chave primária
- `CONSTRAINT lorean_usuarios_pkey PRIMARY KEY (id)`

### Relacionamentos
- `lorean_usuarios_workday_id_fk_fkey`: `workday_id_fk` → `public.lorean_workdays(id)` (ON DELETE CASCADE)

### Constraints

Nenhuma constraint adicional identificada.

### Índices
- `lorean_usuarios_workday`: `USING btree (workday_id_fk)`

### Triggers

Nenhum trigger associado.

### Políticas RLS

RLS: **habilitada**.

Nenhuma política associada.

## lorean_workdays

### Finalidade

Descrição inferida pela estrutura: armazena registros relacionados a `lorean workdays`. A finalidade de negócio exata deve ser confirmada com a equipe responsável.

### Colunas

| Coluna | Tipo | Obrigatória | Padrão | Observação |
|---|---|---|---|---|
| id | uuid | Sim | gen_random_uuid() | — |
| unit_id | uuid | Não | — | — |
| data | date | Sim | — | — |
| workday_id | integer | Não | — | — |
| turno | character varying | Sim | 'dia_inteiro'::character varying | — |
| abertura_at | timestamp with time zone | Não | — | — |
| fechamento_at | timestamp with time zone | Não | — | — |
| receita_bruta | numeric | Não | — | — |
| desconto | numeric | Não | — | — |
| gorjeta | numeric | Não | — | — |
| receita_liquida | numeric | Não | — | — |
| custo | numeric | Não | — | — |
| cmv_pct | numeric | Não | — | — |
| lucro | numeric | Não | — | — |
| clientes | integer | Não | — | — |
| ticket_medio | numeric | Não | — | — |
| ticket_real | numeric | Não | — | — |
| permanencia_media | interval | Não | — | — |
| previsto | numeric | Não | — | — |
| devedor | numeric | Não | — | — |
| criado_em | timestamp with time zone | Não | now() | — |

### Chave primária
- `CONSTRAINT lorean_workdays_pkey PRIMARY KEY (id)`

### Relacionamentos
- `lorean_workdays_unit_id_fkey`: `unit_id` → `public.units(id)`

### Constraints
- `CONSTRAINT lorean_workdays_unit_id_workday_id_key UNIQUE (unit_id, workday_id)`

### Índices

Nenhum índice adicional identificado.

### Triggers

Nenhum trigger associado.

### Políticas RLS

RLS: **habilitada**.

Nenhuma política associada.

## manutencao_aprovacoes

### Finalidade

Descrição inferida pela estrutura: armazena registros relacionados a `manutencao aprovacoes`. A finalidade de negócio exata deve ser confirmada com a equipe responsável.

### Colunas

| Coluna | Tipo | Obrigatória | Padrão | Observação |
|---|---|---|---|---|
| id | uuid | Sim | gen_random_uuid() | — |
| unit_id | uuid | Sim | — | — |
| chamado_id | uuid | Não | — | — |
| operacao | text | Sim | — | — |
| categoria | text | Sim | — | — |
| local | text | Sim | — | — |
| andar | text | Não | — | — |
| prioridade | text | Sim | 'P.3'::text | — |
| servico | text | Sim | — | — |
| data_solicitacao | date | Sim | CURRENT_DATE | — |
| valor_previsto | numeric | Sim | 0 | — |
| forma_pagamento | text | Não | — | — |
| numero_parcelas | integer | Sim | 1 | — |
| valor_parcela | numeric | Não | GENERATED ALWAYS AS ( CASE WHEN (numero_parcelas > 0) THEN (valor_previsto / (numero_parcelas)::numeric) ELSE (0)::numeric END) STORED | Coluna gerada |
| aprovado | text | Sim | 'PENDENTE'::text | — |
| data_aprovacao | date | Não | — | — |
| aprovado_por | uuid | Não | — | — |
| data_execucao | date | Não | — | — |
| garantia_dias | integer | Não | — | — |
| data_vence_garantia | date | Sim | GENERATED ALWAYS AS ( CASE WHEN ((garantia_dias IS NOT NULL) AND (data_execucao IS NOT NULL)) THEN (data_execucao + garantia_dias) ELSE NULL::date END) STORED | Coluna gerada |
| numero_nota_fiscal | text | Não | — | — |
| observacoes | text | Não | — | — |
| criado_por | uuid | Não | — | — |
| created_at | timestamp with time zone | Sim | now() | — |
| updated_at | timestamp with time zone | Sim | now() | — |

### Chave primária
- `CONSTRAINT manutencao_aprovacoes_pkey PRIMARY KEY (id)`

### Relacionamentos
- `manutencao_aprovacoes_chamado_id_fkey`: `chamado_id` → `public.manutencao_chamados(id)` (ON DELETE SET NULL)

### Constraints
- `CONSTRAINT manutencao_aprovacoes_aprovado_check CHECK ((aprovado = ANY (ARRAY['SIM'::text, 'NAO'::text, 'PENDENTE'::text])))`
- `CONSTRAINT manutencao_aprovacoes_numero_parcelas_check CHECK ((numero_parcelas >= 1))`

### Índices
- `idx_mnt_aprov_chamado`: `USING btree (chamado_id)`
- `idx_mnt_aprov_status`: `USING btree (unit_id, aprovado)`
- `idx_mnt_aprov_unit`: `USING btree (unit_id, data_solicitacao DESC)`

### Triggers
- `trg_mnt_aprov_updated`: `BEFORE UPDATE FOR EACH ROW EXECUTE FUNCTION public.set_updated_at()`

### Políticas RLS

RLS: **habilitada**.

Nenhuma política associada.

## manutencao_chamados

### Finalidade

Descrição inferida pela estrutura: armazena registros relacionados a `manutencao chamados`. A finalidade de negócio exata deve ser confirmada com a equipe responsável.

### Colunas

| Coluna | Tipo | Obrigatória | Padrão | Observação |
|---|---|---|---|---|
| id | uuid | Sim | gen_random_uuid() | — |
| unit_id | uuid | Sim | — | — |
| operacao | text | Sim | — | — |
| categoria | text | Sim | — | — |
| local | text | Sim | — | — |
| andar | text | Não | — | — |
| prioridade | text | Sim | 'P.3'::text | — |
| servico | text | Sim | — | — |
| motivo | text | Não | — | — |
| data_solicitacao | date | Sim | CURRENT_DATE | — |
| data_execucao | date | Não | — | — |
| executado_por | text | Não | — | — |
| status | text | Sim | 'aberto'::text | — |
| valor_previsto | numeric | Não | — | — |
| observacoes | text | Não | — | — |
| criado_por | uuid | Não | — | — |
| created_at | timestamp with time zone | Sim | now() | — |
| updated_at | timestamp with time zone | Sim | now() | — |

### Chave primária
- `CONSTRAINT manutencao_chamados_pkey PRIMARY KEY (id)`

### Relacionamentos

Nenhuma chave estrangeira identificada.

### Constraints
- `CONSTRAINT manutencao_chamados_status_check CHECK ((status = ANY (ARRAY['aberto'::text, 'em_andamento'::text, 'em_aprovacao'::text, 'concluido'::text, 'cancelado'::text])))`

### Índices
- `idx_mnt_chamados_categoria`: `USING btree (unit_id, categoria)`
- `idx_mnt_chamados_status`: `USING btree (unit_id, status)`
- `idx_mnt_chamados_unit`: `USING btree (unit_id, data_solicitacao DESC)`

### Triggers
- `trg_mnt_chamados_updated`: `BEFORE UPDATE FOR EACH ROW EXECUTE FUNCTION public.set_updated_at()`

### Políticas RLS

RLS: **habilitada**.

Nenhuma política associada.

## manutencao_parcelas

### Finalidade

Descrição inferida pela estrutura: armazena registros relacionados a `manutencao parcelas`. A finalidade de negócio exata deve ser confirmada com a equipe responsável.

### Colunas

| Coluna | Tipo | Obrigatória | Padrão | Observação |
|---|---|---|---|---|
| id | uuid | Sim | gen_random_uuid() | — |
| aprovacao_id | uuid | Sim | — | — |
| numero | integer | Sim | — | — |
| competencia | date | Sim | — | — |
| valor | numeric | Sim | 0 | — |
| pago | boolean | Sim | false | — |
| data_pagamento | date | Não | — | — |
| comprovante_url | text | Não | — | — |
| comprovante_nome | text | Não | — | — |
| created_at | timestamp with time zone | Sim | now() | — |

### Chave primária
- `CONSTRAINT manutencao_parcelas_pkey PRIMARY KEY (id)`

### Relacionamentos
- `manutencao_parcelas_aprovacao_id_fkey`: `aprovacao_id` → `public.manutencao_aprovacoes(id)` (ON DELETE CASCADE)

### Constraints
- `CONSTRAINT manutencao_parcelas_aprovacao_id_numero_key UNIQUE (aprovacao_id, numero)`

### Índices
- `idx_mnt_parcelas_aprov`: `USING btree (aprovacao_id, numero)`
- `idx_mnt_parcelas_competencia`: `USING btree (competencia, pago)`

### Triggers

Nenhum trigger associado.

### Políticas RLS

RLS: **habilitada**.

Nenhuma política associada.

## mapa_conta_dre

### Finalidade

Descrição inferida pela estrutura: armazena registros relacionados a `mapa conta dre`. A finalidade de negócio exata deve ser confirmada com a equipe responsável.

### Colunas

| Coluna | Tipo | Obrigatória | Padrão | Observação |
|---|---|---|---|---|
| id | uuid | Sim | gen_random_uuid() | — |
| descricao_c_gerencial | text | Sim | — | — |
| linha_dre | text | Não | — | — |
| esperada_mensal | boolean | Não | false | — |
| criado_em | timestamp with time zone | Não | now() | — |
| atualizado_em | timestamp with time zone | Não | now() | — |

### Chave primária
- `CONSTRAINT mapa_conta_dre_pkey PRIMARY KEY (id)`

### Relacionamentos

Nenhuma chave estrangeira identificada.

### Constraints
- `CONSTRAINT mapa_conta_dre_descricao_c_gerencial_key UNIQUE (descricao_c_gerencial)`

### Índices

Nenhum índice adicional identificado.

### Triggers

Nenhum trigger associado.

### Políticas RLS

RLS: **habilitada**.
- `mapa_conta_dre_manage`: `TO service_role USING (true) WITH CHECK (true)`
- `mapa_conta_dre_read`: `FOR SELECT TO authenticated, anon USING (true)`

## menu_items

### Finalidade

Descrição inferida pela estrutura: armazena registros relacionados a `menu items`. A finalidade de negócio exata deve ser confirmada com a equipe responsável.

### Colunas

| Coluna | Tipo | Obrigatória | Padrão | Observação |
|---|---|---|---|---|
| id | uuid | Sim | gen_random_uuid() | — |
| brand_id | uuid | Sim | — | — |
| unit_id | uuid | Não | — | — |
| categoria | text | Sim | — | — |
| nome | text | Sim | — | — |
| descricao | text | Não | — | — |
| preco_venda | numeric(12,2) | Sim | 0 | — |
| custo_total | numeric(12,4) | Sim | 0 | — |
| tem_ficha_tecnica | boolean | Não | false | — |
| ativo | boolean | Não | true | — |
| observacoes | text | Não | — | — |
| ordem | integer | Não | 0 | — |
| created_at | timestamp with time zone | Não | now() | — |
| updated_at | timestamp with time zone | Não | now() | — |
| codigo | text | Não | — | — |
| rendimento | numeric(14,6) | Sim | 1 | — |
| is_subproduto | boolean | Sim | false | — |

### Chave primária
- `CONSTRAINT menu_items_pkey PRIMARY KEY (id)`

### Relacionamentos
- `menu_items_brand_id_fkey`: `brand_id` → `public.brands(id)` (ON DELETE CASCADE)
- `menu_items_unit_id_fkey`: `unit_id` → `public.units(id)` (ON DELETE SET NULL)

### Constraints

Nenhuma constraint adicional identificada.

### Índices
- `idx_menu_items_ativo`: `USING btree (ativo) WHERE (ativo = true)`
- `idx_menu_items_brand`: `USING btree (brand_id)`
- `idx_menu_items_categoria`: `USING btree (categoria)`
- `idx_menu_items_unit`: `USING btree (unit_id) WHERE (unit_id IS NOT NULL)`
- `menu_items_unit_codigo_uniq`: `USING btree (unit_id, codigo) WHERE (codigo IS NOT NULL)`

### Triggers

Nenhum trigger associado.

### Políticas RLS

RLS: **habilitada**.
- `menu_items_modify`: `USING (public.kph_has_role_for_brand(brand_id)) WITH CHECK (public.kph_has_role_for_brand(brand_id))`
- `menu_items_select`: `FOR SELECT USING (public.kph_has_role_for_brand(brand_id))`

## metas_dia_override

### Finalidade

Descrição inferida pela estrutura: armazena registros relacionados a `metas dia override`. A finalidade de negócio exata deve ser confirmada com a equipe responsável.

### Colunas

| Coluna | Tipo | Obrigatória | Padrão | Observação |
|---|---|---|---|---|
| id | bigint | Sim | — | — |
| unit_id | uuid | Sim | — | — |
| data | date | Sim | — | — |
| meta | numeric | Sim | — | — |
| created_at | timestamp with time zone | Não | now() | — |
| updated_at | timestamp with time zone | Não | now() | — |

### Chave primária
- `CONSTRAINT metas_dia_override_pkey PRIMARY KEY (id)`

### Relacionamentos

Nenhuma chave estrangeira identificada.

### Constraints
- `CONSTRAINT metas_dia_override_unit_id_data_key UNIQUE (unit_id, data)`

### Índices

Nenhum índice adicional identificado.

### Triggers

Nenhum trigger associado.

### Políticas RLS

RLS: **habilitada**.

Nenhuma política associada.

## metas_dia_semana

### Finalidade

Descrição inferida pela estrutura: armazena registros relacionados a `metas dia semana`. A finalidade de negócio exata deve ser confirmada com a equipe responsável.

### Colunas

| Coluna | Tipo | Obrigatória | Padrão | Observação |
|---|---|---|---|---|
| id | bigint | Sim | — | — |
| unit_id | uuid | Sim | — | — |
| dia_semana | integer | Sim | — | — |
| meta | numeric | Sim | — | — |
| created_at | timestamp with time zone | Não | now() | — |
| updated_at | timestamp with time zone | Não | now() | — |

### Chave primária
- `CONSTRAINT metas_dia_semana_pkey PRIMARY KEY (id)`

### Relacionamentos

Nenhuma chave estrangeira identificada.

### Constraints
- `CONSTRAINT metas_dia_semana_dia_semana_check CHECK (((dia_semana >= 0) AND (dia_semana <= 6)))`
- `CONSTRAINT metas_dia_semana_unit_id_dia_semana_key UNIQUE (unit_id, dia_semana)`

### Índices

Nenhum índice adicional identificado.

### Triggers

Nenhum trigger associado.

### Políticas RLS

RLS: **habilitada**.

Nenhuma política associada.

## metas_projecoes

### Finalidade

Descrição inferida pela estrutura: armazena registros relacionados a `metas projecoes`. A finalidade de negócio exata deve ser confirmada com a equipe responsável.

### Colunas

| Coluna | Tipo | Obrigatória | Padrão | Observação |
|---|---|---|---|---|
| id | integer | Sim | — | — |
| mes_ano | text | Sim | — | — |
| meta_faturamento | numeric | Não | — | — |
| metas_diarias | jsonb | Não | — | — |
| criado_em | timestamp with time zone | Não | now() | — |

### Chave primária
- `CONSTRAINT metas_projecoes_pkey PRIMARY KEY (id)`

### Relacionamentos

Nenhuma chave estrangeira identificada.

### Constraints

Nenhuma constraint adicional identificada.

### Índices

Nenhum índice adicional identificado.

### Triggers

Nenhum trigger associado.

### Políticas RLS

RLS: **não habilitada no dump**.

Nenhuma política associada.

## movimentacoes_rh

### Finalidade

Descrição inferida pela estrutura: armazena registros relacionados a `movimentacoes rh`. A finalidade de negócio exata deve ser confirmada com a equipe responsável.

### Colunas

| Coluna | Tipo | Obrigatória | Padrão | Observação |
|---|---|---|---|---|
| id | uuid | Sim | gen_random_uuid() | — |
| employee_id | uuid | Sim | — | — |
| tipo | text | Sim | — | — |
| data_movimentacao | date | Sim | — | — |
| unidade_id | uuid | Não | — | — |
| unidade_destino_id | uuid | Não | — | — |
| funcao_antes | text | Não | — | — |
| funcao_depois | text | Não | — | — |
| tier_antes | text | Não | — | — |
| tier_depois | text | Não | — | — |
| motivo | text | Não | — | — |
| registrado_por | uuid | Não | — | — |
| created_at | timestamp with time zone | Sim | now() | — |

### Chave primária
- `CONSTRAINT movimentacoes_rh_pkey PRIMARY KEY (id)`

### Relacionamentos
- `movimentacoes_rh_employee_id_fkey`: `employee_id` → `public.employees(id)` (ON DELETE CASCADE)
- `movimentacoes_rh_registrado_por_fkey`: `registrado_por` → `auth.users(id)` (ON DELETE SET NULL)
- `movimentacoes_rh_unidade_destino_id_fkey`: `unidade_destino_id` → `public.units(id)` (ON DELETE SET NULL)
- `movimentacoes_rh_unidade_id_fkey`: `unidade_id` → `public.units(id)` (ON DELETE SET NULL)

### Constraints
- `CONSTRAINT movimentacoes_rh_tipo_check CHECK ((tipo = ANY (ARRAY['admissao'::text, 'demissao'::text, 'transferencia'::text, 'promocao'::text])))`

### Índices
- `idx_movimentacoes_rh_data`: `USING btree (data_movimentacao DESC)`
- `idx_movimentacoes_rh_employee`: `USING btree (employee_id)`
- `idx_movimentacoes_rh_tipo`: `USING btree (tipo)`
- `idx_movimentacoes_rh_unidade`: `USING btree (unidade_id)`

### Triggers

Nenhum trigger associado.

### Políticas RLS

RLS: **habilitada**.
- `movimentacoes_read_t3`: `FOR SELECT USING ((public.get_my_tier() = ANY (ARRAY['T3'::text, 'T4'::text])))`
- `movimentacoes_write_t4`: `USING ((public.get_my_tier() = 'T4'::text))`

## notas_detalhadas

### Finalidade

Descrição inferida pela estrutura: armazena registros relacionados a `notas detalhadas`. A finalidade de negócio exata deve ser confirmada com a equipe responsável.

### Colunas

| Coluna | Tipo | Obrigatória | Padrão | Observação |
|---|---|---|---|---|
| id | integer | Sim | — | — |
| local | text | Não | — | — |
| topico | text | Não | — | — |
| setor | text | Não | — | — |
| data_inspecao | date | Sim | — | — |
| meta | numeric | Não | — | — |
| nota | numeric | Não | — | — |

### Chave primária
- `CONSTRAINT notas_detalhadas_pkey PRIMARY KEY (id)`

### Relacionamentos

Nenhuma chave estrangeira identificada.

### Constraints

Nenhuma constraint adicional identificada.

### Índices

Nenhum índice adicional identificado.

### Triggers

Nenhum trigger associado.

### Políticas RLS

RLS: **não habilitada no dump**.

Nenhuma política associada.

## notas_nutri

### Finalidade

Descrição inferida pela estrutura: armazena registros relacionados a `notas nutri`. A finalidade de negócio exata deve ser confirmada com a equipe responsável.

### Colunas

| Coluna | Tipo | Obrigatória | Padrão | Observação |
|---|---|---|---|---|
| id | integer | Sim | — | — |
| data_inspecao | date | Sim | — | — |
| local | text | Não | — | — |
| tipo_inspecao | text | Não | — | — |
| nota | numeric | Não | — | — |
| status | text | Não | — | — |

### Chave primária
- `CONSTRAINT notas_nutri_pkey PRIMARY KEY (id)`

### Relacionamentos

Nenhuma chave estrangeira identificada.

### Constraints

Nenhuma constraint adicional identificada.

### Índices

Nenhum índice adicional identificado.

### Triggers

Nenhum trigger associado.

### Políticas RLS

RLS: **não habilitada no dump**.

Nenhuma política associada.

## notifications

### Finalidade

Descrição inferida pela estrutura: armazena registros relacionados a `notifications`. A finalidade de negócio exata deve ser confirmada com a equipe responsável.

### Colunas

| Coluna | Tipo | Obrigatória | Padrão | Observação |
|---|---|---|---|---|
| id | uuid | Sim | gen_random_uuid() | — |
| user_id | uuid | Sim | — | — |
| tipo | text | Sim | — | — |
| titulo | text | Sim | — | — |
| mensagem | text | Não | — | — |
| link | text | Não | — | — |
| lida | boolean | Sim | false | — |
| created_at | timestamp with time zone | Sim | now() | — |

### Chave primária
- `CONSTRAINT notifications_pkey PRIMARY KEY (id)`

### Relacionamentos
- `notifications_user_id_fkey`: `user_id` → `auth.users(id)` (ON DELETE CASCADE)

### Constraints

Nenhuma constraint adicional identificada.

### Índices
- `idx_notifications_user_created`: `USING btree (user_id, created_at DESC)`
- `idx_notifications_user_lida`: `USING btree (user_id, lida, created_at DESC)`

### Triggers

Nenhum trigger associado.

### Políticas RLS

RLS: **habilitada**.
- `notif_select_own`: `FOR SELECT USING ((user_id = auth.uid()))`
- `notif_update_own`: `FOR UPDATE USING ((user_id = auth.uid())) WITH CHECK ((user_id = auth.uid()))`
- `notifications_own`: `USING ((auth.uid() = user_id))`

## occupational_health

### Finalidade

Descrição inferida pela estrutura: armazena registros relacionados a `occupational health`. A finalidade de negócio exata deve ser confirmada com a equipe responsável.

### Colunas

| Coluna | Tipo | Obrigatória | Padrão | Observação |
|---|---|---|---|---|
| id | uuid | Sim | gen_random_uuid() | — |
| unit_id | uuid | Não | — | — |
| employee_id | uuid | Não | — | — |
| nome | text | Não | — | — |
| cpf | text | Não | — | — |
| cargo | text | Não | — | — |
| tipo_exame | text | Não | — | — |
| data_exame | date | Não | — | — |
| resultado | text | Não | — | — |
| restricoes | text | Não | — | — |
| medico | text | Não | — | — |
| crm | text | Não | — | — |
| validade | date | Não | — | — |
| documento_ref | text | Não | — | — |
| created_at | timestamp with time zone | Não | now() | — |

### Chave primária
- `CONSTRAINT occupational_health_pkey PRIMARY KEY (id)`

### Relacionamentos
- `occupational_health_employee_id_fkey`: `employee_id` → `public.employees(id)`
- `occupational_health_unit_id_fkey`: `unit_id` → `public.units(id)`

### Constraints

Nenhuma constraint adicional identificada.

### Índices

Nenhum índice adicional identificado.

### Triggers

Nenhum trigger associado.

### Políticas RLS

RLS: **habilitada**.
- `t1_own`: `FOR SELECT USING ((employee_id = ( SELECT employees.id FROM public.employees WHERE (employees.user_id = auth.uid()))))`
- `t3_dept`: `USING (((public.get_my_tier() = 'T3'::text) AND (public.get_my_dept() = 'pessoas'::text)))`
- `t4_master`: `USING ((public.get_my_tier() = 'T4'::text))`

## onboarding_checklist

### Finalidade

Descrição inferida pela estrutura: armazena registros relacionados a `onboarding checklist`. A finalidade de negócio exata deve ser confirmada com a equipe responsável.

### Colunas

| Coluna | Tipo | Obrigatória | Padrão | Observação |
|---|---|---|---|---|
| id | uuid | Sim | gen_random_uuid() | — |
| run_id | uuid | Sim | — | — |
| tarefa_id | uuid | Sim | — | — |
| status | text | Sim | 'pendente'::text | — |
| concluido_em | timestamp with time zone | Não | — | — |
| concluido_por | uuid | Não | — | — |

### Chave primária
- `CONSTRAINT onboarding_checklist_pkey PRIMARY KEY (id)`

### Relacionamentos
- `onboarding_checklist_concluido_por_fkey`: `concluido_por` → `auth.users(id)`
- `onboarding_checklist_run_id_fkey`: `run_id` → `public.onboarding_runs(id)` (ON DELETE CASCADE)
- `onboarding_checklist_tarefa_id_fkey`: `tarefa_id` → `public.onboarding_tarefas(id)`

### Constraints
- `CONSTRAINT onboarding_checklist_status_check CHECK ((status = ANY (ARRAY['pendente'::text, 'concluido'::text, 'ignorado'::text])))`

### Índices
- `idx_ob_checklist_run`: `USING btree (run_id)`

### Triggers

Nenhum trigger associado.

### Políticas RLS

RLS: **habilitada**.
- `checklist_access`: `USING ((run_id IN ( SELECT onboarding_runs.id FROM public.onboarding_runs WHERE (onboarding_runs.unit_id IN ( SELECT user_roles.unit_id FROM public.user_roles WHERE (user_roles.user_id = auth.uid()))))))`
- `ob_checklist_read`: `FOR SELECT USING (((run_id IN ( SELECT r.id FROM (public.onboarding_runs r JOIN public.employees e ON ((e.id = r.employee_id))) WHERE (e.user_id = auth.uid()))) OR (public.get_my_tier() = ANY (ARRAY['T3'::text, 'T4'::text]))))`
- `ob_checklist_write`: `USING ((public.get_my_tier() = ANY (ARRAY['T3'::text, 'T4'::text])))`

## onboarding_runs

### Finalidade

Descrição inferida pela estrutura: armazena registros relacionados a `onboarding runs`. A finalidade de negócio exata deve ser confirmada com a equipe responsável.

### Colunas

| Coluna | Tipo | Obrigatória | Padrão | Observação |
|---|---|---|---|---|
| id | uuid | Sim | gen_random_uuid() | — |
| unit_id | uuid | Sim | — | — |
| employee_id | uuid | Sim | — | — |
| template_id | uuid | Sim | — | — |
| status | text | Sim | 'em_andamento'::text | — |
| data_inicio | date | Sim | CURRENT_DATE | — |
| created_at | timestamp with time zone | Não | now() | — |

### Chave primária
- `CONSTRAINT onboarding_runs_pkey PRIMARY KEY (id)`

### Relacionamentos
- `onboarding_runs_employee_id_fkey`: `employee_id` → `public.employees(id)`
- `onboarding_runs_template_id_fkey`: `template_id` → `public.onboarding_templates(id)`
- `onboarding_runs_unit_id_fkey`: `unit_id` → `public.units(id)`

### Constraints
- `CONSTRAINT onboarding_runs_status_check CHECK ((status = ANY (ARRAY['em_andamento'::text, 'concluido'::text, 'cancelado'::text])))`

### Índices
- `idx_ob_runs_employee`: `USING btree (employee_id)`
- `idx_ob_runs_unit`: `USING btree (unit_id)`

### Triggers

Nenhum trigger associado.

### Políticas RLS

RLS: **habilitada**.
- `ob_runs_read`: `FOR SELECT USING (((employee_id IN ( SELECT employees.id FROM public.employees WHERE (employees.user_id = auth.uid()))) OR (public.get_my_tier() = ANY (ARRAY['T3'::text, 'T4'::text]))))`
- `ob_runs_write`: `USING ((public.get_my_tier() = ANY (ARRAY['T3'::text, 'T4'::text])))`
- `unit_access_runs`: `USING ((unit_id IN ( SELECT user_roles.unit_id FROM public.user_roles WHERE (user_roles.user_id = auth.uid()))))`

## onboarding_tarefas

### Finalidade

Descrição inferida pela estrutura: armazena registros relacionados a `onboarding tarefas`. A finalidade de negócio exata deve ser confirmada com a equipe responsável.

### Colunas

| Coluna | Tipo | Obrigatória | Padrão | Observação |
|---|---|---|---|---|
| id | uuid | Sim | gen_random_uuid() | — |
| template_id | uuid | Sim | — | — |
| titulo | text | Sim | — | — |
| descricao | text | Não | — | — |
| responsavel | text | Sim | — | — |
| prazo_dias | integer | Sim | 1 | — |
| ordem | integer | Sim | 0 | — |

### Chave primária
- `CONSTRAINT onboarding_tarefas_pkey PRIMARY KEY (id)`

### Relacionamentos
- `onboarding_tarefas_template_id_fkey`: `template_id` → `public.onboarding_templates(id)` (ON DELETE CASCADE)

### Constraints
- `CONSTRAINT onboarding_tarefas_responsavel_check CHECK ((responsavel = ANY (ARRAY['rh'::text, 'gestor'::text, 'colaborador'::text, 'ti'::text])))`

### Índices
- `idx_ob_tarefas_template`: `USING btree (template_id, ordem)`

### Triggers

Nenhum trigger associado.

### Políticas RLS

RLS: **habilitada**.
- `ob_tarefas_read`: `FOR SELECT USING (true)`
- `ob_tarefas_write`: `USING ((public.get_my_tier() = ANY (ARRAY['T3'::text, 'T4'::text])))`

## onboarding_templates

### Finalidade

Descrição inferida pela estrutura: armazena registros relacionados a `onboarding templates`. A finalidade de negócio exata deve ser confirmada com a equipe responsável.

### Colunas

| Coluna | Tipo | Obrigatória | Padrão | Observação |
|---|---|---|---|---|
| id | uuid | Sim | gen_random_uuid() | — |
| unit_id | uuid | Sim | — | — |
| nome | text | Sim | — | — |
| descricao | text | Não | — | — |
| ativo | boolean | Não | true | — |
| created_at | timestamp with time zone | Não | now() | — |

### Chave primária
- `CONSTRAINT onboarding_templates_pkey PRIMARY KEY (id)`

### Relacionamentos
- `onboarding_templates_unit_id_fkey`: `unit_id` → `public.units(id)`

### Constraints

Nenhuma constraint adicional identificada.

### Índices
- `idx_ob_templates_unit`: `USING btree (unit_id)`

### Triggers

Nenhum trigger associado.

### Políticas RLS

RLS: **habilitada**.
- `ob_templates_read`: `FOR SELECT USING ((public.get_my_tier() = ANY (ARRAY['T3'::text, 'T4'::text])))`
- `ob_templates_write`: `USING ((public.get_my_tier() = ANY (ARRAY['T3'::text, 'T4'::text])))`
- `unit_access_templates`: `USING ((unit_id IN ( SELECT user_roles.unit_id FROM public.user_roles WHERE (user_roles.user_id = auth.uid()))))`

## origens_candidato

### Finalidade

Descrição inferida pela estrutura: armazena registros relacionados a `origens candidato`. A finalidade de negócio exata deve ser confirmada com a equipe responsável.

### Colunas

| Coluna | Tipo | Obrigatória | Padrão | Observação |
|---|---|---|---|---|
| id | uuid | Sim | gen_random_uuid() | — |
| codigo | text | Sim | — | — |
| label | text | Sim | — | — |
| automatica | boolean | Sim | false | — |
| ativo | boolean | Sim | true | — |
| ordem | integer | Sim | 99 | — |

### Chave primária
- `CONSTRAINT origens_candidato_pkey PRIMARY KEY (id)`

### Relacionamentos

Nenhuma chave estrangeira identificada.

### Constraints
- `CONSTRAINT origens_candidato_codigo_key UNIQUE (codigo)`

### Índices

Nenhum índice adicional identificado.

### Triggers

Nenhum trigger associado.

### Políticas RLS

RLS: **habilitada**.
- `origens_candidato_select`: `FOR SELECT USING (true)`

## orkestri_achados

### Finalidade

Descrição inferida pela estrutura: armazena registros relacionados a `orkestri achados`. A finalidade de negócio exata deve ser confirmada com a equipe responsável.

### Colunas

| Coluna | Tipo | Obrigatória | Padrão | Observação |
|---|---|---|---|---|
| id | uuid | Sim | gen_random_uuid() | — |
| created_at | timestamp with time zone | Sim | now() | — |
| atualizado_em | timestamp with time zone | Sim | now() | — |
| run_id | text | Não | — | — |
| auditor | text | Sim | — | — |
| zona | text | Sim | — | — |
| marca | text | Sim | — | — |
| unit_id | uuid | Sim | — | — |
| periodo | text | Sim | — | — |
| tipo_periodo | text | Sim | 'mensal'::text | — |
| indicador | text | Sim | — | — |
| tipo | text | Sim | — | — |
| severidade | text | Não | — | — |
| r_em_risco | numeric(14,2) | Não | — | — |
| desvio_pp | numeric(8,2) | Não | — | — |
| realizado | numeric(8,2) | Não | — | — |
| meta_interna | numeric(8,2) | Não | — | — |
| faixa_mercado | text | Não | — | — |
| titulo | text | Sim | — | — |
| causa_provavel | text | Não | — | — |
| status | text | Sim | 'aberto'::text | — |
| resolucao | text | Não | — | — |
| fonte_ok | boolean | Sim | true | — |
| detalhe | jsonb | Não | — | — |
| por_que_importa | text | Não | — | — |
| acao_sugerida | text | Não | — | — |
| dono_sugerido | text | Não | — | — |

### Chave primária
- `CONSTRAINT orkestri_achados_pkey PRIMARY KEY (id)`

### Relacionamentos

Nenhuma chave estrangeira identificada.

### Constraints
- `CONSTRAINT oa_faixa_chk CHECK (((faixa_mercado = ANY (ARRAY['VERDE'::text, 'AMARELO'::text, 'VERMELHO'::text])) OR (faixa_mercado IS NULL)))`
- `CONSTRAINT oa_severidade_chk CHECK (((severidade = ANY (ARRAY['critico'::text, 'alerta'::text, 'atencao'::text])) OR (severidade IS NULL)))`
- `CONSTRAINT oa_status_chk CHECK ((status = ANY (ARRAY['aberto'::text, 'em_tratamento'::text, 'resolvido'::text, 'ignorado'::text])))`
- `CONSTRAINT oa_tipo_chk CHECK ((tipo = ANY (ARRAY['alerta'::text, 'destaque'::text, 'em_aberto'::text])))`
- `CONSTRAINT oa_tipo_periodo_chk CHECK ((tipo_periodo = ANY (ARRAY['mensal'::text, 'semanal'::text, 'diario'::text, 'trimestral'::text])))`
- `CONSTRAINT oa_unico UNIQUE (auditor, unit_id, periodo, indicador, tipo)`

### Índices
- `idx_oa_auditor`: `USING btree (auditor)`
- `idx_oa_created`: `USING btree (created_at DESC)`
- `idx_oa_marca`: `USING btree (marca)`
- `idx_oa_severidade`: `USING btree (severidade)`
- `idx_oa_status`: `USING btree (status)`
- `idx_oa_unit_status`: `USING btree (unit_id, status)`

### Triggers
- `trg_oa_atualizado`: `BEFORE UPDATE FOR EACH ROW EXECUTE FUNCTION public.fn_oa_set_atualizado_em()`

### Políticas RLS

RLS: **habilitada**.
- `authenticated insert orkestri_achados`: `FOR INSERT TO authenticated WITH CHECK (true)`
- `authenticated read orkestri_achados`: `FOR SELECT TO authenticated USING (true)`
- `service upsert orkestri_achados`: `FOR UPDATE TO authenticated USING (true)`

## orkestri_leads

### Finalidade

Descrição inferida pela estrutura: armazena registros relacionados a `orkestri leads`. A finalidade de negócio exata deve ser confirmada com a equipe responsável.

### Colunas

| Coluna | Tipo | Obrigatória | Padrão | Observação |
|---|---|---|---|---|
| id | uuid | Sim | gen_random_uuid() | — |
| created_at | timestamp with time zone | Não | now() | — |
| nome | text | Sim | — | — |
| empresa | text | Sim | — | — |
| cargo | text | Sim | — | — |
| email | text | Sim | — | — |
| celular | text | Sim | — | — |
| dor | text | Não | — | — |
| problema_1 | text | Não | — | — |
| problema_2 | text | Não | — | — |
| problema_3 | text | Não | — | — |

### Chave primária
- `CONSTRAINT orkestri_leads_pkey PRIMARY KEY (id)`

### Relacionamentos

Nenhuma chave estrangeira identificada.

### Constraints

Nenhuma constraint adicional identificada.

### Índices

Nenhum índice adicional identificado.

### Triggers

Nenhum trigger associado.

### Políticas RLS

RLS: **habilitada**.
- `insert convidados`: `FOR INSERT TO anon WITH CHECK (true)`
- `insert livre para convidados`: `FOR INSERT TO anon WITH CHECK (true)`
- `leitura admin`: `FOR SELECT TO anon USING (true)`
- `leitura livre para admin`: `FOR SELECT TO anon USING (true)`

## orquestrador_jobs

### Finalidade

Descrição inferida pela estrutura: armazena registros relacionados a `orquestrador jobs`. A finalidade de negócio exata deve ser confirmada com a equipe responsável.

### Colunas

| Coluna | Tipo | Obrigatória | Padrão | Observação |
|---|---|---|---|---|
| id | uuid | Sim | gen_random_uuid() | — |
| type | text | Sim | — | — |
| status | text | Sim | 'pending'::text | — |
| payload | jsonb | Não | — | — |
| result | jsonb | Não | — | — |
| error_msg | text | Não | — | — |
| created_at | timestamp with time zone | Não | now() | — |
| updated_at | timestamp with time zone | Não | now() | — |
| executed_at | timestamp with time zone | Não | — | — |
| execution_result | jsonb | Não | — | — |

### Chave primária
- `CONSTRAINT orquestrador_jobs_pkey PRIMARY KEY (id)`

### Relacionamentos

Nenhuma chave estrangeira identificada.

### Constraints
- `CONSTRAINT orquestrador_jobs_status_check CHECK ((status = ANY (ARRAY['pending'::text, 'running'::text, 'success'::text, 'error'::text])))`

### Índices
- `orquestrador_jobs_created_at_idx`: `USING btree (created_at DESC)`
- `orquestrador_jobs_type_idx`: `USING btree (type)`

### Triggers

Nenhum trigger associado.

### Políticas RLS

RLS: **habilitada**.
- `authenticated insert orquestrador_jobs`: `FOR INSERT TO authenticated WITH CHECK (true)`
- `authenticated read orquestrador_jobs`: `FOR SELECT TO authenticated USING (true)`
- `service update orquestrador_jobs`: `FOR UPDATE TO authenticated USING (true)`

## overtime_records

### Finalidade

Descrição inferida pela estrutura: armazena registros relacionados a `overtime records`. A finalidade de negócio exata deve ser confirmada com a equipe responsável.

### Colunas

| Coluna | Tipo | Obrigatória | Padrão | Observação |
|---|---|---|---|---|
| id | uuid | Sim | gen_random_uuid() | — |
| employee_id | uuid | Sim | — | — |
| unit_id | uuid | Sim | — | — |
| date | date | Sim | — | — |
| hours | numeric(5,2) | Sim | — | — |
| type | text | Sim | — | — |
| reason | text | Não | — | — |
| approved | boolean | Não | — | — |
| approved_by | uuid | Não | — | — |
| periodo | text | Não | — | — |
| source | text | Não | 'manual'::text | — |
| created_at | timestamp with time zone | Não | now() | — |

### Chave primária
- `CONSTRAINT overtime_records_pkey PRIMARY KEY (id)`

### Relacionamentos
- `overtime_records_approved_by_fkey`: `approved_by` → `auth.users(id)`
- `overtime_records_employee_id_fkey`: `employee_id` → `public.employees(id)` (ON DELETE CASCADE)
- `overtime_records_unit_id_fkey`: `unit_id` → `public.units(id)`

### Constraints
- `CONSTRAINT overtime_records_source_check CHECK ((source = ANY (ARRAY['manual'::text, 'totvs'::text])))`
- `CONSTRAINT overtime_records_type_check CHECK ((type = ANY (ARRAY['50'::text, '100'::text, 'banco'::text])))`

### Índices
- `idx_overtime_employee_periodo`: `USING btree (employee_id, periodo)`

### Triggers

Nenhum trigger associado.

### Políticas RLS

RLS: **habilitada**.
- `overtime_delete`: `FOR DELETE USING (public.kph_is_founder())`
- `overtime_insert`: `FOR INSERT WITH CHECK (public.kph_has_role_for_unit(unit_id))`
- `overtime_select`: `FOR SELECT USING ((EXISTS ( SELECT 1 FROM public.employees e WHERE ((e.id = overtime_records.employee_id) AND public.kph_has_role_for_unit(e.unit_id)))))`
- `overtime_update`: `FOR UPDATE USING (public.kph_has_role_for_unit(unit_id))`

## page_views

### Finalidade

Descrição inferida pela estrutura: armazena registros relacionados a `page views`. A finalidade de negócio exata deve ser confirmada com a equipe responsável.

### Colunas

| Coluna | Tipo | Obrigatória | Padrão | Observação |
|---|---|---|---|---|
| id | uuid | Sim | gen_random_uuid() | — |
| user_id | uuid | Não | — | — |
| path | text | Sim | — | — |
| visited_at | timestamp with time zone | Sim | now() | — |

### Chave primária
- `CONSTRAINT page_views_pkey PRIMARY KEY (id)`

### Relacionamentos
- `page_views_user_id_fkey`: `user_id` → `auth.users(id)` (ON DELETE SET NULL)

### Constraints

Nenhuma constraint adicional identificada.

### Índices
- `idx_page_views_path`: `USING btree (path)`
- `idx_page_views_user`: `USING btree (user_id)`
- `idx_page_views_visited`: `USING btree (visited_at DESC)`

### Triggers

Nenhum trigger associado.

### Políticas RLS

RLS: **habilitada**.
- `insert_own`: `FOR INSERT TO authenticated WITH CHECK ((user_id = auth.uid()))`
- `select_own`: `FOR SELECT USING (((user_id = auth.uid()) OR public.kph_is_founder_or_cfo()))`

## payroll_dominio_cadastro

### Finalidade

Descrição inferida pela estrutura: armazena registros relacionados a `payroll dominio cadastro`. A finalidade de negócio exata deve ser confirmada com a equipe responsável.

### Colunas

| Coluna | Tipo | Obrigatória | Padrão | Observação |
|---|---|---|---|---|
| id | uuid | Sim | gen_random_uuid() | — |
| cod_empresa | text | Sim | — | — |
| cod_colaborador | integer | Sim | — | — |
| nome | text | Sim | — | — |
| nome_norm | text | Sim | — | — |
| cargo_codigo | integer | Não | — | — |
| cargo_nome | text | Não | — | — |
| data_admissao | date | Não | — | — |
| salario | numeric(12,2) | Não | — | — |
| cpf | text | Não | — | — |
| employee_id | uuid | Não | — | — |
| origem_match | text | Não | — | — |
| vigente_desde | date | Sim | '2026-07-01'::date | — |
| criado_em | timestamp with time zone | Sim | now() | — |

### Chave primária
- `CONSTRAINT payroll_dominio_cadastro_pkey PRIMARY KEY (id)`

### Relacionamentos
- `payroll_dominio_cadastro_cod_empresa_fkey`: `cod_empresa` → `public.payroll_dominio_empresa(cod_empresa)`
- `payroll_dominio_cadastro_employee_id_fkey`: `employee_id` → `public.employees(id)`

### Constraints
- `CONSTRAINT uq_dom_cadastro UNIQUE (cod_empresa, cod_colaborador)`

### Índices
- `ix_dom_cad_cpf`: `USING btree (cpf)`
- `ix_dom_cad_emp`: `USING btree (employee_id)`
- `ix_dom_cad_norm`: `USING btree (nome_norm)`

### Triggers

Nenhum trigger associado.

### Políticas RLS

RLS: **habilitada**.

Nenhuma política associada.

## payroll_dominio_cargo

### Finalidade

Descrição inferida pela estrutura: armazena registros relacionados a `payroll dominio cargo`. A finalidade de negócio exata deve ser confirmada com a equipe responsável.

### Colunas

| Coluna | Tipo | Obrigatória | Padrão | Observação |
|---|---|---|---|---|
| cargo_codigo | integer | Sim | — | — |
| cargo_nome | text | Sim | — | — |
| cbo | text | Não | — | — |
| cargo_kph_id | uuid | Não | — | — |
| observacao | text | Não | — | — |
| criado_em | timestamp with time zone | Sim | now() | — |

### Chave primária
- `CONSTRAINT payroll_dominio_cargo_pkey PRIMARY KEY (cargo_codigo)`

### Relacionamentos

Nenhuma chave estrangeira identificada.

### Constraints

Nenhuma constraint adicional identificada.

### Índices

Nenhum índice adicional identificado.

### Triggers

Nenhum trigger associado.

### Políticas RLS

RLS: **habilitada**.

Nenhuma política associada.

## payroll_dominio_empresa

### Finalidade

Descrição inferida pela estrutura: armazena registros relacionados a `payroll dominio empresa`. A finalidade de negócio exata deve ser confirmada com a equipe responsável.

### Colunas

| Coluna | Tipo | Obrigatória | Padrão | Observação |
|---|---|---|---|---|
| cod_empresa | text | Sim | — | — |
| razao_social | text | Sim | — | — |
| cnpj | text | Não | — | — |
| ativa | boolean | Sim | true | — |
| observacao | text | Não | — | — |
| criado_em | timestamp with time zone | Sim | now() | — |

### Chave primária
- `CONSTRAINT payroll_dominio_empresa_pkey PRIMARY KEY (cod_empresa)`

### Relacionamentos

Nenhuma chave estrangeira identificada.

### Constraints

Nenhuma constraint adicional identificada.

### Índices

Nenhum índice adicional identificado.

### Triggers

Nenhum trigger associado.

### Políticas RLS

RLS: **habilitada**.

Nenhuma política associada.

## payroll_extrato_dominio_colaborador

### Finalidade

Descrição inferida pela estrutura: armazena registros relacionados a `payroll extrato dominio colaborador`. A finalidade de negócio exata deve ser confirmada com a equipe responsável.

### Colunas

| Coluna | Tipo | Obrigatória | Padrão | Observação |
|---|---|---|---|---|
| id | uuid | Sim | gen_random_uuid() | — |
| competencia | text | Sim | — | — |
| cod_empresa_dominio | text | Sim | '10131'::text | — |
| cnpj | text | Sim | '46098368000135'::text | — |
| cod_colaborador | integer | Sim | — | — |
| nome | text | Sim | — | — |
| cpf | text | Sim | — | — |
| situacao | text | Não | — | — |
| data_admissao | date | Não | — | — |
| data_demissao | date | Não | — | — |
| motivo_demissao | text | Não | — | — |
| vinculo | text | Não | — | — |
| centro_custo | integer | Não | — | — |
| departamento | integer | Não | — | — |
| cargo_codigo | integer | Não | — | — |
| cargo_nome | text | Não | — | — |
| cbo | text | Não | — | — |
| salario | numeric(12,2) | Não | — | — |
| proventos | numeric(12,2) | Não | — | — |
| descontos | numeric(12,2) | Não | — | — |
| liquido | numeric(12,2) | Não | — | — |
| base_inss | numeric(12,2) | Não | — | — |
| base_fgts | numeric(12,2) | Não | — | — |
| valor_fgts | numeric(12,2) | Não | — | — |
| base_irrf | numeric(12,2) | Não | — | — |
| employee_id | uuid | Não | — | — |
| unit_id | uuid | Não | — | — |
| criado_em | timestamp with time zone | Sim | now() | — |

### Chave primária
- `CONSTRAINT payroll_extrato_dominio_colaborador_pkey PRIMARY KEY (id)`

### Relacionamentos
- `payroll_extrato_dominio_colaborador_employee_id_fkey`: `employee_id` → `public.employees(id)`

### Constraints
- `CONSTRAINT uq_extrato_colab UNIQUE (competencia, cod_colaborador)`

### Índices
- `ix_extrato_colab_comp`: `USING btree (competencia)`
- `ix_extrato_colab_cpf`: `USING btree (cpf)`
- `ix_extrato_colab_emp`: `USING btree (employee_id)`

### Triggers

Nenhum trigger associado.

### Políticas RLS

RLS: **habilitada**.

Nenhuma política associada.

## payroll_extrato_dominio_linha

### Finalidade

Descrição inferida pela estrutura: armazena registros relacionados a `payroll extrato dominio linha`. A finalidade de negócio exata deve ser confirmada com a equipe responsável.

### Colunas

| Coluna | Tipo | Obrigatória | Padrão | Observação |
|---|---|---|---|---|
| id | uuid | Sim | gen_random_uuid() | — |
| competencia | text | Sim | — | — |
| cod_colaborador | integer | Sim | — | — |
| rubrica_codigo | integer | Sim | — | — |
| valor | numeric(14,2) | Sim | — | — |
| employee_id | uuid | Não | — | — |
| criado_em | timestamp with time zone | Sim | now() | — |

### Chave primária
- `CONSTRAINT payroll_extrato_dominio_linha_pkey PRIMARY KEY (id)`

### Relacionamentos
- `payroll_extrato_dominio_linha_employee_id_fkey`: `employee_id` → `public.employees(id)`

### Constraints
- `CONSTRAINT uq_extrato_linha UNIQUE (competencia, cod_colaborador, rubrica_codigo)`

### Índices
- `ix_extrato_linha_comp`: `USING btree (competencia, rubrica_codigo)`
- `ix_extrato_linha_emp`: `USING btree (employee_id)`

### Triggers

Nenhum trigger associado.

### Políticas RLS

RLS: **habilitada**.

Nenhuma política associada.

## payroll_extrato_dominio_rubrica

### Finalidade

Descrição inferida pela estrutura: armazena registros relacionados a `payroll extrato dominio rubrica`. A finalidade de negócio exata deve ser confirmada com a equipe responsável.

### Colunas

| Coluna | Tipo | Obrigatória | Padrão | Observação |
|---|---|---|---|---|
| id | uuid | Sim | gen_random_uuid() | — |
| competencia | text | Sim | — | — |
| cod_empresa_dominio | text | Sim | '10131'::text | — |
| rubrica_codigo | integer | Sim | — | — |
| rubrica_descricao | text | Sim | — | — |
| natureza | text | Sim | — | — |
| quantidade_texto | text | Não | — | — |
| valor | numeric(14,2) | Sim | — | — |
| criado_em | timestamp with time zone | Sim | now() | — |

### Chave primária
- `CONSTRAINT payroll_extrato_dominio_rubrica_pkey PRIMARY KEY (id)`

### Relacionamentos

Nenhuma chave estrangeira identificada.

### Constraints
- `CONSTRAINT payroll_extrato_dominio_rubrica_natureza_check CHECK ((natureza = ANY (ARRAY['PROVENTO'::text, 'DESCONTO'::text])))`
- `CONSTRAINT uq_extrato_rubrica UNIQUE (competencia, rubrica_codigo, natureza)`

### Índices

Nenhum índice adicional identificado.

### Triggers

Nenhum trigger associado.

### Políticas RLS

RLS: **habilitada**.

Nenhuma política associada.

## payroll_extrato_dominio_totais

### Finalidade

Descrição inferida pela estrutura: armazena registros relacionados a `payroll extrato dominio totais`. A finalidade de negócio exata deve ser confirmada com a equipe responsável.

### Colunas

| Coluna | Tipo | Obrigatória | Padrão | Observação |
|---|---|---|---|---|
| id | uuid | Sim | gen_random_uuid() | — |
| competencia | text | Sim | — | — |
| dimensao | text | Sim | — | — |
| codigo | integer | Não | — | — |
| nome | text | Não | — | — |
| proventos | numeric(14,2) | Sim | — | — |
| descontos | numeric(14,2) | Sim | — | — |
| liquido | numeric(14,2) | Sim | — | — |

### Chave primária
- `CONSTRAINT payroll_extrato_dominio_totais_pkey PRIMARY KEY (id)`

### Relacionamentos

Nenhuma chave estrangeira identificada.

### Constraints
- `CONSTRAINT payroll_extrato_dominio_totais_dimensao_check CHECK ((dimensao = ANY (ARRAY['DEPARTAMENTO'::text, 'CENTRO_CUSTO'::text, 'GERAL'::text])))`
- `CONSTRAINT uq_extrato_totais UNIQUE (competencia, dimensao, codigo)`

### Índices

Nenhum índice adicional identificado.

### Triggers

Nenhum trigger associado.

### Políticas RLS

RLS: **habilitada**.

Nenhuma política associada.

## payroll_fechamento_linha

### Finalidade

Descrição inferida pela estrutura: armazena registros relacionados a `payroll fechamento linha`. A finalidade de negócio exata deve ser confirmada com a equipe responsável.

### Colunas

| Coluna | Tipo | Obrigatória | Padrão | Observação |
|---|---|---|---|---|
| id | uuid | Sim | gen_random_uuid() | — |
| periodo_id | uuid | Sim | — | — |
| employee_id | uuid | Sim | — | — |
| cod_folha | text | Não | — | — |
| rubrica_id | uuid | Sim | — | — |
| valor | numeric(14,4) | Não | — | — |
| valor_horas | interval | Não | — | — |
| origem_lancamento | text | Sim | 'AUTO'::text | — |
| observacao | text | Não | — | — |
| created_at | timestamp with time zone | Sim | now() | — |

### Chave primária
- `CONSTRAINT payroll_fechamento_linha_pkey PRIMARY KEY (id)`

### Relacionamentos
- `payroll_fechamento_linha_employee_id_fkey`: `employee_id` → `public.employees(id)`
- `payroll_fechamento_linha_periodo_id_fkey`: `periodo_id` → `public.payroll_fechamento_periodo(id)` (ON DELETE CASCADE)
- `payroll_fechamento_linha_rubrica_id_fkey`: `rubrica_id` → `public.payroll_rubricas(id)`

### Constraints
- `CONSTRAINT payroll_fechamento_linha_origem_lancamento_check CHECK ((origem_lancamento = ANY (ARRAY['AUTO'::text, 'MANUAL'::text, 'AJUSTE'::text])))`
- `CONSTRAINT payroll_fechamento_linha_periodo_id_employee_id_rubrica_id_key UNIQUE (periodo_id, employee_id, rubrica_id)`

### Índices
- `idx_pfl_employee`: `USING btree (employee_id)`
- `idx_pfl_periodo`: `USING btree (periodo_id)`

### Triggers

Nenhum trigger associado.

### Políticas RLS

RLS: **habilitada**.
- `pfl_read`: `FOR SELECT USING ((public.get_my_tier() = ANY (ARRAY['T3'::text, 'T4'::text, 'T5'::text, 'T6'::text])))`
- `pfl_write`: `USING ((public.get_my_tier() = ANY (ARRAY['T4'::text, 'T5'::text, 'T6'::text])))`

## payroll_fechamento_periodo

### Finalidade

Descrição inferida pela estrutura: armazena registros relacionados a `payroll fechamento periodo`. A finalidade de negócio exata deve ser confirmada com a equipe responsável.

### Colunas

| Coluna | Tipo | Obrigatória | Padrão | Observação |
|---|---|---|---|---|
| id | uuid | Sim | gen_random_uuid() | — |
| unit_id | uuid | Sim | — | — |
| competencia | text | Sim | — | — |
| tipo_processo | text | Sim | '11'::text | — |
| status | text | Sim | 'ABERTO'::text | — |
| custo_total_folha | numeric(14,2) | Não | — | — |
| gerado_por | uuid | Não | — | — |
| gerado_em | timestamp with time zone | Sim | now() | — |

### Chave primária
- `CONSTRAINT payroll_fechamento_periodo_pkey PRIMARY KEY (id)`

### Relacionamentos
- `payroll_fechamento_periodo_gerado_por_fkey`: `gerado_por` → `public.employees(id)` (ON DELETE SET NULL)
- `payroll_fechamento_periodo_unit_id_fkey`: `unit_id` → `public.units(id)`

### Constraints
- `CONSTRAINT payroll_fechamento_periodo_status_check CHECK ((status = ANY (ARRAY['ABERTO'::text, 'EM_CONFERENCIA'::text, 'ENVIADO_ESCRITORIO'::text, 'APROVADO'::text, 'FECHADO'::text])))`
- `CONSTRAINT payroll_fechamento_periodo_tipo_processo_check CHECK ((tipo_processo = ANY (ARRAY['11'::text, '41'::text, '42'::text, '51'::text, '52'::text])))`
- `CONSTRAINT payroll_fechamento_periodo_unit_id_competencia_tipo_process_key UNIQUE (unit_id, competencia, tipo_processo)`

### Índices
- `idx_pfp_unit_comp`: `USING btree (unit_id, competencia)`

### Triggers

Nenhum trigger associado.

### Políticas RLS

RLS: **habilitada**.
- `pfp_read`: `FOR SELECT USING ((public.get_my_tier() = ANY (ARRAY['T3'::text, 'T4'::text, 'T5'::text, 'T6'::text])))`
- `pfp_write`: `USING ((public.get_my_tier() = ANY (ARRAY['T4'::text, 'T5'::text, 'T6'::text])))`

## payroll_rubricas

### Finalidade

Descrição inferida pela estrutura: armazena registros relacionados a `payroll rubricas`. A finalidade de negócio exata deve ser confirmada com a equipe responsável.

### Colunas

| Coluna | Tipo | Obrigatória | Padrão | Observação |
|---|---|---|---|---|
| id | uuid | Sim | gen_random_uuid() | — |
| cod_kph | text | Sim | — | — |
| grupo | text | Sim | — | — |
| descricao | text | Sim | — | — |
| tipo | text | Sim | — | — |
| natureza_esocial | text | Não | — | — |
| inc_inss | boolean | Não | — | — |
| inc_irrf | boolean | Não | — | — |
| inc_fgts | boolean | Não | — | — |
| unidade | text | Sim | — | — |
| origem_dado | text | Sim | — | — |
| cod_dominio | text | Não | — | — |
| ativo | boolean | Sim | true | — |
| observacao | text | Não | — | — |
| created_at | timestamp with time zone | Sim | now() | — |

### Chave primária
- `CONSTRAINT payroll_rubricas_pkey PRIMARY KEY (id)`

### Relacionamentos

Nenhuma chave estrangeira identificada.

### Constraints
- `CONSTRAINT payroll_rubricas_grupo_check CHECK ((grupo = ANY (ARRAY['IDENTIFICACAO'::text, 'PROVENTO_FIXO'::text, 'PROVENTO_VARIAVEL'::text, 'DESCONTO'::text, 'INFORMATIVA'::text, 'BENEFICIO'::text, 'BASE'::text, 'RETORNO'::text])))`
- `CONSTRAINT payroll_rubricas_origem_dado_check CHECK ((origem_dado = ANY (ARRAY['AUTO_PONTO'::text, 'AUTO_CADASTRO'::text, 'AUTO'::text, 'MANUAL_RH'::text, 'JUDICIAL'::text, 'EXTERNO'::text, 'CALCULADO'::text])))`
- `CONSTRAINT payroll_rubricas_tipo_check CHECK ((tipo = ANY (ARRAY['PROVENTO'::text, 'DESCONTO'::text, 'INFORMATIVA'::text, 'FLAG'::text, 'BASE'::text])))`
- `CONSTRAINT payroll_rubricas_unidade_check CHECK ((unidade = ANY (ARRAY['R$'::text, 'HORAS'::text, 'DIAS'::text, 'QTD'::text, 'PERCENT'::text, 'FLAG'::text, 'TEXTO'::text])))`
- `CONSTRAINT payroll_rubricas_cod_kph_key UNIQUE (cod_kph)`

### Índices

Nenhum índice adicional identificado.

### Triggers

Nenhum trigger associado.

### Políticas RLS

RLS: **habilitada**.
- `payroll_rubricas_read`: `FOR SELECT USING ((public.get_my_tier() = ANY (ARRAY['T3'::text, 'T4'::text, 'T5'::text, 'T6'::text])))`
- `payroll_rubricas_write`: `USING ((public.get_my_tier() = ANY (ARRAY['T4'::text, 'T5'::text, 'T6'::text])))`

## payslips

### Finalidade

Descrição inferida pela estrutura: armazena registros relacionados a `payslips`. A finalidade de negócio exata deve ser confirmada com a equipe responsável.

### Colunas

| Coluna | Tipo | Obrigatória | Padrão | Observação |
|---|---|---|---|---|
| id | uuid | Sim | gen_random_uuid() | — |
| employee_id | uuid | Sim | — | — |
| competencia | date | Sim | — | — |
| salario_base | numeric(10,2) | Sim | — | — |
| horas_extras | numeric(10,2) | Não | 0 | — |
| adicional_noturno | numeric(10,2) | Não | 0 | — |
| gorjeta | numeric(10,2) | Não | 0 | — |
| dsr_gorjeta | numeric(10,2) | Não | 0 | — |
| desconto_inss | numeric(10,2) | Não | 0 | — |
| desconto_irrf | numeric(10,2) | Não | 0 | — |
| desconto_vale_transporte | numeric(10,2) | Não | 0 | — |
| desconto_vale_refeicao | numeric(10,2) | Não | 0 | — |
| outros_descontos | numeric(10,2) | Não | 0 | — |
| outros_acrescimos | numeric(10,2) | Não | 0 | — |
| liquido | numeric(10,2) | Sim | — | — |
| status | text | Não | 'rascunho'::text | — |
| pdf_url | text | Não | — | — |
| created_at | timestamp with time zone | Não | now() | — |
| fgts_base | numeric(10,2) | Não | — | — |
| fgts_mes | numeric(10,2) | Não | — | — |
| faixa_irrf | text | Não | — | — |
| employee_code | text | Não | — | — |
| unit_id | uuid | Não | — | — |
| nome | text | Não | — | — |
| tipo | text | Não | — | — |
| cargo | text | Não | — | — |
| bonus | numeric(10,2) | Não | — | — |
| horas_trabalhadas | numeric | Não | 0 | — |
| adiantamento | numeric | Não | 0 | — |
| vt | numeric | Não | 0 | — |
| vr | numeric | Não | 0 | — |
| inss | numeric | Não | 0 | — |
| fgts | numeric | Não | 0 | — |
| valor_liquido | numeric | Não | 0 | — |
| observacoes | text | Não | — | — |

### Chave primária
- `CONSTRAINT payslips_pkey PRIMARY KEY (id)`

### Relacionamentos
- `payslips_employee_id_fkey`: `employee_id` → `public.employees(id)` (ON DELETE CASCADE)
- `payslips_unit_id_fkey`: `unit_id` → `public.units(id)`

### Constraints
- `CONSTRAINT payslips_emp_comp_tipo_key UNIQUE (employee_id, competencia, tipo)`

### Índices
- `idx_payslips_employee`: `USING btree (employee_id, competencia DESC)`
- `idx_payslips_employee_code`: `USING btree (employee_code)`

### Triggers

Nenhum trigger associado.

### Políticas RLS

RLS: **habilitada**.
- `payslips_delete`: `FOR DELETE USING (public.kph_is_founder())`
- `payslips_insert`: `FOR INSERT WITH CHECK ((EXISTS ( SELECT 1 FROM public.employees e WHERE ((e.id = payslips.employee_id) AND public.kph_has_role_for_unit(e.unit_id)))))`
- `payslips_select`: `FOR SELECT USING ((EXISTS ( SELECT 1 FROM public.employees e WHERE ((e.id = payslips.employee_id) AND public.kph_has_role_for_unit(e.unit_id)))))`
- `payslips_update`: `FOR UPDATE USING ((EXISTS ( SELECT 1 FROM public.employees e WHERE ((e.id = payslips.employee_id) AND public.kph_has_role_for_unit(e.unit_id)))))`
- `t1_own`: `FOR SELECT USING ((employee_id = ( SELECT employees.id FROM public.employees WHERE (employees.user_id = auth.uid()))))`
- `t3_dept`: `USING (((public.get_my_tier() = 'T3'::text) AND (public.get_my_dept() = 'pessoas'::text)))`
- `t4_master`: `USING ((public.get_my_tier() = 'T4'::text))`

## pdi_metas

### Finalidade

Descrição inferida pela estrutura: armazena registros relacionados a `pdi metas`. A finalidade de negócio exata deve ser confirmada com a equipe responsável.

### Colunas

| Coluna | Tipo | Obrigatória | Padrão | Observação |
|---|---|---|---|---|
| id | uuid | Sim | gen_random_uuid() | — |
| pdi_id | uuid | Sim | — | — |
| descricao | text | Sim | — | — |
| prazo | date | Não | — | — |
| status | text | Sim | 'pendente'::text | — |
| progresso | integer | Não | 0 | — |
| created_at | timestamp with time zone | Não | now() | — |

### Chave primária
- `CONSTRAINT pdi_metas_pkey PRIMARY KEY (id)`

### Relacionamentos
- `pdi_metas_pdi_id_fkey`: `pdi_id` → `public.pdis(id)` (ON DELETE CASCADE)

### Constraints
- `CONSTRAINT pdi_metas_progresso_check CHECK (((progresso >= 0) AND (progresso <= 100)))`
- `CONSTRAINT pdi_metas_status_check CHECK ((status = ANY (ARRAY['pendente'::text, 'em_andamento'::text, 'concluida'::text, 'cancelada'::text])))`

### Índices
- `idx_pdi_metas_pdi`: `USING btree (pdi_id)`
- `pdi_metas_pdi`: `USING btree (pdi_id)`

### Triggers

Nenhum trigger associado.

### Políticas RLS

RLS: **habilitada**.
- `pdi_metas_access`: `USING ((pdi_id IN ( SELECT pdis.id FROM public.pdis WHERE (pdis.unit_id IN ( SELECT user_roles.unit_id FROM public.user_roles WHERE (user_roles.user_id = auth.uid()))))))`
- `pdi_metas_select`: `FOR SELECT USING ((pdi_id IN ( SELECT pdis.id FROM public.pdis)))`
- `pdi_metas_write_t3`: `USING ((public.get_my_tier() = ANY (ARRAY['T3'::text, 'T4'::text])))`

## pdis

### Finalidade

Descrição inferida pela estrutura: armazena registros relacionados a `pdis`. A finalidade de negócio exata deve ser confirmada com a equipe responsável.

### Colunas

| Coluna | Tipo | Obrigatória | Padrão | Observação |
|---|---|---|---|---|
| id | uuid | Sim | gen_random_uuid() | — |
| unit_id | uuid | Sim | — | — |
| employee_id | uuid | Sim | — | — |
| criado_por | uuid | Não | — | — |
| titulo | text | Sim | — | — |
| descricao | text | Não | — | — |
| status | text | Sim | 'ativo'::text | — |
| data_inicio | date | Sim | — | — |
| data_fim | date | Sim | — | — |
| avaliacao_id | uuid | Não | — | — |
| created_at | timestamp with time zone | Não | now() | — |
| updated_at | timestamp with time zone | Não | now() | — |
| created_by | uuid | Não | — | — |

### Chave primária
- `CONSTRAINT pdis_pkey PRIMARY KEY (id)`

### Relacionamentos
- `pdis_avaliacao_id_fkey`: `avaliacao_id` → `public.performance_reviews(id)`
- `pdis_created_by_fkey`: `created_by` → `auth.users(id)` (ON DELETE SET NULL)
- `pdis_criado_por_fkey`: `criado_por` → `auth.users(id)`
- `pdis_employee_id_fkey`: `employee_id` → `public.employees(id)`
- `pdis_unit_id_fkey`: `unit_id` → `public.units(id)`

### Constraints
- `CONSTRAINT pdis_status_check CHECK ((status = ANY (ARRAY['ativo'::text, 'concluido'::text, 'cancelado'::text])))`

### Índices
- `idx_pdis_employee`: `USING btree (employee_id)`
- `idx_pdis_unit`: `USING btree (unit_id)`
- `pdis_employee`: `USING btree (employee_id)`

### Triggers
- `pdis_updated_at`: `BEFORE UPDATE FOR EACH ROW EXECUTE FUNCTION public.set_updated_at()`

### Políticas RLS

RLS: **habilitada**.
- `pdis_select_own`: `FOR SELECT USING (((employee_id IN ( SELECT employees.id FROM public.employees WHERE (employees.user_id = auth.uid()))) OR (public.get_my_tier() = ANY (ARRAY['T3'::text, 'T4'::text]))))`
- `pdis_write_t3`: `USING ((public.get_my_tier() = ANY (ARRAY['T3'::text, 'T4'::text])))`
- `unit_access`: `USING ((unit_id IN ( SELECT user_roles.unit_id FROM public.user_roles WHERE (user_roles.user_id = auth.uid()))))`

## performance_reviews

### Finalidade

Descrição inferida pela estrutura: armazena registros relacionados a `performance reviews`. A finalidade de negócio exata deve ser confirmada com a equipe responsável.

### Colunas

| Coluna | Tipo | Obrigatória | Padrão | Observação |
|---|---|---|---|---|
| id | uuid | Sim | gen_random_uuid() | — |
| employee_id | uuid | Sim | — | — |
| template_id | uuid | Sim | — | — |
| avaliador_id | uuid | Não | — | — |
| periodo | text | Sim | — | — |
| status | text | Sim | 'rascunho'::text | — |
| nota_geral | numeric(4,2) | Não | — | — |
| respostas | jsonb | Sim | '{}'::jsonb | — |
| pontos_fortes | text | Não | — | — |
| pontos_melhoria | text | Não | — | — |
| plano_acao | text | Não | — | — |
| data_avaliacao | date | Não | — | — |
| created_at | timestamp with time zone | Não | now() | — |
| updated_at | timestamp with time zone | Não | now() | — |
| tipo_avaliador | text | Não | 'gestor'::text | — |
| anonimo | boolean | Não | false | — |

### Chave primária
- `CONSTRAINT performance_reviews_pkey PRIMARY KEY (id)`

### Relacionamentos
- `performance_reviews_avaliador_id_fkey`: `avaliador_id` → `auth.users(id)`
- `performance_reviews_employee_id_fkey`: `employee_id` → `public.employees(id)` (ON DELETE CASCADE)
- `performance_reviews_template_id_fkey`: `template_id` → `public.performance_templates(id)`

### Constraints
- `CONSTRAINT performance_reviews_status_check CHECK ((status = ANY (ARRAY['rascunho'::text, 'concluida'::text, 'aprovada'::text])))`
- `CONSTRAINT performance_reviews_tipo_avaliador_check CHECK ((tipo_avaliador = ANY (ARRAY['autoavaliacao'::text, 'par'::text, 'gestor'::text, 'liderado'::text])))`

### Índices
- `idx_perf_reviews_employee`: `USING btree (employee_id)`
- `idx_perf_reviews_template`: `USING btree (template_id)`
- `idx_performance_reviews_avaliador`: `USING btree (avaliador_id)`
- `idx_performance_reviews_data`: `USING btree (data_avaliacao DESC)`
- `idx_performance_reviews_employee`: `USING btree (employee_id)`
- `idx_performance_reviews_periodo`: `USING btree (periodo)`
- `idx_performance_reviews_status`: `USING btree (status)`
- `idx_performance_reviews_template`: `USING btree (template_id)`

### Triggers
- `trg_performance_reviews_updated_at`: `BEFORE UPDATE FOR EACH ROW EXECUTE FUNCTION public.update_updated_at_column()`

### Políticas RLS

RLS: **habilitada**.
- `perf_reviews_read`: `FOR SELECT USING (((employee_id IN ( SELECT employees.id FROM public.employees WHERE (employees.user_id = auth.uid()))) OR (public.get_my_tier() = ANY (ARRAY['T3'::text, 'T4'::text]))))`
- `perf_reviews_write`: `USING ((public.get_my_tier() = ANY (ARRAY['T3'::text, 'T4'::text])))`
- `pr_delete`: `FOR DELETE USING (public.kph_is_founder())`
- `pr_insert`: `FOR INSERT WITH CHECK ((EXISTS ( SELECT 1 FROM public.employees e WHERE ((e.id = performance_reviews.employee_id) AND public.kph_has_role_for_unit(e.unit_id)))))`
- `pr_select`: `FOR SELECT USING ((EXISTS ( SELECT 1 FROM public.employees e WHERE ((e.id = performance_reviews.employee_id) AND public.kph_has_role_for_unit(e.unit_id)))))`
- `pr_update`: `FOR UPDATE USING ((EXISTS ( SELECT 1 FROM public.employees e WHERE ((e.id = performance_reviews.employee_id) AND public.kph_has_role_for_unit(e.unit_id))))) WITH CHECK ((EXISTS ( SELECT 1 FROM public.employees e WHERE ((e.id = performance_reviews.employee_id) AND public.kph_has_role_for_unit(e.unit_id)))))`

## performance_templates

### Finalidade

Descrição inferida pela estrutura: armazena registros relacionados a `performance templates`. A finalidade de negócio exata deve ser confirmada com a equipe responsável.

### Colunas

| Coluna | Tipo | Obrigatória | Padrão | Observação |
|---|---|---|---|---|
| id | uuid | Sim | gen_random_uuid() | — |
| brand_id | uuid | Sim | — | — |
| unit_id | uuid | Não | — | — |
| nome | text | Sim | — | — |
| descricao | text | Não | — | — |
| funcao | text | Não | — | — |
| periodicidade | text | Sim | — | — |
| criterios | jsonb | Sim | '[]'::jsonb | — |
| ativo | boolean | Não | true | — |
| created_by | uuid | Não | — | — |
| created_at | timestamp with time zone | Não | now() | — |
| updated_at | timestamp with time zone | Não | now() | — |

### Chave primária
- `CONSTRAINT performance_templates_pkey PRIMARY KEY (id)`

### Relacionamentos
- `performance_templates_brand_id_fkey`: `brand_id` → `public.brands(id)`
- `performance_templates_created_by_fkey`: `created_by` → `auth.users(id)`
- `performance_templates_unit_id_fkey`: `unit_id` → `public.units(id)`

### Constraints
- `CONSTRAINT performance_templates_periodicidade_check CHECK ((periodicidade = ANY (ARRAY['mensal'::text, 'trimestral'::text, 'semestral'::text, 'anual'::text])))`

### Índices
- `idx_perf_templates_brand`: `USING btree (brand_id)`
- `idx_performance_templates_ativo`: `USING btree (ativo)`
- `idx_performance_templates_brand`: `USING btree (brand_id)`
- `idx_performance_templates_funcao`: `USING btree (funcao)`
- `idx_performance_templates_unit`: `USING btree (unit_id)`

### Triggers
- `trg_performance_templates_updated_at`: `BEFORE UPDATE FOR EACH ROW EXECUTE FUNCTION public.update_updated_at_column()`

### Políticas RLS

RLS: **habilitada**.
- `perf_templates_read`: `FOR SELECT USING ((public.get_my_tier() = ANY (ARRAY['T3'::text, 'T4'::text])))`
- `perf_templates_write`: `USING ((public.get_my_tier() = 'T4'::text))`
- `pt_delete`: `FOR DELETE USING (public.kph_is_founder())`
- `pt_insert`: `FOR INSERT WITH CHECK (public.kph_has_role_for_brand(brand_id))`
- `pt_select`: `FOR SELECT USING (public.kph_has_role_for_brand(brand_id))`
- `pt_update`: `FOR UPDATE USING (public.kph_has_role_for_brand(brand_id)) WITH CHECK (public.kph_has_role_for_brand(brand_id))`

## plan_members

### Finalidade

Descrição inferida pela estrutura: armazena registros relacionados a `plan members`. A finalidade de negócio exata deve ser confirmada com a equipe responsável.

### Colunas

| Coluna | Tipo | Obrigatória | Padrão | Observação |
|---|---|---|---|---|
| plan_id | uuid | Sim | — | — |
| member_id | uuid | Sim | — | — |

### Chave primária
- `CONSTRAINT plan_members_pkey PRIMARY KEY (plan_id, member_id)`

### Relacionamentos
- `plan_members_member_id_fkey`: `member_id` → `public.team_members(id)` (ON DELETE CASCADE)
- `plan_members_plan_id_fkey`: `plan_id` → `public.projects(id)` (ON DELETE CASCADE)

### Constraints

Nenhuma constraint adicional identificada.

### Índices

Nenhum índice adicional identificado.

### Triggers

Nenhum trigger associado.

### Políticas RLS

RLS: **habilitada**.

Nenhuma política associada.

## ponto_mensal

### Finalidade

Descrição inferida pela estrutura: armazena registros relacionados a `ponto mensal`. A finalidade de negócio exata deve ser confirmada com a equipe responsável.

### Colunas

| Coluna | Tipo | Obrigatória | Padrão | Observação |
|---|---|---|---|---|
| id | uuid | Sim | gen_random_uuid() | — |
| unit_id | uuid | Sim | — | — |
| employee_id | uuid | Não | — | — |
| matricula | text | Não | — | — |
| nome | text | Sim | — | — |
| cpf | text | Não | — | — |
| cargo | text | Não | — | — |
| departamento | text | Não | — | — |
| periodo | text | Sim | — | — |
| horas_previstas | text | Não | — | — |
| horas_trabalhadas | text | Não | — | — |
| horas_negativas | text | Não | — | — |
| horas_positivas | text | Não | — | — |
| saldo | text | Não | — | — |
| banco_horas_acumulado | text | Não | — | — |
| banco_horas_mes | text | Não | — | — |
| compensacao_bh | text | Não | — | — |
| adicional_noturno | text | Não | — | — |
| falta_injustificada_horas | text | Não | — | — |
| falta_injustificada_dias | integer | Não | 0 | — |
| afastamentos_horas | text | Não | — | — |
| afastamentos_dias | integer | Não | 0 | — |
| ferias_horas | text | Não | — | — |
| ferias_dias | integer | Não | 0 | — |
| inss_horas | text | Não | — | — |
| inss_dias | integer | Não | 0 | — |
| atestado_medico | text | Não | — | — |
| abonado_horas | text | Não | — | — |
| abonado_dias | integer | Não | 0 | — |
| folga_domingo | text | Não | — | — |
| folga_feriado | text | Não | — | — |
| feriados_dias | integer | Não | 0 | — |
| confraternizacao | text | Não | — | — |
| licenca_paternidade_horas | text | Não | — | — |
| licenca_paternidade_dias | integer | Não | 0 | — |
| data_admissao | text | Não | — | — |
| data_demissao | text | Não | — | — |
| importado_em | timestamp with time zone | Não | now() | — |
| created_at | timestamp with time zone | Não | now() | — |

### Chave primária
- `CONSTRAINT ponto_mensal_pkey PRIMARY KEY (id)`

### Relacionamentos
- `ponto_mensal_employee_id_fkey`: `employee_id` → `public.employees(id)` (ON DELETE SET NULL)
- `ponto_mensal_unit_id_fkey`: `unit_id` → `public.units(id)` (ON DELETE CASCADE)

### Constraints
- `CONSTRAINT ponto_mensal_unit_id_periodo_matricula_key UNIQUE (unit_id, periodo, matricula)`

### Índices

Nenhum índice adicional identificado.

### Triggers

Nenhum trigger associado.

### Políticas RLS

RLS: **habilitada**.
- `unit members can insert ponto_mensal`: `FOR INSERT WITH CHECK (public.kph_has_role_for_unit(unit_id))`
- `unit members can select ponto_mensal`: `FOR SELECT USING (public.kph_has_role_for_unit(unit_id))`
- `unit members can update ponto_mensal`: `FOR UPDATE USING (public.kph_has_role_for_unit(unit_id)) WITH CHECK (public.kph_has_role_for_unit(unit_id))`

## price_quote_items

### Finalidade

Descrição inferida pela estrutura: armazena registros relacionados a `price quote items`. A finalidade de negócio exata deve ser confirmada com a equipe responsável.

### Colunas

| Coluna | Tipo | Obrigatória | Padrão | Observação |
|---|---|---|---|---|
| id | uuid | Sim | gen_random_uuid() | — |
| quote_id | uuid | Sim | — | — |
| descricao | text | Sim | — | — |
| unidade | text | Sim | 'kg'::text | — |
| quantidade | numeric(10,3) | Sim | — | — |
| preco_unitario | numeric(10,4) | Não | — | — |
| total | numeric(12,2) | Sim | GENERATED ALWAYS AS ( CASE WHEN (preco_unitario IS NOT NULL) THEN (quantidade * preco_unitario) ELSE NULL::numeric END) STORED | Coluna gerada |
| observacoes | text | Não | — | — |
| created_at | timestamp with time zone | Sim | now() | — |

### Chave primária
- `CONSTRAINT price_quote_items_pkey PRIMARY KEY (id)`

### Relacionamentos
- `price_quote_items_quote_id_fkey`: `quote_id` → `public.price_quotes(id)` (ON DELETE CASCADE)

### Constraints

Nenhuma constraint adicional identificada.

### Índices
- `price_quote_items_quote_idx`: `USING btree (quote_id)`

### Triggers

Nenhum trigger associado.

### Políticas RLS

RLS: **habilitada**.
- `unit members can delete quote items`: `FOR DELETE USING ((EXISTS ( SELECT 1 FROM public.price_quotes q WHERE ((q.id = price_quote_items.quote_id) AND public.kph_has_role_for_unit(q.unit_id)))))`
- `unit members can insert quote items`: `FOR INSERT WITH CHECK ((EXISTS ( SELECT 1 FROM public.price_quotes q WHERE ((q.id = price_quote_items.quote_id) AND public.kph_has_role_for_unit(q.unit_id)))))`
- `unit members can select quote items`: `FOR SELECT USING ((EXISTS ( SELECT 1 FROM public.price_quotes q WHERE ((q.id = price_quote_items.quote_id) AND public.kph_has_role_for_unit(q.unit_id)))))`
- `unit members can update quote items`: `FOR UPDATE USING ((EXISTS ( SELECT 1 FROM public.price_quotes q WHERE ((q.id = price_quote_items.quote_id) AND public.kph_has_role_for_unit(q.unit_id)))))`

## price_quotes

### Finalidade

Descrição inferida pela estrutura: armazena registros relacionados a `price quotes`. A finalidade de negócio exata deve ser confirmada com a equipe responsável.

### Colunas

| Coluna | Tipo | Obrigatória | Padrão | Observação |
|---|---|---|---|---|
| id | uuid | Sim | gen_random_uuid() | — |
| unit_id | uuid | Sim | — | — |
| supplier_id | uuid | Não | — | — |
| periodo | date | Sim | — | — |
| status | public.quote_status | Sim | 'rascunho'::public.quote_status | — |
| titulo | text | Não | — | — |
| observacoes | text | Não | — | — |
| created_by | uuid | Não | — | — |
| created_at | timestamp with time zone | Sim | now() | — |
| updated_at | timestamp with time zone | Sim | now() | — |

### Chave primária
- `CONSTRAINT price_quotes_pkey PRIMARY KEY (id)`

### Relacionamentos
- `price_quotes_created_by_fkey`: `created_by` → `auth.users(id)`
- `price_quotes_supplier_id_fkey`: `supplier_id` → `public.suppliers(id)` (ON DELETE SET NULL)
- `price_quotes_unit_id_fkey`: `unit_id` → `public.units(id)` (ON DELETE CASCADE)

### Constraints

Nenhuma constraint adicional identificada.

### Índices
- `price_quotes_unit_idx`: `USING btree (unit_id, periodo)`

### Triggers

Nenhum trigger associado.

### Políticas RLS

RLS: **habilitada**.
- `unit members can insert quotes`: `FOR INSERT WITH CHECK (public.kph_has_role_for_unit(unit_id))`
- `unit members can select quotes`: `FOR SELECT USING (public.kph_has_role_for_unit(unit_id))`
- `unit members can update quotes`: `FOR UPDATE USING (public.kph_has_role_for_unit(unit_id)) WITH CHECK (public.kph_has_role_for_unit(unit_id))`

## produtos_relatorio

### Finalidade

Descrição inferida pela estrutura: armazena registros relacionados a `produtos relatorio`. A finalidade de negócio exata deve ser confirmada com a equipe responsável.

### Colunas

| Coluna | Tipo | Obrigatória | Padrão | Observação |
|---|---|---|---|---|
| id | bigint | Sim | — | — |
| unit_id | uuid | Sim | — | — |
| fornecedor_nome | text | Não | — | — |
| nr_danfe | text | Não | — | — |
| v_total_danfe | numeric(14,4) | Não | — | — |
| dt_emissao | text | Não | — | — |
| item_codigo | text | Não | — | — |
| item_descricao | text | Não | — | — |
| unidade_medida | text | Não | — | — |
| tipo_item | text | Não | — | — |
| q_embalagem | numeric(14,4) | Não | — | — |
| q_estoque | numeric(14,4) | Não | — | — |
| v_embalagem | numeric(14,4) | Não | — | — |
| v_total_embalagem | numeric(14,4) | Não | — | — |
| v_custo_medio | numeric(14,4) | Não | — | — |
| v_custo_compra | numeric(14,4) | Não | — | — |
| v_custo_total | numeric(14,4) | Não | — | — |
| perc_variacao | numeric(10,4) | Não | — | — |
| calcula_cmv | boolean | Não | — | — |
| fornecedor_codigo | text | Não | — | — |
| codigo_gerencial | text | Não | — | — |
| desc_gerencial | text | Não | — | — |
| mes_lancamento | integer | Sim | — | — |
| ano_lancamento | integer | Sim | — | — |
| criado_em | timestamp with time zone | Não | now() | — |

### Chave primária
- `CONSTRAINT produtos_relatorio_pkey PRIMARY KEY (id)`

### Relacionamentos

Nenhuma chave estrangeira identificada.

### Constraints

Nenhuma constraint adicional identificada.

### Índices
- `idx_pr_categoria`: `USING btree (unit_id, desc_gerencial)`
- `idx_pr_unit_mes`: `USING btree (unit_id, ano_lancamento, mes_lancamento)`

### Triggers

Nenhum trigger associado.

### Políticas RLS

RLS: **habilitada**.
- `produtos_manage`: `TO service_role USING (true) WITH CHECK (true)`
- `produtos_read`: `FOR SELECT TO authenticated, anon USING (true)`

## profiles

### Finalidade

Descrição inferida pela estrutura: armazena registros relacionados a `profiles`. A finalidade de negócio exata deve ser confirmada com a equipe responsável.

### Colunas

| Coluna | Tipo | Obrigatória | Padrão | Observação |
|---|---|---|---|---|
| id | uuid | Sim | — | — |
| name | text | Não | — | — |
| email | text | Não | — | — |
| avatar_url | text | Não | — | — |
| created_at | timestamp with time zone | Não | now() | — |

### Chave primária
- `CONSTRAINT profiles_pkey PRIMARY KEY (id)`

### Relacionamentos
- `profiles_id_fkey`: `id` → `auth.users(id)`

### Constraints

Nenhuma constraint adicional identificada.

### Índices

Nenhum índice adicional identificado.

### Triggers

Nenhum trigger associado.

### Políticas RLS

RLS: **não habilitada no dump**.
- `profiles_own`: `USING ((auth.uid() = id))`

## project_invites

### Finalidade

Descrição inferida pela estrutura: armazena registros relacionados a `project invites`. A finalidade de negócio exata deve ser confirmada com a equipe responsável.

### Colunas

| Coluna | Tipo | Obrigatória | Padrão | Observação |
|---|---|---|---|---|
| id | uuid | Sim | gen_random_uuid() | — |
| project_id | uuid | Não | — | — |
| token | text | Não | (gen_random_uuid())::text | — |
| created_by | uuid | Não | — | — |
| expires_at | timestamp with time zone | Não | (now() + '7 days'::interval) | — |
| created_at | timestamp with time zone | Não | now() | — |

### Chave primária
- `CONSTRAINT project_invites_pkey PRIMARY KEY (id)`

### Relacionamentos
- `project_invites_created_by_fkey`: `created_by` → `auth.users(id)`
- `project_invites_project_id_fkey`: `project_id` → `public.projects(id)` (ON DELETE CASCADE)

### Constraints
- `CONSTRAINT project_invites_token_key UNIQUE (token)`

### Índices

Nenhum índice adicional identificado.

### Triggers

Nenhum trigger associado.

### Políticas RLS

RLS: **habilitada**.
- `invites_own`: `USING ((auth.uid() = created_by))`

## project_members

### Finalidade

Descrição inferida pela estrutura: armazena registros relacionados a `project members`. A finalidade de negócio exata deve ser confirmada com a equipe responsável.

### Colunas

| Coluna | Tipo | Obrigatória | Padrão | Observação |
|---|---|---|---|---|
| id | uuid | Sim | gen_random_uuid() | — |
| project_id | uuid | Não | — | — |
| user_id | uuid | Não | — | — |
| role | text | Não | 'member'::text | — |
| invited_by | uuid | Não | — | — |
| status | text | Não | 'pending'::text | — |
| created_at | timestamp with time zone | Não | now() | — |

### Chave primária
- `CONSTRAINT project_members_pkey PRIMARY KEY (id)`

### Relacionamentos
- `project_members_invited_by_fkey`: `invited_by` → `auth.users(id)`
- `project_members_project_id_fkey`: `project_id` → `public.projects(id)` (ON DELETE CASCADE)
- `project_members_user_id_fkey`: `user_id` → `auth.users(id)` (ON DELETE CASCADE)

### Constraints
- `CONSTRAINT project_members_role_check CHECK ((role = ANY (ARRAY['owner'::text, 'member'::text])))`
- `CONSTRAINT project_members_status_check CHECK ((status = ANY (ARRAY['pending'::text, 'accepted'::text])))`
- `CONSTRAINT project_members_project_id_user_id_key UNIQUE (project_id, user_id)`

### Índices

Nenhum índice adicional identificado.

### Triggers

Nenhum trigger associado.

### Políticas RLS

RLS: **habilitada**.
- `members_own`: `USING (((auth.uid() = user_id) OR (auth.uid() = invited_by)))`

## projects

### Finalidade

Descrição inferida pela estrutura: armazena registros relacionados a `projects`. A finalidade de negócio exata deve ser confirmada com a equipe responsável.

### Colunas

| Coluna | Tipo | Obrigatória | Padrão | Observação |
|---|---|---|---|---|
| id | uuid | Sim | gen_random_uuid() | — |
| name | text | Sim | — | — |
| description | text | Não | — | — |
| created_at | timestamp with time zone | Sim | timezone('utc'::text, now()) | — |
| start_date | date | Não | — | — |
| end_date | date | Não | — | — |
| status | text | Não | 'Não iniciado'::text | — |
| owner_id | uuid | Não | — | — |

### Chave primária
- `CONSTRAINT projects_pkey PRIMARY KEY (id)`

### Relacionamentos
- `projects_owner_id_fkey`: `owner_id` → `auth.users(id)`

### Constraints
- `CONSTRAINT projects_status_check CHECK ((status = ANY (ARRAY['Não iniciado'::text, 'Em andamento'::text, 'Concluído'::text])))`

### Índices

Nenhum índice adicional identificado.

### Triggers

Nenhum trigger associado.

### Políticas RLS

RLS: **não habilitada no dump**.

Nenhuma política associada.

## punch_adjustment_requests

### Finalidade

Descrição inferida pela estrutura: armazena registros relacionados a `punch adjustment requests`. A finalidade de negócio exata deve ser confirmada com a equipe responsável.

### Colunas

| Coluna | Tipo | Obrigatória | Padrão | Observação |
|---|---|---|---|---|
| id | uuid | Sim | gen_random_uuid() | — |
| employee_id | uuid | Sim | — | — |
| data_referencia | date | Sim | — | — |
| horario_saida_almoco | time without time zone | Sim | — | — |
| horario_retorno_almoco | time without time zone | Sim | — | — |
| motivo | text | Sim | — | — |
| status | text | Sim | 'pendente'::text | — |
| aprovado_por | uuid | Não | — | — |
| aprovado_em | timestamp with time zone | Não | — | — |
| created_at | timestamp with time zone | Sim | now() | — |

### Chave primária
- `CONSTRAINT punch_adjustment_requests_pkey PRIMARY KEY (id)`

### Relacionamentos
- `punch_adjustment_requests_aprovado_por_fkey`: `aprovado_por` → `auth.users(id)`
- `punch_adjustment_requests_employee_id_fkey`: `employee_id` → `public.employees(id)` (ON DELETE CASCADE)

### Constraints
- `CONSTRAINT punch_adjustment_requests_motivo_check CHECK ((motivo = ANY (ARRAY['Esqueci de registrar'::text, 'Estava em atendimento'::text, 'Sistema indisponível'::text, 'Saí para entrega/serviço externo'::text, 'Outro'::text])))`
- `CONSTRAINT punch_adjustment_requests_status_check CHECK ((status = ANY (ARRAY['pendente'::text, 'aprovado'::text, 'rejeitado'::text])))`

### Índices
- `idx_par_employee_data`: `USING btree (employee_id, data_referencia)`
- `idx_par_status`: `USING btree (status)`

### Triggers

Nenhum trigger associado.

### Políticas RLS

RLS: **habilitada**.
- `anon_all_punch_adj`: `TO authenticated, anon USING (true) WITH CHECK (true)`

## purchase_invoice_items

### Finalidade

Descrição inferida pela estrutura: armazena registros relacionados a `purchase invoice items`. A finalidade de negócio exata deve ser confirmada com a equipe responsável.

### Colunas

| Coluna | Tipo | Obrigatória | Padrão | Observação |
|---|---|---|---|---|
| id | uuid | Sim | gen_random_uuid() | — |
| purchase_invoice_id | uuid | Sim | — | — |
| ingredient_id | uuid | Não | — | — |
| ingredient_codigo | text | Sim | — | — |
| ingredient_nome | text | Sim | — | — |
| unidade | text | Não | — | — |
| quantidade_embalagem | numeric(14,4) | Não | — | — |
| quantidade_estoque | numeric(14,4) | Não | — | — |
| valor_embalagem | numeric(14,4) | Não | — | — |
| valor_total | numeric(14,2) | Não | — | — |
| custo_medio | numeric(14,4) | Não | — | — |
| custo_ultima_compra | numeric(14,4) | Não | — | — |
| categoria_gerencial_codigo | text | Não | — | — |
| categoria_gerencial_nome | text | Não | — | — |
| data_lancamento | date | Não | — | — |
| created_at | timestamp with time zone | Não | now() | — |

### Chave primária
- `CONSTRAINT purchase_invoice_items_pkey PRIMARY KEY (id)`

### Relacionamentos
- `purchase_invoice_items_ingredient_id_fkey`: `ingredient_id` → `public.ingredients(id)` (ON DELETE SET NULL)
- `purchase_invoice_items_purchase_invoice_id_fkey`: `purchase_invoice_id` → `public.purchase_invoices(id)` (ON DELETE CASCADE)

### Constraints

Nenhuma constraint adicional identificada.

### Índices
- `idx_purchase_invoice_items_codigo`: `USING btree (ingredient_codigo)`
- `idx_purchase_invoice_items_ingredient`: `USING btree (ingredient_id) WHERE (ingredient_id IS NOT NULL)`
- `idx_purchase_invoice_items_invoice`: `USING btree (purchase_invoice_id)`

### Triggers

Nenhum trigger associado.

### Políticas RLS

RLS: **habilitada**.
- `purchase_invoice_items_delete`: `FOR DELETE USING (public.kph_is_founder())`
- `purchase_invoice_items_insert`: `FOR INSERT WITH CHECK ((EXISTS ( SELECT 1 FROM public.purchase_invoices pi WHERE ((pi.id = purchase_invoice_items.purchase_invoice_id) AND public.kph_has_role_for_unit(pi.unit_id)))))`
- `purchase_invoice_items_select`: `FOR SELECT USING ((EXISTS ( SELECT 1 FROM public.purchase_invoices pi WHERE ((pi.id = purchase_invoice_items.purchase_invoice_id) AND public.kph_has_role_for_unit(pi.unit_id)))))`
- `purchase_invoice_items_update`: `FOR UPDATE USING ((EXISTS ( SELECT 1 FROM public.purchase_invoices pi WHERE ((pi.id = purchase_invoice_items.purchase_invoice_id) AND public.kph_has_role_for_unit(pi.unit_id))))) WITH CHECK ((EXISTS ( SELECT 1 FROM public.purchase_invoices pi WHERE ((pi.id = purchase_invoice_items.purchase_invoice_id) AND public.kph_has_role_for_unit(pi.unit_id)))))`

## purchase_invoices

### Finalidade

Descrição inferida pela estrutura: armazena registros relacionados a `purchase invoices`. A finalidade de negócio exata deve ser confirmada com a equipe responsável.

### Colunas

| Coluna | Tipo | Obrigatória | Padrão | Observação |
|---|---|---|---|---|
| id | uuid | Sim | gen_random_uuid() | — |
| unit_id | uuid | Sim | — | — |
| numero_danfe | text | Sim | — | — |
| valor_total | numeric(14,2) | Sim | — | — |
| data_emissao | date | Sim | — | — |
| fornecedor_codigo | text | Não | — | — |
| fornecedor_nome | text | Não | — | — |
| cfop | text | Não | — | — |
| origem | text | Não | — | — |
| situacao | text | Não | — | — |
| mes_referencia | text | Não | — | — |
| created_at | timestamp with time zone | Não | now() | — |

### Chave primária
- `CONSTRAINT purchase_invoices_pkey PRIMARY KEY (id)`

### Relacionamentos
- `purchase_invoices_unit_id_fkey`: `unit_id` → `public.units(id)`

### Constraints
- `CONSTRAINT purchase_invoices_unit_id_numero_danfe_key UNIQUE (unit_id, numero_danfe)`

### Índices
- `idx_purchase_invoices_data_emissao`: `USING btree (data_emissao DESC)`
- `idx_purchase_invoices_mes_referencia`: `USING btree (mes_referencia)`
- `idx_purchase_invoices_unit`: `USING btree (unit_id)`

### Triggers

Nenhum trigger associado.

### Políticas RLS

RLS: **habilitada**.
- `purchase_invoices_delete`: `FOR DELETE USING (public.kph_is_founder())`
- `purchase_invoices_insert`: `FOR INSERT WITH CHECK (public.kph_has_role_for_unit(unit_id))`
- `purchase_invoices_select`: `FOR SELECT USING (public.kph_has_role_for_unit(unit_id))`
- `purchase_invoices_update`: `FOR UPDATE USING (public.kph_has_role_for_unit(unit_id)) WITH CHECK (public.kph_has_role_for_unit(unit_id))`

## purchase_order_items

### Finalidade

Descrição inferida pela estrutura: armazena registros relacionados a `purchase order items`. A finalidade de negócio exata deve ser confirmada com a equipe responsável.

### Colunas

| Coluna | Tipo | Obrigatória | Padrão | Observação |
|---|---|---|---|---|
| id | uuid | Sim | gen_random_uuid() | — |
| order_id | uuid | Sim | — | — |
| nome | text | Sim | — | — |
| unidade | text | Não | — | — |
| quantidade | numeric(12,3) | Sim | 0 | — |
| quantidade_recebida | numeric(12,3) | Sim | 0 | — |
| preco_unitario | numeric(10,2) | Sim | 0 | — |
| total | numeric(14,2) | Não | GENERATED ALWAYS AS ((quantidade * preco_unitario)) STORED | Coluna gerada |
| created_at | timestamp with time zone | Não | now() | — |

### Chave primária
- `CONSTRAINT purchase_order_items_pkey PRIMARY KEY (id)`

### Relacionamentos
- `purchase_order_items_order_id_fkey`: `order_id` → `public.purchase_orders(id)` (ON DELETE CASCADE)

### Constraints

Nenhuma constraint adicional identificada.

### Índices
- `idx_purchase_order_items_order`: `USING btree (order_id)`

### Triggers
- `trg_recalc_po_total_iud`: `AFTER INSERT OR DELETE OR UPDATE FOR EACH ROW EXECUTE FUNCTION public.recalc_purchase_order_total()`

### Políticas RLS

RLS: **habilitada**.
- `po_items_delete`: `FOR DELETE USING (public.kph_is_founder())`
- `po_items_insert`: `FOR INSERT WITH CHECK ((EXISTS ( SELECT 1 FROM public.purchase_orders po WHERE ((po.id = purchase_order_items.order_id) AND public.kph_has_role_for_unit(po.unit_id)))))`
- `po_items_select`: `FOR SELECT USING ((EXISTS ( SELECT 1 FROM public.purchase_orders po WHERE ((po.id = purchase_order_items.order_id) AND public.kph_has_role_for_unit(po.unit_id)))))`
- `po_items_update`: `FOR UPDATE USING ((EXISTS ( SELECT 1 FROM public.purchase_orders po WHERE ((po.id = purchase_order_items.order_id) AND public.kph_has_role_for_unit(po.unit_id))))) WITH CHECK ((EXISTS ( SELECT 1 FROM public.purchase_orders po WHERE ((po.id = purchase_order_items.order_id) AND public.kph_has_role_for_unit(po.unit_id)))))`

## purchase_orders

### Finalidade

Descrição inferida pela estrutura: armazena registros relacionados a `purchase orders`. A finalidade de negócio exata deve ser confirmada com a equipe responsável.

### Colunas

| Coluna | Tipo | Obrigatória | Padrão | Observação |
|---|---|---|---|---|
| id | uuid | Sim | gen_random_uuid() | — |
| unit_id | uuid | Sim | — | — |
| brand_id | uuid | Sim | — | — |
| numero | text | Sim | ('PO-'::text \|\| lpad((nextval('public.purchase_orders_numero_seq'::regclass))::text, 6, '0'::text)) | — |
| fornecedor | text | Não | — | — |
| supplier_id | uuid | Não | — | — |
| status | public.purchase_order_status | Sim | 'rascunho'::public.purchase_order_status | — |
| data_pedido | date | Sim | CURRENT_DATE | — |
| data_prevista | date | Não | — | — |
| valor_total | numeric(12,2) | Sim | 0 | — |
| observacoes | text | Não | — | — |
| created_by | uuid | Não | — | — |
| created_at | timestamp with time zone | Não | now() | — |
| updated_at | timestamp with time zone | Não | now() | — |
| solicitante_nome | text | Não | — | — |

### Chave primária
- `CONSTRAINT purchase_orders_pkey PRIMARY KEY (id)`

### Relacionamentos
- `purchase_orders_brand_id_fkey`: `brand_id` → `public.brands(id)`
- `purchase_orders_created_by_fkey`: `created_by` → `auth.users(id)`
- `purchase_orders_supplier_id_fkey`: `supplier_id` → `public.suppliers(id)`
- `purchase_orders_unit_id_fkey`: `unit_id` → `public.units(id)`

### Constraints
- `CONSTRAINT purchase_orders_status_check CHECK ((status = ANY (ARRAY['rascunho'::public.purchase_order_status, 'enviado'::public.purchase_order_status, 'parcial'::public.purchase_order_status, 'recebido'::public.purchase_order_status, 'cancelado'::public.purchase_order_status])))`
- `CONSTRAINT purchase_orders_numero_key UNIQUE (numero)`

### Índices
- `idx_purchase_orders_brand`: `USING btree (brand_id)`
- `idx_purchase_orders_data_pedido`: `USING btree (data_pedido DESC)`
- `idx_purchase_orders_status`: `USING btree (status)`
- `idx_purchase_orders_unit`: `USING btree (unit_id)`

### Triggers
- `trg_purchase_orders_updated_at`: `BEFORE UPDATE FOR EACH ROW EXECUTE FUNCTION public.update_updated_at_column()`

### Políticas RLS

RLS: **habilitada**.
- `po_delete`: `FOR DELETE USING (public.kph_is_founder())`
- `po_insert`: `FOR INSERT WITH CHECK (public.kph_has_role_for_unit(unit_id))`
- `po_select`: `FOR SELECT USING (public.kph_has_role_for_unit(unit_id))`
- `po_update`: `FOR UPDATE USING (public.kph_has_role_for_unit(unit_id)) WITH CHECK (public.kph_has_role_for_unit(unit_id))`

## quadro_ideal

### Finalidade

Descrição inferida pela estrutura: armazena registros relacionados a `quadro ideal`. A finalidade de negócio exata deve ser confirmada com a equipe responsável.

### Colunas

| Coluna | Tipo | Obrigatória | Padrão | Observação |
|---|---|---|---|---|
| id | uuid | Sim | gen_random_uuid() | — |
| unit_id | uuid | Sim | — | — |
| departamento | text | Não | — | — |
| cargo | text | Não | — | — |
| cargo_grupo_id | uuid | Não | — | — |
| qtd_alvo | integer | Sim | — | — |
| vigente_desde | date | Sim | ((now() AT TIME ZONE 'America/Sao_Paulo'::text))::date | — |
| vigente_ate | date | Não | — | — |
| created_at | timestamp with time zone | Não | now() | — |
| cargo_id | uuid | Não | — | — |
| alvo_manha | integer | Sim | 0 | — |
| alvo_tarde | integer | Sim | 0 | — |
| alvo_noite | integer | Sim | 0 | — |
| alvo_madrugada | integer | Sim | 0 | — |
| alvo_intermediario | integer | Sim | 0 | — |
| reporta_a_cargo_id | uuid | Não | — | — |

### Chave primária
- `CONSTRAINT quadro_ideal_pkey PRIMARY KEY (id)`

### Relacionamentos
- `quadro_ideal_cargo_grupo_id_fkey`: `cargo_grupo_id` → `public.cargo_grupos(id)`
- `quadro_ideal_cargo_id_fkey`: `cargo_id` → `public.cargos(id)`
- `quadro_ideal_reporta_a_cargo_id_fkey`: `reporta_a_cargo_id` → `public.cargos(id)`
- `quadro_ideal_unit_id_fkey`: `unit_id` → `public.units(id)`

### Constraints
- `CONSTRAINT quadro_ideal_qtd_alvo_check CHECK ((qtd_alvo >= 0))`

### Índices
- `idx_quadro_ideal_unit_vigente`: `USING btree (unit_id) WHERE (vigente_ate IS NULL)`
- `idx_quadro_unit_cargo_ativo`: `USING btree (unit_id, cargo_id) WHERE ((vigente_ate IS NULL) AND (cargo_id IS NOT NULL))`

### Triggers
- `trg_sync_qtd_alvo`: `BEFORE INSERT OR UPDATE FOR EACH ROW EXECUTE FUNCTION public.fn_sync_qtd_alvo()`

### Políticas RLS

RLS: **habilitada**.
- `quadro_ideal_insert`: `FOR INSERT WITH CHECK (true)`
- `quadro_ideal_select`: `FOR SELECT USING (true)`
- `quadro_ideal_update`: `FOR UPDATE USING (true)`

## quality_checklists

### Finalidade

Descrição inferida pela estrutura: armazena registros relacionados a `quality checklists`. A finalidade de negócio exata deve ser confirmada com a equipe responsável.

### Colunas

| Coluna | Tipo | Obrigatória | Padrão | Observação |
|---|---|---|---|---|
| id | uuid | Sim | gen_random_uuid() | — |
| unit_id | uuid | Sim | — | — |
| nome | text | Sim | — | — |
| area | public.checklist_area | Sim | 'geral'::public.checklist_area | — |
| turno | public.checklist_turno | Sim | 'abertura'::public.checklist_turno | — |
| items | jsonb | Sim | '[]'::jsonb | — |
| ativo | boolean | Sim | true | — |
| created_at | timestamp with time zone | Sim | now() | — |

### Chave primária
- `CONSTRAINT quality_checklists_pkey PRIMARY KEY (id)`

### Relacionamentos
- `quality_checklists_unit_id_fkey`: `unit_id` → `public.units(id)` (ON DELETE CASCADE)

### Constraints

Nenhuma constraint adicional identificada.

### Índices
- `quality_checklists_unit_idx`: `USING btree (unit_id)`

### Triggers

Nenhum trigger associado.

### Políticas RLS

RLS: **habilitada**.
- `unit members can manage checklists`: `USING (public.kph_has_role_for_unit(unit_id)) WITH CHECK (public.kph_has_role_for_unit(unit_id))`

## recebimento_itens

### Finalidade

Descrição inferida pela estrutura: armazena registros relacionados a `recebimento itens`. A finalidade de negócio exata deve ser confirmada com a equipe responsável.

### Colunas

| Coluna | Tipo | Obrigatória | Padrão | Observação |
|---|---|---|---|---|
| id | uuid | Sim | gen_random_uuid() | — |
| recebimento_id | uuid | Sim | — | — |
| pedido_item_id | uuid | Sim | — | — |
| nome | text | Sim | — | — |
| quantidade_pedida | numeric | Sim | — | — |
| quantidade_recebida | numeric | Sim | 0 | — |
| unidade | text | Sim | — | — |
| status | text | Sim | 'ok'::text | — |
| observacao | text | Não | — | — |
| created_at | timestamp with time zone | Sim | now() | — |

### Chave primária
- `CONSTRAINT recebimento_itens_pkey PRIMARY KEY (id)`

### Relacionamentos
- `recebimento_itens_pedido_item_id_fkey`: `pedido_item_id` → `public.purchase_order_items(id)`
- `recebimento_itens_recebimento_id_fkey`: `recebimento_id` → `public.recebimentos(id)` (ON DELETE CASCADE)

### Constraints
- `CONSTRAINT recebimento_itens_status_check CHECK ((status = ANY (ARRAY['ok'::text, 'parcial'::text, 'nao_recebido'::text])))`

### Índices
- `idx_recebimento_itens_recebimento`: `USING btree (recebimento_id)`

### Triggers

Nenhum trigger associado.

### Políticas RLS

RLS: **habilitada**.

Nenhuma política associada.

## recebimentos

### Finalidade

Descrição inferida pela estrutura: armazena registros relacionados a `recebimentos`. A finalidade de negócio exata deve ser confirmada com a equipe responsável.

### Colunas

| Coluna | Tipo | Obrigatória | Padrão | Observação |
|---|---|---|---|---|
| id | uuid | Sim | gen_random_uuid() | — |
| pedido_id | uuid | Sim | — | — |
| unit_id | uuid | Sim | — | — |
| recebido_por | uuid | Sim | — | — |
| observacao | text | Não | — | — |
| created_at | timestamp with time zone | Sim | now() | — |
| status | text | Sim | 'rascunho'::text | — |
| assinatura_nome | text | Não | — | — |

### Chave primária
- `CONSTRAINT recebimentos_pkey PRIMARY KEY (id)`

### Relacionamentos
- `recebimentos_pedido_id_fkey`: `pedido_id` → `public.purchase_orders(id)` (ON DELETE CASCADE)

### Constraints
- `CONSTRAINT recebimentos_status_check CHECK ((status = ANY (ARRAY['rascunho'::text, 'finalizado'::text])))`

### Índices
- `idx_recebimentos_pedido`: `USING btree (pedido_id)`
- `idx_recebimentos_status`: `USING btree (pedido_id, status)`
- `idx_recebimentos_unit`: `USING btree (unit_id, created_at DESC)`

### Triggers

Nenhum trigger associado.

### Políticas RLS

RLS: **habilitada**.

Nenhuma política associada.

## recipe_items

### Finalidade

Descrição inferida pela estrutura: armazena registros relacionados a `recipe items`. A finalidade de negócio exata deve ser confirmada com a equipe responsável.

### Colunas

| Coluna | Tipo | Obrigatória | Padrão | Observação |
|---|---|---|---|---|
| id | uuid | Sim | gen_random_uuid() | — |
| menu_item_id | uuid | Sim | — | — |
| ingredient_id | uuid | Não | — | — |
| insumo | text | Sim | ''::text | — |
| unidade | text | Não | — | — |
| quantidade | numeric(12,4) | Sim | 0 | — |
| custo_unitario | numeric(12,4) | Sim | 0 | — |
| custo_total | numeric(14,4) | Não | GENERATED ALWAYS AS ((quantidade * custo_unitario)) STORED | Coluna gerada |
| perda_pct | numeric(5,2) | Não | 0 | — |
| ordem | integer | Não | 0 | — |
| observacoes | text | Não | — | — |
| created_at | timestamp with time zone | Não | now() | — |
| updated_at | timestamp with time zone | Não | now() | — |

### Chave primária
- `CONSTRAINT recipe_items_pkey PRIMARY KEY (id)`

### Relacionamentos
- `recipe_items_ingredient_id_fkey`: `ingredient_id` → `public.ingredients(id)` (ON DELETE SET NULL)
- `recipe_items_menu_item_id_fkey`: `menu_item_id` → `public.menu_items(id)` (ON DELETE CASCADE)

### Constraints

Nenhuma constraint adicional identificada.

### Índices
- `idx_recipe_items_ingredient`: `USING btree (ingredient_id) WHERE (ingredient_id IS NOT NULL)`
- `idx_recipe_items_menu`: `USING btree (menu_item_id)`
- `recipe_items_menu_item_idx`: `USING btree (menu_item_id)`

### Triggers
- `trg_recipe_items_recalc`: `AFTER INSERT OR DELETE OR UPDATE FOR EACH ROW EXECUTE FUNCTION public.fn_recalc_menu_item_custo()`

### Políticas RLS

RLS: **habilitada**.
- `ri_delete`: `FOR DELETE USING ((menu_item_id IN ( SELECT menu_items.id FROM public.menu_items WHERE public.kph_has_role_for_brand(menu_items.brand_id))))`
- `ri_insert`: `FOR INSERT WITH CHECK ((menu_item_id IN ( SELECT menu_items.id FROM public.menu_items WHERE public.kph_has_role_for_brand(menu_items.brand_id))))`
- `ri_modify`: `USING ((menu_item_id IN ( SELECT menu_items.id FROM public.menu_items WHERE public.kph_has_role_for_brand(menu_items.brand_id)))) WITH CHECK ((menu_item_id IN ( SELECT menu_items.id FROM public.menu_items WHERE public.kph_has_role_for_brand(menu_items.brand_id))))`
- `ri_select`: `FOR SELECT USING ((menu_item_id IN ( SELECT menu_items.id FROM public.menu_items WHERE public.kph_has_role_for_brand(menu_items.brand_id))))`
- `ri_update`: `FOR UPDATE USING ((menu_item_id IN ( SELECT menu_items.id FROM public.menu_items WHERE public.kph_has_role_for_brand(menu_items.brand_id)))) WITH CHECK ((menu_item_id IN ( SELECT menu_items.id FROM public.menu_items WHERE public.kph_has_role_for_brand(menu_items.brand_id))))`

## recipe_notes

### Finalidade

Descrição inferida pela estrutura: armazena registros relacionados a `recipe notes`. A finalidade de negócio exata deve ser confirmada com a equipe responsável.

### Colunas

| Coluna | Tipo | Obrigatória | Padrão | Observação |
|---|---|---|---|---|
| id | uuid | Sim | gen_random_uuid() | — |
| menu_item_id | uuid | Sim | — | — |
| nota | text | Sim | — | — |
| created_by | uuid | Não | — | — |
| created_at | timestamp with time zone | Não | now() | — |

### Chave primária
- `CONSTRAINT recipe_notes_pkey PRIMARY KEY (id)`

### Relacionamentos
- `recipe_notes_created_by_fkey`: `created_by` → `auth.users(id)`
- `recipe_notes_menu_item_id_fkey`: `menu_item_id` → `public.menu_items(id)` (ON DELETE CASCADE)

### Constraints

Nenhuma constraint adicional identificada.

### Índices
- `idx_recipe_notes_menu`: `USING btree (menu_item_id, created_at DESC)`

### Triggers

Nenhum trigger associado.

### Políticas RLS

RLS: **habilitada**.
- `rn_delete`: `FOR DELETE USING (public.kph_is_founder())`
- `rn_insert`: `FOR INSERT WITH CHECK ((menu_item_id IN ( SELECT menu_items.id FROM public.menu_items WHERE public.kph_has_role_for_brand(menu_items.brand_id))))`
- `rn_select`: `FOR SELECT USING ((menu_item_id IN ( SELECT menu_items.id FROM public.menu_items WHERE public.kph_has_role_for_brand(menu_items.brand_id))))`

## relatorio_produtos

### Finalidade

Descrição inferida pela estrutura: armazena registros relacionados a `relatorio produtos`. A finalidade de negócio exata deve ser confirmada com a equipe responsável.

### Colunas

| Coluna | Tipo | Obrigatória | Padrão | Observação |
|---|---|---|---|---|
| id | integer | Sim | — | — |
| unit_id | uuid | Não | — | — |
| fornecedor_codigo | integer | Não | — | — |
| fornecedor_nome | text | Não | — | — |
| nr_danfe | text | Não | — | — |
| v_total_danfe | numeric | Não | — | — |
| dt_emissao | date | Não | — | — |
| item_codigo | text | Não | — | — |
| item_descricao | text | Não | — | — |
| unidade_medida | text | Não | — | — |
| tipo_item | text | Não | — | — |
| q_embalagem | numeric | Não | — | — |
| q_estoque | numeric | Não | — | — |
| v_embalagem | numeric | Não | — | — |
| v_total_embalagem | numeric | Não | — | — |
| v_custo_medio | numeric | Não | — | — |
| v_custo_compra | numeric | Não | — | — |
| v_custo_total | numeric | Não | — | — |
| perc_variacao | numeric | Não | — | — |
| calcula_cmv | boolean | Não | — | — |
| codigo_gerencial | integer | Não | — | — |
| desc_gerencial | text | Não | — | — |
| mes_lancamento | integer | Não | — | — |
| ano_lancamento | integer | Não | — | — |
| created_at | timestamp with time zone | Não | now() | — |

### Chave primária
- `CONSTRAINT relatorio_produtos_pkey PRIMARY KEY (id)`

### Relacionamentos
- `relatorio_produtos_unit_id_fkey`: `unit_id` → `public.units(id)`

### Constraints

Nenhuma constraint adicional identificada.

### Índices
- `relatorio_produtos_calcula_cmv_idx`: `USING btree (calcula_cmv)`
- `relatorio_produtos_desc_gerencial_idx`: `USING btree (desc_gerencial)`
- `relatorio_produtos_mes_lancamento_ano_lancamento_idx`: `USING btree (mes_lancamento, ano_lancamento)`
- `relatorio_produtos_unit_id_idx`: `USING btree (unit_id)`

### Triggers

Nenhum trigger associado.

### Políticas RLS

RLS: **habilitada**.

Nenhuma política associada.

## reservations

### Finalidade

Descrição inferida pela estrutura: armazena registros relacionados a `reservations`. A finalidade de negócio exata deve ser confirmada com a equipe responsável.

### Colunas

| Coluna | Tipo | Obrigatória | Padrão | Observação |
|---|---|---|---|---|
| id | uuid | Sim | gen_random_uuid() | — |
| unit_id | uuid | Sim | — | — |
| data | date | Sim | — | — |
| hora | time without time zone | Sim | — | — |
| pax | integer | Sim | — | — |
| status | public.reservation_status | Sim | 'pendente'::public.reservation_status | — |
| origem | public.reservation_origem | Sim | 'whatsapp'::public.reservation_origem | — |
| cliente_nome | text | Sim | — | — |
| cliente_telefone | text | Não | — | — |
| cliente_email | text | Não | — | — |
| mesa | text | Não | — | — |
| observacoes | text | Não | — | — |
| confirmado_por | uuid | Não | — | — |
| confirmado_em | timestamp with time zone | Não | — | — |
| created_by | uuid | Não | — | — |
| created_at | timestamp with time zone | Sim | now() | — |
| updated_at | timestamp with time zone | Sim | now() | — |

### Chave primária
- `CONSTRAINT reservations_pkey PRIMARY KEY (id)`

### Relacionamentos
- `reservations_confirmado_por_fkey`: `confirmado_por` → `auth.users(id)`
- `reservations_created_by_fkey`: `created_by` → `auth.users(id)`
- `reservations_unit_id_fkey`: `unit_id` → `public.units(id)` (ON DELETE CASCADE)

### Constraints
- `CONSTRAINT reservations_pax_check CHECK ((pax > 0))`

### Índices
- `reservations_unit_data_idx`: `USING btree (unit_id, data)`

### Triggers

Nenhum trigger associado.

### Políticas RLS

RLS: **habilitada**.
- `unit members can insert reservations`: `FOR INSERT WITH CHECK (public.kph_has_role_for_unit(unit_id))`
- `unit members can select reservations`: `FOR SELECT USING (public.kph_has_role_for_unit(unit_id))`
- `unit members can update reservations`: `FOR UPDATE USING (public.kph_has_role_for_unit(unit_id)) WITH CHECK (public.kph_has_role_for_unit(unit_id))`

## reuniao_action_items

### Finalidade

Descrição inferida pela estrutura: armazena registros relacionados a `reuniao action items`. A finalidade de negócio exata deve ser confirmada com a equipe responsável.

### Colunas

| Coluna | Tipo | Obrigatória | Padrão | Observação |
|---|---|---|---|---|
| id | uuid | Sim | gen_random_uuid() | — |
| reuniao_id | uuid | Sim | — | — |
| descricao | text | Sim | — | — |
| responsavel_id | uuid | Não | — | — |
| prazo | date | Não | — | — |
| status | text | Sim | 'pendente'::text | — |
| created_at | timestamp with time zone | Não | now() | — |

### Chave primária
- `CONSTRAINT reuniao_action_items_pkey PRIMARY KEY (id)`

### Relacionamentos
- `reuniao_action_items_responsavel_id_fkey`: `responsavel_id` → `public.employees(id)`
- `reuniao_action_items_reuniao_id_fkey`: `reuniao_id` → `public.reunioes_1on1(id)` (ON DELETE CASCADE)

### Constraints
- `CONSTRAINT reuniao_action_items_status_check CHECK ((status = ANY (ARRAY['pendente'::text, 'concluido'::text, 'cancelado'::text])))`

### Índices
- `action_items_reuniao`: `USING btree (reuniao_id)`
- `idx_action_items_reuniao`: `USING btree (reuniao_id)`

### Triggers

Nenhum trigger associado.

### Políticas RLS

RLS: **habilitada**.
- `action_items_access`: `USING ((reuniao_id IN ( SELECT reunioes_1on1.id FROM public.reunioes_1on1 WHERE (reunioes_1on1.unit_id IN ( SELECT user_roles.unit_id FROM public.user_roles WHERE (user_roles.user_id = auth.uid()))))))`
- `action_items_read`: `FOR SELECT USING ((reuniao_id IN ( SELECT reunioes_1on1.id FROM public.reunioes_1on1)))`
- `action_items_write`: `USING (((reuniao_id IN ( SELECT r.id FROM (public.reunioes_1on1 r JOIN public.employees eg ON (((eg.id = r.gestor_id) AND (eg.user_id = auth.uid())))))) OR (public.get_my_tier() = ANY (ARRAY['T3'::text, 'T4'::text]))))`

## reunioes_1on1

### Finalidade

Descrição inferida pela estrutura: armazena registros relacionados a `reunioes 1on1`. A finalidade de negócio exata deve ser confirmada com a equipe responsável.

### Colunas

| Coluna | Tipo | Obrigatória | Padrão | Observação |
|---|---|---|---|---|
| id | uuid | Sim | gen_random_uuid() | — |
| unit_id | uuid | Sim | — | — |
| gestor_id | uuid | Sim | — | — |
| colaborador_id | uuid | Sim | — | — |
| data_reuniao | timestamp with time zone | Sim | — | — |
| duracao_min | integer | Não | 30 | — |
| status | text | Sim | 'agendada'::text | — |
| notas | text | Não | — | — |
| created_by | uuid | Não | — | — |
| created_at | timestamp with time zone | Não | now() | — |

### Chave primária
- `CONSTRAINT reunioes_1on1_pkey PRIMARY KEY (id)`

### Relacionamentos
- `reunioes_1on1_colaborador_id_fkey`: `colaborador_id` → `public.employees(id)`
- `reunioes_1on1_created_by_fkey`: `created_by` → `auth.users(id)`
- `reunioes_1on1_gestor_id_fkey`: `gestor_id` → `public.employees(id)`
- `reunioes_1on1_unit_id_fkey`: `unit_id` → `public.units(id)`

### Constraints
- `CONSTRAINT reuniao_diferentes CHECK ((gestor_id <> colaborador_id))`
- `CONSTRAINT reunioes_1on1_status_check CHECK ((status = ANY (ARRAY['agendada'::text, 'realizada'::text, 'cancelada'::text])))`

### Índices
- `idx_reunioes_colaborador`: `USING btree (colaborador_id)`
- `idx_reunioes_data`: `USING btree (data_reuniao DESC)`
- `idx_reunioes_gestor`: `USING btree (gestor_id)`
- `reunioes_colaborador`: `USING btree (colaborador_id)`
- `reunioes_data`: `USING btree (data_reuniao)`
- `reunioes_gestor`: `USING btree (gestor_id)`

### Triggers

Nenhum trigger associado.

### Políticas RLS

RLS: **habilitada**.
- `reunioes_read`: `FOR SELECT USING (((gestor_id IN ( SELECT employees.id FROM public.employees WHERE (employees.user_id = auth.uid()))) OR (colaborador_id IN ( SELECT employees.id FROM public.employees WHERE (employees.user_id = auth.uid()))) OR (public.get_my_tier() = ANY (ARRAY['T3'::text, 'T4'::text]))))`
- `reunioes_write_t2`: `USING (((gestor_id IN ( SELECT employees.id FROM public.employees WHERE (employees.user_id = auth.uid()))) OR (public.get_my_tier() = ANY (ARRAY['T3'::text, 'T4'::text]))))`
- `unit_access`: `USING ((unit_id IN ( SELECT user_roles.unit_id FROM public.user_roles WHERE (user_roles.user_id = auth.uid()))))`

## roadmap_items

### Finalidade

Descrição inferida pela estrutura: armazena registros relacionados a `roadmap items`. A finalidade de negócio exata deve ser confirmada com a equipe responsável.

### Colunas

| Coluna | Tipo | Obrigatória | Padrão | Observação |
|---|---|---|---|---|
| id | uuid | Sim | gen_random_uuid() | — |
| title | text | Sim | — | — |
| description | text | Não | — | — |
| sprint | integer | Sim | — | — |
| status | text | Sim | 'backlog'::text | — |
| module | text | Não | — | — |
| created_at | timestamp with time zone | Sim | now() | — |

### Chave primária
- `CONSTRAINT roadmap_items_pkey PRIMARY KEY (id)`

### Relacionamentos

Nenhuma chave estrangeira identificada.

### Constraints
- `CONSTRAINT roadmap_items_status_check CHECK ((status = ANY (ARRAY['backlog'::text, 'in_progress'::text, 'done'::text])))`

### Índices
- `idx_roadmap_sprint`: `USING btree (sprint)`
- `idx_roadmap_status`: `USING btree (status)`

### Triggers

Nenhum trigger associado.

### Políticas RLS

RLS: **habilitada**.
- `manage_roadmap`: `USING (public.kph_is_founder_or_cfo()) WITH CHECK (public.kph_is_founder_or_cfo())`
- `select_roadmap`: `FOR SELECT TO authenticated USING (true)`

## roles

### Finalidade

Descrição inferida pela estrutura: armazena registros relacionados a `roles`. A finalidade de negócio exata deve ser confirmada com a equipe responsável.

### Colunas

| Coluna | Tipo | Obrigatória | Padrão | Observação |
|---|---|---|---|---|
| id | uuid | Sim | gen_random_uuid() | — |
| name | text | Sim | — | — |
| description | text | Não | — | — |
| dept | text | Não | — | — |
| tier | text | Não | — | — |
| level | text | Não | — | — |
| sector | text | Não | — | — |
| permissions | jsonb | Sim | '[]'::jsonb | — |

### Chave primária
- `CONSTRAINT roles_pkey PRIMARY KEY (id)`

### Relacionamentos

Nenhuma chave estrangeira identificada.

### Constraints
- `CONSTRAINT roles_tier_check CHECK ((tier = ANY (ARRAY['T1'::text, 'T2A'::text, 'T2B'::text, 'T3'::text, 'T4'::text, 'T5'::text, 'T6'::text])))`
- `CONSTRAINT roles_name_key UNIQUE (name)`

### Índices

Nenhum índice adicional identificado.

### Triggers

Nenhum trigger associado.

### Políticas RLS

RLS: **habilitada**.
- `roles_mutate`: `TO authenticated USING (public.kph_is_founder()) WITH CHECK (public.kph_is_founder())`
- `roles_select`: `FOR SELECT TO authenticated USING (true)`

## score_events

### Finalidade

Descrição inferida pela estrutura: armazena registros relacionados a `score events`. A finalidade de negócio exata deve ser confirmada com a equipe responsável.

### Colunas

| Coluna | Tipo | Obrigatória | Padrão | Observação |
|---|---|---|---|---|
| id | uuid | Sim | gen_random_uuid() | — |
| employee_id | uuid | Sim | — | — |
| tipo | text | Sim | — | — |
| delta | integer | Sim | — | — |
| descricao | text | Não | — | — |
| referencia_id | uuid | Não | — | — |
| created_at | timestamp with time zone | Não | now() | — |

### Chave primária
- `CONSTRAINT score_events_pkey PRIMARY KEY (id)`

### Relacionamentos
- `score_events_employee_id_fkey`: `employee_id` → `public.employees(id)` (ON DELETE CASCADE)

### Constraints

Nenhuma constraint adicional identificada.

### Índices
- `idx_score_events_employee`: `USING btree (employee_id, created_at DESC)`

### Triggers

Nenhum trigger associado.

### Políticas RLS

RLS: **habilitada**.
- `score_insert`: `FOR INSERT WITH CHECK ((EXISTS ( SELECT 1 FROM public.employees e WHERE ((e.id = score_events.employee_id) AND public.kph_has_role_for_unit(e.unit_id)))))`
- `score_select`: `FOR SELECT USING ((EXISTS ( SELECT 1 FROM public.employees e WHERE ((e.id = score_events.employee_id) AND public.kph_has_role_for_unit(e.unit_id)))))`

## shifts

### Finalidade

Descrição inferida pela estrutura: armazena registros relacionados a `shifts`. A finalidade de negócio exata deve ser confirmada com a equipe responsável.

### Colunas

| Coluna | Tipo | Obrigatória | Padrão | Observação |
|---|---|---|---|---|
| id | uuid | Sim | gen_random_uuid() | — |
| employee_id | uuid | Sim | — | — |
| unit_id | uuid | Sim | — | — |
| data | date | Sim | — | — |
| hora_inicio | time without time zone | Sim | — | — |
| hora_fim | time without time zone | Sim | — | — |
| tipo | text | Não | 'normal'::text | — |
| labor_cost | numeric(10,2) | Não | — | — |
| observacao | text | Não | — | — |
| created_at | timestamp with time zone | Não | now() | — |
| area | text | Não | — | — |

### Chave primária
- `CONSTRAINT shifts_pkey PRIMARY KEY (id)`

### Relacionamentos
- `shifts_employee_id_fkey`: `employee_id` → `public.employees(id)` (ON DELETE CASCADE)
- `shifts_unit_id_fkey`: `unit_id` → `public.units(id)`

### Constraints
- `CONSTRAINT shifts_area_check CHECK (((area IS NULL) OR (area = ANY (ARRAY['Adm'::text, 'Salão'::text, 'Cozinha'::text, 'Limpeza'::text, 'Bar'::text, 'Hostess & Segurança'::text, 'Cozinha de Apoio'::text, 'Estoque'::text]))))`
- `CONSTRAINT shifts_employee_id_data_key UNIQUE (employee_id, data)`

### Índices
- `idx_shifts_employee_data`: `USING btree (employee_id, data)`
- `idx_shifts_unit_data`: `USING btree (unit_id, data)`

### Triggers

Nenhum trigger associado.

### Políticas RLS

RLS: **habilitada**.
- `shifts_all`: `USING (public.kph_has_role_for_unit(unit_id))`
- `shifts_select`: `FOR SELECT USING (public.kph_has_role_for_unit(unit_id))`

## sick_leaves

### Finalidade

Descrição inferida pela estrutura: armazena registros relacionados a `sick leaves`. A finalidade de negócio exata deve ser confirmada com a equipe responsável.

### Colunas

| Coluna | Tipo | Obrigatória | Padrão | Observação |
|---|---|---|---|---|
| id | uuid | Sim | gen_random_uuid() | — |
| unit_id | uuid | Não | — | — |
| employee_id | uuid | Não | — | — |
| nome | text | Não | — | — |
| data_inicio | date | Não | — | — |
| data_fim | date | Não | — | — |
| total_dias | integer | Não | — | — |
| tipo | text | Não | 'atestado'::text | — |
| cid | text | Não | — | — |
| medico | text | Não | — | — |
| documento_ref | text | Não | — | — |
| created_at | timestamp with time zone | Não | now() | — |

### Chave primária
- `CONSTRAINT sick_leaves_pkey PRIMARY KEY (id)`

### Relacionamentos
- `sick_leaves_employee_id_fkey`: `employee_id` → `public.employees(id)`
- `sick_leaves_unit_id_fkey`: `unit_id` → `public.units(id)`

### Constraints

Nenhuma constraint adicional identificada.

### Índices

Nenhum índice adicional identificado.

### Triggers

Nenhum trigger associado.

### Políticas RLS

RLS: **habilitada**.
- `t1_own`: `FOR SELECT USING ((employee_id = ( SELECT employees.id FROM public.employees WHERE (employees.user_id = auth.uid()))))`
- `t3_dept`: `USING ((public.get_my_tier() = 'T3'::text))`
- `t4_master`: `USING ((public.get_my_tier() = 'T4'::text))`

## suppliers

### Finalidade

Descrição inferida pela estrutura: armazena registros relacionados a `suppliers`. A finalidade de negócio exata deve ser confirmada com a equipe responsável.

### Colunas

| Coluna | Tipo | Obrigatória | Padrão | Observação |
|---|---|---|---|---|
| id | uuid | Sim | gen_random_uuid() | — |
| unit_id | uuid | Sim | — | — |
| brand_id | uuid | Sim | — | — |
| nome | text | Sim | — | — |
| cnpj | text | Não | — | — |
| telefone | text | Não | — | — |
| email | text | Não | — | — |
| categoria | text | Não | — | — |
| ativo | boolean | Não | true | — |
| created_at | timestamp with time zone | Não | now() | — |

### Chave primária
- `CONSTRAINT suppliers_pkey PRIMARY KEY (id)`

### Relacionamentos
- `suppliers_brand_id_fkey`: `brand_id` → `public.brands(id)`
- `suppliers_unit_id_fkey`: `unit_id` → `public.units(id)`

### Constraints

Nenhuma constraint adicional identificada.

### Índices
- `idx_suppliers_ativo`: `USING btree (ativo)`
- `idx_suppliers_brand`: `USING btree (brand_id)`
- `idx_suppliers_unit`: `USING btree (unit_id)`

### Triggers

Nenhum trigger associado.

### Políticas RLS

RLS: **habilitada**.
- `suppliers_delete`: `FOR DELETE USING (public.kph_is_founder())`
- `suppliers_insert`: `FOR INSERT WITH CHECK (public.kph_has_role_for_unit(unit_id))`
- `suppliers_select`: `FOR SELECT USING (public.kph_has_role_for_unit(unit_id))`
- `suppliers_update`: `FOR UPDATE USING (public.kph_has_role_for_unit(unit_id)) WITH CHECK (public.kph_has_role_for_unit(unit_id))`

## target_notes

### Finalidade

Descrição inferida pela estrutura: armazena registros relacionados a `target notes`. A finalidade de negócio exata deve ser confirmada com a equipe responsável.

### Colunas

| Coluna | Tipo | Obrigatória | Padrão | Observação |
|---|---|---|---|---|
| id | uuid | Sim | gen_random_uuid() | — |
| target_id | uuid | Sim | — | — |
| nota | text | Sim | — | — |
| created_by | uuid | Não | — | — |
| created_at | timestamp with time zone | Não | now() | — |

### Chave primária
- `CONSTRAINT target_notes_pkey PRIMARY KEY (id)`

### Relacionamentos
- `target_notes_created_by_fkey`: `created_by` → `auth.users(id)`
- `target_notes_target_id_fkey`: `target_id` → `public.brand_targets(id)` (ON DELETE CASCADE)

### Constraints

Nenhuma constraint adicional identificada.

### Índices
- `idx_target_notes_target`: `USING btree (target_id, created_at DESC)`

### Triggers

Nenhum trigger associado.

### Políticas RLS

RLS: **habilitada**.
- `tn_delete`: `FOR DELETE USING (public.kph_is_founder())`
- `tn_insert`: `FOR INSERT WITH CHECK ((target_id IN ( SELECT brand_targets.id FROM public.brand_targets WHERE public.kph_has_role_for_brand(brand_targets.brand_id))))`
- `tn_select`: `FOR SELECT USING ((target_id IN ( SELECT brand_targets.id FROM public.brand_targets WHERE public.kph_has_role_for_brand(brand_targets.brand_id))))`

## task_assignees

### Finalidade

Descrição inferida pela estrutura: armazena registros relacionados a `task assignees`. A finalidade de negócio exata deve ser confirmada com a equipe responsável.

### Colunas

| Coluna | Tipo | Obrigatória | Padrão | Observação |
|---|---|---|---|---|
| task_id | uuid | Sim | — | — |
| member_id | uuid | Sim | — | — |

### Chave primária
- `CONSTRAINT task_assignees_pkey PRIMARY KEY (task_id, member_id)`

### Relacionamentos
- `task_assignees_member_id_fkey`: `member_id` → `public.team_members(id)` (ON DELETE CASCADE)
- `task_assignees_task_id_fkey`: `task_id` → `public.tasks(id)` (ON DELETE CASCADE)

### Constraints

Nenhuma constraint adicional identificada.

### Índices

Nenhum índice adicional identificado.

### Triggers

Nenhum trigger associado.

### Políticas RLS

RLS: **não habilitada no dump**.

Nenhuma política associada.

## tasks

### Finalidade

Descrição inferida pela estrutura: armazena registros relacionados a `tasks`. A finalidade de negócio exata deve ser confirmada com a equipe responsável.

### Colunas

| Coluna | Tipo | Obrigatória | Padrão | Observação |
|---|---|---|---|---|
| id | uuid | Sim | gen_random_uuid() | — |
| project_id | uuid | Sim | — | — |
| title | text | Sim | — | — |
| description | text | Não | — | — |
| due_date | date | Não | — | — |
| status | text | Sim | 'Não iniciado'::text | — |
| bucket_id | uuid | Não | — | — |
| start_date | date | Não | — | — |
| label_text | text | Não | — | — |
| label_color | text | Não | — | — |
| priority | text | Não | 'Média'::text | — |

### Chave primária
- `CONSTRAINT tasks_pkey PRIMARY KEY (id)`

### Relacionamentos
- `tasks_bucket_id_fkey`: `bucket_id` → `public.buckets(id)` (ON DELETE CASCADE)
- `tasks_project_id_fkey`: `project_id` → `public.projects(id)` (ON DELETE CASCADE)

### Constraints
- `CONSTRAINT tasks_priority_check CHECK ((priority = ANY (ARRAY['Baixa'::text, 'Média'::text, 'Alta'::text, 'Urgente'::text])))`
- `CONSTRAINT tasks_status_check CHECK ((status = ANY (ARRAY['Não iniciado'::text, 'Em andamento'::text, 'Concluído'::text])))`

### Índices

Nenhum índice adicional identificado.

### Triggers

Nenhum trigger associado.

### Políticas RLS

RLS: **não habilitada no dump**.

Nenhuma política associada.

## team_members

### Finalidade

Descrição inferida pela estrutura: armazena registros relacionados a `team members`. A finalidade de negócio exata deve ser confirmada com a equipe responsável.

### Colunas

| Coluna | Tipo | Obrigatória | Padrão | Observação |
|---|---|---|---|---|
| id | uuid | Sim | gen_random_uuid() | — |
| name | text | Sim | — | — |
| role | text | Sim | — | — |

### Chave primária
- `CONSTRAINT team_members_pkey PRIMARY KEY (id)`

### Relacionamentos

Nenhuma chave estrangeira identificada.

### Constraints

Nenhuma constraint adicional identificada.

### Índices

Nenhum índice adicional identificado.

### Triggers

Nenhum trigger associado.

### Políticas RLS

RLS: **não habilitada no dump**.

Nenhuma política associada.

## terminations

### Finalidade

Descrição inferida pela estrutura: armazena registros relacionados a `terminations`. A finalidade de negócio exata deve ser confirmada com a equipe responsável.

### Colunas

| Coluna | Tipo | Obrigatória | Padrão | Observação |
|---|---|---|---|---|
| id | uuid | Sim | gen_random_uuid() | — |
| unit_id | uuid | Não | — | — |
| employee_id | uuid | Não | — | — |
| nome | text | Não | — | — |
| tipo_aviso | text | Não | — | — |
| data_aviso | date | Não | — | — |
| motivo | text | Não | — | — |
| status | text | Não | 'registrado'::text | — |
| created_at | timestamp with time zone | Não | now() | — |

### Chave primária
- `CONSTRAINT terminations_pkey PRIMARY KEY (id)`

### Relacionamentos
- `terminations_employee_id_fkey`: `employee_id` → `public.employees(id)`
- `terminations_unit_id_fkey`: `unit_id` → `public.units(id)`

### Constraints
- `CONSTRAINT terminations_employee_id_tipo_aviso_data_aviso_key UNIQUE (employee_id, tipo_aviso, data_aviso)`

### Índices

Nenhum índice adicional identificado.

### Triggers

Nenhum trigger associado.

### Políticas RLS

RLS: **habilitada**.
- `t3_dept`: `USING ((public.get_my_tier() = 'T3'::text))`
- `t4_master`: `USING ((public.get_my_tier() = 'T4'::text))`

## theo_tickets

### Finalidade

Descrição inferida pela estrutura: armazena registros relacionados a `theo tickets`. A finalidade de negócio exata deve ser confirmada com a equipe responsável.

### Colunas

| Coluna | Tipo | Obrigatória | Padrão | Observação |
|---|---|---|---|---|
| id | uuid | Sim | gen_random_uuid() | — |
| employee_id | uuid | Não | — | — |
| categoria | text | Sim | — | — |
| descricao | text | Não | — | — |
| status | text | Sim | 'aberto'::text | — |
| created_at | timestamp with time zone | Não | now() | — |
| updated_at | timestamp with time zone | Não | now() | — |

### Chave primária
- `CONSTRAINT theo_tickets_pkey PRIMARY KEY (id)`

### Relacionamentos
- `theo_tickets_employee_id_fkey`: `employee_id` → `public.employees(id)` (ON DELETE SET NULL)

### Constraints

Nenhuma constraint adicional identificada.

### Índices
- `idx_theo_tickets_employee`: `USING btree (employee_id)`
- `idx_theo_tickets_status`: `USING btree (status)`

### Triggers

Nenhum trigger associado.

### Políticas RLS

RLS: **habilitada**.
- `theo_tickets_select`: `FOR SELECT TO authenticated USING ((public.kph_is_founder() OR (EXISTS ( SELECT 1 FROM public.employees e WHERE ((e.id = theo_tickets.employee_id) AND public.kph_has_role_for_unit(e.unit_id))))))`

## time_bank_balance

### Finalidade

Descrição inferida pela estrutura: armazena registros relacionados a `time bank balance`. A finalidade de negócio exata deve ser confirmada com a equipe responsável.

### Colunas

| Coluna | Tipo | Obrigatória | Padrão | Observação |
|---|---|---|---|---|
| id | uuid | Sim | gen_random_uuid() | — |
| employee_id | uuid | Sim | — | — |
| saldo_minutos | integer | Não | 0 | — |
| ultimo_calculo | date | Não | — | — |
| updated_at | timestamp with time zone | Não | now() | — |
| source | text | Não | 'kph'::text | — |
| observacao | text | Não | — | — |

### Chave primária
- `CONSTRAINT time_bank_balance_pkey PRIMARY KEY (id)`

### Relacionamentos
- `time_bank_balance_employee_id_fkey`: `employee_id` → `public.employees(id)` (ON DELETE CASCADE)

### Constraints
- `CONSTRAINT time_bank_balance_employee_id_key UNIQUE (employee_id)`

### Índices

Nenhum índice adicional identificado.

### Triggers

Nenhum trigger associado.

### Políticas RLS

RLS: **habilitada**.

Nenhuma política associada.

## time_clock_punches

### Finalidade

Descrição inferida pela estrutura: armazena registros relacionados a `time clock punches`. A finalidade de negócio exata deve ser confirmada com a equipe responsável.

### Colunas

| Coluna | Tipo | Obrigatória | Padrão | Observação |
|---|---|---|---|---|
| id | uuid | Sim | gen_random_uuid() | — |
| employee_id | uuid | Sim | — | — |
| tipo | text | Sim | — | — |
| timestamp_punch | timestamp with time zone | Sim | now() | — |
| latitude | numeric(10,7) | Não | — | — |
| longitude | numeric(10,7) | Não | — | — |
| device_info | text | Não | — | — |
| aprovado | boolean | Não | — | — |
| created_at | timestamp with time zone | Não | now() | — |
| distance_meters | integer | Não | — | — |
| aprovado_por | uuid | Não | — | — |
| gps_failed | boolean | Não | false | — |

### Chave primária
- `CONSTRAINT time_clock_punches_pkey PRIMARY KEY (id)`

### Relacionamentos
- `time_clock_punches_aprovado_por_fkey`: `aprovado_por` → `public.employees(id)`
- `time_clock_punches_employee_id_fkey`: `employee_id` → `public.employees(id)` (ON DELETE CASCADE)

### Constraints

Nenhuma constraint adicional identificada.

### Índices
- `idx_punches_employee`: `USING btree (employee_id, timestamp_punch DESC)`

### Triggers

Nenhum trigger associado.

### Políticas RLS

RLS: **habilitada**.
- `punches_delete`: `FOR DELETE TO authenticated USING ((public.get_my_tier() = ANY (ARRAY['T3'::text, 'T4'::text])))`
- `punches_insert`: `FOR INSERT TO authenticated WITH CHECK (((public.get_my_tier() = ANY (ARRAY['T3'::text, 'T4'::text])) OR ((public.get_my_tier() = ANY (ARRAY['T2A'::text, 'T2B'::text])) AND (employee_id IN ( SELECT employees.id FROM public.employees WHERE (employees.unit_id = public.get_my_unit())))) OR (employee_id IN ( SELECT employees.id FROM public.employees WHERE (employees.user_id = auth.uid())))))`
- `punches_select`: `FOR SELECT TO authenticated USING (((public.get_my_tier() = ANY (ARRAY['T3'::text, 'T4'::text])) OR ((public.get_my_tier() = ANY (ARRAY['T2A'::text, 'T2B'::text])) AND (employee_id IN ( SELECT employees.id FROM public.employees WHERE (employees.unit_id = public.get_my_unit())))) OR (employee_id IN ( SELECT employees.id FROM public.employees WHERE (employees.user_id = auth.uid())))))`
- `punches_self_select`: `FOR SELECT TO authenticated USING ((employee_id IN ( SELECT employees.id FROM public.employees WHERE (employees.user_id = auth.uid()))))`
- `punches_update`: `FOR UPDATE TO authenticated USING ((public.get_my_tier() = ANY (ARRAY['T2A'::text, 'T2B'::text, 'T3'::text, 'T4'::text])))`

## time_records

### Finalidade

Descrição inferida pela estrutura: armazena registros relacionados a `time records`. A finalidade de negócio exata deve ser confirmada com a equipe responsável.

### Colunas

| Coluna | Tipo | Obrigatória | Padrão | Observação |
|---|---|---|---|---|
| id | uuid | Sim | gen_random_uuid() | — |
| employee_id | uuid | Sim | — | — |
| unit_id | uuid | Sim | — | — |
| periodo | text | Sim | — | — |
| horas_previstas | text | Não | — | — |
| horas_trabalhadas | text | Não | — | — |
| banco_horas_positivo | text | Não | — | — |
| banco_horas_negativo | text | Não | — | — |
| saldo_banco | text | Não | — | — |
| banco_horas_acumulado | text | Não | — | — |
| faltas_injustificadas_dias | integer | Não | 0 | — |
| atestado_horas | text | Não | — | — |
| afastamentos_dias | integer | Não | 0 | — |
| ferias_dias | integer | Não | 0 | — |
| adicional_noturno | text | Não | — | — |
| fonte | text | Não | 'totvs'::text | — |
| notes | text | Não | — | — |
| created_at | timestamp with time zone | Não | now() | — |

### Chave primária
- `CONSTRAINT time_records_pkey PRIMARY KEY (id)`

### Relacionamentos
- `time_records_employee_id_fkey`: `employee_id` → `public.employees(id)` (ON DELETE CASCADE)
- `time_records_unit_id_fkey`: `unit_id` → `public.units(id)`

### Constraints

Nenhuma constraint adicional identificada.

### Índices
- `idx_time_records_employee_periodo`: `USING btree (employee_id, periodo)`

### Triggers

Nenhum trigger associado.

### Políticas RLS

RLS: **habilitada**.
- `time_records_delete`: `FOR DELETE USING (public.kph_is_founder())`
- `time_records_insert`: `FOR INSERT WITH CHECK (public.kph_has_role_for_unit(unit_id))`
- `time_records_select`: `FOR SELECT USING ((EXISTS ( SELECT 1 FROM public.employees e WHERE ((e.id = time_records.employee_id) AND public.kph_has_role_for_unit(e.unit_id)))))`
- `time_records_update`: `FOR UPDATE USING (public.kph_has_role_for_unit(unit_id))`

## titulo_override

### Finalidade

Descrição inferida pela estrutura: armazena registros relacionados a `titulo override`. A finalidade de negócio exata deve ser confirmada com a equipe responsável.

### Colunas

| Coluna | Tipo | Obrigatória | Padrão | Observação |
|---|---|---|---|---|
| id | uuid | Sim | gen_random_uuid() | — |
| titulo_id | text | Sim | — | — |
| linha_dre_corrigida | text | Não | — | — |
| observacao | text | Não | — | — |
| criado_em | timestamp with time zone | Não | now() | — |

### Chave primária
- `CONSTRAINT titulo_override_pkey PRIMARY KEY (id)`

### Relacionamentos

Nenhuma chave estrangeira identificada.

### Constraints
- `CONSTRAINT titulo_override_titulo_id_key UNIQUE (titulo_id)`

### Índices
- `idx_titulo_override_titulo`: `USING btree (titulo_id)`

### Triggers

Nenhum trigger associado.

### Políticas RLS

RLS: **habilitada**.
- `titulo_override_manage`: `TO service_role USING (true) WITH CHECK (true)`
- `titulo_override_read`: `FOR SELECT TO authenticated, anon USING (true)`

## titulos_a_pagar

### Finalidade

Descrição inferida pela estrutura: armazena registros relacionados a `titulos a pagar`. A finalidade de negócio exata deve ser confirmada com a equipe responsável.

### Colunas

| Coluna | Tipo | Obrigatória | Padrão | Observação |
|---|---|---|---|---|
| id | text | Sim | — | — |
| tipo | text | Não | — | — |
| n_nota_fiscal | text | Não | — | — |
| fantasia_fornecedor | text | Não | — | — |
| razao_fornecedor | text | Não | — | — |
| cnpj_cpf_fornecedor | text | Não | — | — |
| t_fornecedor | text | Não | — | — |
| descricao_c_gerencial | text | Não | — | — |
| n_titulo | text | Não | — | — |
| parcela | text | Não | — | — |
| portador | text | Não | — | — |
| d_lancamento | date | Não | — | — |
| d_competencia | date | Não | — | — |
| d_vencimento | date | Não | — | — |
| v_titulo | numeric | Não | — | — |
| v_saldo_atual | numeric | Não | — | — |
| dias_atraso_atual | integer | Não | — | — |
| situacao_atual | text | Não | — | — |
| tipo_sep | text | Não | — | — |
| fluxo_de_caixa | boolean | Não | false | — |
| importado_em | timestamp with time zone | Não | now() | — |
| ref_mes | date | Não | — | — |
| origem | text | Não | — | — |
| empresa | text | Não | — | — |
| fantasia_empresa | text | Não | — | — |
| fornecedor | text | Não | — | — |
| n_conta | text | Não | — | — |
| grupo_economico | text | Não | — | — |
| cep | text | Não | — | — |
| bairro | text | Não | — | — |
| cidade | text | Não | — | — |
| uf | text | Não | — | — |
| pais | text | Não | — | — |
| condicao_compra | text | Não | — | — |
| prazo_medio | numeric | Não | — | — |
| serie | text | Não | — | — |
| documento | text | Não | — | — |
| portador_num | text | Não | — | — |
| c_gerencial | text | Não | — | — |
| d_autorizacao_pgto | date | Não | — | — |
| dia_semana | text | Não | — | — |
| v_desconto | numeric | Não | — | — |
| v_multa_atraso | numeric | Não | — | — |
| v_juros_dia | numeric | Não | — | — |
| v_original | numeric | Não | — | — |
| v_saldo_anterior | numeric | Não | — | — |
| v_credito_periodo | numeric | Não | — | — |
| v_debito_periodo | numeric | Não | — | — |
| d_liquidacao_periodo | date | Não | — | — |
| situacao_periodo | text | Não | — | — |
| v_saldo_periodo | numeric | Não | — | — |
| dias_atraso_periodo | numeric | Não | — | — |
| v_atraso_periodo | numeric | Não | — | — |
| v_atualizado_periodo | numeric | Não | — | — |
| d_liquidacao_atual | date | Não | — | — |
| v_atraso_atual | numeric | Não | — | — |
| v_atualizado_atual | numeric | Não | — | — |
| ano | numeric | Não | — | — |
| mes | text | Não | — | — |
| semana | numeric | Não | — | — |
| trimestre | numeric | Não | — | — |
| quadrimestre | numeric | Não | — | — |

### Chave primária
- `CONSTRAINT titulos_a_pagar_pkey PRIMARY KEY (id)`

### Relacionamentos

Nenhuma chave estrangeira identificada.

### Constraints

Nenhuma constraint adicional identificada.

### Índices

Nenhum índice adicional identificado.

### Triggers

Nenhum trigger associado.

### Políticas RLS

RLS: **não habilitada no dump**.

Nenhuma política associada.

## training_participants

### Finalidade

Descrição inferida pela estrutura: armazena registros relacionados a `training participants`. A finalidade de negócio exata deve ser confirmada com a equipe responsável.

### Colunas

| Coluna | Tipo | Obrigatória | Padrão | Observação |
|---|---|---|---|---|
| id | uuid | Sim | gen_random_uuid() | — |
| training_id | uuid | Não | — | — |
| employee_id | uuid | Não | — | — |
| status | text | Não | 'inscrito'::text | — |
| nota | numeric | Não | — | — |
| certificado_url | text | Não | — | — |
| created_at | timestamp with time zone | Não | now() | — |

### Chave primária
- `CONSTRAINT training_participants_pkey PRIMARY KEY (id)`

### Relacionamentos
- `training_participants_employee_id_fkey`: `employee_id` → `public.employees(id)`
- `training_participants_training_id_fkey`: `training_id` → `public.trainings(id)` (ON DELETE CASCADE)

### Constraints

Nenhuma constraint adicional identificada.

### Índices

Nenhum índice adicional identificado.

### Triggers

Nenhum trigger associado.

### Políticas RLS

RLS: **habilitada**.

Nenhuma política associada.

## training_records

### Finalidade

Descrição inferida pela estrutura: armazena registros relacionados a `training records`. A finalidade de negócio exata deve ser confirmada com a equipe responsável.

### Colunas

| Coluna | Tipo | Obrigatória | Padrão | Observação |
|---|---|---|---|---|
| id | uuid | Sim | gen_random_uuid() | — |
| employee_id | uuid | Sim | — | — |
| template_id | uuid | Sim | — | — |
| status | text | Sim | 'pendente'::text | — |
| data_inicio | date | Não | — | — |
| data_conclusao | date | Não | — | — |
| validade_dias_snapshot | integer | Não | — | — |
| validade_ate | date | Não | GENERATED ALWAYS AS ( CASE WHEN ((data_conclusao IS NULL) OR (validade_dias_snapshot IS NULL)) THEN NULL::date ELSE (data_conclusao + validade_dias_snapshot) END) STORED | Coluna gerada |
| observacoes | text | Não | — | — |
| created_by | uuid | Não | — | — |
| created_at | timestamp with time zone | Não | now() | — |
| updated_at | timestamp with time zone | Não | now() | — |

### Chave primária
- `CONSTRAINT training_records_pkey PRIMARY KEY (id)`

### Relacionamentos
- `training_records_created_by_fkey`: `created_by` → `auth.users(id)`
- `training_records_employee_id_fkey`: `employee_id` → `public.employees(id)` (ON DELETE CASCADE)
- `training_records_template_id_fkey`: `template_id` → `public.training_templates(id)`

### Constraints
- `CONSTRAINT training_records_status_check CHECK ((status = ANY (ARRAY['pendente'::text, 'em_andamento'::text, 'concluido'::text, 'vencido'::text])))`
- `CONSTRAINT training_records_employee_id_template_id_key UNIQUE (employee_id, template_id)`

### Índices
- `idx_training_records_emp`: `USING btree (employee_id)`
- `idx_training_records_employee`: `USING btree (employee_id)`
- `idx_training_records_status`: `USING btree (status)`
- `idx_training_records_template`: `USING btree (template_id)`
- `idx_training_records_tmpl`: `USING btree (template_id)`
- `idx_training_records_validade`: `USING btree (validade_ate)`

### Triggers
- `trg_training_records_updated_at`: `BEFORE UPDATE FOR EACH ROW EXECUTE FUNCTION public.update_updated_at_column()`

### Políticas RLS

RLS: **habilitada**.
- `tr_delete`: `FOR DELETE USING (public.kph_is_founder())`
- `tr_insert`: `FOR INSERT WITH CHECK ((EXISTS ( SELECT 1 FROM public.employees e WHERE ((e.id = training_records.employee_id) AND public.kph_has_role_for_unit(e.unit_id)))))`
- `tr_select`: `FOR SELECT USING ((EXISTS ( SELECT 1 FROM public.employees e WHERE ((e.id = training_records.employee_id) AND public.kph_has_role_for_unit(e.unit_id)))))`
- `tr_update`: `FOR UPDATE USING ((EXISTS ( SELECT 1 FROM public.employees e WHERE ((e.id = training_records.employee_id) AND public.kph_has_role_for_unit(e.unit_id))))) WITH CHECK ((EXISTS ( SELECT 1 FROM public.employees e WHERE ((e.id = training_records.employee_id) AND public.kph_has_role_for_unit(e.unit_id)))))`
- `training_records_read`: `FOR SELECT USING (((employee_id IN ( SELECT employees.id FROM public.employees WHERE (employees.user_id = auth.uid()))) OR (public.get_my_tier() = ANY (ARRAY['T3'::text, 'T4'::text]))))`
- `training_records_write`: `USING ((public.get_my_tier() = ANY (ARRAY['T3'::text, 'T4'::text])))`

## training_templates

### Finalidade

Descrição inferida pela estrutura: armazena registros relacionados a `training templates`. A finalidade de negócio exata deve ser confirmada com a equipe responsável.

### Colunas

| Coluna | Tipo | Obrigatória | Padrão | Observação |
|---|---|---|---|---|
| id | uuid | Sim | gen_random_uuid() | — |
| brand_id | uuid | Sim | — | — |
| unit_id | uuid | Não | — | — |
| nome | text | Sim | — | — |
| descricao | text | Não | — | — |
| funcao | text | Não | — | — |
| obrigatorio | boolean | Não | false | — |
| validade_dias | integer | Não | — | — |
| ativo | boolean | Não | true | — |
| created_by | uuid | Não | — | — |
| created_at | timestamp with time zone | Não | now() | — |
| updated_at | timestamp with time zone | Não | now() | — |

### Chave primária
- `CONSTRAINT training_templates_pkey PRIMARY KEY (id)`

### Relacionamentos
- `training_templates_brand_id_fkey`: `brand_id` → `public.brands(id)`
- `training_templates_created_by_fkey`: `created_by` → `auth.users(id)`
- `training_templates_unit_id_fkey`: `unit_id` → `public.units(id)`

### Constraints

Nenhuma constraint adicional identificada.

### Índices
- `idx_training_templates_brand`: `USING btree (brand_id)`
- `idx_training_templates_funcao`: `USING btree (funcao)`
- `idx_training_templates_unit`: `USING btree (unit_id)`
- `idx_training_tmpl_brand`: `USING btree (brand_id)`

### Triggers
- `trg_training_templates_updated_at`: `BEFORE UPDATE FOR EACH ROW EXECUTE FUNCTION public.update_updated_at_column()`

### Políticas RLS

RLS: **habilitada**.
- `training_templates_read`: `FOR SELECT USING (true)`
- `training_templates_write`: `USING ((public.get_my_tier() = ANY (ARRAY['T3'::text, 'T4'::text])))`
- `tt_delete`: `FOR DELETE USING (public.kph_is_founder())`
- `tt_insert`: `FOR INSERT WITH CHECK (public.kph_has_role_for_brand(brand_id))`
- `tt_select`: `FOR SELECT USING (public.kph_has_role_for_brand(brand_id))`
- `tt_update`: `FOR UPDATE USING (public.kph_has_role_for_brand(brand_id)) WITH CHECK (public.kph_has_role_for_brand(brand_id))`

## trainings

### Finalidade

Descrição inferida pela estrutura: armazena registros relacionados a `trainings`. A finalidade de negócio exata deve ser confirmada com a equipe responsável.

### Colunas

| Coluna | Tipo | Obrigatória | Padrão | Observação |
|---|---|---|---|---|
| id | uuid | Sim | gen_random_uuid() | — |
| unit_id | uuid | Não | — | — |
| titulo | text | Sim | — | — |
| descricao | text | Não | — | — |
| tipo | text | Não | 'interno'::text | — |
| carga_horaria | numeric | Não | — | — |
| data_inicio | date | Não | — | — |
| data_fim | date | Não | — | — |
| instrutor | text | Não | — | — |
| status | text | Não | 'agendado'::text | — |
| created_at | timestamp with time zone | Não | now() | — |

### Chave primária
- `CONSTRAINT trainings_pkey PRIMARY KEY (id)`

### Relacionamentos
- `trainings_unit_id_fkey`: `unit_id` → `public.units(id)`

### Constraints

Nenhuma constraint adicional identificada.

### Índices

Nenhum índice adicional identificado.

### Triggers

Nenhum trigger associado.

### Políticas RLS

RLS: **habilitada**.

Nenhuma política associada.

## transport_vouchers

### Finalidade

Descrição inferida pela estrutura: armazena registros relacionados a `transport vouchers`. A finalidade de negócio exata deve ser confirmada com a equipe responsável.

### Colunas

| Coluna | Tipo | Obrigatória | Padrão | Observação |
|---|---|---|---|---|
| id | uuid | Sim | gen_random_uuid() | — |
| employee_id | uuid | Sim | — | — |
| unit_id | uuid | Sim | — | — |
| periodo | text | Sim | — | — |
| dias_uteis | integer | Não | — | — |
| valor_diario | numeric(10,2) | Não | — | — |
| total_bruto | numeric(10,2) | Não | — | — |
| desconto_funcionario | numeric(10,2) | Não | — | — |
| valor_empresa | numeric(10,2) | Não | — | — |
| operadora | text | Não | — | — |
| observacoes | text | Não | — | — |
| created_at | timestamp with time zone | Não | now() | — |

### Chave primária
- `CONSTRAINT transport_vouchers_pkey PRIMARY KEY (id)`

### Relacionamentos
- `transport_vouchers_employee_id_fkey`: `employee_id` → `public.employees(id)` (ON DELETE CASCADE)
- `transport_vouchers_unit_id_fkey`: `unit_id` → `public.units(id)`

### Constraints
- `CONSTRAINT transport_vouchers_employee_id_periodo_key UNIQUE (employee_id, periodo)`

### Índices
- `idx_vt_employee_periodo`: `USING btree (employee_id, periodo)`

### Triggers

Nenhum trigger associado.

### Políticas RLS

RLS: **habilitada**.
- `vt_delete`: `FOR DELETE USING (public.kph_is_founder())`
- `vt_insert`: `FOR INSERT WITH CHECK (public.kph_has_role_for_unit(unit_id))`
- `vt_select`: `FOR SELECT USING ((EXISTS ( SELECT 1 FROM public.employees e WHERE ((e.id = transport_vouchers.employee_id) AND public.kph_has_role_for_unit(e.unit_id)))))`
- `vt_update`: `FOR UPDATE USING (public.kph_has_role_for_unit(unit_id))`

## uniforms

### Finalidade

Descrição inferida pela estrutura: armazena registros relacionados a `uniforms`. A finalidade de negócio exata deve ser confirmada com a equipe responsável.

### Colunas

| Coluna | Tipo | Obrigatória | Padrão | Observação |
|---|---|---|---|---|
| id | uuid | Sim | gen_random_uuid() | — |
| unit_id | uuid | Não | — | — |
| employee_id | uuid | Não | — | — |
| nome | text | Não | — | — |
| item | text | Não | — | — |
| tamanho | text | Não | — | — |
| quantidade | integer | Não | — | — |
| data_entrega | date | Não | — | — |
| created_at | timestamp with time zone | Não | now() | — |

### Chave primária
- `CONSTRAINT uniforms_pkey PRIMARY KEY (id)`

### Relacionamentos
- `uniforms_employee_id_fkey`: `employee_id` → `public.employees(id)`
- `uniforms_unit_id_fkey`: `unit_id` → `public.units(id)`

### Constraints

Nenhuma constraint adicional identificada.

### Índices

Nenhum índice adicional identificado.

### Triggers

Nenhum trigger associado.

### Políticas RLS

RLS: **habilitada**.
- `t3_dept`: `USING ((public.get_my_tier() = 'T3'::text))`
- `t4_master`: `USING ((public.get_my_tier() = 'T4'::text))`

## units

### Finalidade

Descrição inferida pela estrutura: armazena registros relacionados a `units`. A finalidade de negócio exata deve ser confirmada com a equipe responsável.

### Colunas

| Coluna | Tipo | Obrigatória | Padrão | Observação |
|---|---|---|---|---|
| id | uuid | Sim | gen_random_uuid() | — |
| brand_id | uuid | Não | — | — |
| name | text | Sim | — | — |
| address | text | Não | — | — |
| whatsapp_number | text | Não | — | — |
| active | boolean | Não | true | — |
| created_at | timestamp with time zone | Não | now() | — |
| cnpj | text | Não | — | — |
| latitude | numeric(10,7) | Não | — | — |
| longitude | numeric(10,7) | Não | — | — |
| geofence_radius_m | integer | Não | 200 | — |

### Chave primária
- `CONSTRAINT units_pkey PRIMARY KEY (id)`

### Relacionamentos
- `units_brand_id_fkey`: `brand_id` → `public.brands(id)` (ON DELETE CASCADE)

### Constraints

Nenhuma constraint adicional identificada.

### Índices
- `idx_units_brand`: `USING btree (brand_id)`

### Triggers

Nenhum trigger associado.

### Políticas RLS

RLS: **habilitada**.
- `units_delete`: `FOR DELETE TO authenticated USING (public.kph_is_founder())`
- `units_insert`: `FOR INSERT TO authenticated WITH CHECK (public.kph_is_founder())`
- `units_select`: `FOR SELECT TO authenticated USING (public.kph_has_role_for_unit(id))`
- `units_update`: `FOR UPDATE TO authenticated USING ((public.kph_is_founder() OR (EXISTS ( SELECT 1 FROM (public.user_roles ur JOIN public.roles r ON ((r.id = ur.role_id))) WHERE ((ur.user_id = auth.uid()) AND (ur.unit_id = units.id) AND (r.name = ANY (ARRAY['founder'::text, 'gm'::text]))))))) WITH CHECK ((public.kph_is_founder() OR (EXISTS ( SELECT 1 FROM (public.user_roles ur JOIN public.roles r ON ((r.id = ur.role_id))) WHERE ((ur.user_id = auth.uid()) AND (ur.unit_id = units.id) AND (r.name = ANY (ARRAY['founder'::text, 'gm'::text])))))))`

## user_roles

### Finalidade

Descrição inferida pela estrutura: armazena registros relacionados a `user roles`. A finalidade de negócio exata deve ser confirmada com a equipe responsável.

### Colunas

| Coluna | Tipo | Obrigatória | Padrão | Observação |
|---|---|---|---|---|
| id | uuid | Sim | gen_random_uuid() | — |
| user_id | uuid | Sim | — | — |
| role_id | uuid | Sim | — | — |
| unit_id | uuid | Não | — | — |
| brand_id | uuid | Não | — | — |
| group_id | uuid | Não | — | — |
| created_at | timestamp with time zone | Não | now() | — |

### Chave primária
- `CONSTRAINT user_roles_pkey PRIMARY KEY (id)`

### Relacionamentos
- `user_roles_brand_id_fkey`: `brand_id` → `public.brands(id)` (ON DELETE CASCADE)
- `user_roles_group_id_fkey`: `group_id` → `public.groups(id)` (ON DELETE CASCADE)
- `user_roles_role_id_fkey`: `role_id` → `public.roles(id)`
- `user_roles_unit_id_fkey`: `unit_id` → `public.units(id)` (ON DELETE CASCADE)
- `user_roles_user_id_fkey`: `user_id` → `auth.users(id)` (ON DELETE CASCADE)

### Constraints
- `CONSTRAINT user_roles_check CHECK (((unit_id IS NOT NULL) OR (brand_id IS NOT NULL) OR (group_id IS NOT NULL)))`
- `CONSTRAINT user_roles_user_id_role_id_unit_id_key UNIQUE (user_id, role_id, unit_id)`

### Índices
- `idx_user_roles_brand`: `USING btree (brand_id)`
- `idx_user_roles_unit`: `USING btree (unit_id)`
- `idx_user_roles_user`: `USING btree (user_id)`

### Triggers

Nenhum trigger associado.

### Políticas RLS

RLS: **habilitada**.
- `user_roles_delete`: `FOR DELETE TO authenticated USING (public.kph_is_founder())`
- `user_roles_insert`: `FOR INSERT TO authenticated WITH CHECK (public.kph_is_founder())`
- `user_roles_select`: `FOR SELECT TO authenticated USING (((user_id = auth.uid()) OR public.kph_is_founder()))`
- `user_roles_update`: `FOR UPDATE TO authenticated USING (public.kph_is_founder()) WITH CHECK (public.kph_is_founder())`

## vacation_schedules

### Finalidade

Descrição inferida pela estrutura: armazena registros relacionados a `vacation schedules`. A finalidade de negócio exata deve ser confirmada com a equipe responsável.

### Colunas

| Coluna | Tipo | Obrigatória | Padrão | Observação |
|---|---|---|---|---|
| id | uuid | Sim | gen_random_uuid() | — |
| unit_id | uuid | Não | — | — |
| employee_id | uuid | Não | — | — |
| nome | text | Não | — | — |
| total_dias | integer | Não | — | — |
| data_inicio | date | Não | — | — |
| data_fim | date | Não | — | — |
| data_retorno | date | Não | — | — |
| status | text | Não | 'agendado'::text | — |
| created_at | timestamp with time zone | Não | now() | — |

### Chave primária
- `CONSTRAINT vacation_schedules_pkey PRIMARY KEY (id)`

### Relacionamentos
- `vacation_schedules_employee_id_fkey`: `employee_id` → `public.employees(id)`
- `vacation_schedules_unit_id_fkey`: `unit_id` → `public.units(id)`

### Constraints
- `CONSTRAINT vacation_schedules_employee_id_data_inicio_key UNIQUE (employee_id, data_inicio)`

### Índices

Nenhum índice adicional identificado.

### Triggers

Nenhum trigger associado.

### Políticas RLS

RLS: **habilitada**.
- `t1_own`: `FOR SELECT USING ((employee_id = ( SELECT employees.id FROM public.employees WHERE (employees.user_id = auth.uid()))))`
- `t3_dept`: `USING ((public.get_my_tier() = 'T3'::text))`
- `t4_master`: `USING ((public.get_my_tier() = 'T4'::text))`

## vacations

### Finalidade

Descrição inferida pela estrutura: armazena registros relacionados a `vacations`. A finalidade de negócio exata deve ser confirmada com a equipe responsável.

### Colunas

| Coluna | Tipo | Obrigatória | Padrão | Observação |
|---|---|---|---|---|
| id | uuid | Sim | gen_random_uuid() | — |
| employee_id | uuid | Sim | — | — |
| unit_id | uuid | Sim | — | — |
| start_date | date | Sim | — | — |
| end_date | date | Sim | — | — |
| acquisitive_period_start | date | Não | — | — |
| acquisitive_period_end | date | Não | — | — |
| days_entitled | integer | Não | 30 | — |
| days_taken | integer | Não | — | — |
| abono_days | integer | Não | 0 | — |
| is_double_pay | boolean | Não | false | — |
| status | text | Sim | 'agendada'::text | — |
| notes | text | Não | — | — |
| created_by | uuid | Não | — | — |
| created_at | timestamp with time zone | Não | now() | — |
| updated_at | timestamp with time zone | Não | now() | — |

### Chave primária
- `CONSTRAINT vacations_pkey PRIMARY KEY (id)`

### Relacionamentos
- `vacations_created_by_fkey`: `created_by` → `auth.users(id)`
- `vacations_employee_id_fkey`: `employee_id` → `public.employees(id)` (ON DELETE CASCADE)
- `vacations_unit_id_fkey`: `unit_id` → `public.units(id)`

### Constraints
- `CONSTRAINT vacations_status_check CHECK ((status = ANY (ARRAY['agendada'::text, 'em_andamento'::text, 'concluida'::text, 'cancelada'::text])))`

### Índices
- `idx_vacations_employee`: `USING btree (employee_id)`
- `idx_vacations_status`: `USING btree (status)`

### Triggers

Nenhum trigger associado.

### Políticas RLS

RLS: **habilitada**.
- `vacations_delete`: `FOR DELETE USING (public.kph_is_founder())`
- `vacations_insert`: `FOR INSERT WITH CHECK (public.kph_has_role_for_unit(unit_id))`
- `vacations_select`: `FOR SELECT USING (public.kph_has_role_for_unit(unit_id))`
- `vacations_update`: `FOR UPDATE USING (public.kph_has_role_for_unit(unit_id))`

## vendas_consolidado_ambiente

### Finalidade

Descrição inferida pela estrutura: armazena registros relacionados a `vendas consolidado ambiente`. A finalidade de negócio exata deve ser confirmada com a equipe responsável.

### Colunas

| Coluna | Tipo | Obrigatória | Padrão | Observação |
|---|---|---|---|---|
| id | uuid | Sim | gen_random_uuid() | — |
| periodo_id | uuid | Sim | — | — |
| ambiente | text | Sim | — | — |
| bruto | numeric | Não | — | — |
| clientes | integer | Não | — | — |
| participacao_pct | numeric | Não | — | — |

### Chave primária
- `CONSTRAINT vendas_consolidado_ambiente_pkey PRIMARY KEY (id)`

### Relacionamentos
- `vendas_consolidado_ambiente_periodo_id_fkey`: `periodo_id` → `public.vendas_consolidado_periodo(id)` (ON DELETE CASCADE)

### Constraints

Nenhuma constraint adicional identificada.

### Índices
- `idx_vcamb_periodo`: `USING btree (periodo_id)`

### Triggers

Nenhum trigger associado.

### Políticas RLS

RLS: **habilitada**.
- `vendas_consolidado_ambiente_manage`: `TO service_role USING (true) WITH CHECK (true)`
- `vendas_consolidado_ambiente_read`: `FOR SELECT TO authenticated, anon USING (true)`

## vendas_consolidado_dia_semana

### Finalidade

Descrição inferida pela estrutura: armazena registros relacionados a `vendas consolidado dia semana`. A finalidade de negócio exata deve ser confirmada com a equipe responsável.

### Colunas

| Coluna | Tipo | Obrigatória | Padrão | Observação |
|---|---|---|---|---|
| id | uuid | Sim | gen_random_uuid() | — |
| periodo_id | uuid | Sim | — | — |
| dia_semana | text | Sim | — | — |
| ordem | integer | Não | — | — |
| bruto | numeric | Não | — | — |
| clientes | integer | Não | — | — |
| ticket_medio | numeric | Não | — | — |

### Chave primária
- `CONSTRAINT vendas_consolidado_dia_semana_pkey PRIMARY KEY (id)`

### Relacionamentos
- `vendas_consolidado_dia_semana_periodo_id_fkey`: `periodo_id` → `public.vendas_consolidado_periodo(id)` (ON DELETE CASCADE)

### Constraints

Nenhuma constraint adicional identificada.

### Índices
- `idx_vcdia_periodo`: `USING btree (periodo_id, ordem)`

### Triggers

Nenhum trigger associado.

### Políticas RLS

RLS: **habilitada**.
- `vendas_consolidado_dia_semana_manage`: `TO service_role USING (true) WITH CHECK (true)`
- `vendas_consolidado_dia_semana_read`: `FOR SELECT TO authenticated, anon USING (true)`

## vendas_consolidado_funcionarios

### Finalidade

Descrição inferida pela estrutura: armazena registros relacionados a `vendas consolidado funcionarios`. A finalidade de negócio exata deve ser confirmada com a equipe responsável.

### Colunas

| Coluna | Tipo | Obrigatória | Padrão | Observação |
|---|---|---|---|---|
| id | uuid | Sim | gen_random_uuid() | — |
| periodo_id | uuid | Sim | — | — |
| funcionario | text | Sim | — | — |
| bruto | numeric | Não | — | — |
| qtd_vendas | integer | Não | — | — |

### Chave primária
- `CONSTRAINT vendas_consolidado_funcionarios_pkey PRIMARY KEY (id)`

### Relacionamentos
- `vendas_consolidado_funcionarios_periodo_id_fkey`: `periodo_id` → `public.vendas_consolidado_periodo(id)` (ON DELETE CASCADE)

### Constraints

Nenhuma constraint adicional identificada.

### Índices
- `idx_vcfunc_periodo`: `USING btree (periodo_id, bruto DESC)`

### Triggers

Nenhum trigger associado.

### Políticas RLS

RLS: **habilitada**.
- `vendas_consolidado_funcionarios_manage`: `TO service_role USING (true) WITH CHECK (true)`
- `vendas_consolidado_funcionarios_read`: `FOR SELECT TO authenticated, anon USING (true)`

## vendas_consolidado_mensal

### Finalidade

Descrição inferida pela estrutura: armazena registros relacionados a `vendas consolidado mensal`. A finalidade de negócio exata deve ser confirmada com a equipe responsável.

### Colunas

| Coluna | Tipo | Obrigatória | Padrão | Observação |
|---|---|---|---|---|
| id | uuid | Sim | gen_random_uuid() | — |
| periodo_id | uuid | Sim | — | — |
| mes | text | Sim | — | — |
| ordem | integer | Não | — | — |
| bruto | numeric | Não | — | — |
| liquido | numeric | Não | — | — |
| clientes | integer | Não | — | — |
| ticket_medio | numeric | Não | — | — |

### Chave primária
- `CONSTRAINT vendas_consolidado_mensal_pkey PRIMARY KEY (id)`

### Relacionamentos
- `vendas_consolidado_mensal_periodo_id_fkey`: `periodo_id` → `public.vendas_consolidado_periodo(id)` (ON DELETE CASCADE)

### Constraints

Nenhuma constraint adicional identificada.

### Índices
- `idx_vcmensal_periodo`: `USING btree (periodo_id, ordem)`

### Triggers

Nenhum trigger associado.

### Políticas RLS

RLS: **habilitada**.
- `vendas_consolidado_mensal_manage`: `TO service_role USING (true) WITH CHECK (true)`
- `vendas_consolidado_mensal_read`: `FOR SELECT TO authenticated, anon USING (true)`

## vendas_consolidado_periodo

### Finalidade

Descrição inferida pela estrutura: armazena registros relacionados a `vendas consolidado periodo`. A finalidade de negócio exata deve ser confirmada com a equipe responsável.

### Colunas

| Coluna | Tipo | Obrigatória | Padrão | Observação |
|---|---|---|---|---|
| id | uuid | Sim | gen_random_uuid() | — |
| unit_id | uuid | Sim | — | — |
| data_inicio | date | Sim | — | — |
| data_fim | date | Sim | — | — |
| label | text | Sim | — | — |
| importado_em | timestamp with time zone | Sim | now() | — |

### Chave primária
- `CONSTRAINT vendas_consolidado_periodo_pkey PRIMARY KEY (id)`

### Relacionamentos

Nenhuma chave estrangeira identificada.

### Constraints

Nenhuma constraint adicional identificada.

### Índices
- `idx_vcp_unit`: `USING btree (unit_id, data_inicio DESC)`

### Triggers

Nenhum trigger associado.

### Políticas RLS

RLS: **habilitada**.
- `vcp_manage`: `TO service_role USING (true) WITH CHECK (true)`
- `vcp_read`: `FOR SELECT TO authenticated, anon USING (true)`

## vendas_consolidado_produtos

### Finalidade

Descrição inferida pela estrutura: armazena registros relacionados a `vendas consolidado produtos`. A finalidade de negócio exata deve ser confirmada com a equipe responsável.

### Colunas

| Coluna | Tipo | Obrigatória | Padrão | Observação |
|---|---|---|---|---|
| id | uuid | Sim | gen_random_uuid() | — |
| periodo_id | uuid | Sim | — | — |
| grupo | text | Não | — | — |
| produto | text | Sim | — | — |
| quantidade | numeric | Não | — | — |
| valor_bruto | numeric | Não | — | — |
| valor_desconto | numeric | Não | — | — |
| valor_liquido | numeric | Não | — | — |
| participacao_pct | numeric | Não | — | — |

### Chave primária
- `CONSTRAINT vendas_consolidado_produtos_pkey PRIMARY KEY (id)`

### Relacionamentos
- `vendas_consolidado_produtos_periodo_id_fkey`: `periodo_id` → `public.vendas_consolidado_periodo(id)` (ON DELETE CASCADE)

### Constraints

Nenhuma constraint adicional identificada.

### Índices
- `idx_vcprod_periodo`: `USING btree (periodo_id, valor_liquido DESC)`

### Triggers

Nenhum trigger associado.

### Políticas RLS

RLS: **habilitada**.
- `vcprod_manage`: `TO service_role USING (true) WITH CHECK (true)`
- `vcprod_read`: `FOR SELECT TO authenticated, anon USING (true)`

## vendas_consolidado_resumo

### Finalidade

Descrição inferida pela estrutura: armazena registros relacionados a `vendas consolidado resumo`. A finalidade de negócio exata deve ser confirmada com a equipe responsável.

### Colunas

| Coluna | Tipo | Obrigatória | Padrão | Observação |
|---|---|---|---|---|
| id | uuid | Sim | gen_random_uuid() | — |
| periodo_id | uuid | Sim | — | — |
| acessos | integer | Não | — | — |
| permanencia_media | text | Não | — | — |
| ticket_medio | numeric | Não | — | — |
| ticket_real | numeric | Não | — | — |
| bruto | numeric | Não | — | — |
| produto | numeric | Não | — | — |
| custo | numeric | Não | — | — |
| desconto | numeric | Não | — | — |
| gorjeta | numeric | Não | — | — |
| convite | numeric | Não | — | — |
| lucro | numeric | Não | — | — |
| entrada | numeric | Não | — | — |
| consumo | numeric | Não | — | — |
| devedor | numeric | Não | — | — |
| pgto_fechado | numeric | Não | — | — |
| pgto_recebido | numeric | Não | — | — |
| pgto_diferenca | numeric | Não | — | — |
| cash | numeric | Não | — | — |
| card | numeric | Não | — | — |
| pix | numeric | Não | — | — |

### Chave primária
- `CONSTRAINT vendas_consolidado_resumo_pkey PRIMARY KEY (id)`

### Relacionamentos
- `vendas_consolidado_resumo_periodo_id_fkey`: `periodo_id` → `public.vendas_consolidado_periodo(id)` (ON DELETE CASCADE)

### Constraints

Nenhuma constraint adicional identificada.

### Índices
- `idx_vcr_periodo`: `USING btree (periodo_id)`

### Triggers

Nenhum trigger associado.

### Políticas RLS

RLS: **habilitada**.
- `vendas_consolidado_resumo_manage`: `TO service_role USING (true) WITH CHECK (true)`
- `vendas_consolidado_resumo_read`: `FOR SELECT TO authenticated, anon USING (true)`

## vendas_consolidado_turno

### Finalidade

Descrição inferida pela estrutura: armazena registros relacionados a `vendas consolidado turno`. A finalidade de negócio exata deve ser confirmada com a equipe responsável.

### Colunas

| Coluna | Tipo | Obrigatória | Padrão | Observação |
|---|---|---|---|---|
| id | uuid | Sim | gen_random_uuid() | — |
| periodo_id | uuid | Sim | — | — |
| turno | text | Sim | — | — |
| bruto | numeric | Não | — | — |
| clientes | integer | Não | — | — |
| ticket_medio | numeric | Não | — | — |
| participacao_pct | numeric | Não | — | — |

### Chave primária
- `CONSTRAINT vendas_consolidado_turno_pkey PRIMARY KEY (id)`

### Relacionamentos
- `vendas_consolidado_turno_periodo_id_fkey`: `periodo_id` → `public.vendas_consolidado_periodo(id)` (ON DELETE CASCADE)

### Constraints

Nenhuma constraint adicional identificada.

### Índices
- `idx_vcturno_periodo`: `USING btree (periodo_id)`

### Triggers

Nenhum trigger associado.

### Políticas RLS

RLS: **habilitada**.
- `vendas_consolidado_turno_manage`: `TO service_role USING (true) WITH CHECK (true)`
- `vendas_consolidado_turno_read`: `FOR SELECT TO authenticated, anon USING (true)`

## vendas_diarias

### Finalidade

Descrição inferida pela estrutura: armazena registros relacionados a `vendas diarias`. A finalidade de negócio exata deve ser confirmada com a equipe responsável.

### Colunas

| Coluna | Tipo | Obrigatória | Padrão | Observação |
|---|---|---|---|---|
| id | integer | Sim | — | — |
| data_venda | date | Sim | — | — |
| turno | text | Não | — | — |
| qtd_clientes | integer | Não | — | — |
| faturamento_bruto | numeric | Não | — | — |
| descontos_clientes | numeric | Não | — | — |
| descontos_socios | numeric | Não | — | — |
| descontos_internos | numeric | Não | — | — |
| gorjetas | numeric | Não | — | — |
| penduras | numeric | Não | — | — |
| perdas | numeric | Não | — | — |
| meta_faturamento | numeric | Não | — | — |
| criado_em | timestamp with time zone | Não | now() | — |

### Chave primária
- `CONSTRAINT vendas_diarias_pkey PRIMARY KEY (id)`

### Relacionamentos

Nenhuma chave estrangeira identificada.

### Constraints

Nenhuma constraint adicional identificada.

### Índices

Nenhum índice adicional identificado.

### Triggers

Nenhum trigger associado.

### Políticas RLS

RLS: **não habilitada no dump**.

Nenhuma política associada.

## warnings

### Finalidade

Descrição inferida pela estrutura: armazena registros relacionados a `warnings`. A finalidade de negócio exata deve ser confirmada com a equipe responsável.

### Colunas

| Coluna | Tipo | Obrigatória | Padrão | Observação |
|---|---|---|---|---|
| id | uuid | Sim | gen_random_uuid() | — |
| employee_id | uuid | Sim | — | — |
| nivel | text | Sim | — | — |
| descricao | text | Sim | — | — |
| score_impact | integer | Não | 0 | — |
| documento_path | text | Não | — | — |
| data | date | Sim | CURRENT_DATE | — |
| created_at | timestamp with time zone | Não | now() | — |

### Chave primária
- `CONSTRAINT warnings_pkey PRIMARY KEY (id)`

### Relacionamentos
- `warnings_employee_id_fkey`: `employee_id` → `public.employees(id)` (ON DELETE CASCADE)

### Constraints

Nenhuma constraint adicional identificada.

### Índices
- `idx_warnings_employee`: `USING btree (employee_id, data DESC)`

### Triggers

Nenhum trigger associado.

### Políticas RLS

RLS: **habilitada**.
- `warnings_all`: `USING ((EXISTS ( SELECT 1 FROM public.employees e WHERE ((e.id = warnings.employee_id) AND public.kph_has_role_for_unit(e.unit_id)))))`

## work_schedules

### Finalidade

Descrição inferida pela estrutura: armazena registros relacionados a `work schedules`. A finalidade de negócio exata deve ser confirmada com a equipe responsável.

### Colunas

| Coluna | Tipo | Obrigatória | Padrão | Observação |
|---|---|---|---|---|
| id | uuid | Sim | gen_random_uuid() | — |
| unit_id | uuid | Não | — | — |
| employee_id | uuid | Não | — | — |
| nome | text | Não | — | — |
| mes_referencia | date | Não | — | — |
| escala_numero | integer | Não | — | — |
| departamento | text | Não | — | — |
| cargo | text | Não | — | — |
| created_at | timestamp with time zone | Não | now() | — |

### Chave primária
- `CONSTRAINT work_schedules_pkey PRIMARY KEY (id)`

### Relacionamentos
- `work_schedules_employee_id_fkey`: `employee_id` → `public.employees(id)`
- `work_schedules_unit_id_fkey`: `unit_id` → `public.units(id)`

### Constraints
- `CONSTRAINT work_schedules_employee_id_mes_referencia_key UNIQUE (employee_id, mes_referencia)`

### Índices

Nenhum índice adicional identificado.

### Triggers

Nenhum trigger associado.

### Políticas RLS

RLS: **habilitada**.
- `t1_own`: `FOR SELECT USING ((employee_id = ( SELECT employees.id FROM public.employees WHERE (employees.user_id = auth.uid()))))`
- `t3_dept`: `USING ((public.get_my_tier() = 'T3'::text))`
- `t4_master`: `USING ((public.get_my_tier() = 'T4'::text))`

## workday_caixas

### Finalidade

Descrição inferida pela estrutura: armazena registros relacionados a `workday caixas`. A finalidade de negócio exata deve ser confirmada com a equipe responsável.

### Colunas

| Coluna | Tipo | Obrigatória | Padrão | Observação |
|---|---|---|---|---|
| caixa_id | integer | Sim | — | — |
| workday_id | integer | Sim | — | — |
| operador_nome | text | Não | — | — |
| operador_cpf | text | Não | — | — |
| abertura | text | Não | — | — |
| fechamento | text | Não | — | — |
| total_fechado | numeric | Não | — | — |
| total_recebido | numeric | Não | — | — |
| diferenca_total | numeric | Não | — | — |
| dinheiro_total | numeric | Não | — | — |
| despesa | numeric | Não | — | — |
| transacao | numeric | Não | — | — |
| pagamentos | jsonb | Não | — | — |
| cedulas | jsonb | Não | — | — |
| moedas | jsonb | Não | — | — |

### Chave primária
- `CONSTRAINT workday_caixas_pkey PRIMARY KEY (caixa_id)`

### Relacionamentos

Nenhuma chave estrangeira identificada.

### Constraints

Nenhuma constraint adicional identificada.

### Índices

Nenhum índice adicional identificado.

### Triggers

Nenhum trigger associado.

### Políticas RLS

RLS: **não habilitada no dump**.

Nenhuma política associada.

## workday_grupos

### Finalidade

Descrição inferida pela estrutura: armazena registros relacionados a `workday grupos`. A finalidade de negócio exata deve ser confirmada com a equipe responsável.

### Colunas

| Coluna | Tipo | Obrigatória | Padrão | Observação |
|---|---|---|---|---|
| id | integer | Sim | — | — |
| workday_id | integer | Sim | — | — |
| posicao | integer | Não | — | — |
| nome | text | Não | — | — |
| percentual | numeric | Não | — | — |
| bruto | numeric | Não | — | — |
| desconto | numeric | Não | — | — |
| gorjeta | numeric | Não | — | — |
| consumo | numeric | Não | — | — |

### Chave primária
- `CONSTRAINT workday_grupos_pkey PRIMARY KEY (id)`

### Relacionamentos

Nenhuma chave estrangeira identificada.

### Constraints

Nenhuma constraint adicional identificada.

### Índices

Nenhum índice adicional identificado.

### Triggers

Nenhum trigger associado.

### Políticas RLS

RLS: **não habilitada no dump**.

Nenhuma política associada.

## workday_produtos

### Finalidade

Descrição inferida pela estrutura: armazena registros relacionados a `workday produtos`. A finalidade de negócio exata deve ser confirmada com a equipe responsável.

### Colunas

| Coluna | Tipo | Obrigatória | Padrão | Observação |
|---|---|---|---|---|
| id | integer | Sim | — | — |
| workday_id | integer | Sim | — | — |
| posicao | integer | Não | — | — |
| nome | text | Não | — | — |
| qtde | numeric | Não | — | — |
| unitario | numeric | Não | — | — |
| cmv_pct | numeric | Não | — | — |
| custo | numeric | Não | — | — |
| lucro | numeric | Não | — | — |
| consumo | numeric | Não | — | — |

### Chave primária
- `CONSTRAINT workday_produtos_pkey PRIMARY KEY (id)`

### Relacionamentos

Nenhuma chave estrangeira identificada.

### Constraints

Nenhuma constraint adicional identificada.

### Índices

Nenhum índice adicional identificado.

### Triggers

Nenhum trigger associado.

### Políticas RLS

RLS: **não habilitada no dump**.

Nenhuma política associada.

## workday_resumo

### Finalidade

Descrição inferida pela estrutura: armazena registros relacionados a `workday resumo`. A finalidade de negócio exata deve ser confirmada com a equipe responsável.

### Colunas

| Coluna | Tipo | Obrigatória | Padrão | Observação |
|---|---|---|---|---|
| workday_id | integer | Sim | — | — |
| data | date | Sim | — | — |
| unidade_id | integer | Sim | — | — |
| acessos | integer | Não | — | — |
| permanencia | text | Não | — | — |
| cmv_pct | numeric | Não | — | — |
| ticket_zero | numeric | Não | — | — |
| ticket_real | numeric | Não | — | — |
| ticket_medio | numeric | Não | — | — |
| bruto | numeric | Não | — | — |
| desconto | numeric | Não | — | — |
| gorjeta | numeric | Não | — | — |
| custo | numeric | Não | — | — |
| despesa | numeric | Não | — | — |
| lucro | numeric | Não | — | — |
| convite | numeric | Não | — | — |
| produto | numeric | Não | — | — |
| consumo_total | numeric | Não | — | — |
| devedor_total | numeric | Não | — | — |
| pendencia_antiga | numeric | Não | — | — |
| total_fechado | numeric | Não | — | — |
| total_recebido | numeric | Não | — | — |
| diferenca_caixa | numeric | Não | — | — |
| diferenca_real | numeric | Não | — | — |
| cancelamentos_total | numeric | Não | — | — |
| descontos_total | numeric | Não | — | — |
| pagamentos | jsonb | Não | — | — |
| caixas | jsonb | Não | — | — |
| ambientes | jsonb | Não | — | — |
| turnos | jsonb | Não | — | — |
| clientes_tipo | jsonb | Não | — | — |
| clientes_sexo | jsonb | Não | — | — |
| clientes_idade | jsonb | Não | — | — |
| cidades | jsonb | Não | — | — |
| devedores | jsonb | Não | — | — |
| pendencias_antigas | jsonb | Não | — | — |
| gorjetas_edit | jsonb | Não | — | — |
| descontos_motivo | jsonb | Não | — | — |
| cancelamentos_motivo | jsonb | Não | — | — |
| cancelamentos_usuario | jsonb | Não | — | — |
| created_at | timestamp with time zone | Não | now() | — |
| updated_at | timestamp with time zone | Não | now() | — |

### Chave primária
- `CONSTRAINT workday_resumo_pkey PRIMARY KEY (workday_id)`

### Relacionamentos

Nenhuma chave estrangeira identificada.

### Constraints

Nenhuma constraint adicional identificada.

### Índices

Nenhum índice adicional identificado.

### Triggers

Nenhum trigger associado.

### Políticas RLS

RLS: **não habilitada no dump**.

Nenhuma política associada.

## workday_usuarios

### Finalidade

Descrição inferida pela estrutura: armazena registros relacionados a `workday usuarios`. A finalidade de negócio exata deve ser confirmada com a equipe responsável.

### Colunas

| Coluna | Tipo | Obrigatória | Padrão | Observação |
|---|---|---|---|---|
| id | integer | Sim | — | — |
| workday_id | integer | Sim | — | — |
| posicao | integer | Não | — | — |
| nome | text | Não | — | — |
| qtde | numeric | Não | — | — |
| gorjeta | numeric | Não | — | — |
| convite | numeric | Não | — | — |
| produto | numeric | Não | — | — |
| consumo | numeric | Não | — | — |

### Chave primária
- `CONSTRAINT workday_usuarios_pkey PRIMARY KEY (id)`

### Relacionamentos

Nenhuma chave estrangeira identificada.

### Constraints

Nenhuma constraint adicional identificada.

### Índices

Nenhum índice adicional identificado.

### Triggers

Nenhum trigger associado.

### Políticas RLS

RLS: **não habilitada no dump**.

Nenhuma política associada.

## workday_venda

### Finalidade

Descrição inferida pela estrutura: armazena registros relacionados a `workday venda`. A finalidade de negócio exata deve ser confirmada com a equipe responsável.

### Colunas

| Coluna | Tipo | Obrigatória | Padrão | Observação |
|---|---|---|---|---|
| workday_id | integer | Sim | — | — |
| data | date | Sim | — | — |
| bruto_total | numeric | Não | — | — |
| desconto_total | numeric | Não | — | — |
| gorjeta_total | numeric | Não | — | — |
| total | numeric | Não | — | — |
| categorias | jsonb | Não | — | — |

### Chave primária
- `CONSTRAINT workday_venda_pkey PRIMARY KEY (workday_id)`

### Relacionamentos

Nenhuma chave estrangeira identificada.

### Constraints

Nenhuma constraint adicional identificada.

### Índices

Nenhum índice adicional identificado.

### Triggers

Nenhum trigger associado.

### Políticas RLS

RLS: **não habilitada no dump**.

Nenhuma política associada.
<!-- AUTO-GENERATED:END -->
