---
name: NotebookLM RAG Setup
description: How agents should use the NotebookLM MCP tools as a stable knowledge source.
profile: shared
category: architecture
auto-triggers: ["notebooklm", "rag", "knowledge base"]
---

# NotebookLM RAG Skill

> This skill tells agents how to use the NotebookLM MCP as a dynamic Retrieval-Augmented Generation (RAG) system for projects.

---

## 🚀 Core Principles

1.  **Context Preservation**: Loading large documents directly into the IDE context window burns tokens and slows down execution.
2.  **Stable RAG**: By uploading project specs, brand guidelines, and API docs to NotebookLM, you create a "stable" source of truth that agents can query without exhausting their context window.
3.  **One Notebook Per Project**: Whenever starting a complex project, the `project-planner` or `orchestrator` should create a dedicated NotebookLM notebook for it.

---

## 🛠️ Typical Agent Workflow

When a user asks you to implement a large feature that depends on external documentation or project specs:

### Step 1. Initialize Knowledge (Orchestrator / Planner)

If the project doesn't have a notebook yet:

1.  Check existing notebooks: `notebook_list {}`
2.  If none match the project, create one: `notebook_create { title: "Project Alpha Knowledge Base" }`
3.  Add sources to it. If the user provided URLs or file paths:
    - `source_add { notebook_id: "...", source: "https://docs.example.com", is_url: true }`
    - `source_add { notebook_id: "...", source: "/path/to/PRD.md", is_url: false }`

### Step 2. Query Knowledge (Specialist Agents)

Before writing code or answering complex questions:

1.  Query the notebook: `notebook_query { notebook_id: "...", query: "What are the authentication requirements for the API?" }`
2.  Use the returned summary and citations to inform your implementation.

### Step 3. Generate Summaries (Optional)

If the user asks for high-level overviews or marketing assets based on the docs:

1.  Generate a briefing doc: `studio_create { notebook_id: "...", type: "briefingDoc" }`
2.  Wait for generation to finish, then download/display it.

---

## ⚠️ Important Constraints

- **Rate Limits**: The underlying NotebookLM free tier allows ~50 queries per day. _Do not spam queries in a loop._
- **Cookie Expiration**: If an MCP tool returns an "Authentication required" or "Cookie expired" error, inform the user they need to run `nlm login` in their terminal to refresh the auth tokens.
- **Context Window**: This MCP server exposes 29 tools. If you are not actively using NotebookLM, consider asking the user to disable the MCP server (e.g., in Claude Desktop or Cursor settings) to save context tokens.

---

## 🤝 Using with Other Skills

- **`plan-writing`**: When drafting a `task.md` or `implementation_plan.md`, the `project-planner` should first run a `notebook_query` against the project's brand guidelines (`vib.md` or `context.md`) to ensure the plan aligns with the company identity.
- **`brainstorming`**: If the Socratic Gate reveals missing information (e.g., "I don't know the API endpoints"), suggest using `research_start` to build a notebook on that topic.
