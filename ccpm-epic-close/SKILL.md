---
name: ccpm-epic-close
description: Mark a CCPM epic as complete, close the GitHub issue, and optionally archive the epic directory. Use when all tasks in an epic are done. Part of the CCPM spec-driven development workflow.
---

# CCPM: Epic Close

Mark an epic as complete when all tasks are done.

## Usage

```
/pm:epic-close <epic_name>
```

## Instructions

### 1. Verify All Tasks Complete

Check all task files in `.claude/epics/$ARGUMENTS/`:
- Each task must have `status: closed` in frontmatter
- If any open tasks found, output and stop:
  ```
  ❌ Cannot close epic. Open tasks remain:
     - #{task_id}: {task_name}
  ```

### 2. Update Epic Status

Get current datetime: `date -u +"%Y-%m-%dT%H:%M:%SZ"`

Update `epic.md` frontmatter:
```yaml
status: completed
progress: 100%
updated: {current_datetime}
completed: {current_datetime}
```

### 3. Update PRD Status

If epic references a PRD, update `.claude/prds/{prd_name}.md`:
```yaml
status: complete
```

### 4. Close on GitHub

If epic has a GitHub issue:
```bash
gh issue close {epic_issue_number} --comment "✅ Epic completed - all tasks done"
```

### 5. Archive Option

Ask user: "Archive completed epic? (yes/no)"

If yes:
```bash
mkdir -p .claude/epics/.archived/
mv .claude/epics/$ARGUMENTS .claude/epics/.archived/$ARGUMENTS
```

Create `.claude/epics/.archived/$ARGUMENTS/archive-summary.md`:
```markdown
# Archive: {epic_name}

Completed: {current_datetime}
Tasks completed: {count}
Duration: {days from created to completed}
```

### 6. Output

```
✅ Epic closed: $ARGUMENTS
  Tasks completed: {count}
  Duration: {days} days
  GitHub: Issue #{number} closed

{If archived}: Archived to .claude/epics/.archived/

Next: Run /pm:next to see priority work
```

## Notes

Only close epics where all tasks are truly complete. Preserve all data when archiving — the archive is a historical record, not a trash bin.
