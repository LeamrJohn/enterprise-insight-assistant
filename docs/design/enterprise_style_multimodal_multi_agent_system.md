# 项目文档一：企业级风格多模态多 Agent 工作流系统（推荐实现版）

## 0. 文档定位

本项目不是完整企业级 AI 平台，也不是生产级 SaaS 系统，而是一个尽可能接近真实工程项目的 AI Agent 应用系统原型。

目标是：

> 在可控开发量内，实现真实工程项目常见的基础配置、后端结构、权限认证、任务状态、异步执行、日志、输出校验、Docker 部署和测试，让项目不像 Demo，而像一个可以继续扩展的工程项目。

本项目适合用于：

- AI 应用工程师项目
- Agent 工程师项目
- LLM 应用开发项目
- 应届生 / 初级开发者面试项目
- Python 后端工程能力提升项目

---

## 1. 项目名称

中文名称：

> 企业级风格多模态多 Agent 工作流系统

英文名称：

> Enterprise-style Multimodal Multi-Agent Workflow System

---

## 2. 项目业务背景

企业员工经常需要处理不同来源的信息，例如：

- PDF 报告
- 图片截图
- 用户反馈
- 产品文档
- 业务说明
- 简单结构化数据

传统方式下，员工需要人工阅读、总结、归纳、分析并生成报告，效率较低。

本项目提供一个 AI 工作流系统，用户上传文本、PDF 或图片后，系统通过多个 Agent 协作完成：

1. 任务理解
2. 任务拆解
3. 文档 / 图片解析
4. RAG 知识检索
5. 信息分析
6. 报告生成
7. 输出结构化校验
8. 任务结果持久化

最终输出一份结构化分析报告。

---

## 3. 项目目标

### 3.1 核心目标

实现一个具备真实工程项目基础结构的 AI Agent 应用系统。

必须包含：

- FastAPI 后端服务
- 配置管理
- JWT 登录认证
- 简单 RBAC 权限
- 多 Agent 架构
- Workflow 执行器
- Tool Registry
- RAG 文档检索
- 多模态输入处理
- Pydantic 输出校验
- PostgreSQL 数据持久化
- Redis + Celery 异步任务
- 结构化日志
- 基础错误处理与重试
- Docker / docker-compose
- pytest 基础测试
- README 项目说明

---

## 4. 不做什么

本项目不追求完整生产级平台能力，因此暂不实现：

- 多租户完整隔离
- 大型 Control Plane / Execution Plane 物理拆分
- SLO / SLA
- 灾备恢复
- Admin Console
- Feature Flag
- 灰度发布
- API 套餐计费
- Secret Manager / Vault
- Kubernetes
- Terraform
- 复杂模型路由平台
- 复杂安全合规体系
- 企业级告警系统
- 供应链安全
- 事故响应流程

这些内容可以写在“后续扩展”中，但不作为当前项目必须实现范围。

---

## 5. 系统总体架构

```text
User / API Client
        |
        v
FastAPI API Layer
        |
        v
Auth Layer
JWT + Simple RBAC
        |
        v
Task Service
Create Task / Query Task / Store Result
        |
        v
Workflow Engine
Router -> Planner -> RAG / Vision -> Analysis -> Report -> Validate
        |
        v
Agent Layer
Router Agent / Planner Agent / RAG Agent / Vision Agent / Analysis Agent / Report Agent
        |
        v
Tool Layer
RAG Tool / Image Tool / Calculator Tool / Mock SQL Tool / Report Tool
        |
        v
Data Layer
PostgreSQL / Redis / Vector DB / Local File Storage
```

---

## 6. 技术栈

### 6.1 后端

- Python
- FastAPI
- Pydantic
- SQLAlchemy
- Alembic
- Uvicorn

### 6.2 AI / Agent

- OpenAI API / Qwen API / Kimi API 任选
- LangChain / LangGraph 可选
- 自定义 Workflow Engine 推荐先做
- FAISS / Chroma

### 6.3 数据与任务

- PostgreSQL
- Redis
- Celery

### 6.4 多模态

