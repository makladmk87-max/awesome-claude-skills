---
name: ccpm-testing-run
description: Run the project's test suite using the configuration from /testing:prime. Supports running all tests, a specific file, or a pattern. Reports results clearly with fix suggestions for failures. Part of the CCPM spec-driven development workflow.
---

# CCPM: Testing Run

Execute the test suite using the configured test framework.

## Usage

```
/testing:run [test_target]
```

**Test targets:**
- No argument — run all tests
- File path — run a specific test file
- Pattern — run tests matching a pattern (e.g., `auth`, `*.unit.ts`)

## Instructions

### 1. Check Configuration

Read `.claude/testing-config.md`:
- If missing, run `/testing:prime` first
- Extract test command, framework, and environment setup

### 2. Determine Test Command

| Target | Command |
|--------|---------|
| All tests | `{run_all_command}` |
| Specific file | `{framework_file_command} {file_path}` |
| Pattern | `{framework_pattern_command} {pattern}` |

### 3. Execute via Test Runner

Use the test-runner agent from `.claude/agents/test-runner.md` with:
- Maximum verbosity flags
- No mocks — real services only
- Output captured to log file

```bash
# Example invocations
jest --verbose --no-coverage
pytest -v --tb=long
cargo test -- --nocapture
go test ./... -v
```

### 4. Report Results

**On success:**
```
✅ All tests passed ({count} tests in {time}s)
```

**On failure:**
```
❌ {count} tests failed

FAILED: {test_name}
  File: {file_path}:{line_number}
  Error: {error_message}
  Likely cause: {diagnosis}
  Suggested fix: {actionable_suggestion}

FAILED: {test_name}
  ...

Summary: {passed}/{total} passed, {failed} failed, {skipped} skipped
```

**Mixed results:**
```
⚠️  {passed} passed, {failed} failed, {skipped} skipped

{failure details as above}
```

### 5. Cleanup

After test run, clean up any lingering test processes:
```bash
pkill -f "jest|mocha|pytest|phpunit|rspec|ctest|mvn|gradle|dotnet|cargo test|go test|swift test|flutter test" 2>/dev/null || true
```

## Rules

- Always use the test-runner agent — never run tests directly in the main conversation
- No mocking — use real service implementations
- Maximum verbosity for accurate diagnosis
- Sequential execution, not parallel

## Notes

Test failures include actionable fix suggestions. For persistent failures, check that test dependencies are installed and environment variables are set correctly.
