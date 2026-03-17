---
name: ccpm-issue-sync
description: Post progress updates from local CCPM task files to the GitHub issue as a structured comment. Use periodically while working on an issue to keep GitHub up to date. Part of the CCPM spec-driven development workflow.
---

# CCPM: Issue Sync

Sync local task progress to GitHub as a structured comment.

## Usage

```
/pm:issue-sync <issue_number>
```

## Instructions

### 1. Validate

- Verify git remote is not `automazeio/ccpm`
- Check GitHub CLI authentication: `gh auth status`
- Confirm issue exists: `gh issue view $ARGUMENTS`

### 2. Find Local Files

- Task file: `.claude/epics/*/$ARGUMENTS.md` or search by `github:` frontmatter field
- Progress file: `.claude/epics/{epic}/updates/$ARGUMENTS/progress.md`
- Recent update files: `.claude/epics/{epic}/updates/$ARGUMENTS/`

### 3. Detect Changes

- Read local task file and progress notes
- Check recent git commits referencing issue #$ARGUMENTS
- Compare `last_sync` timestamp to current state

### 4. Format Progress Comment

```markdown
## Progress Update — {timestamp}

**Status:** {current_status}
**Completion:** {percentage}%

### Completed This Session
{what was done}

### Acceptance Criteria
- [x] {completed criterion}
- [ ] {pending criterion}

### Technical Notes
{implementation details, decisions made}

### Recent Commits
- `{hash}` {commit_message}

### Next Steps
{what's remaining}

---
*Synced via CCPM at {timestamp}*
<!-- ccpm-sync-marker:{timestamp} -->
```

### 5. Post to GitHub

```bash
# Check for duplicate (look for ccpm-sync-marker)
gh issue view $ARGUMENTS --json comments | grep "ccpm-sync-marker"

# Post comment (avoid duplicates within 5 minutes)
gh issue comment $ARGUMENTS --body-file /tmp/progress-comment.md
```

Handle GitHub limits: truncate body at 65000 characters if needed.

### 6. Update Timestamps

Update `last_sync` in:
- Task file frontmatter
- Progress file frontmatter
- Epic file frontmatter (if progress changed)

### 7. Output

```
✅ Synced issue #$ARGUMENTS
  Comment posted to GitHub
  Progress: {percentage}%
  Last sync: {timestamp}
```

## Notes

Prevents duplicate comments using sync markers. Enforces a minimum 5-minute cooldown between syncs. Handles GitHub API rate limiting with exponential backoff.