- PDF：pypdf / pdfplumber
- 图片：OCR / VLM API
- 文本：普通解析

### 6.5 工程配置

- python-dotenv
- Docker
- docker-compose
- pytest
- ruff / black 可选

---

## 7. 项目目录结构

```text
enterprise_style_agent_system/
  app/
    api/
      v1/
        auth.py
        agent.py
        files.py
        tasks.py
    core/
      config.py
      security.py
      exceptions.py
      logging.py
      permissions.py
    auth/
      jwt.py
      password.py
      rbac.py
    workflow/
      engine.py
      state.py
      schemas.py
    agents/
      base.py
      router_agent.py
      planner_agent.py
      rag_agent.py
      vision_agent.py
      analysis_agent.py
      report_agent.py
      verifier_agent.py
    tools/
      base.py
      registry.py
      rag_tool.py
      image_tool.py
      calculator_tool.py
      mock_sql_tool.py
      report_tool.py
    rag/
      parser.py
      chunker.py
      embeddings.py
      retriever.py
      vector_store.py
    models/
      user.py
      task.py
      agent_step.py
      file.py
      report.py
    schemas/
      auth.py
      requests.py
      responses.py
      agent_outputs.py
      tool_outputs.py
      reports.py
    services/
      auth_service.py
      task_service.py
      workflow_service.py
      file_service.py
      report_service.py
    workers/
      celery_app.py
      tasks.py
    db/
      session.py
      base.py
    utils/
      ids.py
      time.py
      json_utils.py
  migrations/
  tests/
    test_api/
    test_agents/
    test_tools/
    test_workflow/
    test_schemas/
  storage/
    uploads/
  docker-compose.yml
  Dockerfile
  .env.example
  requirements.txt
  README.md
```

---

## 8. 核心模块说明

## 8.1 API 层

### 主要接口

```text
POST /api/v1/auth/login
POST /api/v1/agent/run
GET  /api/v1/tasks/{task_id}
GET  /api/v1/tasks/{task_id}/result
POST /api/v1/files/upload
GET  /api/v1/reports/{report_id}
```

### 应该做到什么

- 路由按业务模块拆分
- 所有请求使用 Pydantic schema
- 所有响应使用统一格式
- 所有错误使用统一异常处理
- API 路径包含版本号 `/api/v1`
- Swagger 可以正常访问

### 怎么验证

- 启动服务后访问 `/docs`
- 使用 Postman / Swagger 调用接口
- 输入非法参数时返回明确错误
- 正常请求返回固定响应结构

---

## 8.2 配置管理

### 应该做到什么

- 使用 `.env` 管理环境变量
- 提供 `.env.example`
- `config.py` 统一读取配置
- 区分 dev / prod 基础配置

示例配置：

```text
APP_ENV=dev
DATABASE_URL=postgresql://user:password@localhost:5432/agent_db
REDIS_URL=redis://localhost:6379/0
LLM_API_KEY=your-key
JWT_SECRET=your-secret
LOG_LEVEL=INFO
```

### 怎么验证

- 删除 `.env` 后项目不会直接泄露真实密钥
- 修改 `.env` 后项目能读取新配置
- 启动日志能打印当前环境，但不能打印密钥原文

---

## 8.3 用户认证与 RBAC

### 应该做到什么

- 实现登录接口
- 登录后返回 JWT
- 访问 Agent 接口需要携带 Token
- 根据用户角色控制权限

角色：

```text
admin:
- run_agent
- upload_file
- view_all_tasks

user:
- run_agent
- upload_file
- view_own_tasks

viewer:
- view_own_tasks
```

### 怎么验证

- 未登录访问 `/agent/run` 返回 401
- user 可以创建任务
- viewer 不能创建任务
- user 不能查看其他用户任务
- admin 可以查看全部任务

---

## 8.4 Multi-Agent 模块

### Agent 列表

第一版必须实现：

- Router Agent
- Planner Agent
- RAG Agent
- Analysis Agent
- Report Agent

增强实现：

- Vision Agent
- Verifier Agent

### 各 Agent 职责

