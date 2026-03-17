---
name: ccpm-sync
description: Run a full bidirectional sync between local CCPM files and GitHub issues. Pulls updates from GitHub, pushes local changes, and resolves conflicts. Use to keep local and remote state in sync. Part of the CCPM spec-driven development workflow.
---

# CCPM: Sync

Full bidirectional sync between local CCPM workspace and GitHub.

## Usage

```
/pm:sync [epic_name]
```

If `epic_name` is provided, syncs only that epic. Otherwise syncs all epics.

## Instructions

### 1. Pull from GitHub

```bash
# Fetch all epics from GitHub
gh issue list --label "epic" --limit 1000 \
  --json number,title,state,body,labels,updatedAt

# Fetch all tasks from GitHub
gh issue list --label "task" --limit 1000 \
  --json number,title,state,body,labels,updatedAt
```

### 2. Update Local from GitHub

For each GitHub issue with a matching local file:
- Compare `updatedAt` timestamps
- If GitHub is newer: update local frontmatter to match GitHub state
- Update `status`, `updated` fields

### 3. Push Local to GitHub

For each local file:
- If no `github:` URL → create new GitHub issue
- If `updated` timestamp > `last_sync` → push changes via:

```bash
gh issue edit {number} --body "{updated_content}"
```

### 4. Handle Conflicts

If both local and GitHub were updated since last sync:
```
⚠️  Conflict detected for issue #{number}: {title}

Local updated:  {local_timestamp}
GitHub updated: {github_timestamp}

Which version should win?
  [L] Keep local version
  [G] Keep GitHub version
  [M] Merge manually
```

### 5. Update Sync Timestamps

Update `last_sync` in all synced file frontmatter.

### 6. Output

```
🔄 Sync Complete

Updated from GitHub: {count}
Pushed to GitHub:    {count}
New issues created:  {count}
Conflicts resolved:  {count}

Run /pm:status for current project overview
```

## Important Notes

Always backup local state before a full sync. Follow `/rules/github-operations.md` for GitHub CLI commands. For large projects, run epic-scoped syncs to avoid rate limits.
