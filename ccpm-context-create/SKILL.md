---
name: ccpm-context-create
description: Analyze the project codebase and create comprehensive baseline context documentation in .claude/context/. Generates 9 structured files covering project structure, tech stack, patterns, vision, and progress. Use at the start of a project or after major architectural changes.
---

# CCPM: Context Create

Create comprehensive baseline context documentation by analyzing the project codebase.

## Usage

```
/context:create
```

## Instructions

### Preflight Checklist

1. **Context directory check** — `ls -la .claude/context/`; ask before overwriting existing files
2. **Project type detection** — check for `package.json`, `requirements.txt`, `Cargo.toml`, `go.mod`, `pom.xml`, etc.
3. **Directory creation** — `mkdir -p .claude/context/` if missing
4. **Get current datetime** — `date -u +"%Y-%m-%dT%H:%M:%SZ"`

### Project Analysis

Systematically analyze:
- Repository structure and file organization
- Dependencies and tech stack versions
- Existing patterns, conventions, and architecture
- Test coverage and CI/CD setup
- README, docs, and existing documentation

### Files to Create

Create all 9 files in `.claude/context/` with frontmatter:

```yaml
---
created: {ISO_8601_datetime}
last_updated: {ISO_8601_datetime}
version: 1.0.0
author: claude
---
```

**Files:**

1. **`project-overview.md`** — High-level summary, purpose, current state
2. **`project-brief.md`** — Concise project description for onboarding
3. **`project-vision.md`** — Long-term goals and direction
4. **`project-structure.md`** — Directory layout, key files, module organization
5. **`tech-context.md`** — Stack, dependencies, versions, external services
6. **`system-patterns.md`** — Architecture patterns, design decisions, conventions
7. **`product-context.md`** — User-facing features, user flows, product goals
8. **`project-style-guide.md`** — Code style, naming conventions, formatting rules
9. **`progress.md`** — Current milestone, recent work, upcoming tasks

### Quality Validation

For each file, verify:
- Minimum 10 lines of content
- Valid frontmatter
- No placeholder text remaining
- Accurate reflection of actual codebase

### Error Handling

- Permission errors → check directory ownership
- Disk space errors → notify and stop
- Creation failures → report specific file and error

### Output

```
✅ Context Created

Files created: 9
Project type: {detected_type}
Language: {primary_language}
Git status: {branch_and_status}

Files:
  ✓ project-overview.md   ({lines} lines)
  ✓ project-brief.md      ({lines} lines)
  ✓ tech-context.md       ({lines} lines)
  ✓ system-patterns.md    ({lines} lines)
  ✓ product-context.md    ({lines} lines)
  ✓ project-brief.md      ({lines} lines)
  ✓ project-structure.md  ({lines} lines)
  ✓ project-vision.md     ({lines} lines)
  ✓ project-style-guide.md ({lines} lines)
  ✓ progress.md           ({lines} lines)

Next: Run /context:prime to load context into conversation
```

## Notes

Run this once at project start. Update individual files with `/context:update` as the project evolves. The context files help Claude maintain accurate understanding across sessions.