#### Router Agent

判断任务类型：

- 文档分析
- 图片分析
- 普通文本分析
- 混合输入分析

#### Planner Agent

根据任务类型生成执行步骤。

#### RAG Agent

检索文档知识库，返回相关上下文。

#### Vision Agent

解析图片或截图，返回结构化文本。

#### Analysis Agent

对上下文进行分析、归纳、提炼。

#### Report Agent

生成最终报告。

#### Verifier Agent

检查最终输出是否符合格式。

### 怎么验证

- 给纯文本输入，Router 能识别为 text_task
- 给 PDF 输入，Router 能识别为 document_task
- Planner 输出的步骤是合法 JSON
- 每个 Agent 的输出能通过 Pydantic schema 校验
- 最终报告包含 summary、findings、recommendations

---

## 8.5 Workflow 执行器

### 应该做到什么

实现一个简单工作流：

```text
Router Agent
  -> Planner Agent
  -> RAG Agent / Vision Agent
  -> Analysis Agent
  -> Report Agent
  -> Output Validation
```

任务状态：

```text
queued
running
success
failed
```

每一步需要记录：

- step_name
- input
- output
- status
- error_message
- started_at
- finished_at

### 怎么验证

- 创建任务后数据库中有 task 记录
- 每个 Agent 执行后有 agent_step 记录
- 中途失败时 task 状态变为 failed
- 全部成功后 task 状态变为 success
- 可以通过接口查询任务执行状态

---

## 8.6 Tool Registry

### 应该做到什么

实现统一工具注册机制：

```text
tool_name
description
input_schema
output_schema
run()
```

基础工具：

- rag_search_tool
- image_parse_tool
- calculator_tool
- mock_sql_tool
- report_generate_tool

### 怎么验证

- 工具可以通过名称调用
- 调用不存在的工具会报明确错误
- 工具输入不符合 schema 时返回校验错误
- 工具输出能被后续 Agent 正常使用

---

## 8.7 RAG 系统

### 应该做到什么

实现基本 RAG 流程：

```text
File Upload
  -> Parse Text
  -> Chunk
  -> Embedding
  -> Store Vector
  -> Retrieve
  -> Return Context
```

### 怎么验证

- 上传 PDF 后能提取文本
- 文本能被切分为 chunks
- 向量库中能查到对应内容
- 用户提问时能返回相关 chunk
- 报告中能引用检索到的上下文

---

## 8.8 多模态输入

### 应该做到什么

支持：

- 文本输入
- PDF 上传
- 图片上传

图片处理可以先用：

- OCR
- 或 VLM API

统一转成：

```json
{
  "text_context": "",
  "document_context": "",
  "image_context": ""
}
```

### 怎么验证

- 上传 PDF 后能进入 RAG 流程
- 上传图片后能提取文字或描述
- 文本 + 文件混合输入时 workflow 能正常执行
- 解析失败时返回明确错误

---

## 8.9 输出结构化校验

### 应该做到什么

最终输出固定为：

```json
{
  "summary": "",
  "key_findings": [],
  "recommendations": [],
  "risks": [],
  "confidence": 0.0
}
```

要求：

- 使用 Pydantic 校验最终输出
- LLM 输出非法 JSON 时自动重试一次
- 校验失败后任务状态为 failed，并记录错误

### 怎么验证

- 正常任务输出合法 JSON
- 模拟 LLM 输出非法格式，系统会重试
- 重试仍失败时记录错误
- 接口返回的 result 字段结构固定

---

## 8.10 数据持久化

### 核心表

```text
users
tasks
agent_steps
files
reports
```

### 应该做到什么

- 用户信息入库
- 任务状态入库
- Agent 步骤入库
- 文件信息入库
- 报告结果入库

### 怎么验证

- 服务重启后任务记录仍存在
- 可以查询历史任务
- 可以查看某个任务的执行步骤
- 可以查看某个任务的最终报告

---

## 8.11 异步任务队列

### 应该做到什么

推荐使用：

```text
Celery + Redis
```

接口模式：

