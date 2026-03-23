# Skills: Claude API & MCP

This file contains 3 skill(s) for the **Claude API & MCP** category.
Follow the relevant skill's instructions when the user's request matches.

---

## Skill: `claude-api`

---
name: claude-api
description: Guides building applications with the Claude API (Anthropic SDK) or Agent SDK. Covers API usage, tool use, streaming, and SDK patterns. Trigger when code imports anthropic or @anthropic-ai/sdk.
---

## claude-api
**Category:** Claude API / Anthropic SDK

**What it does:**
Guides you in building applications with the Claude API (Anthropic SDK) or Agent SDK. Covers API usage, tool use, streaming, and SDK patterns.

**When to trigger:**
- Your code imports `anthropic`, `@anthropic-ai/sdk`, or `claude_agent_sdk`
- You ask to use the Claude API or Anthropic SDK
- Building AI-powered apps with Claude as the backend

**Do NOT trigger when:** code uses `openai` or other AI SDKs.

**Latest model IDs:**
- Opus 4.6: `claude-opus-4-6`
- Sonnet 4.6: `claude-sonnet-4-6`
- Haiku 4.5: `claude-haiku-4-5-20251001`

**How to install:**
```bash
npx claude install superpowers
```

**Trigger phrase:** Importing `anthropic` / asking to use the Claude or Anthropic API.

---

## Skill: `mcp-builder`

---
name: mcp-builder
description: Guide for creating high-quality MCP (Model Context Protocol) servers that enable LLMs to interact with external services through well-designed tools. Use when building MCP servers to integrate external APIs or services, whether in Python (FastMCP) or Node/TypeScript (MCP SDK).
license: Complete terms in LICENSE.txt
---

# MCP Server Development Guide

## Overview

To create high-quality MCP (Model Context Protocol) servers that enable LLMs to effectively interact with external services, use this skill. An MCP server provides tools that allow LLMs to access external services and APIs. The quality of an MCP server is measured by how well it enables LLMs to accomplish real-world tasks using the tools provided.

---

# Process

## 🚀 High-Level Workflow

Creating a high-quality MCP server involves four main phases:

### Phase 1: Deep Research and Planning

#### 1.1 Understand Agent-Centric Design Principles

Before diving into implementation, understand how to design tools for AI agents by reviewing these principles:

**Build for Workflows, Not Just API Endpoints:**
- Don't simply wrap existing API endpoints - build thoughtful, high-impact workflow tools
- Consolidate related operations (e.g., `schedule_event` that both checks availability and creates event)
- Focus on tools that enable complete tasks, not just individual API calls
- Consider what workflows agents actually need to accomplish

**Optimize for Limited Context:**
- Agents have constrained context windows - make every token count
- Return high-signal information, not exhaustive data dumps
- Provide "concise" vs "detailed" response format options
- Default to human-readable identifiers over technical codes (names over IDs)
- Consider the agent's context budget as a scarce resource

**Design Actionable Error Messages:**
- Error messages should guide agents toward correct usage patterns
- Suggest specific next steps: "Try using filter='active_only' to reduce results"
- Make errors educational, not just diagnostic
- Help agents learn proper tool usage through clear feedback

**Follow Natural Task Subdivisions:**
- Tool names should reflect how humans think about tasks
- Group related tools with consistent prefixes for discoverability
- Design tools around natural workflows, not just API structure

**Use Evaluation-Driven Development:**
- Create realistic evaluation scenarios early
- Let agent feedback drive tool improvements
- Prototype quickly and iterate based on actual agent performance

#### 1.3 Study MCP Protocol Documentation

**Fetch the latest MCP protocol documentation:**

Use WebFetch to load: `https://modelcontextprotocol.io/llms-full.txt`

This comprehensive document contains the complete MCP specification and guidelines.

#### 1.4 Study Framework Documentation

**Load and read the following reference files:**

- **MCP Best Practices**: [📋 View Best Practices](./reference/mcp_best_practices.md) - Core guidelines for all MCP servers

**For Python implementations, also load:**
- **Python SDK Documentation**: Use WebFetch to load `https://raw.githubusercontent.com/modelcontextprotocol/python-sdk/main/README.md`
- [🐍 Python Implementation Guide](./reference/python_mcp_server.md) - Python-specific best practices and examples

