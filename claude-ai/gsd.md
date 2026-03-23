# Skills: GSD — Getting Stuff Done

This file contains 32 skill(s) for the **GSD — Getting Stuff Done** category.
Follow the relevant skill's instructions when the user's request matches.

---

## Skill: `gsd-add-phase`

---
name: gsd:add-phase
description: Adds a new phase to the end of the current milestone in your project roadmap. Use when you realize you need additional work that wasn't in the original plan.
---

## gsd:add-phase
**Category:** GSD (Get Stuff Done)

**What it does:**
Adds a new phase to the end of the current milestone in your project roadmap. Use this when you realize you need additional work that wasn't in the original plan.

**How to install GSD:**
```bash
npx claude install superpowers
```

**Trigger phrase:** `/gsd:add-phase`

---

## Skill: `gsd-add-tests`

---
name: gsd:add-tests
description: Generates tests for a completed phase based on UAT criteria and the actual implementation. Ensures your code is properly covered after a phase finishes.
---

## gsd:add-tests
**Category:** GSD (Get Stuff Done)

**What it does:**
Generates tests for a completed phase based on UAT (User Acceptance Testing) criteria and the actual implementation. Ensures your code is properly covered after a phase finishes.

**When to trigger:**
After completing a GSD phase and wanting to add test coverage.

**How to install GSD:**
```bash
npx claude install superpowers
```
Then in Claude Code:
```
/gsd:update
```

**Trigger phrase:** `/gsd:add-tests` — run after a phase is done to generate tests.

---

## Skill: `gsd-add-todo`

---
name: gsd:add-todo
description: Captures an idea or task as a todo directly from the current conversation context. Quick way to log something without losing it mid-session.
---

## gsd:add-todo
**Category:** GSD (Get Stuff Done)

**What it does:**
Captures an idea or task as a todo directly from the current conversation context. Quick way to log something without losing it mid-session.

**How to install GSD:**
```bash
npx claude install superpowers
```

**Trigger phrase:** `/gsd:add-todo`

---

## Skill: `gsd-audit-milestone`

---
name: gsd:audit-milestone
description: Audits a milestone's completion against its original intent before archiving it. Checks whether what was built actually matches what was planned, not just that tasks were checked off.
---

## gsd:audit-milestone
**Category:** GSD (Get Stuff Done)

**What it does:**
Audits a milestone's completion against its original intent before archiving it. Checks whether what was built actually matches what was planned, not just that tasks were checked off.

**When to trigger:**
Before archiving a milestone.

**How to install GSD:**
```bash
npx claude install superpowers
```

**Trigger phrase:** `/gsd:audit-milestone`

---

## Skill: `gsd-check-todos`

---
name: gsd:check-todos
description: Lists all pending todos and lets you select one to work on. Gives you a quick overview of outstanding items so you can prioritize what to tackle next.
---

## gsd:check-todos
**Category:** GSD (Get Stuff Done)

**What it does:**
Lists all pending todos and lets you select one to work on. Gives you a quick overview of outstanding items so you can prioritize what to tackle next.

**How to install GSD:**
```bash
npx claude install superpowers
```

**Trigger phrase:** `/gsd:check-todos`

---

## Skill: `gsd-cleanup`

---
name: gsd:cleanup
description: Archives accumulated phase directories from completed milestones, keeping your .planning/ directory tidy.
---

## gsd:cleanup
**Category:** GSD (Get Stuff Done)

**What it does:**
Archives accumulated phase directories from completed milestones, keeping your `.planning/` directory tidy.

**How to install GSD:**
```bash
npx claude install superpowers
```

**Trigger phrase:** `/gsd:cleanup`

---

## Skill: `gsd-complete-milestone`

---
name: gsd:complete-milestone
description: Archives a completed milestone and prepares the project for the next version. Wraps up loose ends and sets the stage for the next cycle.
---

## gsd:complete-milestone
**Category:** GSD (Get Stuff Done)

**What it does:**
Archives a completed milestone and prepares the project for the next version. Wraps up loose ends and sets the stage for the next cycle.

