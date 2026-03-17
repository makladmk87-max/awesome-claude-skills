---
name: ccpm-context-prime
description: Load all CCPM project context files into the current conversation. Run at the start of every session to give Claude full project understanding before working on tasks. Part of the CCPM spec-driven development workflow.
---

# CCPM: Context Prime

Load project context files into the current conversation for accurate, context-aware assistance.

## Usage

```
/context:prime
```

Run this at the **start of every session** before working on any tasks.

## Instructions

### Preflight

- Check `.claude/context/` exists
- Validate file integrity: readable, non-empty, has valid frontmatter
- Check `git status` and current branch

### Load Files in Priority Order

**Priority 1 (load first — critical context):**
1. `project-overview.md`
2. `project-brief.md`
3. `tech-context.md`

**Priority 2 (important context):**
4. `progress.md`
5. `project-structure.md`

**Priority 3 (supplementary):**
6. `system-patterns.md`
7. `product-context.md`
8. `project-style-guide.md`
9. `project-vision.md`

### Validation Per File

For each file, parse and validate:
- `created` — valid ISO 8601 date
- `last_updated` — valid ISO 8601 date
- `version` — semantic version string
- Track success/failure per file

### Supplementary Loading

After context files, also read:
- Any untracked files in `.claude/context/`
- `README.md` (if present)
- `.env.example` (if present)

### Error Recovery

| Missing File | Recovery Action |
|---|---|
| `project-overview.md` | Use `README.md` as fallback |
| `tech-context.md` | Analyze config files directly |
| `progress.md` | Check recent git commits |

### Output

```
✅ Context Loaded

Project: {project_name}
Type: {project_type}
Language: {primary_language}
Status: {current_status}
Branch: {current_branch}

Files loaded:
  ✓ project-overview.md   (updated {X} days ago)
  ✓ project-brief.md      (updated {X} days ago)
  ✓ tech-context.md       (updated {X} days ago)
  ✓ progress.md           (updated {X} days ago)
  ✓ project-structure.md  (updated {X} days ago)
  ✓ system-patterns.md    (updated {X} days ago)
  ✓ product-context.md    (updated {X} days ago)
  ✓ project-style-guide.md (updated {X} days ago)
  ✓ project-vision.md     (updated {X} days ago)

Warnings:
  ⚠️ tech-context.md last updated 30+ days ago — consider /context:update

{2-3 sentence summary of the project and current focus}

Ready to assist with: {project_name}
```

## Notes

Context files that are outdated (>7 days) will trigger a warning. Run `/context:update` periodically to keep context accurate.
