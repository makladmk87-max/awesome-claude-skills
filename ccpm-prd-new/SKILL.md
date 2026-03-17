---
name: ccpm-prd-new
description: Create a new Product Requirements Document (PRD) through guided brainstorming. Use this skill when starting a new feature to document requirements before writing any code. Part of the CCPM (Claude Code PM) spec-driven development workflow.
---

# CCPM: New PRD

Create a comprehensive Product Requirements Document (PRD) through guided brainstorming.

## Usage

```
/pm:prd-new <feature_name>
```

Feature name must be in **kebab-case** (e.g., `user-authentication`, `payment-flow`).

## Instructions

### 1. Validate Input

- Feature name must be kebab-case
- Check if `.claude/prds/$ARGUMENTS.md` already exists — if so, confirm before overwriting

### 2. Guided Brainstorming

Ask the user structured questions to build the PRD:

1. **Problem** — What problem does this solve? Who experiences it?
2. **Users** — Who are the primary users? What are their goals?
3. **Scope** — What's in scope? What's explicitly out of scope?
4. **Success** — How will you measure success? What are the KPIs?
5. **Constraints** — Technical, time, or resource constraints?
6. **Dependencies** — What other systems or features does this depend on?

### 3. Create PRD File

Create `.claude/prds/$ARGUMENTS.md` with this structure:

```markdown
---
name: {feature_name}
description: {one_line_description}
status: backlog
created: {ISO_8601_datetime}
---

# {Feature Name}

## Executive Summary
{2-3 sentence overview}

## Problem Statement
{What problem this solves and why it matters}

## User Stories
- As a {user_type}, I want to {action} so that {benefit}
- As a {user_type}, I want to {action} so that {benefit}

## Functional Requirements
1. {Requirement}
2. {Requirement}

## Non-Functional Requirements
- Performance: {requirement}
- Security: {requirement}
- Scalability: {requirement}

## Success Criteria
- [ ] {Measurable criterion}
- [ ] {Measurable criterion}

## Constraints
{Technical, time, or resource constraints}

## Dependencies
{Other features, systems, or teams this depends on}
```

### 4. Pre-Save Verification

Before saving, verify the PRD is complete:
- All sections filled out
- Success criteria are measurable
- Scope clearly defined
- Get datetime: `date -u +"%Y-%m-%dT%H:%M:%SZ"`

### 5. Next Step

After creating the PRD:
```
✅ PRD created: .claude/prds/$ARGUMENTS.md

Next: Run /pm:prd-parse $ARGUMENTS to convert to technical epic
```

## Notes

Every feature starts with a PRD. This ensures full traceability from requirement to code.