**When to trigger:**
After all phases in a milestone are done.

**How to install GSD:**
```bash
npx claude install superpowers
```

**Trigger phrase:** `/gsd:complete-milestone`

---

## Skill: `gsd-debug`

---
name: gsd-debug
description: Run a focused GSD (Get Stuff Done) debugging session — identify the root cause of a specific bug and fix it systematically. Use this skill when actively working through a bug with a clear reproduce case, within a larger GSD workflow.
---

# GSD: Debug

Run a focused debugging session to identify and fix a specific bug.

## Quick Debug Process

This is a streamlined version of full debugging, optimized for speed within a GSD workflow.

### Phase 1: Lock Down the Bug (2-5 min)

Answer these before touching code:
1. **What is the exact error?** (message, stack trace, screenshot)
2. **What is the expected behavior?**
3. **Can you reproduce it consistently?** If not, what are the conditions?
4. **When did it start?** (recent change? always existed?)

```bash
# If it's a regression, find the culprit commit fast
git log --oneline -20
git bisect start
git bisect bad HEAD
git bisect good <last-known-good>
```

### Phase 2: Locate (5-10 min)

**Read the stack trace top-to-bottom.** The error message usually tells you exactly where.

```bash
# Find relevant code
grep -rn "functionName\|ErrorType\|error message" src/

# Check recent changes to relevant files
git log --oneline src/relevant-file.ts
git diff HEAD~3 src/relevant-file.ts
```

Add targeted logging to trace execution:
```js
console.log('[DEBUG] variable:', JSON.stringify(variable, null, 2))
```

```python
print(f"[DEBUG] variable: {variable!r}")
```

### Phase 3: Fix (5-15 min)

Once the root cause is known:
1. Write the smallest possible fix
2. Test the exact reproduction case
3. Remove all debug logging
4. Run the full test suite

```bash
npm test
# or pytest
```

### Phase 4: Commit

```bash
git add [specific files]
git commit -m "fix: [what was broken and why]"
```

## Common Bug Patterns (Quick Reference)

| Error | First thing to check |
|-------|---------------------|
| `TypeError: Cannot read properties of undefined` | Null check missing; trace where value comes from |
| `KeyError` / `AttributeError` (Python) | Check dict keys exist; check object shape |
| `404 Not Found` | API route path, trailing slash, method (GET vs POST) |
| Test passes locally, fails in CI | Environment variable missing, timezone difference, hardcoded path |
| Works once, breaks on retry | State not reset between calls; mutation of shared object |
| `CORS error` | Backend missing CORS headers for that origin |
| Async operation completes but result not used | Missing `await`, unhandled promise |

## If Stuck After 15 Minutes

Stop guessing. Do one of:
1. **Rubber duck** — explain the bug out loud step by step
2. **Minimal reproduction** — strip everything down to the smallest failing case
3. **Check git blame** — who changed the relevant code last?
4. **Search the error message** — exact message in quotes + technology name
5. **Ask for help** — provide: expected behavior, actual behavior, code, what was tried

## After Fixing

- Add a test that would have caught this bug
- Check if the same pattern exists elsewhere: `grep -rn "same-pattern" src/`
- Note in the commit message what caused the bug (helps future you)

---

## Skill: `gsd-discuss-phase`

---
name: gsd:discuss-phase
description: Gathers phase context through adaptive questioning before planning begins. Ensures Claude fully understands the goals and constraints of a phase before writing a plan.
---

## gsd:discuss-phase
**Category:** GSD (Get Stuff Done)

**What it does:**
Gathers phase context through adaptive questioning before planning begins. Ensures Claude fully understands the goals and constraints of a phase before writing a plan.

**When to trigger:**
Before planning a phase, when you want to have a discussion first.

**How to install GSD:**
```bash
npx claude install superpowers
```

**Trigger phrase:** `/gsd:discuss-phase`

---

## Skill: `gsd-execute-phase`

