# 学习进度与掌握证据

## 使用规则

本文件记录实际学习过程和掌握证据，不是预先填写的课程计划。

- 每完成一课立即更新。
- 测试结果必须来自实际运行。
- 没有通过掌握验证时不能标记为“已掌握”。
- 同一阶段允许多次记录，保留错误和修正过程。
- 不删除失败记录；失败记录用于证明排错能力的成长。

掌握状态：

| 状态 | 含义 |
|---|---|
| 未开始 | 尚未学习 |
| 学习中 | 能在较强提示下完成 |
| 待补强 | 主流程基本掌握，但排错或迁移能力不足 |
| 已掌握 | 解释、实现、排错和迁移验证全部通过 |

## 总体进度

| 阶段 | 主题 | 状态 | 最近验证 | 主要遗留问题 |
|---|---|---|---|---|
| 0 | 工程基线、Git和现有调用链 | 学习中 | 2026-07-04：pytest 3 passed | 尚未掌握`python -m`与命令参数解析 |
| 1 | HTTP契约、Schema和异常 | 未开始 | - | - |
| 2 | 用户身份、资源归属和最小RBAC | 未开始 | - | - |
| 3 | 文件上传闭环 | 未开始 | - | - |
| 4 | 文档解析、分块和生命周期 | 未开始 | - | - |
| 5 | 本地基础设施与环境分层 | 未开始 | - | - |
| 6 | 持久化任务模型和状态职责 | 未开始 | - | - |
| 7 | Celery异步执行 | 未开始 | - | - |
| 8 | pgvector和Embedding | 未开始 | - | - |
| 9 | 检索与增量评测 | 未开始 | - | - |
| 10 | Model Gateway和数据发送策略 | 未开始 | - | - |
| 11 | 可靠RAG | 未开始 | - | - |
| 12 | 独立经营数据源、KPI和标准场景 | 未开始 | - | - |
| 13 | 安全只读SQL工具 | 未开始 | - | - |
| 14 | Tool Registry | 未开始 | - | - |
| 15 | 四个核心Agent | 未开始 | - | - |
| 16 | LangGraph状态工作流 | 未开始 | - | - |
| 17 | 确定性校验、拒答和人工审核 | 未开始 | - | - |
| 18 | 可靠性和故障恢复 | 未开始 | - | - |
| 19 | 安全和数据治理 | 未开始 | - | - |
| 20 | 可观测性、评测和SLO | 未开始 | - | - |
| 21 | 最小前端 | 未开始 | - | - |
| 22 | 可复现构建、部署和运维验收 | 未开始 | - | - |

## Agent上下文专项进度

上下文能力随项目阶段逐步升级，不单独搭建脱离业务的记忆系统。

| 上下文能力 | 对应项目阶段 | 状态 | 验证证据 | 遗留问题 |
|---|---|---|---|---|
| 内存State和字段流转 | 0～1的独立练习 | 未开始 | - | - |
| 请求、身份和权限上下文 | 2 | 未开始 | - | - |
| 文档与chunk证据引用 | 3～4 | 未开始 | - | - |
| 持久化任务和异步上下文 | 6～7 | 未开始 | - | - |
| 向量检索上下文 | 8～9 | 未开始 | - | - |
| Model Gateway和单Agent上下文 | 10～11 | 未开始 | - | - |
| SQL与Tool结果上下文 | 12～14 | 未开始 | - | - |
| Multi-Agent输入隔离 | 15 | 未开始 | - | - |
| Workflow State和checkpoint | 16 | 未开始 | - | - |
| 校验、拒答和审核上下文 | 17 | 未开始 | - | - |
| Token、安全、失效和可重放 | 18～20 | 未开始 | - | - |
| 生产部署和恢复上下文 | 21～22 | 未开始 | - | - |

## 单课记录模板

复制下面模板，在每一课结束后填写。

```markdown
## YYYY-MM-DD：阶段X / 第X课 / 主题

### 本课目标

- 待填写

### 阅读与修改

- 阅读文件：
- 修改文件：
- 独立编写内容：
- 使用的提示级别：完整讲解/接口与伪代码/仅需求
- 第几次尝试通过：
- 对应Commit Hash：

### 数据流复述

用自己的语言说明输入、处理过程、输出和失败路径。

### 上下文检查

涉及RAG、Agent、Tool或Workflow时填写；不涉及时写“不适用”并说明原因。

- 当前节点需要哪些上下文：
- 每项上下文来自哪里：
- 哪些内容可信，哪些不可信：
- 权限在什么位置检查：
- 大型内容保存在哪里，State保存什么引用：
- Token不足时按什么顺序压缩：
- 哪些变化会让上下文失效：
- 如何通过task_id和证据ID重建：

### 验证证据

- 执行命令：
- 实际结果：
- 新增测试：
- 正常路径：
- 异常路径：

### 错误与根因

- 现象：
- 证据：
- 根因：
- 修复：
- 如何避免再次发生：

### 掌握验证

| 验证项 | 结果 | 证据 |
|---|---|---|
| 不看答案解释 | 未通过/通过 | |
| 独立实现同类功能 | 未通过/通过 | |
| 独立定位故障 | 未通过/通过 | |
| 独立迁移到相似场景并测试 | 未通过/通过 | |

### 当前结论

- 掌握状态：学习中/待补强/已掌握
- 已经掌握：
- 仍不理解：
- 下一步补强：
```