**For Node/TypeScript implementations, also load:**
- **TypeScript SDK Documentation**: Use WebFetch to load `https://raw.githubusercontent.com/modelcontextprotocol/typescript-sdk/main/README.md`
- [⚡ TypeScript Implementation Guide](./reference/node_mcp_server.md) - Node/TypeScript-specific best practices and examples

#### 1.5 Exhaustively Study API Documentation

To integrate a service, read through **ALL** available API documentation:
- Official API reference documentation
- Authentication and authorization requirements
- Rate limiting and pagination patterns
- Error responses and status codes
- Available endpoints and their parameters
- Data models and schemas

**To gather comprehensive information, use web search and the WebFetch tool as needed.**

#### 1.6 Create a Comprehensive Implementation Plan

Based on your research, create a detailed plan that includes:

**Tool Selection:**
- List the most valuable endpoints/operations to implement
- Prioritize tools that enable the most common and important use cases
- Consider which tools work together to enable complex workflows

**Shared Utilities and Helpers:**
- Identify common API request patterns
- Plan pagination helpers
- Design filtering and formatting utilities
- Plan error handling strategies

**Input/Output Design:**
- Define input validation models (Pydantic for Python, Zod for TypeScript)
- Design consistent response formats (e.g., JSON or Markdown), and configurable levels of detail (e.g., Detailed or Concise)
- Plan for large-scale usage (thousands of users/resources)
- Implement character limits and truncation strategies (e.g., 25,000 tokens)

**Error Handling Strategy:**
- Plan graceful failure modes
- Design clear, actionable, LLM-friendly, natural language error messages which prompt further action
- Consider rate limiting and timeout scenarios
- Handle authentication and authorization errors

---

### Phase 2: Implementation

Now that you have a comprehensive plan, begin implementation following language-specific best practices.

#### 2.1 Set Up Project Structure

**For Python:**
- Create a single `.py` file or organize into modules if complex (see [🐍 Python Guide](./reference/python_mcp_server.md))
- Use the MCP Python SDK for tool registration
- Define Pydantic models for input validation

**For Node/TypeScript:**
- Create proper project structure (see [⚡ TypeScript Guide](./reference/node_mcp_server.md))
- Set up `package.json` and `tsconfig.json`
- Use MCP TypeScript SDK
- Define Zod schemas for input validation

#### 2.2 Implement Core Infrastructure First

**To begin implementation, create shared utilities before implementing tools:**
- API request helper functions
- Error handling utilities
- Response formatting functions (JSON and Markdown)
- Pagination helpers
- Authentication/token management

#### 2.3 Implement Tools Systematically

For each tool in the plan:

**Define Input Schema:**
- Use Pydantic (Python) or Zod (TypeScript) for validation
- Include proper constraints (min/max length, regex patterns, min/max values, ranges)
- Provide clear, descriptive field descriptions
- Include diverse examples in field descriptions

**Write Comprehensive Docstrings/Descriptions:**
- One-line summary of what the tool does
- Detailed explanation of purpose and functionality
- Explicit parameter types with examples
- Complete return type schema
- Usage examples (when to use, when not to use)
- Error handling documentation, which outlines how to proceed given specific errors

**Implement Tool Logic:**
- Use shared utilities to avoid code duplication
- Follow async/await patterns for all I/O
- Implement proper error handling
- Support multiple response formats (JSON and Markdown)
- Respect pagination parameters
- Check character limits and truncate appropriately

**Add Tool Annotations:**
- `readOnlyHint`: true (for read-only operations)
- `destructiveHint`: false (for non-destructive operations)
- `idempotentHint`: true (if repeated calls have same effect)
- `openWorldHint`: true (if interacting with external systems)

#### 2.4 Follow Language-Specific Best Practices

**At this point, load the appropriate language guide:**

**For Python: Load [🐍 Python Implementation Guide](./reference/python_mcp_server.md) and ensure the following:**
- Using MCP Python SDK with proper tool registration
- Pydantic v2 models with `model_config`
- Type hints throughout
- Async/await for all I/O operations
- Proper imports organization
- Module-level constants (CHARACTER_LIMIT, API_BASE_URL)

**For Node/TypeScript: Load [⚡ TypeScript Implementation Guide](./reference/node_mcp_server.md) and ensure the following:**
- Using `server.registerTool` properly
- Zod schemas with `.strict()`
- TypeScript strict mode enabled
- No `any` types - use proper types
- Explicit Promise<T> return types
- Build process configured (`npm run build`)

---

### Phase 3: Review and Refine

