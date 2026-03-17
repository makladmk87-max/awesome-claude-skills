---
name: ccpm-import
description: Import existing GitHub issues into the CCPM local workspace. Use to bring existing issues into the CCPM system when setting up a project or when issues were created outside of CCPM. Part of the CCPM spec-driven development workflow.
---

# CCPM: Import

Import existing GitHub issues into the local CCPM workspace.

## Usage

```
/pm:import [--epic <epic_name>] [--label <label>]
```

**Options:**
- `--epic` — Import into a specific epic
- `--label` — Import only issues with a specific label
- No args — Import all untracked issues

## Instructions

### 1. Fetch GitHub Issues

```bash
# Filtered by label
gh issue list --label "{label}" --limit 1000 \
  --json number,title,body,state,labels,createdAt,updatedAt

# All issues
gh issue list --limit 1000 \
  --json number,title,body,state,labels,createdAt,updatedAt
```

### 2. Identify Untracked Issues

For each GitHub issue:
- Search local `.claude/epics/` for matching `github:` URL
- If not found → issue is untracked and needs import

### 3. Categorize Issues

Based on labels:
- `epic` label → Create epic structure
- `task` label → Create task in appropriate epic
- `epic:{name}` label → Assign to that named epic
- No PM labels → Ask user or create in `imported` epic

### 4. Create Local Structure

**For Epic issues:**
```bash
mkdir -p .claude/epics/{epic_name}
# Create epic.md with GitHub content and frontmatter
```

**For Task issues:**
```bash
# Find next available number: 001.md, 002.md, etc.
# Create task file with GitHub content
```

**Frontmatter for imported files:**
```yaml
name: {issue_title}
status: {open|closed based on GitHub state}
created: {GitHub createdAt}
updated: {GitHub updatedAt}
github: https://github.com/{org}/{repo}/issues/{number}
imported: true
```

### 5. Output

```
📥 Import Complete

Imported:
  Epics: {count}
  Tasks: {count}

Created structure:
  {epic_1}/
    - {count} tasks
  {epic_2}/
    - {count} tasks

Skipped (already tracked): {count}

Next steps:
  Run /pm:status to see imported work
  Run /pm:sync to ensure full synchronization
```

## Important Notes

- Preserve all GitHub metadata in frontmatter
- Mark imported files with `imported: true` flag
- Never overwrite existing local files
- Use `--dry-run` mentally to preview before importing large sets
