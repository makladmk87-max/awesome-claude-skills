---
name: ccpm-epic-oneshot
description: Decompose a CCPM epic into tasks AND sync to GitHub in one operation. A convenience wrapper that runs epic-decompose followed by epic-sync. Use when you want to go from epic to GitHub issues in a single step. Part of the CCPM spec-driven development workflow.
---

# CCPM: Epic Oneshot

Decompose an epic into tasks and sync to GitHub in one operation.

## Usage

```
/pm:epic-oneshot <feature_name>
```

## Prerequisites

- `.claude/epics/$ARGUMENTS/epic.md` must exist
- No existing task files (would create duplicates)
- Epic not already synced to GitHub (no `github:` field in frontmatter)

## Instructions

### Step 1: Decompose

Run `/pm:epic-decompose $ARGUMENTS`

This breaks the epic into numbered task files with proper frontmatter, dependencies, and acceptance criteria.

### Step 2: Sync

Run `/pm:epic-sync $ARGUMENTS`

This creates GitHub issues for the epic and all tasks, renames local files to match issue IDs, and creates a git worktree.

## Output

```
🚀 Epic Oneshot Complete

Step 1: Decomposition ✓
  Tasks created: {count}

Step 2: GitHub Sync ✓
  Epic: #{epic_number}
  Sub-issues: {count}
  Worktree: ../epic-$ARGUMENTS

Next: Run /pm:issue-start {issue_number} to begin work on the first task
```

## Notes

This is a convenience wrapper. Both sub-commands handle their own error checking, parallel execution, and validation. If either step fails, run the individual commands to debug.