---
name: gsd-execute-phase
description: Execute a planned implementation — work through steps systematically, write code, run tests, and ship. Use this skill when the user has a plan (from gsd-plan-phase or similar) and is ready to implement it, or wants help executing a specific implementation task.
---

# GSD: Execute Phase

Work through an implementation plan systematically to produce working, tested code.

## Before Starting

Ensure there's a clear plan. If not, use `gsd-plan-phase` first. At minimum, know:
- What feature/change is being implemented?
- What are the steps?
- What files need to change?

## Execution Principles

- **One step at a time** — complete each step before moving to the next
- **Run tests frequently** — catch regressions early
- **Commit incrementally** — small, logical commits (not one giant commit at the end)
- **Don't scope-creep** — if you notice unrelated improvements, note them but don't do them now

## Execution Loop

For each step in the plan:

```
1. Read the relevant existing code
2. Implement the change
3. Run tests → fix if failing
4. Commit with a clear message
5. Mark the step done
6. Move to next step
```

## Step Execution Pattern

### Before writing code for each step:
- Re-read the plan step
- Read the files that will change
- Understand the existing patterns (follow them)
- Confirm the approach is still correct given what you've learned

### While writing code:
- Follow existing code style and patterns
- Write the simplest code that works
- Handle error cases
- Add/update types

### After writing code:
```bash
# Run tests
npm test
# or
pytest

# Run linter
npm run lint
# or
ruff check .

# Check types
npx tsc --noEmit
# or
mypy src/
```

### Commit pattern:
```bash
git add [specific files]
git commit -m "type: description"
```

Commit types: `feat`, `fix`, `refactor`, `test`, `chore`, `docs`

## Handling Blockers

If a step is blocked:
1. **Try to unblock** — investigate the issue, check docs, look for similar patterns
2. **Note the blocker** — write down what's blocking and what was tried
3. **Continue with other steps** if the blocker doesn't affect them
4. **Escalate** — if completely stuck, pause and ask/research

Never silently skip a step. Always explicitly note what was done and why.

## Progress Tracking

Use the `gsd-progress` skill to track which steps are done. Update the plan:
```
Steps:
1. [x] Set up X — done
2. [x] Implement Y — done
3. [ ] Add tests — IN PROGRESS
4. [ ] Update docs
```

## Testing Strategy During Execution

After each logical unit of work:
- Run the existing test suite — ensure no regressions
- Add tests for new behavior before or immediately after implementing it
- Test the happy path first, then edge cases

## Pre-Completion Checklist

Before calling a feature "done":
- [ ] All plan steps completed
- [ ] All tests pass
- [ ] Linter passes
- [ ] Types check out
- [ ] No debug code or console.logs left in
- [ ] Error cases handled
- [ ] README or docs updated if needed
- [ ] PR description written (if opening a PR)

## Git Workflow During Execution

```bash
# Start on a feature branch
git checkout -b feature/my-feature

# Commit often
git add src/specific-file.ts tests/specific-file.test.ts
git commit -m "feat: add X functionality"

# Push to remote regularly
git push origin feature/my-feature

# When done, open PR
gh pr create --title "feat: add X functionality" --body "..."
```

## Notes for Claude

- Read files before editing them — never make blind edits
- Prefer editing existing patterns over introducing new ones
- If the implementation diverges from the plan, note the deviation and why
- When multiple implementation steps are independent, they can be done in parallel (multiple file edits in one turn)

---

## Skill: `gsd-health`

---
name: gsd:health
description: Diagnoses the health of your .planning/ directory and optionally repairs issues. Useful when something seems off with your project structure.
---

## gsd:health
**Category:** GSD (Get Stuff Done)

**What it does:**
Diagnoses the health of your `.planning/` directory and optionally repairs issues. Useful when something seems off with your project structure.

**How to install GSD:**
```bash
npx claude install superpowers
```

**Trigger phrase:** `/gsd:health`

---

## Skill: `gsd-help`

---
name: gsd:help
description: Shows all available GSD commands and a usage guide. Your starting point for learning the GSD workflow.
---

