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
| 0 | 工程基线、Git和现有调用链 | 已掌握 | 2026-07-05：独立识别ModuleNotFoundError | - |
| 1 | HTTP契约、Schema和异常 | 学习中 | 2026-07-05：开始分析DocumentOut契约 | content可空冲突待修复 |
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
- 初始提交成功：`ab8c5a3 chore: establish project baseline`，属于`root-commit`，
  共纳入56个文件。
- 提交后状态：只显示`## main`，证明当时暂存区和工作区均无未提交文件。
- 学习记录提交：`5778710 docs: record stage 0 learning progress`。
- 分支迁移：从干净的`main`创建并切换到`feature/api-contracts`，两个基线提交均保留。
- 独立故障验证：运行导入不存在模块的命令，依据`ModuleNotFoundError`判断为模块导入
  问题，并根据退出码`1`确认命令失败；未盲目安装依赖。

### 掌握验证

| 验证项 | 结果 | 证据 |
|---|---|---|
| 不看答案解释 | 通过 | 能说明命令参数、请求分层和数据库事务边界 |
| 独立实现同类功能 | 通过 | 能根据pip帮助组合模块运行命令 |
| 独立定位故障 | 通过 | 独立依据异常类型和退出码识别模块导入问题 |
| 独立迁移到相似场景并测试 | 通过 | 将`python -m`迁移到pip模块，并完成Git分支迁移 |

### 当前结论

- 掌握状态：已掌握
- 已经掌握：解释器与模块运行、退出码、HTTP到数据库调用链、Session事务基础、
  Schema与ORM边界、Git忽略/暂存/提交/分支和基础故障分类。
- 仍不理解：阶段1将学习API契约、响应校验和统一异常处理。
- 下一步补强：在`feature/api-contracts`进入阶段1。

## 2026-07-05：阶段1 / 第1课 / DocumentOut响应契约

### 本课目标

- 理解数据库可空字段与API输出类型必须一致。
- 区分创建请求契约与查询响应契约。
- 先建立失败验证，再做最小修复。

### 阅读与修改

- 阅读文件：`backend/app/schemas/document.py`、`backend/app/models/documents.py`
- 修改文件：尚未修改应用代码。
- 独立编写内容：尚未开始。
- 使用的提示级别：接口与问题说明。
- 第几次尝试通过：进行中。
- 对应Commit Hash：进行中。

### 数据流复述

```text
Documents.content允许NULL
→ Service可能返回content=None
→ FastAPI使用DocumentOut校验响应
→ DocumentOut.content只允许str
→ 响应校验失败
```

### 上下文检查

不适用：本课处理普通API契约，尚未涉及Agent上下文。

### 验证证据

- 当前ORM：`Documents.content`类型为`str | None`，数据库列`nullable=True`。
- 当前响应Schema：`DocumentOut.content`类型为`str`。
- 预期：先新增一个能稳定重现冲突的Schema测试。
- 最小修改判断：学习者正确选择只将`DocumentOut.content`改为`str | None`。
- 语义修正：`Documents`是所有文档共用的数据库模型；`DocumentOut`是当前通用查询
  响应，不只表示解析完成状态。
- 空值区别：`None`表示尚无内容，空字符串`""`表示存在字符串但长度为零，两者不同。
- 失败测试第1次：pytest退出码`4`并提示找不到
  `backend/tests/test_document_schema.py`。
- 根因1：实际文件名误写为`tets_document_schema.py`，不符合pytest默认的
  `test_*.py`发现规则。
- 根因2：测试数据写成字符串`"None."`而不是Python值`None`，即使运行也不会触发
  当前Schema冲突。
- 失败测试第2次：重命名后pytest找到并通过1个测试，但检查文件发现测试仍传入
  `"None."`并断言字符串相等，因此这是未覆盖目标问题的“错误通过”。
- 失败测试第3次：测试真正传入Python的`None`后，pytest找到1个测试并按预期失败，
  Pydantic报告`DocumentOut`存在1项字符串类型校验错误，退出码为`1`。
- 结论：测试已稳定证明`DocumentOut.content: str`与数据库可空字段不一致。
- 最小修复：只将`DocumentOut.content`改为接受`str | None`，未修改创建/更新Schema、
  ORM、Service或Repository。