## 学习记录

## 2026-07-04：阶段0 / 第1课 / 确认解释器和测试基线

### 本课目标

- 确认项目实际使用的Python解释器。
- 使用同一个解释器运行pytest。
- 理解退出码和`python -m`。

### 阅读与修改

- 阅读文件：`backend/app/api/document.py`、`backend/app/services/document_service.py`、
  `backend/app/repositories/document_repository.py`、
  `backend/app/services/document_ingestion_service.py`、
  `backend/app/schemas/document.py`、`backend/app/models/documents.py`
- 修改文件：仅更新本学习记录。
- 独立编写内容：执行环境和测试检查命令。
- 使用的提示级别：完整讲解。
- 第几次尝试通过：第2次。
- 对应Commit Hash：当前仓库尚无提交。

### 数据流复述

已完成第一跳：

```text
POST /documents
→ create_document
→ save_document_service
→ save_document
→ Documents ORM对象
→ PostgreSQL
```

Repository返回ORM对象，Service将需要的字段转换为字典，FastAPI再依据
`DocumentOut`生成响应。学习者已识别API、Service和Repository的基本职责。

综合调用链复述通过：

```text
客户端
→ API
→ Service
→ Repository
→ ORM Model
→ PostgreSQL
→ Repository
→ Service
→ API使用DocumentOut校验和序列化
→ 客户端
```

Schema与ORM边界：

- `DocumentCreate`定义客户端可提交的`name/content/source`。
- `DocumentOut`增加服务端返回的`id`。
- `Documents`保存数据库需要的完整内部状态。

### 上下文检查

不适用：本课尚未涉及RAG、Agent、Tool或Workflow。

### 验证证据

- 解释器：`C:\Users\qyf21\Documents\Agent项目学习\.venv\Scripts\python.exe`
- 第1次命令：误用`pytest.exe -m pytest -q backend`
- 第1次结果：`3 deselected`，实际未执行测试
- 修正命令：`.venv\Scripts\python.exe -m pytest -q backend`
- 实际结果：`3 passed in 0.48s`
- 退出码：`0`
- 退出码理解：`0`表示命令成功；非零表示进程未按成功条件结束，不限定为代码异常。
- 迁移练习第1次：执行`.venv\Scripts\python.exe -m pip -q backend`。
- 迁移练习第1次结果：`ERROR: unknown command "backend"`。
- 迁移练习证据：pip帮助显示必须使用`pip <command> [options]`，查看版本使用`-V`或`--version`。
- 迁移练习第2次：执行`.venv\Scripts\python.exe -m pip --version`。
- 迁移练习第2次结果：pip 26.1.2，来自项目`.venv`，退出码为`0`。
- 正常路径：通过
- 异常路径：观察到错误参数导致测试全部被筛除

### 错误与根因

- 现象：pytest显示`3 deselected`。
- 证据：命令直接启动`pytest.exe`，后面仍传入`-m pytest`。
- 根因：直接启动pytest时，`-m`由pytest解释为标记筛选表达式，而不是由Python解释器解释为模块运行参数。
- 修复：改用`.venv\Scripts\python.exe -m pytest -q backend`。
- 如何避免再次发生：先判断当前启动的是Python解释器还是具体命令，再判断后续参数由谁解析。
- 新现象：pip报告`unknown command "backend"`。
- 新根因：把pytest接受的目录参数照搬给pip；不同模块拥有不同的命令行接口。
- 新证据：pip自身帮助列出了合法命令和`--version`选项。
- 源码理解修正：`response_model`具体为`DocumentOut`；`db`是通过`Depends(get_db)`
  注入的数据库Session，不是HTTP会话。
- ORM术语修正：`Documents`是ORM类，`record`只是该实例的变量名；`refresh()`用于
  从数据库重新加载当前记录。
- 事务理解：`add()`只把对象加入Session；`commit()`提交事务并完成持久化；
  `refresh()`重新读取数据库生成或修改后的字段。
- 异常理解：`commit()`抛出异常后不会继续执行`refresh()`，Session需要先
  `rollback()`才能安全继续使用。
- 跨存储一致性：数据库`rollback()`不能删除磁盘文件，因此数据库失败时还需要
  删除本次新建文件。
- 独立识别风险：当前代码在`commit()`成功后执行`refresh()`；如果`refresh()`失败，
  `rollback()`无法撤销已提交记录，但异常分支会删除文件，可能留下数据库记录存在、
  文件不存在的不一致状态。
