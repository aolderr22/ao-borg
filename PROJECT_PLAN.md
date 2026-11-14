# AI Software Engineering Agent (AI-SEA)
## High-Level Project Plan

### 1. Project Objective

Build an intelligent AI software engineering agent that can understand an existing software repository, interpret business feature requests, reduce requirements uncertainty, analyze potential code changes, and assist with implementation and verification.

The project aims to explore and develop practical AI engineering capabilities using agentic workflows, retrieval-augmented generation (RAG), context engineering, and software engineering automation.

### 2. Initial Technology Stack

| Component | Technology |
|---|---|
| Programming Language | Python |
| LLM | Microsoft Azure AI Foundry |
| Agent Orchestration | LangGraph |
| API Framework | FastAPI |
| Codebase Parsing | Tree-sitter |
| Embeddings | Azure embedding model |
| Vector Search | Azure AI Search |
| Workflow Persistence | PostgreSQL (later phase) |
| Source Control | Git |
| Testing | Pytest |
| Observability | OpenTelemetry / LangSmith |

Technology choices may evolve as the project develops. Additional Azure infrastructure should only be introduced when necessary, with particular attention to operating costs.

---

### 3. Development Phases

#### Phase 1 — Project Foundation

Establish the application architecture and development environment.

Tasks:
- Create the Python repository.
- Configure Azure AI Foundry and model deployment.
- Establish FastAPI endpoints.
- Configure environment variables and logging.
- Connect to a sample Git repository.

**Deliverable:** A running Python application that can communicate with an LLM and receive software feature requests.

#### Phase 2 — Codebase Understanding

Teach the agent to understand an existing software application.

Tasks:
- Read and process repository files.
- Identify programming languages and frameworks.
- Extract classes, functions, and dependencies.
- Build a searchable codebase index.
- Retrieve relevant source code based on a feature request.

**Deliverable:** An agent that can answer questions about an existing codebase using actual source code as context.

#### Phase 3 — Requirements Engineering

Develop the agent's ability to understand business requirements and identify uncertainty.

Tasks:
- Accept a business feature request.
- Analyze functional requirements.
- Identify ambiguity and missing information.
- Generate clarifying questions.
- Accept human responses.
- Maintain an updated requirements specification.

**Deliverable:** An agent capable of conducting an iterative requirements clarification process.

#### Phase 4 — Impact Analysis

Determine which parts of the existing application may be affected by a proposed feature.

Tasks:
- Identify relevant source files.
- Analyze dependencies.
- Identify affected classes, functions, and APIs.
- Identify potential database changes.
- Detect possible regressions.
- Explain the reasoning behind its findings.

**Deliverable:** A structured impact analysis report.

#### Phase 5 — Implementation Planning

Convert approved requirements into an actionable development plan.

Tasks:
- Break features into development tasks.
- Identify files requiring modification.
- Recommend architectural changes.
- Identify necessary tests.
- Document implementation assumptions.
- Request human approval.

**Deliverable:** An implementation plan ready for developer review.

#### Phase 6 — Code Generation

Allow the agent to assist with software implementation.

Tasks:
- Generate code suggestions.
- Propose file modifications.
- Generate unit tests.
- Explain implementation decisions.
- Produce changes in an isolated Git branch.

**Deliverable:** Agent-generated code changes that a human can inspect before merging.

#### Phase 7 — Testing and Verification

Evaluate whether the generated implementation satisfies the requirements.

Tasks:
- Execute tests in an isolated environment.
- Analyze test failures.
- Identify regressions.
- Compare implementation against requirements.
- Produce a verification report.

**Deliverable:** A report detailing implementation correctness, test results, and outstanding issues.

#### Phase 8 — Advanced Agent Orchestration

Introduce more sophisticated agentic capabilities.

Tasks:
- Separate specialized agents where beneficial.
- Introduce persistent workflow state.
- Add semantic and episodic memory where useful.
- Implement agent handoffs.
- Add observability and evaluation.
- Improve error recovery and cost management.