- 修复后单项测试：`1 passed in 0.07s`。
- 完整回归测试：`4 passed in 0.29s`。
- Ruff检查：`All checks passed!`。
- 测试整理后回归：`4 passed in 0.29s`，Ruff lint仍通过。
- 格式复查：`ruff format --check`指出Schema和新测试共2个文件需要格式化，说明
  `ruff check`通过不等于代码排版已经规范。
- 格式化后验证：完整测试`4 passed`、Ruff lint通过、两个目标文件均已格式化。
- 理解验证结果：能说明手工创建文档时内容必须提供；尚未掌握`str | None`是“字符串
  或None”的联合类型，并混淆了pytest行为测试与Ruff格式检查的职责。
- 补强后复述通过：能确认`str | None`同时接受字符串和None，并能区分pytest行为
  测试与Ruff格式化职责。
- 本课提交：`5ef008b fix: allow document responses without content`，包含Schema最小
  修复、回归测试和学习记录；提交后工作区干净。
- 第2课提交：`1c07722 test: define document not-found response contract`，固定404状态、
  响应内容和请求追踪ID。
- 第3课提交：`4cdcaf5 test: define missing-field validation contract`，固定缺少必填字段
  时的422、错误类型、字段位置和Request ID。

### 掌握验证

| 验证项 | 结果 | 证据 |
|---|---|---|
| 不看答案解释 | 通过 | 能判断创建输入必填、数据库和输出允许None |
| 独立实现同类功能 | 通过 | 完成最小类型修改并保持其他契约不变 |
| 独立定位故障 | 通过 | 根据ValidationError确认响应Schema拒绝None |
| 独立迁移到相似场景并测试 | 未通过 | 尚未进行 |

### 当前结论

- 掌握状态：学习中
- 已经掌握：使用失败测试证明契约冲突，完成最小修复、回归测试和格式检查。
- 仍不理解：阶段1的迁移验证和统一异常契约尚未完成。
- 下一步补强：提交当前独立修复，再进入HTTP错误响应。

## 2026-07-05：阶段1 / 第2课 / 404错误链路

### 本课目标

- 区分“资源不存在”与“服务器异常”。
- 跟踪Repository返回None后如何转换为HTTP 404。
- 观察FastAPI当前错误响应，不提前建立复杂异常框架。

### 阅读与修改

- 阅读文件：`backend/app/api/document.py`、`backend/app/services/document_service.py`、
  `backend/app/repositories/document_repository.py`、
  `backend/tests/integration/test_documents.py`
- 修改文件：尚未修改应用代码。
- 独立编写内容：尚未开始。
- 使用的提示级别：问题说明。
- 第几次尝试通过：进行中。
- 对应Commit Hash：进行中。

### 数据流复述

```text
Repository使用first()查询
→ 没有记录时返回None
→ Service保持返回None
→ API判断record is None
→ 抛出HTTPException 404
→ FastAPI生成404响应
```

### 上下文检查

不适用：本课处理普通HTTP错误契约。

### 验证证据

- 现有集成测试删除文档后再次查询，并断言HTTP状态码为404。
- 当前API使用`HTTPException(status_code=404, detail="document not found")`。
- 理解验证：学习者能说明资源不存在应返回404，500用于预期外服务器故障。
- 术语修正：必须明确说`None`，不能把`None`、空字符串和空列表统称为“空”。
- 集成测试第1次：目标测试、完整测试和Ruff均通过，但diff检查发现只新增了
  `X-Request-ID`断言，遗漏`{"detail": "document not found"}`响应体断言。
- 教训：测试通过只说明现有断言成立，不能证明需求中的所有检查都已编写。
- 集成测试第2次：补齐404响应JSON后，目标测试`1 passed`、完整测试`4 passed`、
  Ruff通过；最终同时验证状态码、错误内容和`X-Request-ID`。
- 最终复述通过：API负责把`None`转换为HTTP 404；Service不依赖HTTP，便于被API、
  Worker或工作流复用；Request ID用于将用户失败请求关联到具体日志。

### 掌握验证

