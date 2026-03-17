---
name: ccpm-code-rabbit
description: Process CodeRabbit review comments with context-aware discretion. Evaluates each suggestion against the actual codebase, applies valid improvements, and ignores context-unaware suggestions. Use after receiving a CodeRabbit review to efficiently process its feedback.
---

# CCPM: CodeRabbit Review Handler

Process CodeRabbit review comments intelligently, applying valid suggestions while ignoring those that don't fit the project context.

## Usage

```
/code-rabbit
```

Then paste one or more CodeRabbit comments.

## Instructions

### 1. Initial Context

Inform the user:
```
I'll review the CodeRabbit comments with discretion — CodeRabbit doesn't have access
to the entire codebase and may not understand the full context.

For each comment, I'll:
- Evaluate if it's valid given our codebase context
- Accept suggestions that improve code quality
- Ignore suggestions that don't apply to our architecture
- Explain my reasoning for accept/ignore decisions
```

### 2. Process Comments

#### Single File Comments

If all comments relate to one file:
1. Read the file for full context
2. Evaluate each suggestion
3. Apply accepted changes in batch using MultiEdit
4. Report which suggestions were accepted/ignored and why

#### Multiple File Comments

For multi-file reviews, launch parallel sub-agents:

```yaml
For each file:
  Task:
    description: "CodeRabbit fixes for {filename}"
    prompt: |
      Review and apply CodeRabbit suggestions for {filename}.

      Comments to evaluate:
      {relevant_comments_for_this_file}

      Instructions:
      1. Read the file to understand context
      2. For each suggestion:
         - Evaluate validity given codebase patterns
         - Accept if it improves quality/correctness
         - Ignore if not applicable to our architecture
      3. Apply accepted changes using Edit/MultiEdit
      4. Return summary:
         - Accepted: {list with reasons}
         - Ignored: {list with reasons}
         - Changes made: {brief description}

      Use discretion — CodeRabbit lacks full codebase context.
```

### 3. Decision Framework

For each suggestion, evaluate:
1. **Is it correct?** — Does the issue actually exist in the code?
2. **Is it relevant?** — Does it apply to our specific use case?
3. **Is it beneficial?** — Will fixing it genuinely improve the code?
4. **Is it safe?** — Could the change introduce new problems?

Apply only when all four answers are "yes" (or benefit clearly outweighs risk).

### 4. Common Patterns to **Accept**

- Actual bugs (null checks, error handling gaps)
- Security vulnerabilities (unless false positive)
- Resource leaks (unclosed connections, memory leaks)
- Type safety issues (TypeScript errors, missing type hints)
- Logic errors (off-by-one, incorrect conditions)
- Missing error handling for real failure cases

### 5. Common Patterns to **Ignore**

- Style preferences conflicting with project conventions
- Generic best practices not applicable to our use case
- Performance optimizations for non-critical paths
- Accessibility suggestions for internal tooling
- Security warnings for already-validated patterns
- Import reorganization that would break project structure

### 6. Output

```
📋 CodeRabbit Review Summary

Files processed: {count}

Accepted suggestions:
  {file}: {change_made} — {why_accepted}

Ignored suggestions:
  {file}: {suggestion} — {why_ignored}

Overall: {X}/{Y} suggestions applied
```

## Notes

CodeRabbit is helpful but lacks full project context. Your judgment about what fits the codebase takes precedence over generic suggestions. Always explain decisions to maintain an audit trail.