- 异常分类修正：`IntegrityError`是数据库完整性约束异常，不是文件异常；它用于
  处理SHA256唯一约束等数据库冲突，并转换为业务可理解的重复文档异常。
- `flush()`理解修正：它把Session中的待执行SQL发送到当前数据库事务，但不提交；
  `commit()`会自动flush并提交事务。
- 可见性修正：在项目使用的PostgreSQL常规隔离级别下，当前事务能看到flush后的
  记录，其他连接在commit前通常看不到。
- 安全顺序判断：学习者正确提出`flush → refresh → commit`，使`refresh()`失败时
  事务仍未提交，可以rollback并删除文件。
- 事务复述验证：学习者能说明flush后其他连接通常不可见，并能说明commit放在
  refresh后可避免失败时残留已提交数据库记录。
- 字段来源修正：`id/created_at`可由数据库生成，`status`可来自默认值，
  `sha256/file_type/file_size`由上传服务计算后写入。
- 响应风险：ORM允许`content=None`，当前`DocumentOut`要求字符串，上传记录返回时
  会触发FastAPI响应校验异常。
- Schema设计判断：学习者正确选择为上传接口建立单独响应Schema，但最初只考虑返回
  名字和来源，遗漏了客户端后续查询所需的记录ID和处理状态。
- 状态术语补充：`pending`等待处理、`processing`正在处理、`completed`处理完成、
  `failed`处理失败。
- 当前实现边界：设计上客户端应使用文档`id`查询同一条记录的最新`status`；当前
  `DocumentOut`和文档查询接口尚未返回`status`，因此这一能力还没有实现。
- 状态查询验证：给定上传返回`id=42`，学习者能判断后续应请求`GET /documents/42`。
- ORM术语补充：ORM类映射数据库表，ORM实例承载某条记录的数据和状态。
- Git状态证据：`## No commits yet on master`，仓库已初始化但没有任何提交；
  `.gitignore`、`README.md`、`backend/`和`docs/`均显示为`??`未跟踪。
- Git理解验证：学习者能识别`??`表示未跟踪，并知道未提交的未跟踪文件无法由Git恢复。
- 名称修正：`.venv/`是本地虚拟环境；`backend/.env`是运行配置，可能包含数据库密码
  和API密钥；`.env.example`是可以提交的无密钥配置模板。
- 版本控制范围修正：Git不仅保存业务代码，还应保存测试、迁移、文档、依赖声明和
  安全的配置模板。
- 提交分类验证：正确判断`.venv/`、`.env`不提交，`.env.example`和测试应提交；
  最初误判数据库迁移不提交，已说明迁移是数据库结构的版本历史，必须进入Git。
- 迁移作用复述通过：只提交新ORM字段而不提交迁移，会导致同事数据库缺少对应列并
  在运行时出错。
- Git忽略验证：`git check-ignore -v`确认`.venv/`由第1条规则忽略，
  `backend/.env`由`.env`规则忽略。
- 暂存第1次尝试：只执行`git add`，因缺少路径参数而没有暂存；后续
  `git status --short`仍显示`??`，证明文件保持未跟踪。
- 暂存第2次尝试：使用`git add .`后状态变为`A`，表示文件已进入暂存区。
- 暂存审查：共56个文件，包含源码、测试、迁移、文档和`.env.example`；真实
  `.env`、`.venv`和明显密钥模式未进入暂存区。
- 暂存格式检查：`git diff --cached --check`发现文件末尾空白行和行尾空格；修正后
  退出码为`0`。
- 误改识别：清理迁移文件空格时误改`script.py.mako`模板中的必要分隔空格，
  `git status`显示`AM`，通过`git diff`确认差异后使用`git restore`恢复工作区。
- Git状态理解：短状态第一列表示暂存区，第二列表示工作区；`AM`表示已暂存新增文件
  后，工作区又发生修改。
- 提交前验证：pytest结果为`3 passed in 0.53s`，暂存格式检查通过。
- 分支调整：当前默认分支已从`master`改为`main`，尚未创建首个提交。
- 换行提示：Git提示LF以后可能转换为CRLF；这是Windows工作区换行策略提示，不是
  测试或暂存失败，当前阶段不增加额外换行配置。

### 掌握验证

| 验证项 | 结果 | 证据 |
|---|---|---|
| 不看答案解释 | 通过 | 能说明命令参数、请求分层和数据库事务边界 |
| 独立实现同类功能 | 通过 | 能根据pip帮助组合模块运行命令 |
| 独立定位故障 | 未通过 | 能在给定场景下识别commit后删除文件的风险，但尚未独立提出修复顺序 |
| 独立迁移到相似场景并测试 | 通过 | 将`python -m`迁移到pip模块并得到退出码0 |

### 当前结论

- 掌握状态：学习中
- 已经掌握：确认解释器路径、使用`python -m`运行模块、读取帮助和退出码。
- 仍不理解：分支名称、提交信息和初始基线提交。
- 下一步补强：将默认分支调整为`main`并创建可回退的初始提交。
