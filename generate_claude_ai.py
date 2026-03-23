#!/usr/bin/env python3
"""
Generate claude-ai/ package — bundles skills into category files
suitable for upload to a claude.ai Project.

Usage:
    python3 generate_claude_ai.py
"""

import os
import re

REPO = os.path.dirname(os.path.abspath(__file__))
OUT  = os.path.join(REPO, "claude-ai")

# Map skill directory prefix → category file name
CATEGORIES = {
    "superpowers": "superpowers",
    "gsd":         "gsd",
    "notion":      "notion",
    "figma":       "figma",
    "adspirer":    "adspirer",
    "competitive": "adspirer",
    "mcp":         "claude-api",
    "claude-api":  "claude-api",
    "tdd":         "claude-api",
}

# Skills that should go into utilities if not matched above
UTILITY_SKILLS = {
    "simplify", "loop", "keybindings-help", "brainstorming", "planning",
    "debugging", "code-review", "frontend-design", "git-worktrees",
    "changelog-generator", "content-research-writer",
    "tailored-resume-generator", "twitter-algorithm-optimizer",
    "webapp-testing", "video-downloader", "instagram-prompt-extractor",
    "instagram-fetch", "image-enhancer", "file-organizer",
    "invoice-organizer", "lead-research-assistant",
    "meeting-insights-analyzer", "raffle-winner-picker",
    "domain-name-brainstormer", "theme-factory", "artifacts-builder",
    "canvas-design", "brand-guidelines", "developer-growth-analysis",
    "langsmith-fetch", "skill-creator", "skill-share", "connect",
    "connect-apps", "slack-gif-creator", "mintlify", "mintlify-mintlify",
    "internal-comms", "keybindings",
}

SKIP = {"template-skill", "connect-apps-plugin", "document-skills",
        "composio-skills"}


def get_category(skill_name: str) -> str:
    for prefix, cat in CATEGORIES.items():
        if skill_name.startswith(prefix):
            return cat
    if skill_name in UTILITY_SKILLS:
        return "utilities"
    return "utilities"


def load_skill(path: str) -> str:
    with open(path, "r", encoding="utf-8") as f:
        return f.read().strip()


def build_bundles():
    bundles: dict[str, list[tuple[str, str]]] = {}

    for entry in sorted(os.listdir(REPO)):
        if entry in SKIP:
            continue
        skill_dir = os.path.join(REPO, entry)
        skill_file = os.path.join(skill_dir, "SKILL.md")
        if not os.path.isfile(skill_file):
            continue

        cat   = get_category(entry)
        content = load_skill(skill_file)
        bundles.setdefault(cat, []).append((entry, content))

    return bundles


CATEGORY_LABELS = {
    "superpowers": "Superpowers — Workflow Intelligence",
    "gsd":         "GSD — Getting Stuff Done",
    "notion":      "Notion Integration",
    "figma":       "Figma Integration",
    "adspirer":    "Adspirer — Ads & Marketing",
    "claude-api":  "Claude API & MCP",
    "utilities":   "Utilities & Productivity",
}

SYSTEM_PROMPT = """\
# Claude Skills — Active

This project contains uploaded skill files that extend your capabilities.
Each file covers one category of skills. When the user asks for something
that matches a skill, locate and follow that skill's instructions exactly.

## How skills work

1. Read the relevant skill section from the uploaded files.
2. Follow its instructions step-by-step.
3. Tell the user which skill you're applying if it's not obvious.

## Skill categories available

| File | Category |
|------|----------|
| superpowers.md | Workflow intelligence — brainstorming, planning, TDD, debugging, code review |
| gsd.md | GSD productivity system — phases, milestones, todos, progress |
| notion.md | Notion — search, create pages, manage databases |
| figma.md | Figma — implement designs, design systems, Code Connect |
| adspirer.md | Ads & marketing — Google Ads, Meta, keyword research |
| claude-api.md | Claude API, MCP server building, TDD |
| utilities.md | Everything else — resume, tweet optimizer, file organizer, etc. |

## Triggering skills

Users trigger skills with natural language. Examples:

- "Load superpowers" → follow superpowers:using-superpowers
- "Brainstorm [feature]" → follow superpowers:brainstorming
- "Plan phase 3" → follow gsd:plan-phase
- "Search Notion for X" → follow notion-search
- "Implement this Figma design" → follow figma:implement-design
- "Research keywords for X" → follow adspirer keyword research
- "Tailor my resume for [job]" → follow tailored-resume-generator
- "Organize my Downloads folder" → follow file-organizer

When in doubt, search the uploaded files for matching skills and apply them.
"""


def write_bundle(cat: str, skills: list[tuple[str, str]], out_dir: str):
    label = CATEGORY_LABELS.get(cat, cat.title())
    lines = [f"# Skills: {label}\n",
             f"This file contains {len(skills)} skill(s) for the **{label}** category.",
             "Follow the relevant skill's instructions when the user's request matches.\n",
             "---\n"]

    for skill_name, content in skills:
        lines.append(f"## Skill: `{skill_name}`\n")
        lines.append(content)
        lines.append("\n---\n")

    path = os.path.join(out_dir, f"{cat}.md")
    with open(path, "w", encoding="utf-8") as f:
        f.write("\n".join(lines))
    return path, len(skills)


def main():
    os.makedirs(OUT, exist_ok=True)

    bundles = build_bundles()
    total   = 0

    print(f"Writing skill bundles to {OUT}/")
    for cat in ["superpowers", "gsd", "notion", "figma", "adspirer", "claude-api", "utilities"]:
        skills = bundles.get(cat, [])
        if not skills:
            continue
        path, n = write_bundle(cat, skills, OUT)
        print(f"  {cat}.md  ({n} skills)")
        total += n

    # System prompt
    sp_path = os.path.join(OUT, "system-prompt.md")
    with open(sp_path, "w", encoding="utf-8") as f:
        f.write(SYSTEM_PROMPT)
    print(f"  system-prompt.md  (paste into Project instructions)")

    # Setup guide
    readme = f"""\
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
| `superpowers.md` | {len(bundles.get('superpowers', []))} skills |
| `gsd.md` | {len(bundles.get('gsd', []))} skills |
| `notion.md` | {len(bundles.get('notion', []))} skills |
| `figma.md` | {len(bundles.get('figma', []))} skills |
| `adspirer.md` | {len(bundles.get('adspirer', []))} skills |
| `claude-api.md` | {len(bundles.get('claude-api', []))} skills |
| `utilities.md` | {len(bundles.get('utilities', []))} skills |

**Total: {total} skills**

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
"""

    readme_path = os.path.join(OUT, "README.md")
    with open(readme_path, "w", encoding="utf-8") as f:
        f.write(readme)
    print(f"  README.md  (setup guide)")
    print(f"\nDone — {total} skills bundled into {len(bundles)} files.")


if __name__ == "__main__":
    main()
