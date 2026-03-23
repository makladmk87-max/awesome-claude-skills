# Skills: Superpowers — Workflow Intelligence

This file contains 14 skill(s) for the **Superpowers — Workflow Intelligence** category.
Follow the relevant skill's instructions when the user's request matches.

---

## Skill: `superpowers-brainstorming`

---
name: superpowers:brainstorming
description: MUST be used before any creative work — creating features, building components, adding functionality, or modifying behavior. Explores user intent, requirements, and design constraints before implementation begins.
---

## superpowers:brainstorming
**Category:** Superpowers — Core Workflow

**What it does:**
MUST be used before any creative work — creating features, building components, adding functionality, or modifying behavior. Explores user intent, requirements, and design constraints before implementation begins. Prevents wasted effort by aligning on the right approach upfront.

**When to trigger:**
- Before building any new feature
- Before any `/gsd:plan-phase`
- Whenever entering plan mode

**How to install:**
```bash
npx claude install superpowers
```

**Trigger phrase:** Automatically triggered before creative implementation work. Also: `/superpowers:brainstorming`

> **Note:** `superpowers:brainstorm` is the deprecated alias — use `superpowers:brainstorming` instead.

---

## Skill: `superpowers-dispatching-parallel-agents`

---
name: superpowers:dispatching-parallel-agents
description: Use when facing 2+ independent tasks that can be worked on without shared state or sequential dependencies. Orchestrates multiple Claude subagents running in parallel to dramatically speed up execution.
---

## superpowers:dispatching-parallel-agents
**Category:** Superpowers — Core Workflow

**What it does:**
Use when facing 2+ independent tasks that can be worked on without shared state or sequential dependencies. Orchestrates multiple Claude subagents running in parallel, dramatically speeding up execution.

**When to trigger:**
- You have multiple independent tasks
- Research across several unrelated topics
- Building parallel features with no shared state

**How to install:**
```bash
npx claude install superpowers
```

**Trigger phrase:** `/superpowers:dispatching-parallel-agents`

---

## Skill: `superpowers-executing-plans`

---
name: superpowers:executing-plans
description: Use when you have a written implementation plan to execute in a separate session with review checkpoints. Ensures disciplined execution with steps, commit checkpoints, and review before proceeding.
---

## superpowers:executing-plans
**Category:** Superpowers — Core Workflow

**What it does:**
Use when you have a written implementation plan to execute in a separate session with review checkpoints. Ensures disciplined execution: work in steps, commit checkpoints, and review before proceeding.

**When to trigger:**
When you have a written plan and want to execute it.

**How to install:**
```bash
npx claude install superpowers
```

**Trigger phrase:** `/superpowers:executing-plans`

> **Note:** `superpowers:execute-plan` is the deprecated alias.

---

## Skill: `superpowers-finishing-a-development-branch`

---
name: superpowers:finishing-a-development-branch
description: Use when implementation is complete, all tests pass, and you need to decide how to integrate the work. Guides completion by presenting structured options — merge, PR, or cleanup.
---

## superpowers:finishing-a-development-branch
**Category:** Superpowers — Quality

**What it does:**
Use when implementation is complete, all tests pass, and you need to decide how to integrate the work. Guides completion by presenting structured options: merge, PR, or cleanup.

**When to trigger:**
- Implementation done, tests passing
- Ready to integrate a feature branch

**How to install:**
```bash
npx claude install superpowers
```

**Trigger phrase:** `/superpowers:finishing-a-development-branch`

---

## Skill: `superpowers-receiving-code-review`

---
name: superpowers:receiving-code-review
description: Use when receiving code review feedback, before implementing suggestions — especially if feedback seems unclear or technically questionable. Requires technical rigor rather than blind implementation.
---

## superpowers:receiving-code-review
**Category:** Superpowers — Quality

**What it does:**
Use when receiving code review feedback, before implementing suggestions — especially if feedback seems unclear or technically questionable. Requires technical rigor and verification rather than performative agreement or blind implementation.

**When to trigger:**
- After getting code review comments
- Before implementing review suggestions

**How to install:**
```bash
npx claude install superpowers
```

**Trigger phrase:** `/superpowers:receiving-code-review`

---

## Skill: `superpowers-requesting-code-review`

---
name: superpowers:requesting-code-review
description: Use when completing tasks, implementing major features, or before merging — to verify work meets requirements. Structures the code review request to ensure meaningful feedback.
---

## superpowers:requesting-code-review
**Category:** Superpowers — Quality

**What it does:**
Use when completing tasks, implementing major features, or before merging — to verify work meets requirements. Structures the code review request to ensure meaningful feedback.

**When to trigger:**
- After completing a feature
- Before merging a branch
- After a major implementation step

**How to install:**
```bash
npx claude install superpowers
```

**Trigger phrase:** `/superpowers:requesting-code-review`

---

## Skill: `superpowers-subagent-driven-development`

---
name: superpowers:subagent-driven-development
description: Use when executing implementation plans with independent tasks in the current session. Coordinates subagents within the current Claude Code session.
---

## superpowers:subagent-driven-development
**Category:** Superpowers — Core Workflow

**What it does:**
Use when executing implementation plans with independent tasks in the current session. Coordinates subagents within the current Claude Code session (unlike `dispatching-parallel-agents` which spawns external processes).

**When to trigger:**
When you have a plan with multiple independent implementation tasks.

