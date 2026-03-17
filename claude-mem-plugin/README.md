# Claude-Mem Plugin

Persistent memory for Claude Code. Automatically captures tool usage observations, generates semantic summaries, and injects relevant context into future sessions — so Claude never loses track of your work.

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
- **Search project history** — natural language queries across all past sessions with the `mem-search` skill
- **Reduce token waste** — progressive disclosure means Claude re-discovers nothing it already knows
- **Cite past observations** — reference specific observations by ID via the web viewer

## How It Works

1. Run `/claude-mem:install` to install from the Claude Code plugin marketplace
2. Restart Claude Code
3. Claude automatically starts capturing session context locally (SQLite + Chroma vector database)
4. Future sessions receive relevant past context at startup via 5 lifecycle hooks

## Requirements

- Node.js 18.0.0 or higher
- Claude Code (latest version with plugin support)
- Bun (auto-installed if missing)
- uv (auto-installed if missing)

## Web UI

After installation, a local web interface is available at `http://localhost:37777` to view and manage your memory store, search observations, and switch between stable and beta channels.

## Privacy

All data is stored locally on your machine. Mark sensitive content with `<private>` tags to exclude it from storage.

---

<p align="center">
  <a href="https://github.com/thedotmack/claude-mem">
    <img src="https://img.shields.io/badge/GitHub-thedotmack%2Fclaude--mem-181717?style=for-the-badge&logo=github" alt="GitHub"/>
  </a>
</p>