| 验证项 | 结果 | 证据 |
|---|---|---|
| 不看答案解释 | 通过 | 能复述None到HTTP 404的转换和404/500区别 |
| 独立实现同类功能 | 通过 | 扩展现有集成测试验证错误响应契约 |
| 独立定位故障 | 通过 | 通过diff发现绿色测试遗漏响应体断言并补齐 |
| 独立迁移到相似场景并测试 | 通过 | 复用健康检查中的Request ID断言到404响应 |

### 当前结论

- 掌握状态：已掌握
- 已经掌握：404错误链路、HTTP边界，以及状态码、响应体和追踪ID测试。
- 仍不理解：阶段1还需要学习Pydantic请求校验产生的422响应。
- 下一步补强：提交本课测试，再观察非法请求如何在进入API函数前被拒绝。

## 2026-07-05：阶段1 / 第3课 / Pydantic请求校验与422

### 本课目标

- 理解请求Schema是进入API函数前的信任边界。
- 区分合法JSON与符合业务字段契约的JSON。
- 使用集成测试观察缺少必填字段时的422响应。

### 阅读与修改

- 阅读文件：`backend/app/schemas/document.py`、`backend/app/api/document.py`
- 修改文件：尚未修改。
- 独立编写内容：尚未开始。
- 使用的提示级别：概念说明。
- 第几次尝试通过：进行中。
- 对应Commit Hash：进行中。

### 数据流复述

```text
合法JSON请求
→ FastAPI构造DocumentCreate
→ 缺少content导致Pydantic校验失败
→ 返回422
→ API函数、Service、Repository均不执行
→ 数据库不新增记录
```

### 上下文检查

不适用：本课处理普通HTTP输入校验。

### 验证证据

- `DocumentCreate`要求`name`、`content`和`source`都是字符串。
- FastAPI在调用`create_document()`之前使用`DocumentCreate`校验请求体。
- 理解验证：学习者能判断缺少`content`返回422，后续函数和数据库写入不会发生。
- 术语修正：请求是合法JSON，但不符合Schema，不应称为JSON格式错误。
- 观察测试：缺少`content`时响应`detail[0]`包含`type="missing"`、
  `loc=["body", "content"]`、`msg="Field required"`和原始输入。
- 当前测试已断言422和`X-Request-ID`，临时`print()`仅用于观察，最终测试应删除。
- `loc`术语：location路径`["body", "content"]`表示错误位于请求体的`content`字段。
- 测试整理第1次：误将422和Request ID断言注释，导致测试只检查detail；注释代码
  不是删除，也不应为了增加新断言而移除原有必要契约。
- 最终测试结构：同时验证422、`X-Request-ID`、错误类型`missing`和错误位置
  `["body", "content"]`，临时打印与注释已删除。
- 最终验证：完整测试`5 passed in 0.37s`，Ruff检查通过，两个退出码均为`0`。
- 完整错误JSON判断修正：测试不锁死`msg`和`input`，因为文字可能随Pydantic版本
  变化，原始输入也可能包含敏感或与目标无关的数据。
- 迁移验证：能判断缺少`source`时`type`仍为`missing`但位置变为
  `["body", "source"]`；缺少`name`时位置为`["body", "name"]`。

### 掌握验证

| 验证项 | 结果 | 证据 |
|---|---|---|
| 不看答案解释 | 通过 | 能复述Schema校验失败后停止后续调用 |
| 独立实现同类功能 | 通过 | 新增缺少必填字段的422集成测试 |
| 独立定位故障 | 通过 | 根据detail定位请求体content字段缺失 |
| 独立迁移到相似场景并测试 | 通过 | 能将type与loc规则迁移到source和name字段 |

### 当前结论

- 掌握状态：已掌握
- 已经掌握：422发生位置、稳定错误字段、集成测试和字段位置迁移。
- 仍不理解：阶段1还需要学习“字符串存在但为空”的边界校验。
- 下一步补强：提交本课，再验证空字符串是否会绕过当前Schema。

## 2026-07-05 至 2026-07-06：阶段1 / 第4课 / 空字符串边界

### 本课目标

- 区分缺少字段、空字符串和只包含空格的字符串。
- 证明普通`str`类型不会自动拒绝空字符串。
- 在请求信任边界增加最小有效内容约束。