## gsd:help
**Category:** GSD (Get Stuff Done)

**What it does:**
Shows all available GSD commands and a usage guide. Your starting point for learning the GSD workflow.

**How to install GSD:**
```bash
npx claude install superpowers
```

**Trigger phrase:** `/gsd:help`

---

## Skill: `gsd-insert-phase`

---
name: gsd:insert-phase
description: Inserts urgent work as a decimal phase (e.g., 7.1) between two existing phases without renumbering the whole roadmap. Perfect for hotfixes or urgent additions.
---

## gsd:insert-phase
**Category:** GSD (Get Stuff Done)

**What it does:**
Inserts urgent work as a decimal phase (e.g., `7.1`) between two existing phases, without renumbering the whole roadmap. Perfect for hotfixes or urgent additions.

**How to install GSD:**
```bash
npx claude install superpowers
```

**Trigger phrase:** `/gsd:insert-phase`

---

## Skill: `gsd-join-discord`

---
name: gsd:join-discord
description: Joins you to the GSD Discord community — a place to get help, share projects, and connect with other GSD users.
---

## gsd:join-discord
**Category:** GSD (Get Stuff Done)

**What it does:**
Joins you to the GSD Discord community — a place to get help, share projects, and connect with other GSD users.

**How to install GSD:**
```bash
npx claude install superpowers
```

**Trigger phrase:** `/gsd:join-discord`

---

## Skill: `gsd-list-phase-assumptions`

---
name: gsd:list-phase-assumptions
description: Surfaces Claude's assumptions about how a phase will be approached before planning begins. Lets you catch and correct wrong assumptions early, before a bad plan is written.
---

## gsd:list-phase-assumptions
**Category:** GSD (Get Stuff Done)

**What it does:**
Surfaces Claude's assumptions about how a phase will be approached before planning begins. Lets you catch and correct wrong assumptions early, before a bad plan is written.

**When to trigger:**
Before planning a phase.

**How to install GSD:**
```bash
npx claude install superpowers
```

**Trigger phrase:** `/gsd:list-phase-assumptions`

---

## Skill: `gsd-map-codebase`

---
name: gsd:map-codebase
description: Analyzes your entire codebase using parallel mapper agents and produces structured documents in .planning/codebase/. Covers tech stack, architecture, quality, and concerns.
---

## gsd:map-codebase
**Category:** GSD (Get Stuff Done)

**What it does:**
Analyzes your entire codebase using parallel mapper agents and produces structured documents in `.planning/codebase/`. Covers tech stack, architecture, quality, and concerns. Gives Claude (and you) a comprehensive understanding of the project before major changes.

**How to install GSD:**
```bash
npx claude install superpowers
```

**Trigger phrase:** `/gsd:map-codebase`

---

## Skill: `gsd-new-milestone`

---
name: gsd:new-milestone
description: Starts a new milestone cycle by updating PROJECT.md and routing to requirements gathering. Use after completing one milestone and starting the next.
---

## gsd:new-milestone
**Category:** GSD (Get Stuff Done)

**What it does:**
Starts a new milestone cycle by updating `PROJECT.md` and routing to requirements gathering. Use after completing one milestone and starting the next.

**How to install GSD:**
```bash
npx claude install superpowers
```

**Trigger phrase:** `/gsd:new-milestone`

---

## Skill: `gsd-new-project`

---
name: gsd-new-project
description: Bootstrap a new project from scratch — scaffold structure, set up tooling, configure environments, and get to a working first commit. Use this skill when the user wants to start a new software project and needs help with initial setup, structure, and configuration.
---

# GSD: New Project

Bootstrap a new project efficiently to reach a working, well-structured starting point.

## Philosophy

Get to a working state fast. Avoid over-engineering the foundation. The best new project setup is one that can be built on immediately.

## Step 1: Understand What's Being Built

Before scaffolding anything, clarify:
- **Type**: Web app? API? CLI? Library? Script? Mobile?
- **Stack**: Language, framework, runtime
- **Scale**: Solo project? Team? Production? Prototype?
- **Existing constraints**: Must use specific tools, deploy targets, org standards?

