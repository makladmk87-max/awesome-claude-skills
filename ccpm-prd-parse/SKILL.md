---
name: ccpm-prd-parse
description: Convert a Product Requirements Document (PRD) into a technical implementation epic. Use after creating a PRD with /pm:prd-new to generate the technical plan. Part of the CCPM spec-driven development workflow.
---

# CCPM: Parse PRD to Epic

Convert a PRD into a technical implementation epic with architecture decisions and implementation strategy.

## Usage

```
/pm:prd-parse <feature_name>
```

## Instructions

### 1. Validate PRD

- Check `.claude/prds/<feature_name>.md` exists
- Validate frontmatter: `name`, `description`, `status`, `created`
- If epic already exists at `.claude/epics/<feature_name>/epic.md`, confirm before overwriting

### 2. Analyze Requirements

Read the PRD and map requirements to technical components:
- Identify affected systems and services
- Determine data models needed
- Identify API endpoints or interfaces
- Note integration points with existing code
- Assess security and performance implications

### 3. Create Epic File

Create `.claude/epics/<feature_name>/epic.md`:

```markdown
---
name: {feature_name}
status: planning
created: {ISO_8601_datetime}
progress: 0%
prd: .claude/prds/{feature_name}.md
---

# {Feature Name} — Implementation Epic

## Overview
{Technical summary of what needs to be built}

## Architecture Decisions
- **Approach**: {chosen architecture}
- **Why**: {rationale}
- **Trade-offs**: {what we're giving up}

## Technical Approach
{Detailed technical description of implementation strategy}

## Implementation Strategy
1. {Phase 1 — Foundation}
2. {Phase 2 — Core functionality}
3. {Phase 3 — Integration & polish}

## Dependencies
- **Internal**: {other features/systems}
- **External**: {third-party services, packages}

## Success Criteria
- [ ] {Technical criterion tied to PRD requirement}
- [ ] {Technical criterion tied to PRD requirement}

## Effort Estimate
- Tasks: {estimated count, max 10}
- Complexity: {low/medium/high}
- Risk areas: {known unknowns}
```

### 4. Constraints

- Limit total tasks to **10 or fewer** — break large features into multiple epics if needed
- Prioritize extending existing functionality over writing new code
- Get current datetime: `date -u +"%Y-%m-%dT%H:%M:%SZ"`

### 5. Output

```
✅ Epic created: .claude/epics/{feature_name}/epic.md

PRD: .claude/prds/{feature_name}.md → Epic: .claude/epics/{feature_name}/epic.md

Next: Run /pm:epic-decompose {feature_name} to break into tasks
```

## Notes

The epic should be technical — it translates business requirements into an engineering plan.
