---
description: Install claude-mem - persistent memory across Claude Code sessions
allowed-tools: [Bash, AskUserQuestion]
---

# Claude-Mem Installation

Install the claude-mem plugin to give Claude persistent memory across coding sessions. It automatically captures context, compresses it with AI, and injects relevant history into future sessions — no API keys or accounts required.

## Instructions

### Step 1: Install from Marketplace

Tell the user to run these two commands in their Claude Code terminal:

```
/plugin marketplace add thedotmack/claude-mem
/plugin install claude-mem
```

**Note:** Do not use `npm install -g claude-mem` — that installs the SDK library only and does not set up the plugin hooks or worker service. Always use the `/plugin` commands above.

### Step 2: Restart Claude Code

After both commands complete, the user must restart Claude Code for the plugin to activate.

### Step 3: Verify

After restarting, context from previous sessions will automatically appear in new conversations.

To confirm the plugin is running, the user can check:
```
http://localhost:37777
```

The web viewer UI should be accessible and showing the memory stream.

### Step 4: Confirm

Tell the user:

```
Claude-Mem installed successfully!

Restart Claude Code to activate.

Once running, Claude will automatically:
- Capture context from every coding session
- Remember past work across all projects
- Inject relevant history at the start of each session

View your memory at: http://localhost:37777

To search past sessions, use the mem-search skill.
```

## Important

- All data is stored locally in a SQLite database on your machine
- No API keys, accounts, or cloud services required
- Mark sensitive content with `<private>` tags to exclude from storage
- Node.js 18.0.0 or higher is required (Bun and uv are auto-installed if missing)
- For troubleshooting, describe the issue to Claude — the troubleshoot skill will diagnose it automatically