## Step 2: Initialize the Repository

```bash
# Create directory and initialize git
mkdir project-name && cd project-name
git init

# Set up .gitignore immediately
curl -sL https://www.gitignore.io/api/node,python,macos,vscode > .gitignore
# Or manually create based on stack
```

## Step 3: Project Structure

Establish a clear directory structure based on project type:

**Node.js / TypeScript:**
```
project/
  src/
    index.ts
  tests/
  dist/
  package.json
  tsconfig.json
  .env.example
  README.md
```

**Python:**
```
project/
  src/
    package_name/
      __init__.py
  tests/
  pyproject.toml (or setup.py)
  requirements.txt
  .env.example
  README.md
```

**Full-stack web:**
```
project/
  client/          # frontend
  server/          # backend API
  shared/          # shared types/utils
  docker-compose.yml
  .env.example
  README.md
```

## Step 4: Initialize Package Manager

**Node.js:**
```bash
npm init -y
# or
pnpm init
```

**Python:**
```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

## Step 5: Configure Essential Tooling

At minimum, configure:
- **Linter**: ESLint, Flake8, Ruff
- **Formatter**: Prettier, Black
- **Type checking**: TypeScript, mypy
- **Testing**: Jest, pytest, Vitest

Add to `package.json` scripts:
```json
{
  "scripts": {
    "dev": "...",
    "build": "...",
    "test": "...",
    "lint": "...",
    "format": "..."
  }
}
```

## Step 6: Environment Configuration

Create `.env.example` with all required variables (no values):
```env
DATABASE_URL=
API_KEY=
PORT=3000
NODE_ENV=development
```

Add `.env` to `.gitignore`. Never commit real secrets.

## Step 7: First Commit

```bash
git add .
git commit -m "chore: initial project setup"
```

## Step 8: Connect to Remote

```bash
# Create repo on GitHub/GitLab first, then:
git remote add origin https://github.com/user/project.git
git branch -M main
git push -u origin main
```

## Project README Template

Every project should have a README covering:
```md
# Project Name

One sentence description.

