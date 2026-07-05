# Enterprise Insight Agent

面向企业内部经营分析场景的 AI Agent 平台学习项目。项目以 FastAPI 和
PostgreSQL 为后端基础，按可测试、可恢复、可审计的方式逐步实现文档知识库、
数据分析、Multi-Agent 工作流和人工审核。

> 当前仓库仍处于基础工程阶段。设计文档描述的是目标能力，不代表相关功能已经实现。

## 当前状态

已经实现：

- FastAPI 应用、健康检查和依赖注入
- PostgreSQL、SQLAlchemy 与 Alembic 迁移
- 文档和聊天记录的基础 CRUD
- 文件落盘、大小限制、文件类型校验和 SHA256 去重服务
- 请求 ID、结构化日志和数据库连接检查
- 基础集成测试

正在建设：

- 文件上传 API、文档解析与分块
- Embedding、向量检索和带引用的 RAG
- 安全 SQL 数据分析工具
- Multi-Agent 工作流、任务恢复和人工审核
- 评测、可观测性、权限和生产部署

## 仓库结构

```text
.
├── backend/              # FastAPI 后端、迁移、测试和脚本
│   ├── app/
│   │   ├── api/          # HTTP 接口
│   │   ├── core/         # 配置、日志、中间件和异常
│   │   ├── db/           # 数据库会话与 ORM 基类
│   │   ├── models/       # SQLAlchemy 模型
│   │   ├── repositories/ # 数据访问
│   │   ├── schemas/      # API 输入输出结构
│   │   └── services/     # 业务逻辑
│   ├── migrations/       # Alembic 数据库迁移
│   ├── scripts/          # 本地基础设施脚本
│   └── tests/            # 自动化测试
├── docs/
│   └── design/           # 推荐实现方案与长期完整架构参考
├── .gitignore
└── README.md
```

## 设计文档

设计文档入口见 [docs/README.md](docs/README.md)。

- 推荐实现版用于指导当前项目逐步落地。
- 完整平台版用于理解生产系统的长期能力边界。
- 实际进度以源码、测试和本 README 的“当前状态”为准。

## 本地运行

环境要求：

- Python 3.10+
- PostgreSQL

安装开发依赖：

```powershell
cd backend
..\.venv\Scripts\python.exe -m pip install -e ".[dev]"
```

复制并填写本地配置：

```powershell
Copy-Item .env.example .env
```

初始化数据库后执行迁移：

```powershell
..\.venv\Scripts\python.exe -m alembic upgrade head
```

启动 API：

```powershell
..\.venv\Scripts\python.exe -m uvicorn app.main:app --reload
```

运行测试：

```powershell
..\.venv\Scripts\python.exe -m pytest -q
```

运行代码检查：

```powershell
..\.venv\Scripts\python.exe -m ruff check app tests
```

## 开发原则

- 每项能力先定义输入、输出、状态和失败路径，再编写实现。
- 所有数据库结构变化使用 Alembic，不手工修改生产表。
- LLM 只负责理解和归纳；数字由受控工具计算。
- 所有结论必须能够追溯到文档证据或查询结果。
- 暂时性故障才重试，确定性错误应终止或进入人工处理。
- README 只记录已验证能力，规划内容必须明确标记为未实现。