**How to install:**
```bash
npx claude install superpowers
```

**Trigger phrase:** `/superpowers:subagent-driven-development`

---

## Skill: `superpowers-systematic-debugging`

---
name: superpowers:systematic-debugging
description: Use when encountering any bug, test failure, or unexpected behavior — before proposing fixes. Uses a structured scientific method to prevent jumping to the wrong fix.
---

## superpowers:systematic-debugging
**Category:** Superpowers — Core Workflow

**What it does:**
Use when encountering any bug, test failure, or unexpected behavior — before proposing fixes. Uses a structured scientific method: observe → hypothesize → test → conclude. Prevents jumping to the wrong fix.

**When to trigger:**
- Any bug or test failure
- Unexpected behavior in code
- Before running `gsd:debug`

**How to install:**
```bash
npx claude install superpowers
```

**Trigger phrase:** `/superpowers:systematic-debugging`

---

## Skill: `superpowers-test-driven-development`

---
name: superpowers:test-driven-development
description: Use when implementing any feature or bugfix, before writing implementation code. Follows strict TDD — write failing tests first, then make them pass. This is a rigid skill — follow it exactly.
---

## superpowers:test-driven-development
**Category:** Superpowers — Core Workflow

**What it does:**
Use when implementing any feature or bugfix, before writing implementation code. Follows strict TDD: write failing tests first, then make them pass. This is a **rigid skill** — follow it exactly.

**When to trigger:**
Before writing implementation code for any feature or fix.

**How to install:**
```bash
npx claude install superpowers
```

**Trigger phrase:** `/superpowers:test-driven-development`

---

## Skill: `superpowers-using-git-worktrees`

---
name: superpowers:using-git-worktrees
description: Use when starting feature work that needs isolation from the current workspace, or before executing implementation plans. Creates isolated git worktrees so experiments never pollute the main branch.
---

## superpowers:using-git-worktrees
**Category:** Superpowers — Core Workflow

**What it does:**
Use when starting feature work that needs isolation from the current workspace, or before executing implementation plans. Creates isolated git worktrees with smart directory selection and safety verification — so experiments never pollute the main branch.

**When to trigger:**
- Starting isolated feature work
- Before executing a large implementation plan

**How to install:**
```bash
npx claude install superpowers
```

**Trigger phrase:** `/superpowers:using-git-worktrees`

---

## Skill: `superpowers-using-superpowers`

---
name: superpowers:using-superpowers
description: The master skill — establishes how to find and use all other skills. Loaded at the start of every conversation. Defines when and how to invoke skills, skill priority order, and red flags for rationalizing away skill invocations.
---

## superpowers:using-superpowers
**Category:** Superpowers — Meta

**What it does:**
The master skill — establishes how to find and use all other skills. Loaded at the start of every conversation. Defines when and how to invoke skills, the skill priority order, and red flags that indicate you're rationalizing away a skill invocation.

**Key rules it enforces:**
- Invoke relevant skills BEFORE any response
- Even 1% chance a skill applies → invoke it
- Process skills (brainstorming, debugging) before implementation skills

**How to install:**
```bash
npx claude install superpowers
```

**Trigger phrase:** Automatically loaded at session start.

---

## Skill: `superpowers-verification-before-completion`

---
name: superpowers:verification-before-completion
description: Use when about to claim work is complete, fixed, or passing — before committing or creating PRs. Requires running verification commands and confirming output before making any success claims.
---

## superpowers:verification-before-completion
**Category:** Superpowers — Quality

**What it does:**
Use when about to claim work is complete, fixed, or passing — before committing or creating PRs. Requires running verification commands and confirming output before making any success claims. Evidence before assertions, always.

**When to trigger:**
- Before saying "it works"
- Before committing
- Before creating a PR

**How to install:**
```bash
npx claude install superpowers
```

**Trigger phrase:** `/superpowers:verification-before-completion`

---

## Skill: `superpowers-writing-plans`

---
name: superpowers:writing-plans
description: Use when you have a spec or requirements for a multi-step task, before touching any code. Structures a detailed implementation plan covering architecture decisions, file changes, dependencies, and sequencing.
---

## superpowers:writing-plans
**Category:** Superpowers — Core Workflow

**What it does:**
Use when you have a spec or requirements for a multi-step task, before touching any code. Structures a detailed implementation plan covering architecture decisions, file changes, dependencies, and sequencing.

**When to trigger:**
- You have requirements and are about to start coding
- Before entering plan mode on a complex feature

**How to install:**
```bash
npx claude install superpowers
```

**Trigger phrase:** `/superpowers:writing-plans`

> **Note:** `superpowers:write-plan` is the deprecated alias.

---

## Skill: `superpowers-writing-skills`

---
name: superpowers:writing-skills
description: Use when creating new skills, editing existing skills, or verifying skills work before deployment. Guides the correct structure, frontmatter, trigger conditions, and testing methodology for Claude Code skills.
---

## superpowers:writing-skills
**Category:** Superpowers — Meta

**What it does:**
Use when creating new skills, editing existing skills, or verifying skills work before deployment. Guides the correct structure, frontmatter, trigger conditions, and testing methodology for Claude Code skills.

**When to trigger:**
- Writing a new skill
- Editing or improving an existing skill
- Verifying a skill's behavior

**How to install:**
```bash
npx claude install superpowers
```

**Trigger phrase:** `/superpowers:writing-skills`

---