## Setup
## Usage
## Development
## Deployment
## Contributing
```

## Common Stacks Quick Setup

**Express + TypeScript API:**
```bash
npm init -y
npm install express
npm install -D typescript ts-node @types/node @types/express nodemon
npx tsc --init
```

**Next.js:**
```bash
npx create-next-app@latest project-name --typescript --tailwind --app
```

**FastAPI (Python):**
```bash
pip install fastapi uvicorn python-dotenv
```

**React + Vite:**
```bash
npm create vite@latest project-name -- --template react-ts
```

## Notes

- Resist adding dependencies that aren't immediately needed
- Set up CI/CD early — even a simple lint/test on push pays off
- Document the setup process in README as you go, not after

---

## Skill: `gsd-pause-work`

---
name: gsd:pause-work
description: Creates a context handoff document when you need to pause work mid-phase. Saves your current state so you or Claude can resume exactly where you left off.
---

## gsd:pause-work
**Category:** GSD (Get Stuff Done)

**What it does:**
Creates a context handoff document when you need to pause work mid-phase. Saves your current state so you or Claude can resume exactly where you left off in a future session.

**When to trigger:**
When you need to stop working mid-phase.

**How to install GSD:**
```bash
npx claude install superpowers
```

**Trigger phrase:** `/gsd:pause-work`

---

## Skill: `gsd-plan-milestone-gaps`

---
name: gsd:plan-milestone-gaps
description: Creates phases to close all gaps identified by a milestone audit. After gsd:audit-milestone reveals missing work, this skill turns those gaps into actionable phases.
---

## gsd:plan-milestone-gaps
**Category:** GSD (Get Stuff Done)

**What it does:**
Creates phases to close all gaps identified by a milestone audit. After running `gsd:audit-milestone` reveals missing work, this skill turns those gaps into actionable phases.

**When to trigger:**
After `gsd:audit-milestone` finds gaps.

**How to install GSD:**
```bash
npx claude install superpowers
```

**Trigger phrase:** `/gsd:plan-milestone-gaps`

---

## Skill: `gsd-plan-phase`

---
name: gsd-plan-phase
description: Run the planning phase of a GSD (Get Stuff Done) workflow — break down a feature or task into a concrete implementation plan before writing code. Use this skill when the user wants to plan how to implement a specific feature, task, or change before starting to code.
---

# GSD: Plan Phase

Transform a feature request or task into a concrete, actionable implementation plan.

## When to Use

Run the plan phase before any significant implementation:
- New features (more than a few lines of code)
- Architectural changes
- Refactors
- Bug fixes that require design decisions

Skip for truly trivial changes (typo fix, one-line change).

## Plan Phase Process

### 1. Understand the Requirement

Re-state the requirement in your own words. Identify:
- **Goal**: What user problem does this solve?
- **Scope**: What's in scope? What's explicitly out of scope?
- **Acceptance criteria**: How will you know it's done?
- **Constraints**: Performance targets, backward compatibility, deadlines

If anything is unclear, ask before planning.

### 2. Explore the Codebase

Before planning the implementation, understand the existing system:
- Where does the change live? Which files/modules?
- What existing code can be reused or extended?
- What are the relevant data models and APIs?
- Are there existing patterns to follow?

```bash
# Find relevant files
grep -r "relevant_term" src/
# or use Glob/search tools
```

### 3. Identify Approach Options

For non-trivial features, consider 2-3 implementation approaches:
- **Option A**: [approach] — pros, cons
- **Option B**: [approach] — pros, cons
- **Recommended**: [which and why]

### 4. Define Implementation Steps

Break the work into concrete, ordered steps. Each step should:
- Be completable in a single focused session
- Have a clear done state
- Be in dependency order (what must happen first?)

**Plan format:**
```
Feature: [name]

Approach: [chosen approach and why]

Steps:
1. [ ] [Specific task] — [files/components affected]
2. [ ] [Specific task] — [files/components affected]
3. [ ] [Write tests for X]
4. [ ] [Update docs/types if needed]

Edge cases to handle:
- [edge case 1]
- [edge case 2]

Open questions:
- [anything that needs decision before or during implementation]
```

### 5. Identify Risks and Unknowns

Flag before starting:
- **Breaking changes**: Will this affect existing functionality?
- **Dependencies**: Does this require other changes first?
- **Assumptions**: What are you assuming is true?
- **Unknowns**: What might you discover that changes the plan?

### 6. Estimate Complexity

Tag each plan with complexity:
- **S** (Small): <2 hours, straightforward
- **M** (Medium): 2-8 hours, some complexity
- **L** (Large): 1-3 days, significant work
- **XL** (X-Large): 3+ days, consider breaking down further

XL tasks should be broken into multiple M or L tasks.

## Output Format

Produce a plan document like:

```
# Plan: [Feature Name]

**Goal:** [one sentence]
**Complexity:** M
**Branch:** feature/[name]

## Approach
[1-2 paragraphs explaining the implementation approach]

## Steps
1. [ ] Set up [X] in [file]
2. [ ] Implement [Y] — extends existing [Z]
3. [ ] Add tests for [scenarios]
4. [ ] Update [types/docs/API]

## Files to Change
- `src/components/Foo.tsx` — add new prop
- `src/api/bar.ts` — new endpoint
- `tests/foo.test.ts` — new test cases

## Edge Cases
- Empty state
- Error state
- Concurrent requests

## Open Questions
- [ ] Should X be configurable or hardcoded?
```

## Transition to Execute Phase

After the plan is approved:
1. Create a feature branch: `git checkout -b feature/[name]`
2. Use `gsd-execute-phase` skill to work through the steps
3. Check off steps as completed

---

## Skill: `gsd-progress`

---
name: gsd-progress
description: Track and report progress on a GSD (Get Stuff Done) workflow — show what's done, what's in progress, and what's next. Use this skill when the user wants a status update on their current task or project, or needs to see where they are in a plan.
---

# GSD: Progress

Surface a clear, actionable progress snapshot of the current GSD workflow.

## Progress Report Format

When asked for progress, produce a report like:

```
## Progress: [Feature/Task Name]

