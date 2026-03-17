---
name: ccpm-epic-sync
description: Push a CCPM epic and its tasks to GitHub as issues with proper labels and sub-issue relationships. Use after decomposing an epic to create GitHub issues and a git worktree for parallel development. Part of the CCPM spec-driven development workflow.
---

# CCPM: Epic Sync

Push an epic and its task files to GitHub as issues, then create a git worktree for parallel development.

## Usage

```
/pm:epic-sync <epic_name>
```

## Instructions

### 0. Guard Check

Exit with error if the git remote URL matches `automazeio/ccpm` — this command must not be run on the template repository.

### 1. Create Epic Issue

```bash
# Detect repo from git remote
gh repo view --json nameWithOwner -q .nameWithOwner

# Create epic issue with labels
gh issue create \
  --title "{epic_name}" \
  --body "{epic content without frontmatter, Tasks section replaced with Stats}" \
  --label "epic,epic:$ARGUMENTS,feature"
```

### 2. Create Task Sub-Issues

Check for `gh-sub-issue` extension:
```bash
gh extension list | grep sub-issue
```

**Small batches (<5 tasks):** Create sequentially
**Larger batches:** Use parallel Task agents

For each task:
```bash
gh issue create \
  --title "{task_name}" \
  --body "{task_content}" \
  --label "task,epic:$ARGUMENTS"
```

### 3. Rename Task Files

After creating issues, rename local files from sequential numbers to GitHub issue IDs:
- `001.md` → `{issue_id}.md`
- Update `depends_on` and `conflicts_with` references to use new issue IDs
- Update `github` URL and `updated` timestamp in each task's frontmatter

### 4. Link Sub-Issues to Epic

If `gh-sub-issue` extension available:
```bash
gh sub-issue add {epic_number} {task_number}
```

Otherwise, append task checklist to epic issue body:
```markdown
## Tasks
- [ ] #{task1_number} Task 1 Name
- [ ] #{task2_number} Task 2 Name
```

### 5. Update Epic File

Update `.claude/epics/$ARGUMENTS/epic.md` frontmatter:
```yaml
github: https://github.com/{org}/{repo}/issues/{epic_number}
updated: {current_datetime}
```

Rewrite "Tasks Created" section with real GitHub issue IDs.

### 6. Create GitHub Mapping File

Create `.claude/epics/$ARGUMENTS/github-mapping.md`:
```markdown
# GitHub Issue Mapping

Epic: #{epic_number}

| Task File | Issue Number | URL |
|-----------|--------------|-----|
| {old_id}.md | #{issue_id} | {url} |
```

### 7. Create Git Worktree

```bash
git worktree add ../epic-$ARGUMENTS -b epic/$ARGUMENTS
```

### 8. Output

```
✅ Epic synced: $ARGUMENTS
  Epic: #{epic_number}
  Tasks: {count} issues created
  Labels: epic, epic:$ARGUMENTS
  Files renamed: {count}
  Worktree: ../epic-$ARGUMENTS

Next: Run /pm:issue-start {issue_number} to begin work
```

## Notes

Follow `/rules/github-operations.md` for GitHub CLI commands. Rename task files immediately after issue creation to keep local and remote in sync.
