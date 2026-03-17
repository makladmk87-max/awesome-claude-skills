---
name: ccpm-epic-decompose
description: Break a CCPM epic into concrete, actionable task files with proper dependencies and parallelization flags. Use after creating an epic with /pm:prd-parse to generate individual task files. Part of the CCPM spec-driven development workflow.
---

# CCPM: Epic Decompose

Break an epic into concrete, actionable task files that can be executed by agents.

## Usage

```
/pm:epic-decompose <epic_name>
```

## Instructions

### 1. Validate Epic

- Check `.claude/epics/$ARGUMENTS/epic.md` exists
- Validate frontmatter: `name`, `status`, `created`, `prd`
- If task files already exist, prompt: "Delete existing tasks and re-decompose? (yes/no)"

### 2. Analyze Scope

Read the epic and identify:
- All work units that can be independently executed
- Dependencies between tasks
- Parallelization opportunities
- Risk areas requiring sequential execution

### 3. Create Task Files

Create numbered task files in `.claude/epics/$ARGUMENTS/`:

**Naming:** `001.md`, `002.md`, ... (later renamed to GitHub issue numbers after sync)

**Task frontmatter:**
```yaml
---
name: {task_title}
status: backlog
created: {ISO_8601_datetime}
updated: {ISO_8601_datetime}
depends_on: [002, 003]  # task numbers this depends on
conflicts_with: []       # tasks that cannot run in parallel
parallel: true           # can this run in parallel with others?
---
```

**Task body structure:**
```markdown
# {Task Title}

## Context
{Why this task exists, what problem it solves}

## Acceptance Criteria
- [ ] {Specific, testable criterion}
- [ ] {Specific, testable criterion}

## Technical Notes
{Implementation hints, gotchas, relevant files}

## Files to Modify
- `path/to/file.ts` — {what to change}

## Out of Scope
{Explicitly what NOT to do in this task}
```

### 4. Execution Strategy Based on Size

- **Small epic (<5 tasks):** Create tasks sequentially
- **Medium epic (5-10 tasks):** Use parallel agents for creation
- **Large epic (>10 tasks):** Perform dependency analysis first, then create in batches

### 5. Post-Creation Validation

- Update epic.md with task summary
- Verify acceptance criteria are testable
- Confirm no scope overlap between tasks
- Check dependency chain is acyclic

### 6. Output

```
✅ Decomposed epic: $ARGUMENTS
  Tasks created: {count}
  Can run in parallel: {count}
  Sequential dependencies: {count}

Next: Run /pm:epic-sync $ARGUMENTS to push to GitHub
  Or: Run /pm:epic-oneshot $ARGUMENTS to decompose + sync in one step
```

## Notes

Tasks should be independently executable with clear acceptance criteria. Aim for tasks completable in 1-4 hours.