**Deliverable:** An advanced AI software engineering system capable of managing longer development workflows.

---

### 4. High-Level Agent Architecture

The initial implementation will use a single LangGraph workflow with specialized nodes.

Proposed workflow:

1. Feature Request
2. Repository Analyzer
3. Codebase Retrieval
4. Requirements Analyst
5. Requirements Clarification
6. Human Feedback
7. Impact Analyzer
8. Implementation Planner
9. Human Approval
10. Code Generation
11. Testing and Verification
12. Engineering Report

The workflow must support:
- Shared state between workflow nodes.
- Human-in-the-loop interactions.
- Conditional execution and branching.
- Error handling and retries.
- Persistent workflow checkpoints.
- Structured outputs.

**Architectural principle:** Begin with a single orchestrated workflow. Introduce multiple specialized agents only when their separation provides a measurable benefit.

---

### 5. Data and Memory Architecture

The agent will eventually maintain several categories of information.

| Information | Purpose |
|---|---|
| Repository Index | Understand and retrieve source code |
| Requirements Specification | Preserve agreed business requirements |
| Working Memory | Track the current development task |
| Episodic Memory | Retain previous workflow experiences |
| Semantic Memory | Retrieve reusable engineering knowledge |
| Impact Analysis | Preserve identified dependencies |
| Implementation History | Track proposed and approved changes |

These capabilities should be introduced progressively rather than implemented all at once.

Initially, LangGraph state and checkpointing should handle the workflow's working state.

---

### 6. Evaluation and Success Metrics

The project should be evaluated using measurable engineering criteria.

| Capability | Evaluation |
|---|---|
| Codebase Understanding | Accuracy of answers about repository contents |
| Requirements Analysis | Number of meaningful ambiguities identified |
| Requirements Clarification | Ability to discover missing requirements |
| Impact Analysis | Precision of affected-file identification |
| Implementation Planning | Completeness of proposed tasks |
| Code Generation | Test pass rate and requirement compliance |
| Verification | Ability to detect implementation defects |

A benchmark dataset of approximately 20 predefined feature requests can be created to evaluate the agent's performance.

Results should be tracked as the system evolves.

---

### 7. Project Milestones

**Milestone 1 — Repository-Aware AI Assistant**

Complete Phases 1–2.

Outcome: The agent understands an existing codebase and can answer questions about it.

**Milestone 2 — Requirements and Analysis Agent**

Complete Phases 3–4.

Outcome: The agent asks clarifying questions, maintains requirements, and produces impact analysis.

**Milestone 3 — AI Implementation Assistant**

Complete Phases 5–7.

Outcome: The agent proposes implementation changes, generates code, and verifies results.

**Milestone 4 — Advanced Agentic Engineering System**

Complete Phase 8.

Outcome: Improved orchestration, memory, observability, and autonomy.

---

### 8. Initial MVP Scope

The first working version should concentrate on three capabilities:

1. Accept a software feature request.
2. Examine a code repository and generate clarifying questions.
3. Produce a structured requirements document based on the request and human responses.

Once these capabilities work reliably, introduce impact analysis.

Avoid premature architectural complexity and unnecessary infrastructure.

---

### 9. Overall Learning Objectives

Through this project, develop practical experience in:

- AI application engineering.
- Agentic workflows and orchestration.
- LangGraph and state management.
- Retrieval-augmented generation.
- Codebase indexing and retrieval.
- Context engineering and prompt design.
- Requirements engineering.
- Software architecture and impact analysis.
- Human-in-the-loop systems.
- Code generation and verification.
- LLM evaluation and observability.
- Persistent agent memory.

### 10. Guiding Principle

Build a reliable AI software engineering assistant incrementally.

Prioritize understanding, requirements clarification, and impact analysis before introducing autonomous implementation.

The ultimate goal is to develop an agent that can participate meaningfully in the software development lifecycle while keeping the human engineer responsible for requirements, architectural judgment, and final implementation approval.