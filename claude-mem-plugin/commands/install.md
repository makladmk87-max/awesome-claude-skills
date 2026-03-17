---
description: Install claude-mem - persistent memory for Claude Code sessions
allowed-tools: [Bash, AskUserQuestion]
---

# Claude-Mem Installation

Install the claude-mem plugin to give Claude persistent memory across coding sessions. It automatically captures context, compresses it with AI, and injects relevant history into future sessions.

## Instructions

### Step 1: Install from Marketplace

Run these two commands in sequence:

```bash
claude --dangerously-skip-permissions -p "/plugin marketplace add thedotmack/claude-mem"
```

Then:

```bash
claude --dangerously-skip-permissions -p "/plugin install claude-mem"
```

If running inside a Claude Code session, you can run the slash commands directly:

```
/plugin marketplace add thedotmack/claude-mem
/plugin install claude-mem
```

### Step 2: Verify Installation

Check that claude-mem is listed in installed plugins:

```bash
claude --dangerously-skip-permissions -p "/plugin list"
```

You should see `claude-mem` in the output.

### Step 3: Confirm

Tell the user:

```
Claude-Mem installed successfully!

To activate: exit and run `claude` again

Once restarted, Claude will automatically:
- Capture context from your coding sessions
- Remember past work across projects
- Inject relevant history at the start of each session

View your memory store at: http://localhost:37777
```

## Important

- claude-mem stores all data locally in a SQLite database on your machine
- No API keys or accounts required
- Mark sensitive content with `<private>` tags to exclude from storage
- Node.js 18.0.0 or higher is required
