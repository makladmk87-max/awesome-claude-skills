---
name: ccpm-issue-close
description: Mark a CCPM task as complete, close the GitHub issue, and update epic progress. Use when implementation of an issue is done and acceptance criteria are met. Part of the CCPM spec-driven development workflow.
---

# CCPM: Issue Close

Mark a task complete, close the GitHub issue, and update epic progress.

## Usage

```
/pm:issue-close <issue_number> [completion_notes]
```

## Instructions

### 1. Find Local Task File

- Check `.claude/epics/*/$ARGUMENTS.md` (issue number as filename)
- Fallback: search for `github:.*issues/$ARGUMENTS` in frontmatter
- If not found: "❌ No local task for issue #$ARGUMENTS"

### 2. Update Local Status

```bash
date -u +"%Y-%m-%dT%H:%M:%SZ"
```

Update task file frontmatter:
```yaml
status: closed
updated: {current_datetime}
```

### 3. Update Progress File

If `.claude/epics/{epic}/updates/$ARGUMENTS/progress.md` exists:
- Set completion: 100%
- Add completion note with timestamp
- Update `last_sync` field

### 4. Close on GitHub

```bash
# Add completion comment
echo "✅ Task completed

{completion_notes if provided}

---
Closed at: {timestamp}" | gh issue comment $ARGUMENTS --body-file -

# Close the issue
gh issue close $ARGUMENTS
```

### 5. Update Epic Checklist on GitHub

```bash
# Get epic name from local file path
# Get epic issue number from epic.md frontmatter
epic_issue=$(grep 'github:' .claude/epics/{epic_name}/epic.md | grep -oE '[0-9]+$')

if [ ! -z "$epic_issue" ]; then
  gh issue view $epic_issue --json body -q .body > /tmp/epic-body.md
  sed -i "s/- \[ \] #$ARGUMENTS/- [x] #$ARGUMENTS/" /tmp/epic-body.md
  gh issue edit $epic_issue --body-file /tmp/epic-body.md
fi
```

### 6. Update Epic Progress

- Count total tasks in epic directory
- Count tasks with `status: closed`
- Calculate progress percentage
- Update `epic.md` frontmatter `progress` field

### 7. Output

```
✅ Closed issue #$ARGUMENTS
  Local: Task marked complete
  GitHub: Issue closed & epic checklist updated
  Epic progress: {new_progress}% ({closed}/{total} tasks)

Next: Run /pm:next for the next priority task
```

## Notes

Follow `/rules/frontmatter-operations.md` for file updates. Always sync local state before updating GitHub. Run `/pm:epic-close {epic_name}` when all tasks in the epic are done.