```text
POST /agent/run -> 返回 task_id
GET /tasks/{task_id} -> 查询状态
GET /tasks/{task_id}/result -> 获取结果
```

### 怎么验证

- POST 请求不会一直阻塞
- Worker 能从队列中消费任务
- Worker 执行完成后数据库状态更新
- Redis 停止时任务无法执行但 API 返回明确错误
- Worker 重启后可以继续处理新任务

---

## 8.12 日志系统

### 应该做到什么

结构化日志包含：

```text
trace_id
task_id
user_id
agent_name
step_name
latency_ms
status
error_message
```

### 怎么验证

- 每次请求都有 trace_id
- 每个 Agent 执行都有日志
- 出错时日志能定位到具体 step
- 日志中不包含 LLM_API_KEY、JWT_SECRET 等敏感信息

---

## 8.13 错误处理与重试

### 应该做到什么

- 统一异常响应
- Tool 调用失败可重试
- LLM 调用失败可重试
- 任务失败记录 error_message
- 不让 Python traceback 直接暴露给用户

### 怎么验证

- 故意让某个 Tool 报错
- 系统重试指定次数
- 仍失败后 task 状态为 failed
- API 返回统一错误结构

---

## 8.14 Docker 部署

### 应该做到什么

提供：

```text
Dockerfile
docker-compose.yml
.env.example
```

服务包括：

```text
api
worker
postgres
redis
```

### 怎么验证

执行：

```bash
docker-compose up --build
```

验证：

- API 能启动
- PostgreSQL 能连接
- Redis 能连接
- Worker 能启动
- Swagger 页面能访问
- 创建任务能进入 Worker 执行

---

## 8.15 测试

### 应该做到什么

至少实现：

- API 测试
- schema 测试
- tool 测试
- workflow 测试

测试目录：

```text
tests/
  test_api/
  test_tools/
  test_workflow/
  test_schemas/
```

### 怎么验证

运行：

```bash
pytest
```

检查：

- 登录接口测试通过
- 无权限访问测试通过
- Tool 输入输出测试通过
- Workflow 主链路测试通过
- 输出 schema 校验测试通过

---

## 9. 项目实现拆分路线

## Phase 1：项目骨架与配置

### 要做什么

- 创建目录结构
- 配置 FastAPI
- 配置 `.env`
- 配置 PostgreSQL 连接
- 配置 Redis 连接
- 配置统一响应格式
- 配置统一异常处理

### 做到什么程度

- 项目能启动
- `/docs` 能访问
- 健康检查接口正常
- 能读取环境变量

### 怎么验证

- `uvicorn app.main:app --reload`
- 访问 `/docs`
- 调用 `/health`
- 修改 `.env` 后配置生效

---

## Phase 2：用户认证与权限

### 要做什么

- 用户模型
- 登录接口
- JWT 生成与校验
- RBAC 权限判断
- 当前用户依赖注入

### 做到什么程度

- 用户能登录
- 受保护接口需要 Token
- 不同角色权限不同

### 怎么验证

- 未登录访问 Agent 接口失败
- user 可以运行任务
- viewer 无法运行任务
- admin 可以访问管理接口

---

## Phase 3：数据库模型与任务系统

### 要做什么

- users 表
- tasks 表
- agent_steps 表
- files 表
- reports 表
- task service

### 做到什么程度

- 创建任务能入库
- 更新任务状态能入库
- 查询任务状态正常

### 怎么验证

- 创建任务后数据库出现记录
- 查询接口返回 queued / running / success / failed
- 服务重启后记录仍存在

---

## Phase 4：Agent 基础框架

### 要做什么

- Agent base class
- Router Agent
- Planner Agent
- Analysis Agent
- Report Agent
- Agent 输出 schema

### 做到什么程度

- 每个 Agent 能单独运行
- 每个 Agent 输出结构化结果
- 输出不合法时能报错

### 怎么验证

- 单元测试每个 Agent
- Router 能分类任务
- Planner 能生成步骤
- Report 输出符合 schema

---

## Phase 5：Workflow 执行器

### 要做什么

