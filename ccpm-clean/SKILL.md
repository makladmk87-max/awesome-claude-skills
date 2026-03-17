---
name: ccpm-clean
description: Archive completed CCPM epics and remove stale progress files to keep the local workspace tidy. Shows a cleanup plan before making changes. Part of the CCPM spec-driven development workflow.
---

# CCPM: Clean

Archive completed work and remove stale files from the CCPM workspace.

## Usage

```
/pm:clean [--dry-run]
```

Use `--dry-run` to preview what would be cleaned without making changes.

## Instructions

### 1. Identify Completed Epics

Find epics in `.claude/epics/` where:
- `status: completed` in `epic.md` frontmatter
- All task files have `status: closed`
- Last update was more than 30 days ago

### 2. Detect Stale Materials

- Progress files for closed issues
- Update directories for finished work
- Orphaned task files (no matching GitHub issue)
- Empty directories

### 3. Show Cleanup Plan

Before making changes, display what would happen:

```
📋 Cleanup Plan

Epics to archive (3):
  .claude/epics/user-auth/        (completed 45 days ago, 8 tasks)
  .claude/epics/payment-flow/     (completed 32 days ago, 5 tasks)
  .claude/epics/email-templates/  (completed 38 days ago, 3 tasks)

Stale files to remove (12):
  .claude/epics/active-epic/updates/42/   (issue #42 closed 35 days ago)
  ...

Estimated space recovered: ~2.4MB

Proceed? (yes/no)
```

### 4. Archive Process

```bash
mkdir -p .claude/epics/.archived/

# Move completed epics
mv .claude/epics/{epic_name} .claude/epics/.archived/{epic_name}
```

Create archive entry in `.claude/epics/.archived/archive-log.md`:
```markdown
| Epic | Archived | Tasks | Duration |
|------|----------|-------|----------|
| {epic_name} | {date} | {count} | {days} |
```

### 5. Remove Stale Progress Files

```bash
# Remove old update directories for closed issues
rm -rf .claude/epics/{epic}/updates/{closed_issue_id}/
# Remove empty directories
find .claude/epics -type d -empty -delete
```

### 6. Critical Safeguards

- **Never** delete incomplete epics or open tasks
- **Never** delete PRDs
- Archive log preserves historical records
- Dry-run by default for first-time users

### 7. Output

```
✅ Cleanup Complete

Archived epics: {count}
Removed stale files: {count}
Space recovered: {size}

Archive location: .claude/epics/.archived/
```

## Notes

Run periodically to keep the workspace manageable. Archived epics are preserved, not deleted — they can be restored if needed.