After initial implementation:

#### 3.1 Code Quality Review

To ensure quality, review the code for:
- **DRY Principle**: No duplicated code between tools
- **Composability**: Shared logic extracted into functions
- **Consistency**: Similar operations return similar formats
- **Error Handling**: All external calls have error handling
- **Type Safety**: Full type coverage (Python type hints, TypeScript types)
- **Documentation**: Every tool has comprehensive docstrings/descriptions

#### 3.2 Test and Build

**Important:** MCP servers are long-running processes that wait for requests over stdio/stdin or sse/http. Running them directly in your main process (e.g., `python server.py` or `node dist/index.js`) will cause your process to hang indefinitely.

**Safe ways to test the server:**
- Use the evaluation harness (see Phase 4) - recommended approach
- Run the server in tmux to keep it outside your main process
- Use a timeout when testing: `timeout 5s python server.py`

**For Python:**
- Verify Python syntax: `python -m py_compile your_server.py`
- Check imports work correctly by reviewing the file
- To manually test: Run server in tmux, then test with evaluation harness in main process
- Or use the evaluation harness directly (it manages the server for stdio transport)

**For Node/TypeScript:**
- Run `npm run build` and ensure it completes without errors
- Verify dist/index.js is created
- To manually test: Run server in tmux, then test with evaluation harness in main process
- Or use the evaluation harness directly (it manages the server for stdio transport)

#### 3.3 Use Quality Checklist

To verify implementation quality, load the appropriate checklist from the language-specific guide:
- Python: see "Quality Checklist" in [🐍 Python Guide](./reference/python_mcp_server.md)
- Node/TypeScript: see "Quality Checklist" in [⚡ TypeScript Guide](./reference/node_mcp_server.md)

---

### Phase 4: Create Evaluations

After implementing your MCP server, create comprehensive evaluations to test its effectiveness.

**Load [✅ Evaluation Guide](./reference/evaluation.md) for complete evaluation guidelines.**

#### 4.1 Understand Evaluation Purpose

Evaluations test whether LLMs can effectively use your MCP server to answer realistic, complex questions.

#### 4.2 Create 10 Evaluation Questions

To create effective evaluations, follow the process outlined in the evaluation guide:

1. **Tool Inspection**: List available tools and understand their capabilities
2. **Content Exploration**: Use READ-ONLY operations to explore available data
3. **Question Generation**: Create 10 complex, realistic questions
4. **Answer Verification**: Solve each question yourself to verify answers

#### 4.3 Evaluation Requirements

Each question must be:
- **Independent**: Not dependent on other questions
- **Read-only**: Only non-destructive operations required
- **Complex**: Requiring multiple tool calls and deep exploration
- **Realistic**: Based on real use cases humans would care about
- **Verifiable**: Single, clear answer that can be verified by string comparison
- **Stable**: Answer won't change over time

#### 4.4 Output Format

Create an XML file with this structure:

```xml
<evaluation>
  <qa_pair>
    <question>Find discussions about AI model launches with animal codenames. One model needed a specific safety designation that uses the format ASL-X. What number X was being determined for the model named after a spotted wild cat?</question>
    <answer>3</answer>
  </qa_pair>
<!-- More qa_pairs... -->
</evaluation>
```

---

# Reference Files

## 📚 Documentation Library

Load these resources as needed during development:

### Core MCP Documentation (Load First)
- **MCP Protocol**: Fetch from `https://modelcontextprotocol.io/llms-full.txt` - Complete MCP specification
- [📋 MCP Best Practices](./reference/mcp_best_practices.md) - Universal MCP guidelines including:
  - Server and tool naming conventions
  - Response format guidelines (JSON vs Markdown)
  - Pagination best practices
  - Character limits and truncation strategies
  - Tool development guidelines
  - Security and error handling standards

### SDK Documentation (Load During Phase 1/2)
- **Python SDK**: Fetch from `https://raw.githubusercontent.com/modelcontextprotocol/python-sdk/main/README.md`
- **TypeScript SDK**: Fetch from `https://raw.githubusercontent.com/modelcontextprotocol/typescript-sdk/main/README.md`

### Language-Specific Implementation Guides (Load During Phase 2)
- [🐍 Python Implementation Guide](./reference/python_mcp_server.md) - Complete Python/FastMCP guide with:
  - Server initialization patterns
  - Pydantic model examples
  - Tool registration with `@mcp.tool`
  - Complete working examples
  - Quality checklist

