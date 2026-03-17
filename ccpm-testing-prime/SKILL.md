---
name: ccpm-testing-prime
description: Detect and configure the project's testing framework for use with CCPM. Stores test configuration for use by /testing:run. Supports JS/TS, Python, Rust, Go, PHP, C#, Java, Kotlin, Swift, Ruby, and more. Part of the CCPM spec-driven development workflow.
---

# CCPM: Testing Prime

Detect and configure the project's testing framework.

## Usage

```
/testing:prime
```

Run once per project, or after adding/changing the test framework.

## Instructions

### Detection Strategy

**Never assume** the testing framework — always detect it from project files.

Scan for framework indicators:

| Language | Framework | Detection |
|----------|-----------|-----------|
| JS/TS | Jest | `jest.config.*`, `"jest"` in package.json |
| JS/TS | Vitest | `vitest.config.*`, `"vitest"` in package.json |
| JS/TS | Mocha | `mocha.opts`, `.mocharc.*` |
| Python | pytest | `pytest.ini`, `pyproject.toml [tool.pytest*]` |
| Python | unittest | `test_*.py` with `unittest.TestCase` |
| Rust | cargo test | `Cargo.toml` with `[dev-dependencies]` |
| Go | go test | `*_test.go` files |
| PHP | PHPUnit | `phpunit.xml`, `composer.json` |
| C#/.NET | xUnit/NUnit/MSTest | `*.csproj` with test packages |
| Java | JUnit | `pom.xml` or `build.gradle` with JUnit |
| Kotlin | Kotest | `build.gradle.kts` |
| Swift | XCTest | `*.xcodeproj`, `Package.swift` |
| Ruby | RSpec | `.rspec`, `spec/` directory |
| C/C++ | CTest | `CMakeLists.txt` |

### Configuration Detection

After detecting framework:
- Find test command (from scripts in `package.json`, `Makefile`, etc.)
- Identify test directory pattern
- Detect coverage configuration
- Find any test environment setup requirements

### Store Configuration

Create `.claude/testing-config.md`:

```markdown
---
framework: {detected_framework}
language: {language}
version: {framework_version}
detected: {ISO_8601_datetime}
---

# Testing Configuration

## Framework
{framework_name} v{version}

## Commands
- Run all: `{full_test_command}`
- Run file: `{framework_specific_file_command}`
- Run pattern: `{framework_specific_pattern_command}`
- Coverage: `{coverage_command}`

## Test Location
{test_directory_pattern}

## Environment
{any_env_vars_or_setup_needed}

## Notes
{any_special_configuration_notes}
```

### Error Handling

- **Framework not detected** — ask user to specify, or check `package.json` scripts manually
- **Missing dependencies** — provide install command
- **No test files found** — note in config, suggest creating first test
- **Permission issues** — flag and suggest fix

### Rules

- Run tests sequentially, **not in parallel**
- Use maximum verbosity
- Use real implementations — **no mocks** unless explicitly configured
- Always use test-runner agent from `.claude/agents/test-runner.md`

### Output

```
✅ Testing Framework Detected

Framework: {framework_name} v{version}
Language: {language}
Test directory: {pattern}
Run command: {command}

Config saved: .claude/testing-config.md

Next: Run /testing:run to execute tests
```

## Notes

Configuration is stored in `.claude/testing-config.md` and used by `/testing:run`. Re-run this command if you change test frameworks.
