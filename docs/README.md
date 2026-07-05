# 项目文档

本目录保存项目设计、学习记录、架构决策、评测和部署说明。设计目标与当前实现
必须分开维护，避免把规划中的能力包装成已经完成。

## 执行与教学主线

[Enterprise Insight Agent：项目实施与工程能力学习指南](project_implementation_learning_guide.md)

这份文档是当前项目唯一的实施和教学主线，包含：

- 当前代码的真实基线
- 筛选后的项目范围
- 分阶段开发顺序
- Agent上下文从内存Demo到生产治理的演进路线
- 每阶段学习目标和验收门槛
- 项目变更规则
- 工程能力毕业标准

两份设计文档用于提供方案参考；发生范围或进度冲突时，以实际源码、测试和这份
实施指南为准。

学习过程与每一步掌握证据记录在：

[学习进度与掌握证据](learning_notes.md)

## 设计文档

### 1. 推荐实现版

[企业级风格多模态多 Agent 工作流系统](design/enterprise_style_multimodal_multi_agent_system.md)

用途：

- 当前项目的主要实现参考
- 控制初版开发范围
- 拆分后端、RAG、Agent、工作流和部署阶段

其中部分内容仍超过当前代码能力。具体实现顺序以源码测试和后续教学计划为准。

### 2. 完整平台参考版

[企业级 AI Multi-Agent Workflow Platform 完整版](design/full_enterprise_ai_multi_agent_platform_design.md)

用途：

- 理解生产系统可能涉及的完整模块
- 记录安全、可靠性、治理和运维方面的长期方向
- 为架构讨论和面试扩展问题提供参考

这份文档不是当前版本的全部开发清单。多租户、复杂控制平面、Kubernetes、
基础设施即代码等能力只有在实际需要时才进入实施范围。

## 后续文档规划

随着代码推进，再按实际内容增加：

```text
docs/
├── architecture.md       # 当前已实现架构和数据流
├── learning_notes.md     # 每一步学习记录
├── error-handling.md     # 异常分类、重试和恢复
├── security.md           # 安全边界和验证
├── evaluation.md         # 标准数据集和评测结果
├── deployment.md         # 部署、备份、恢复和回滚
├── operations-runbook.md # 常见故障和运维处置
├── requirements-traceability.md # 需求、代码和测试对应关系
├── interview-notes.md    # 基于已实现代码的面试问答
└── adr/                  # 重要技术选型记录
```

没有真实内容时不提前创建空文件。
