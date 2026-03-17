# Claude-Mem Plugin

Give Claude persistent memory across coding sessions. Automatically captures what Claude does, compresses it with AI, and injects relevant context back into future sessions.

## Install

```bash
claude --plugin-dir ./claude-mem-plugin
```

Then run the setup:
```
/claude-mem:install
```

## What You Get

Once installed, Claude can:
- **Remember past sessions** — context from previous work is automatically injected at session start
- **Track decisions & discoveries** — bug fixes, architectural choices, and key findings are stored
- **Search project history** — ask about work done days or weeks ago across any project
- **Reduce token waste** — no need to re-explain the codebase every session

## How It Works

1. Run `/claude-mem:install` to install the plugin via the Claude Code marketplace
2. Restart Claude Code
3. Claude automatically starts capturing and storing session context locally (SQLite database)
4. Future sessions receive relevant past context at startup

## Requirements

- Node.js 18.0.0 or higher
- Claude Code with plugin support

## Web UI

After installation, a local web interface is available at `http://localhost:37777` to view and manage your memory store.

## Privacy

All data is stored locally on your machine. Mark sensitive content with `<private>` tags to exclude it from storage.

---

<p align="center">
  <a href="https://github.com/thedotmack/claude-mem">
    <img src="https://img.shields.io/badge/GitHub-thedotmack%2Fclaude--mem-181717?style=for-the-badge&logo=github" alt="GitHub"/>
  </a>
</p>
