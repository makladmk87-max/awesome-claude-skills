---
name: ccpm-init
description: Initialize the Claude Code PM (CCPM) system in a project — installs dependencies, configures GitHub integration, and sets up the .claude/ workspace structure. Use when starting to use CCPM in a new project.
---

# CCPM Init

Install CCPM dependencies and configure GitHub integration for spec-driven development.

## Usage

```
/pm:init
```

## Instructions

Run the CCPM initialization script to set up the project management system:

```bash
bash ccpm/scripts/pm/init.sh
```

This will:
1. Verify GitHub CLI (`gh`) is installed and authenticated
2. Create the `.claude/` workspace directory structure:
   - `.claude/prds/` — Product requirement documents
   - `.claude/epics/` — Epic and task files
   - `.claude/context/` — Project context documentation
3. Configure `ccpm.config` with repository settings
4. Verify the setup is complete and ready

## Prerequisites

- GitHub CLI (`gh`) installed and authenticated
- Git repository initialized with a remote
- CCPM files present in `ccpm/` directory

## After Initialization

Once initialized, use these commands to begin:
- `/pm:prd-new <feature>` — Start a new feature with a PRD
- `/context:create` — Generate project context documentation
- `/pm:import` — Import existing GitHub issues

## Notes

Do not run this on the automazeio/ccpm template repository itself. This command is for setting up CCPM in your own project.
