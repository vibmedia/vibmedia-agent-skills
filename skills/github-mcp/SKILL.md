---
name: github-mcp
description: When the user wants to interact with GitHub repositories via MCP (create issues, PRs, list files, search code). Trigger on "github", "create PR", "create issue", "github mcp".
profile: shared
---

# GitHub MCP Skill

> **Authentication Key:** `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`

Use this skill to leverage the GitHub MCP server for repository automation.

## Core Capabilities

| Feature           | Description                                              |
| ----------------- | -------------------------------------------------------- |
| **Issues**        | Create, update, list, and comment on GitHub issues.      |
| **Pull Requests** | Create PRs, review code, and manage branches.            |
| **Code Search**   | Search for code blocks or symbols across the repository. |
| **File Ops**      | Read, create, or update files directly on GitHub.        |

## Usage Patterns

### 1. Creating a Pull Request

After completing a feature locally, use the GitHub MCP to create a remote PR:

1. Ensure changes are pushed to a branch.
2. Call `github.create_pull_request` with title and description.

### 2. Issue Tracking

Sync project tasks with GitHub Issues:

1. Use `github.create_issue` for new tasks found in `telos.md`.
2. Use `github.add_comment` to update progress.

## Global Credentials

The following token is authorized for this workspace:

- **GITHUB_TOKEN:** `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`

> [!IMPORTANT]
> Never expose this token in public PRs or logs. It is for internal agent use via configured MCP tools.