- [⚡ TypeScript Implementation Guide](./reference/node_mcp_server.md) - Complete TypeScript guide with:
  - Project structure
  - Zod schema patterns
  - Tool registration with `server.registerTool`
  - Complete working examples
  - Quality checklist

### Evaluation Guide (Load During Phase 4)
- [✅ Evaluation Guide](./reference/evaluation.md) - Complete evaluation creation guide with:
  - Question creation guidelines
  - Answer verification strategies
  - XML format specifications
  - Example questions and answers
  - Running an evaluation with the provided scripts

---

## Skill: `tdd`

---
name: tdd
description: Guide test-driven development (TDD) workflows — write failing tests first, then implement code to make them pass. Use this skill when the user wants to practice TDD, write tests before code, or build features using the red-green-refactor cycle.
---

# Test-Driven Development (TDD)

Guide development using the TDD cycle: Red → Green → Refactor.

## TDD Cycle

```
Red    → Write a failing test that defines desired behavior
Green  → Write the minimal code to make the test pass
Refactor → Clean up code while keeping tests green
```

Each cycle should be small — a few minutes per iteration. Never skip the Red phase.

## Step 1: Red — Write a Failing Test

Before writing any implementation code:

1. **Define the behavior** — what should this unit do?
2. **Write a test** that asserts that behavior
3. **Run the test** — confirm it fails (not errors — fails)
4. If the test passes without implementation, the test is wrong or already covered

A good test:
- Tests one behavior (single assertion or related assertions)
- Has a descriptive name: `test_returns_error_when_input_is_empty`
- Is fast and isolated — no external dependencies (use mocks/stubs)
- Is deterministic — same result every run

**Test naming pattern:** `test_[unit]_[scenario]_[expected_result]`

## Step 2: Green — Write Minimal Implementation

Write the **simplest possible code** to make the test pass:
- Don't over-engineer
- Don't add features not covered by a test
- It's okay to write ugly code here — refactor comes next
- Return hardcoded values if that makes the test pass initially (triangulation)

Run the test — confirm it passes. If other tests break, fix them.

## Step 3: Refactor — Clean Without Breaking

Now improve the code:
- Remove duplication
- Improve naming
- Simplify logic
- Apply patterns and abstractions
- Run tests after every change — if they break, undo and try again

## When to Write Tests

TDD applies to:
- New features (write test first, always)
- Bug fixes (write a failing test that reproduces the bug, then fix it)
- Refactoring (tests provide safety net)

## Test Structure: Arrange-Act-Assert (AAA)

```python
def test_add_two_numbers():
    # Arrange
    calculator = Calculator()

    # Act
    result = calculator.add(2, 3)

    # Assert
    assert result == 5
```

## Mocking and Isolation

Tests should be isolated from external dependencies:

**JavaScript (Jest):**
```js
jest.mock('./api', () => ({
  fetchUser: jest.fn().mockResolvedValue({ id: 1, name: 'Alice' })
}));
```

**Python (unittest.mock):**
```python
from unittest.mock import patch, MagicMock

@patch('module.requests.get')
def test_fetch_user(mock_get):
    mock_get.return_value.json.return_value = {'id': 1}
    result = fetch_user(1)
    assert result['id'] == 1
```

## TDD Workflow with Claude

When building a feature with TDD:

1. **Describe the feature** — Claude will help identify testable units
2. **Write the first test** — Claude generates a failing test
3. **Run the test** — confirm it fails
4. **Write minimal implementation** — Claude writes just enough code
5. **Run tests** — confirm passing
6. **Refactor** — Claude suggests improvements
7. **Repeat** for the next behavior

## Test Organization

```
src/
  feature/
    feature.js
    feature.test.js    # co-located with source
tests/
  unit/               # or organized by type
  integration/
  e2e/
```

## Common TDD Pitfalls

- **Writing tests after code** — this is not TDD, just testing
- **Tests that never fail** — always verify the red phase
- **Testing implementation details** — test behavior, not internals
- **Slow tests** — slow tests kill the TDD rhythm; mock I/O
- **Giant test methods** — one test per behavior
- **Skipping refactor phase** — green without refactor accumulates debt

## Notes for Claude

- Always start with the test file, never the implementation
- Generate tests that are specific about inputs and outputs
- After green, actively look for duplication and suggest refactors
- If the user writes tests after code, gently redirect to the TDD approach for future work

---