- workflow state
- workflow engine
- step 执行记录
- step 失败处理
- 最终输出保存

### 做到什么程度

- 一个任务能串联多个 Agent 执行
- 每一步都有数据库记录
- 最终生成报告

### 怎么验证

- 调用 `/agent/run`
- 查询 task 状态
- 查看 agent_steps 表
- 查看最终 report

---

## Phase 6：Tool Registry

### 要做什么

- Tool base class
- Tool registry
- calculator_tool
- report_tool
- mock_sql_tool
- rag_tool 占位

### 做到什么程度

- Agent 可以调用工具
- 工具输入输出有 schema
- 工具调用失败能记录错误

### 怎么验证

- 通过工具名调用工具
- 输入非法参数时校验失败
- mock_sql_tool 返回模拟数据

---

## Phase 7：RAG 系统

### 要做什么

- 文件上传
- PDF 文本解析
- chunk
- embedding
- vector store
- rag_search_tool

### 做到什么程度

- 上传文档能建立索引
- Agent 能检索文档
- 报告能使用检索上下文

### 怎么验证

- 上传一份 PDF
- 针对 PDF 内容提问
- 检索结果包含相关文本
- 最终报告引用相关内容

---

## Phase 8：多模态输入

### 要做什么

- 图片上传
- OCR / VLM 解析
- Vision Agent
- Unified Context

### 做到什么程度

- 图片可以被解析为文本描述
- 图片内容能参与 Analysis Agent 分析

### 怎么验证

- 上传截图
- 系统返回图片解析内容
- 报告中包含图片信息

---

## Phase 9：异步任务

### 要做什么

- Celery 配置
- Redis broker
- worker task
- API 返回 task_id
- 查询结果接口

### 做到什么程度

- Agent 任务后台执行
- API 不阻塞等待
- 用户可以轮询任务状态

### 怎么验证

- 启动 worker
- 调用 `/agent/run`
- 立即返回 task_id
- 查询状态从 queued -> running -> success

---

## Phase 10：日志、重试与输出校验

### 要做什么

- trace_id
- 结构化日志
- LLM retry
- Tool retry
- final output schema validation
- failed 状态记录

### 做到什么程度

- 每个任务可追踪
- 输出格式稳定
- 失败可定位

### 怎么验证

- 日志中能看到完整执行链
- 模拟 Tool 失败，检查 retry
- 模拟非法输出，检查 schema validation
- 任务失败时 error_message 入库

---

## Phase 11：Docker 与测试

### 要做什么

- Dockerfile
- docker-compose.yml
- pytest
- README
- .env.example

### 做到什么程度

- 一条命令启动完整项目
- 基础测试可运行
- README 能指导别人跑起来

### 怎么验证

- `docker-compose up --build`
- `pytest`
- 按 README 步骤从零启动项目

---

## 10. 最终验收标准

项目完成后，应满足：

```text
1. 能登录
2. 能上传 PDF / 图片
3. 能创建 Agent 任务
4. 能异步执行任务
5. 能查询任务状态
6. 能查看 Agent 执行步骤
7. 能生成结构化报告
8. 能保存任务和报告
9. 能通过 Docker 启动
10. 能通过 pytest 基础测试
```

---

## 11. 简历表达

可以写：

> 基于 FastAPI、Celery、Redis、PostgreSQL、RAG 与多 Agent 架构，实现了一个企业级风格的多模态 AI 工作流系统。系统支持文本、PDF、图片输入，通过 Router、Planner、RAG、Vision、Analysis、Report 等 Agent 协作完成任务拆解、知识检索、信息分析和报告生成；同时引入 JWT 认证、RBAC 权限、任务状态持久化、异步队列、结构化输出校验、基础重试和结构化日志，提升 AI 应用的工程完整性与可维护性。

---

## 12. 后续扩展方向

如果后续继续升级，可以增加：

- Verifier Agent
- Prompt versioning
- token usage 统计
- cost tracking
- API rate limit
- audit log
- webhook result delivery
- simple admin dashboard
- CI/CD
- monitoring dashboard

这些是增强项，不是当前必须完成项。