### 阅读与修改

- 阅读文件：`backend/app/schemas/document.py`、
  `backend/tests/integration/test_documents.py`
- 修改文件：`backend/app/schemas/document.py`、
  `backend/tests/integration/test_documents.py`
- 独立编写内容：创建和更新接口的空白内容参数化测试、共享`NonBlankStr`约束、
  更新失败后的数据库内容保持断言。
- 使用的提示级别：问题说明、约束语法提示、测试审查。
- 第几次尝试通过：创建测试先正确失败；更新测试先出现1次收集错误，修正后正确
  失败；加入共享约束后通过。
- 对应Commit Hash：进行中。

### 数据流复述

```text
content键存在
→ DocumentCreate或DocumentUpdate执行NonBlankStr校验
→ 先去除首尾空格
→ 去除后长度小于1则返回422
→ 路由函数、Service和Repository均不执行
→ 数据库不新增文档，也不修改已有文档
```

### 上下文检查

不适用：本课处理普通API输入边界。

### 验证证据

- 当前`DocumentCreate.content`仅声明为`str`。
- Python中的`""`仍然是字符串，因此当前类型检查预计会接受。
- 预测验证：学习者能判断当前接口预计返回200，但业务规则应该拒绝空内容。
- 失败测试：`test_create_document_rejects_empty_content`期望422，实际得到200，
  pytest显示`assert 200 == 422`，退出码为`1`。
- 结论：测试已经证明当前`DocumentCreate`错误接受空字符串并执行后续保存。
- 参数化验证：同一测试分别使用`""`和`"   "`，两个用例均实际返回200并失败，
  结果为`2 failed, 2 deselected`。
- 当前环境验证：Pydantic 2.13.4的`StringConstraints(strip_whitespace=True,
  min_length=1)`接受普通文本，并以`string_too_short`拒绝空字符串和纯空格字符串。
- 约束理解：`"  hello  "`会规范化为`"hello"`；创建和更新输入都应拒绝空白内容。
- 输出边界：`DocumentOut.content`不应用非空输入约束，因为待处理上传记录允许None，
  且输出层不应为了通过响应校验而改写数据库已有值。
- 更新测试第1次：pytest在收集阶段报错`function uses no argument 'content'`；装饰器
  声明了`content`参数，但测试函数签名没有接收，且PUT仍使用固定空字符串。
- 测试审查还发现：不应在获得422实际响应前猜测Pydantic错误类型；更新后的内容应
  通过JSON字段比较，不应直接比较HTTP响应的原始字节`response.content`。
- 最小修复：`DocumentCreate.content`和`DocumentUpdate.content`共享
  `NonBlankStr`；`DocumentOut.content`继续使用`str | None`。
- 绿色验证：创建和更新接口的4个空白内容用例全部通过，结果为
  `4 passed, 2 deselected`。
- 错误契约验证：空白内容返回422，错误类型为`string_too_short`，字段位置为
  `["body", "content"]`，并包含`X-Request-ID`。
- 状态一致性验证：非法更新后重新查询文档，原始`content`保持不变。
- 全量回归：`9 passed in 0.71s`。
- 静态检查：`ruff check backend\app backend\tests`返回`All checks passed!`。
- 差异检查：`git diff --check`退出码为0；CRLF信息是Windows换行符提示，不是
  校验失败。

### 掌握验证

| 验证项 | 结果 | 证据 |
|---|---|---|
| 不看答案解释 | 通过 | 能解释先去除空格，再用最小长度拒绝空白内容 |
| 独立实现同类功能 | 通过 | 为创建和更新接口编写参数化测试并完成约束 |
| 独立定位故障 | 通过 | 用失败测试证明空字符串绕过当前Schema |
| 独立迁移到相似场景并测试 | 通过 | 将创建规则迁移到更新接口，并验证原数据不变 |

### 当前结论

- 掌握状态：已掌握
- 已经掌握：普通`str`与业务有效字符串的区别、Pydantic字符串约束、参数化测试、
  422错误结构、请求校验失败后的状态一致性。
- 仍不理解：本课暂无未解决问题。
- 下一步补强：提交本课变更，再按阶段1计划进入下一课。
