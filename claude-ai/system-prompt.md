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