**Status:** In Progress | Blocked | Review | Done
**Completed:** X/Y steps

### ✅ Done
- [Step 1] — [brief note if relevant]
- [Step 2]

### 🔄 In Progress
- [Current step] — [what's happening]

### ⏳ Up Next
- [Next step]
- [Step after that]

### ❌ Blocked
- [Blocked step] — [what's blocking it]

### 📝 Notes / Deviations from Plan
- [Any changes from original plan]
- [Decisions made]
- [Open questions]

### Next Action
[Single most important thing to do right now]
```

## How to Assess Progress

To generate an accurate progress report:

1. **Review the plan** — re-read the original plan steps
2. **Check completed work** — review git commits, file changes
3. **Check test status** — are tests passing?
4. **Identify blockers** — what (if anything) is stopping progress?
5. **Update the plan** — mark completed steps, flag new issues

```bash
# Review recent commits
git log --oneline -10

# See what files have changed
git diff --stat HEAD~5 HEAD

# Check test status
npm test 2>&1 | tail -20
```

## Keeping Progress Visible

Update progress inline in the plan document:

```
Steps:
1. [x] Initialize database schema — done
2. [x] Create API endpoint — done
3. [~] Add authentication — 50% done (middleware done, tests pending)
4. [ ] Write integration tests
5. [ ] Update API documentation
```

Legend:
- `[x]` — Done
- `[~]` — In progress
- `[ ]` — Not started
- `[!]` — Blocked

## When Progress is Stalled

If progress has stalled:
1. Identify the exact stall point
2. Determine if it's a blocker (external) or a struggle (internal)
3. For blockers: escalate or work around
4. For struggles: break the step into smaller sub-steps, get help

## End of Session Summary

At the end of a work session, produce a summary:

```
## Session Summary

**Time:** [duration]
**Completed today:** [list]
**State:** [where things stand]
**Next session start:** [exactly what to pick up with]
**Open questions:** [anything that needs a decision]
```

This makes it easy to resume work without context loss.

---

## Skill: `gsd-quick`

---
name: gsd:quick
description: Executes a quick task with GSD guarantees (atomic commits, state tracking) but skips optional agents. Faster than a full phase execution — best for small, well-defined tasks.
---

## gsd:quick
**Category:** GSD (Get Stuff Done)

**What it does:**
Executes a quick task with GSD guarantees (atomic commits, state tracking) but skips optional agents like researchers and planners. Faster than a full phase execution — best for small, well-defined tasks.

**How to install GSD:**
```bash
npx claude install superpowers
```

**Trigger phrase:** `/gsd:quick [task description]`

---

## Skill: `gsd-reapply-patches`

---
name: gsd:reapply-patches
description: Reapplies your local modifications after a GSD update. When you update GSD and your customizations are overwritten, this skill restores them.
---

## gsd:reapply-patches
**Category:** GSD (Get Stuff Done)

**What it does:**
Reapplies your local modifications after a GSD update. When you update GSD and your customizations are overwritten, this skill restores them.

**When to trigger:**
After running `gsd:update` and losing local customizations.

**How to install GSD:**
```bash
npx claude install superpowers
```

**Trigger phrase:** `/gsd:reapply-patches`

---

## Skill: `gsd-remove-phase`

---
name: gsd:remove-phase
description: Removes a future phase from the roadmap and automatically renumbers subsequent phases. Safe way to cancel planned work.
---

## gsd:remove-phase
**Category:** GSD (Get Stuff Done)

**What it does:**
Removes a future phase from the roadmap and automatically renumbers subsequent phases. Safe way to cancel planned work.

**How to install GSD:**
```bash
npx claude install superpowers
```

**Trigger phrase:** `/gsd:remove-phase`

---

## Skill: `gsd-research-phase`

---
name: gsd:research-phase
description: Researches how to implement a phase before planning. Standalone research step — normally runs automatically inside gsd:plan-phase, but can be invoked separately for deeper investigation.
---

## gsd:research-phase
**Category:** GSD (Get Stuff Done)

**What it does:**
Researches how to implement a phase before planning. Standalone research step — normally this runs automatically inside `gsd:plan-phase`, but you can invoke it separately for deeper investigation.

**How to install GSD:**
```bash
npx claude install superpowers
```

**Trigger phrase:** `/gsd:research-phase`

---

## Skill: `gsd-resume-work`

---
name: gsd:resume-work
description: Resumes work from a previous session with full context restoration. Reads the handoff document created by gsd:pause-work and gets Claude back up to speed instantly.
---

## gsd:resume-work
**Category:** GSD (Get Stuff Done)

**What it does:**
Resumes work from a previous session with full context restoration. Reads the handoff document created by `gsd:pause-work` and gets Claude back up to speed instantly.

**When to trigger:**
At the start of a new session when you paused work previously.

**How to install GSD:**
```bash
npx claude install superpowers
```

**Trigger phrase:** `/gsd:resume-work`

---

## Skill: `gsd-set-profile`

---
name: gsd:set-profile
description: Switches the model profile used by GSD agents. Three profiles available — quality (best models), balanced (default), budget (faster/cheaper).
---

## gsd:set-profile
**Category:** GSD (Get Stuff Done)

**What it does:**
Switches the model profile used by GSD agents. Three profiles available:
- **quality** — uses the most capable models (slower, costlier)
- **balanced** — good default mix
- **budget** — faster and cheaper models

**How to install GSD:**
```bash
npx claude install superpowers
```

**Trigger phrase:** `/gsd:set-profile [quality|balanced|budget]`

---

## Skill: `gsd-settings`

---
name: gsd:settings
description: Configures GSD workflow toggles and model profile settings. Adjust how GSD behaves — which agents run, what's skipped, and which AI model profile to use.
---

## gsd:settings
**Category:** GSD (Get Stuff Done)

**What it does:**
Configures GSD workflow toggles and model profile settings. Adjust how GSD behaves — which agents run, what's skipped, and which AI model profile to use.

**How to install GSD:**
```bash
npx claude install superpowers
```

**Trigger phrase:** `/gsd:settings`

---

## Skill: `gsd-update`

---
name: gsd:update
description: Updates GSD to the latest version and displays a changelog. Always run this on new machines or after a period away from GSD.
---

## gsd:update
**Category:** GSD (Get Stuff Done)

**What it does:**
Updates GSD to the latest version and displays a changelog. Always run this on new machines or after a period away from GSD.

**How to install GSD:**
```bash
npx claude install superpowers
```

**Trigger phrase:** `/gsd:update`

---

## Skill: `gsd-validate-phase`

---
name: gsd:validate-phase
description: Retroactively audits and fills Nyquist validation gaps for a completed phase. Generates missing tests and verifies coverage for phase requirements.
---

## gsd:validate-phase
**Category:** GSD (Get Stuff Done)

**What it does:**
Retroactively audits and fills Nyquist validation gaps for a completed phase. Generates missing tests and verifies coverage for phase requirements. Use when a phase was completed but validation was skipped.

**How to install GSD:**
```bash
npx claude install superpowers
```

**Trigger phrase:** `/gsd:validate-phase`

---

## Skill: `gsd-verify-work`

---
name: gsd:verify-work
description: Validates built features through conversational UAT. Confirms that the phase goal was actually achieved, not just that tasks were completed.
---

## gsd:verify-work
**Category:** GSD (Get Stuff Done)

**What it does:**
Validates built features through conversational UAT (User Acceptance Testing). Confirms that the phase goal was actually achieved, not just that tasks were completed.

**When to trigger:**
After executing a phase.

**How to install GSD:**
```bash
npx claude install superpowers
```

**Trigger phrase:** `/gsd:verify-work`

---
