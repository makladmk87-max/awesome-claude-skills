---
name: ccpm-issue-start
description: Launch parallel agents to begin work on a GitHub issue tracked by CCPM. Creates a git worktree, assigns the issue, and spawns scoped agents with file pattern assignments. Use when ready to implement a CCPM task. Part of the CCPM spec-driven development workflow.
---

# CCPM: Issue Start

Launch parallel agents to implement a GitHub issue using git worktrees.

## Usage

```
/pm:issue-start <issue_number>
```

## Instructions

### 1. Validate Issue

```bash
gh issue view $ARGUMENTS --json number,title,state,labels,assignees
```

- Confirm issue exists and is open
- Verify it has the `task` label
- Confirm it's not already assigned

### 2. Find Local Task File

- First check: `.claude/epics/*/$ARGUMENTS.md` (issue number as filename)
- Fallback: search for `github:.*issues/$ARGUMENTS` in frontmatter

If not found: "❌ No local task file for issue #$ARGUMENTS. Run /pm:import first."

### 3. Verify Prerequisites

Check that an analysis file exists for the issue — agents need this context to proceed.

### 4. Create Git Worktree

```bash
# Create isolated workspace for this issue
git worktree add ../issue-$ARGUMENTS -b issue/$ARGUMENTS
```

Create workspace directories:
```bash
mkdir -p .claude/epics/{epic_name}/updates/$ARGUMENTS/
```

### 5. Assign Issue

```bash
gh issue edit $ARGUMENTS --add-assignee "@me"
gh issue edit $ARGUMENTS --add-label "in-progress"
```

### 6. Spawn Parallel Agents

Analyze the task file and split work into file-scoped agents:

```yaml
Agent assignments:
  - Agent 1: Frontend files (src/components/**, src/pages/**)
  - Agent 2: Backend files (src/api/**, src/services/**)
  - Agent 3: Tests (tests/**, **/*.test.ts)
```

Each agent operates with:
- File pattern scope (prevents conflicts)
- Issue context from task file
- Progress tracking instructions
- Commit message format: `feat: {description} (fixes #$ARGUMENTS)`

### 7. Agent Coordination Rules

- Agents commit frequently (every logical unit of work)
- Agents write progress updates to `.claude/epics/{epic}/updates/$ARGUMENTS/`
- Agents must not modify files outside their assigned patterns
- Blocking issues are reported immediately to coordinator

### 8. Output

```
🚀 Starting issue #$ARGUMENTS: {issue_title}

Worktree: ../issue-$ARGUMENTS
Branch: issue/$ARGUMENTS

Agents spawned:
  Agent 1 → {file_patterns}
  Agent 2 → {file_patterns}

Progress: .claude/epics/{epic}/updates/$ARGUMENTS/
```

## Notes

Uses git worktrees to prevent merge conflicts when multiple issues are in progress simultaneously. Run `/pm:issue-sync $ARGUMENTS` periodically to post progress to GitHub.
