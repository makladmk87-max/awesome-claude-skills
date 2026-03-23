# Using Claude Skills in claude.ai

This folder contains pre-bundled skill files ready to upload to a **claude.ai Project**.

## Quick Setup (5 minutes)

### Step 1 — Create a Project

1. Go to [claude.ai](https://claude.ai) and click **New Project**
2. Give it a name like "Claude Code Skills"

### Step 2 — Add the system prompt

1. Open the project → **Edit project instructions**
2. Paste the entire contents of **`system-prompt.md`** into the instructions box
3. Save

### Step 3 — Upload the skill files

Upload all the `.md` files from this folder to the project's **Knowledge** section:

| File | Skills inside |
|------|--------------|
| `superpowers.md` | 14 skills |
| `gsd.md` | 32 skills |
| `notion.md` | 10 skills |
| `figma.md` | 5 skills |
| `adspirer.md` | 4 skills |
| `claude-api.md` | 3 skills |
| `utilities.md` | 39 skills |

**Total: 107 skills**

### Step 4 — Use it

Start a new conversation inside the project and trigger any skill in plain English:

| Say this... | Activates skill |
|-------------|----------------|
| "Load superpowers" | `superpowers:using-superpowers` |
| "Brainstorm [topic]" | `superpowers:brainstorming` |
| "Plan phase 3" | `gsd:plan-phase` |
| "Write a plan for [feature]" | `superpowers:writing-plans` |
| "Execute the plan" | `superpowers:executing-plans` |
| "Debug this systematically" | `superpowers:systematic-debugging` |
| "Finish this branch" | `superpowers:finishing-a-development-branch` |
| "Search Notion for [topic]" | `notion-search` |
| "Implement this Figma design: [URL]" | `figma:implement-design` |
| "Research keywords for [product]" | `adspirer keyword research` |
| "Tailor my resume for [job]" | `tailored-resume-generator` |
| "Organize my Downloads folder" | `file-organizer` |

## Keeping skills up to date

Re-run the generator from the repo root whenever skills are updated:

```bash
python3 generate_claude_ai.py
```

Then re-upload the changed `.md` files to your Project.
