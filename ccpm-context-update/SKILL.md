---
name: ccpm-context-update
description: Update CCPM project context files based on recent code changes, new features, or architectural updates. Run at the end of development sessions to keep context accurate. Part of the CCPM spec-driven development workflow.
---

# CCPM: Context Update

Refresh project context documentation based on recent changes.

## Usage

```
/context:update
```

Run at the **end of development sessions** after making significant changes.

## Instructions

### Phase 1: Preflight Validation

- Check `.claude/context/` exists and count files
- Validate each file is readable, non-empty, has valid frontmatter

### Phase 2: Change Detection

Analyze recent changes using a 5-commit window:

```bash
git log --oneline -5
git diff HEAD~5..HEAD --stat
```

Identify:
- New dependencies added/removed
- New files or directories created
- Architecture changes (new services, modules)
- New user-facing features
- Configuration changes

### Phase 3: Strategic Updates

Update only files where content has actually changed:

| File | Update When |
|------|-------------|
| `progress.md` | **Always** — reflects current state |
| `tech-context.md` | Dependencies or versions changed |
| `system-patterns.md` | Architectural changes only |
| `product-context.md` | New user-facing features added |
| `project-structure.md` | New directories or major files added |
| `project-overview.md` | Rarely — only for major pivots |

### Update Methodology

For each file to update:
1. Read existing content fully
2. Identify specific sections to modify
3. **Preserve frontmatter** — only update `last_updated` timestamp
4. Make targeted edits, not rewrites
5. Skip unchanged files entirely

### Validation

After updates:
- Verify frontmatter integrity
- Check minimum file size maintained
- Validate markdown formatting
- Confirm no placeholder text

### Output

```
✅ Context Updated

Files scanned: 9
Updated: {count}
  ✓ progress.md           — current milestone and recent work
  ✓ tech-context.md       — added {new_package} v{version}
Skipped: {count} (no changes detected)
Errors: 0

All timestamps updated to {current_datetime}
```

## Notes

Context updates should be targeted, not wholesale rewrites. The goal is keeping files accurate, not verbose. Outdated context causes Claude to make incorrect assumptions, so run this regularly.
