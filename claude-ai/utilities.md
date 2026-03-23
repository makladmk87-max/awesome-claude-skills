# Skills: Utilities & Productivity

This file contains 39 skill(s) for the **Utilities & Productivity** category.
Follow the relevant skill's instructions when the user's request matches.

---

## Skill: `artifacts-builder`

---
name: artifacts-builder
description: Suite of tools for creating elaborate, multi-component claude.ai HTML artifacts using modern frontend web technologies (React, Tailwind CSS, shadcn/ui). Use for complex artifacts requiring state management, routing, or shadcn/ui components - not for simple single-file HTML/JSX artifacts.
license: Complete terms in LICENSE.txt
---

# Artifacts Builder

To build powerful frontend claude.ai artifacts, follow these steps:
1. Initialize the frontend repo using `scripts/init-artifact.sh`
2. Develop your artifact by editing the generated code
3. Bundle all code into a single HTML file using `scripts/bundle-artifact.sh`
4. Display artifact to user
5. (Optional) Test the artifact

**Stack**: React 18 + TypeScript + Vite + Parcel (bundling) + Tailwind CSS + shadcn/ui

## Design & Style Guidelines

VERY IMPORTANT: To avoid what is often referred to as "AI slop", avoid using excessive centered layouts, purple gradients, uniform rounded corners, and Inter font.

## Quick Start

### Step 1: Initialize Project

Run the initialization script to create a new React project:
```bash
bash scripts/init-artifact.sh <project-name>
cd <project-name>
```

This creates a fully configured project with:
- ✅ React + TypeScript (via Vite)
- ✅ Tailwind CSS 3.4.1 with shadcn/ui theming system
- ✅ Path aliases (`@/`) configured
- ✅ 40+ shadcn/ui components pre-installed
- ✅ All Radix UI dependencies included
- ✅ Parcel configured for bundling (via .parcelrc)
- ✅ Node 18+ compatibility (auto-detects and pins Vite version)

### Step 2: Develop Your Artifact

To build the artifact, edit the generated files. See **Common Development Tasks** below for guidance.

### Step 3: Bundle to Single HTML File

To bundle the React app into a single HTML artifact:
```bash
bash scripts/bundle-artifact.sh
```

This creates `bundle.html` - a self-contained artifact with all JavaScript, CSS, and dependencies inlined. This file can be directly shared in Claude conversations as an artifact.

**Requirements**: Your project must have an `index.html` in the root directory.

**What the script does**:
- Installs bundling dependencies (parcel, @parcel/config-default, parcel-resolver-tspaths, html-inline)
- Creates `.parcelrc` config with path alias support
- Builds with Parcel (no source maps)
- Inlines all assets into single HTML using html-inline

### Step 4: Share Artifact with User

Finally, share the bundled HTML file in conversation with the user so they can view it as an artifact.

### Step 5: Testing/Visualizing the Artifact (Optional)

Note: This is a completely optional step. Only perform if necessary or requested.

To test/visualize the artifact, use available tools (including other Skills or built-in tools like Playwright or Puppeteer). In general, avoid testing the artifact upfront as it adds latency between the request and when the finished artifact can be seen. Test later, after presenting the artifact, if requested or if issues arise.

## Reference

- **shadcn/ui components**: https://ui.shadcn.com/docs/components

---

## Skill: `brainstorming`

---
name: brainstorming
description: Facilitate creative brainstorming sessions to generate ideas, explore possibilities, and unlock novel solutions. Use this skill when the user wants to generate ideas, explore options, think through a problem from multiple angles, or needs creative inspiration.
---

# Brainstorming

Facilitate high-quality brainstorming sessions that generate novel, diverse, and actionable ideas.

## Core Approach

Brainstorming works best when judgment is suspended during idea generation. Generate quantity first, then evaluate quality. Encourage divergent thinking before converging on solutions.

## Brainstorming Modes

### Mode 1: Open Exploration
When the user has a vague prompt or wants to explore broadly:
1. Reframe the problem in 2-3 different ways to unlock new angles
2. Generate ideas across different categories: conventional, unconventional, contrarian, and wild
3. Aim for at least 10-15 distinct ideas before filtering
4. Present ideas in clusters/themes, not just a flat list

### Mode 2: Constrained Generation
When the user has specific constraints (time, budget, tech, audience):
1. Acknowledge constraints explicitly upfront
2. Generate ideas that respect hard constraints
3. Flag which ideas push soft constraints — sometimes constraints are negotiable
4. Include at least one idea that challenges a stated constraint

### Mode 3: Build on Existing Ideas
When the user has partial ideas and wants to expand:
1. Extract the core insight from each existing idea
2. Generate variations: bigger, smaller, inverted, combined, applied elsewhere
3. Apply SCAMPER: Substitute, Combine, Adapt, Modify, Put to other uses, Eliminate, Reverse

## Framing Techniques

Use these to unlock stuck thinking:

- **Analogy**: "How would [unrelated industry/person] solve this?"
- **First principles**: "What's the most fundamental version of this problem?"
- **Inversion**: "What would make this maximally worse? Now invert."
- **Time travel**: "What would a solution from 10 years ago / 10 years future look like?"
- **Scale extremes**: "What if this needed to work for 1 person? 1 billion people?"
- **Resource extremes**: "What if budget were zero? Unlimited?"

## Output Format

Structure brainstorming output as:
1. **Reframed problem** (1-2 sentences) — confirm the real problem being solved
2. **Idea clusters** — group related ideas under themes
3. **Wild card** — one deliberately unconventional or counterintuitive idea
4. **Top 3 picks** — brief rationale for the most promising ideas
5. **Next step** — a concrete action to move from ideas to execution

## Facilitating Multi-Round Sessions

If the user wants to iterate:
- Ask "Which of these resonates most? Why?" to identify promising directions
- Drill deeper into selected ideas: risks, variations, prerequisites
- Combine ideas from different clusters
- Narrow to 1-3 actionable concepts with clear next steps

## Notes

- Never dismiss an idea during generation — defer evaluation to later
- If the user seems stuck on one approach, introduce deliberate constraints to force new thinking
- Brainstorming sessions should end with clarity, not just more options

---

## Skill: `brand-guidelines`

---
name: brand-guidelines
description: Applies Anthropic's official brand colors and typography to any sort of artifact that may benefit from having Anthropic's look-and-feel. Use it when brand colors or style guidelines, visual formatting, or company design standards apply.
license: Complete terms in LICENSE.txt
---

# Anthropic Brand Styling

## Overview

To access Anthropic's official brand identity and style resources, use this skill.

**Keywords**: branding, corporate identity, visual identity, post-processing, styling, brand colors, typography, Anthropic brand, visual formatting, visual design

## Brand Guidelines

### Colors

**Main Colors:**

- Dark: `#141413` - Primary text and dark backgrounds
- Light: `#faf9f5` - Light backgrounds and text on dark
- Mid Gray: `#b0aea5` - Secondary elements
- Light Gray: `#e8e6dc` - Subtle backgrounds

**Accent Colors:**

- Orange: `#d97757` - Primary accent
- Blue: `#6a9bcc` - Secondary accent
- Green: `#788c5d` - Tertiary accent

### Typography

- **Headings**: Poppins (with Arial fallback)
- **Body Text**: Lora (with Georgia fallback)
- **Note**: Fonts should be pre-installed in your environment for best results

## Features

### Smart Font Application

- Applies Poppins font to headings (24pt and larger)
- Applies Lora font to body text
- Automatically falls back to Arial/Georgia if custom fonts unavailable
- Preserves readability across all systems

### Text Styling

- Headings (24pt+): Poppins font
- Body text: Lora font
- Smart color selection based on background
- Preserves text hierarchy and formatting

### Shape and Accent Colors

- Non-text shapes use accent colors
- Cycles through orange, blue, and green accents
- Maintains visual interest while staying on-brand

## Technical Details

### Font Management

- Uses system-installed Poppins and Lora fonts when available
- Provides automatic fallback to Arial (headings) and Georgia (body)
- No font installation required - works with existing system fonts
- For best results, pre-install Poppins and Lora fonts in your environment

### Color Application

- Uses RGB color values for precise brand matching
- Applied via python-pptx's RGBColor class
- Maintains color fidelity across different systems

---

## Skill: `canvas-design`

---
name: canvas-design
description: Create beautiful visual art in .png and .pdf documents using design philosophy. You should use this skill when the user asks to create a poster, piece of art, design, or other static piece. Create original visual designs, never copying existing artists' work to avoid copyright violations.
license: Complete terms in LICENSE.txt
---

These are instructions for creating design philosophies - aesthetic movements that are then EXPRESSED VISUALLY. Output only .md files, .pdf files, and .png files.

Complete this in two steps:
1. Design Philosophy Creation (.md file)
2. Express by creating it on a canvas (.pdf file or .png file)

First, undertake this task:

## DESIGN PHILOSOPHY CREATION

To begin, create a VISUAL PHILOSOPHY (not layouts or templates) that will be interpreted through:
- Form, space, color, composition
- Images, graphics, shapes, patterns
- Minimal text as visual accent

### THE CRITICAL UNDERSTANDING
- What is received: Some subtle input or instructions by the user that should be taken into account, but used as a foundation; it should not constrain creative freedom.
- What is created: A design philosophy/aesthetic movement.
- What happens next: Then, the same version receives the philosophy and EXPRESSES IT VISUALLY - creating artifacts that are 90% visual design, 10% essential text.

Consider this approach:
- Write a manifesto for an art movement
- The next phase involves making the artwork

The philosophy must emphasize: Visual expression. Spatial communication. Artistic interpretation. Minimal words.

### HOW TO GENERATE A VISUAL PHILOSOPHY

**Name the movement** (1-2 words): "Brutalist Joy" / "Chromatic Silence" / "Metabolist Dreams"

**Articulate the philosophy** (4-6 paragraphs - concise but complete):

To capture the VISUAL essence, express how the philosophy manifests through:
- Space and form
- Color and material
- Scale and rhythm
- Composition and balance
- Visual hierarchy

**CRITICAL GUIDELINES:**
- **Avoid redundancy**: Each design aspect should be mentioned once. Avoid repeating points about color theory, spatial relationships, or typographic principles unless adding new depth.
- **Emphasize craftsmanship REPEATEDLY**: The philosophy MUST stress multiple times that the final work should appear as though it took countless hours to create, was labored over with care, and comes from someone at the absolute top of their field. This framing is essential - repeat phrases like "meticulously crafted," "the product of deep expertise," "painstaking attention," "master-level execution."
- **Leave creative space**: Remain specific about the aesthetic direction, but concise enough that the next Claude has room to make interpretive choices also at a extremely high level of craftmanship.

The philosophy must guide the next version to express ideas VISUALLY, not through text. Information lives in design, not paragraphs.

### PHILOSOPHY EXAMPLES

**"Concrete Poetry"**
Philosophy: Communication through monumental form and bold geometry.
Visual expression: Massive color blocks, sculptural typography (huge single words, tiny labels), Brutalist spatial divisions, Polish poster energy meets Le Corbusier. Ideas expressed through visual weight and spatial tension, not explanation. Text as rare, powerful gesture - never paragraphs, only essential words integrated into the visual architecture. Every element placed with the precision of a master craftsman.

**"Chromatic Language"**
Philosophy: Color as the primary information system.
Visual expression: Geometric precision where color zones create meaning. Typography minimal - small sans-serif labels letting chromatic fields communicate. Think Josef Albers' interaction meets data visualization. Information encoded spatially and chromatically. Words only to anchor what color already shows. The result of painstaking chromatic calibration.

**"Analog Meditation"**
Philosophy: Quiet visual contemplation through texture and breathing room.
Visual expression: Paper grain, ink bleeds, vast negative space. Photography and illustration dominate. Typography whispered (small, restrained, serving the visual). Japanese photobook aesthetic. Images breathe across pages. Text appears sparingly - short phrases, never explanatory blocks. Each composition balanced with the care of a meditation practice.

**"Organic Systems"**
Philosophy: Natural clustering and modular growth patterns.
Visual expression: Rounded forms, organic arrangements, color from nature through architecture. Information shown through visual diagrams, spatial relationships, iconography. Text only for key labels floating in space. The composition tells the story through expert spatial orchestration.

**"Geometric Silence"**
Philosophy: Pure order and restraint.
Visual expression: Grid-based precision, bold photography or stark graphics, dramatic negative space. Typography precise but minimal - small essential text, large quiet zones. Swiss formalism meets Brutalist material honesty. Structure communicates, not words. Every alignment the work of countless refinements.

*These are condensed examples. The actual design philosophy should be 4-6 substantial paragraphs.*

### ESSENTIAL PRINCIPLES
- **VISUAL PHILOSOPHY**: Create an aesthetic worldview to be expressed through design
- **MINIMAL TEXT**: Always emphasize that text is sparse, essential-only, integrated as visual element - never lengthy
- **SPATIAL EXPRESSION**: Ideas communicate through space, form, color, composition - not paragraphs
- **ARTISTIC FREEDOM**: The next Claude interprets the philosophy visually - provide creative room
- **PURE DESIGN**: This is about making ART OBJECTS, not documents with decoration
- **EXPERT CRAFTSMANSHIP**: Repeatedly emphasize the final work must look meticulously crafted, labored over with care, the product of countless hours by someone at the top of their field

**The design philosophy should be 4-6 paragraphs long.** Fill it with poetic design philosophy that brings together the core vision. Avoid repeating the same points. Keep the design philosophy generic without mentioning the intention of the art, as if it can be used wherever. Output the design philosophy as a .md file.

---

## DEDUCING THE SUBTLE REFERENCE

**CRITICAL STEP**: Before creating the canvas, identify the subtle conceptual thread from the original request.

**THE ESSENTIAL PRINCIPLE**:
The topic is a **subtle, niche reference embedded within the art itself** - not always literal, always sophisticated. Someone familiar with the subject should feel it intuitively, while others simply experience a masterful abstract composition. The design philosophy provides the aesthetic language. The deduced topic provides the soul - the quiet conceptual DNA woven invisibly into form, color, and composition.

This is **VERY IMPORTANT**: The reference must be refined so it enhances the work's depth without announcing itself. Think like a jazz musician quoting another song - only those who know will catch it, but everyone appreciates the music.

---

## CANVAS CREATION

With both the philosophy and the conceptual framework established, express it on a canvas. Take a moment to gather thoughts and clear the mind. Use the design philosophy created and the instructions below to craft a masterpiece, embodying all aspects of the philosophy with expert craftsmanship.

**IMPORTANT**: For any type of content, even if the user requests something for a movie/game/book, the approach should still be sophisticated. Never lose sight of the idea that this should be art, not something that's cartoony or amateur.

To create museum or magazine quality work, use the design philosophy as the foundation. Create one single page, highly visual, design-forward PDF or PNG output (unless asked for more pages). Generally use repeating patterns and perfect shapes. Treat the abstract philosophical design as if it were a scientific bible, borrowing the visual language of systematic observation—dense accumulation of marks, repeated elements, or layered patterns that build meaning through patient repetition and reward sustained viewing. Add sparse, clinical typography and systematic reference markers that suggest this could be a diagram from an imaginary discipline, treating the invisible subject with the same reverence typically reserved for documenting observable phenomena. Anchor the piece with simple phrase(s) or details positioned subtly, using a limited color palette that feels intentional and cohesive. Embrace the paradox of using analytical visual language to express ideas about human experience: the result should feel like an artifact that proves something ephemeral can be studied, mapped, and understood through careful attention. This is true art. 

**Text as a contextual element**: Text is always minimal and visual-first, but let context guide whether that means whisper-quiet labels or bold typographic gestures. A punk venue poster might have larger, more aggressive type than a minimalist ceramics studio identity. Most of the time, font should be thin. All use of fonts must be design-forward and prioritize visual communication. Regardless of text scale, nothing falls off the page and nothing overlaps. Every element must be contained within the canvas boundaries with proper margins. Check carefully that all text, graphics, and visual elements have breathing room and clear separation. This is non-negotiable for professional execution. **IMPORTANT: Use different fonts if writing text. Search the `./canvas-fonts` directory. Regardless of approach, sophistication is non-negotiable.**

Download and use whatever fonts are needed to make this a reality. Get creative by making the typography actually part of the art itself -- if the art is abstract, bring the font onto the canvas, not typeset digitally.

To push boundaries, follow design instinct/intuition while using the philosophy as a guiding principle. Embrace ultimate design freedom and choice. Push aesthetics and design to the frontier. 

**CRITICAL**: To achieve human-crafted quality (not AI-generated), create work that looks like it took countless hours. Make it appear as though someone at the absolute top of their field labored over every detail with painstaking care. Ensure the composition, spacing, color choices, typography - everything screams expert-level craftsmanship. Double-check that nothing overlaps, formatting is flawless, every detail perfect. Create something that could be shown to people to prove expertise and rank as undeniably impressive.

Output the final result as a single, downloadable .pdf or .png file, alongside the design philosophy used as a .md file.

---

## FINAL STEP

**IMPORTANT**: The user ALREADY said "It isn't perfect enough. It must be pristine, a masterpiece if craftsmanship, as if it were about to be displayed in a museum."

**CRITICAL**: To refine the work, avoid adding more graphics; instead refine what has been created and make it extremely crisp, respecting the design philosophy and the principles of minimalism entirely. Rather than adding a fun filter or refactoring a font, consider how to make the existing composition more cohesive with the art. If the instinct is to call a new function or draw a new shape, STOP and instead ask: "How can I make what's already here more of a piece of art?"

Take a second pass. Go back to the code and refine/polish further to make this a philosophically designed masterpiece.

## MULTI-PAGE OPTION

To create additional pages when requested, create more creative pages along the same lines as the design philosophy but distinctly different as well. Bundle those pages in the same .pdf or many .pngs. Treat the first page as just a single page in a whole coffee table book waiting to be filled. Make the next pages unique twists and memories of the original. Have them almost tell a story in a very tasteful way. Exercise full creative freedom.

---

## Skill: `changelog-generator`

---
name: changelog-generator
description: Automatically creates user-facing changelogs from git commits by analyzing commit history, categorizing changes, and transforming technical commits into clear, customer-friendly release notes. Turns hours of manual changelog writing into minutes of automated generation.
---

# Changelog Generator

This skill transforms technical git commits into polished, user-friendly changelogs that your customers and users will actually understand and appreciate.

## When to Use This Skill

- Preparing release notes for a new version
- Creating weekly or monthly product update summaries
- Documenting changes for customers
- Writing changelog entries for app store submissions
- Generating update notifications
- Creating internal release documentation
- Maintaining a public changelog/product updates page

## What This Skill Does

1. **Scans Git History**: Analyzes commits from a specific time period or between versions
2. **Categorizes Changes**: Groups commits into logical categories (features, improvements, bug fixes, breaking changes, security)
3. **Translates Technical → User-Friendly**: Converts developer commits into customer language
4. **Formats Professionally**: Creates clean, structured changelog entries
5. **Filters Noise**: Excludes internal commits (refactoring, tests, etc.)
6. **Follows Best Practices**: Applies changelog guidelines and your brand voice

## How to Use

### Basic Usage

From your project repository:

```
Create a changelog from commits since last release
```

```
Generate changelog for all commits from the past week
```

```
Create release notes for version 2.5.0
```

### With Specific Date Range

```
Create a changelog for all commits between March 1 and March 15
```

### With Custom Guidelines

```
Create a changelog for commits since v2.4.0, using my changelog 
guidelines from CHANGELOG_STYLE.md
```

## Example

**User**: "Create a changelog for commits from the past 7 days"

**Output**:
```markdown
# Updates - Week of March 10, 2024

## ✨ New Features

- **Team Workspaces**: Create separate workspaces for different 
  projects. Invite team members and keep everything organized.

- **Keyboard Shortcuts**: Press ? to see all available shortcuts. 
  Navigate faster without touching your mouse.

## 🔧 Improvements

- **Faster Sync**: Files now sync 2x faster across devices
- **Better Search**: Search now includes file contents, not just titles

## 🐛 Fixes

- Fixed issue where large images wouldn't upload
- Resolved timezone confusion in scheduled posts
- Corrected notification badge count
```

**Inspired by:** Manik Aggarwal's use case from Lenny's Newsletter

## Tips

- Run from your git repository root
- Specify date ranges for focused changelogs
- Use your CHANGELOG_STYLE.md for consistent formatting
- Review and adjust the generated changelog before publishing
- Save output directly to CHANGELOG.md

## Related Use Cases

- Creating GitHub release notes
- Writing app store update descriptions
- Generating email updates for users
- Creating social media announcement posts

---

## Skill: `code-review`

---
name: code-review
description: Perform thorough, constructive code reviews covering correctness, security, performance, maintainability, and style. Use this skill when the user wants code reviewed, asks for feedback on their code, or needs a diff/PR reviewed.
---

# Code Review

Perform thorough, actionable code reviews that improve code quality, catch bugs, and share knowledge.

## Review Dimensions

Review code across these dimensions, in order of importance:

### 1. Correctness
Does the code do what it's supposed to do?
- Does it handle edge cases? (empty input, null/undefined, zero, large values)
- Are there off-by-one errors in loops or indices?
- Is the logic correct for all branches?
- Does error handling cover all failure paths?
- Are async operations handled correctly? (race conditions, unresolved promises)
- Are there any infinite loops or missing loop termination conditions?

### 2. Security
Does the code introduce security vulnerabilities?
- **Injection** — SQL injection, XSS, command injection, template injection
- **Authentication/Authorization** — are permissions checked? Can users access others' data?
- **Input validation** — is user input sanitized/validated before use?
- **Secrets** — are credentials, tokens, or keys hardcoded or leaked in logs?
- **Sensitive data** — is PII/sensitive data logged, exposed in errors, or stored insecurely?
- **Dependencies** — are new dependencies vetted for known vulnerabilities?

### 3. Performance
Does the code perform well at scale?
- **N+1 queries** — database queries inside loops
- **Unnecessary computation** — repeated calculations that could be cached
- **Memory leaks** — unreleased resources, growing collections
- **Blocking operations** — sync I/O in async contexts
- **Inefficient data structures** — O(n) lookups where O(1) is possible

### 4. Maintainability
Will this code be easy to understand and change?
- Is the code readable? Would another developer understand it quickly?
- Are variable/function names descriptive and accurate?
- Is there duplication that should be extracted?
- Are functions/methods doing too much? (single responsibility)
- Is complexity appropriate? (avoid over-engineering)
- Are there magic numbers or strings that should be named constants?

### 5. Tests
Is the change adequately tested?
- Are new features covered by tests?
- Are edge cases and error paths tested?
- Are tests meaningful? (not just asserting implementation details)
- Does test coverage actually test the behavior that matters?

### 6. Style and Conventions
Does the code follow team/project conventions?
- Naming conventions (camelCase, snake_case, etc.)
- File and module organization
- Comment style and quality
- Import ordering

## Review Output Format

Structure reviews as:

```
## Summary
[1-3 sentence overview of the change and overall assessment]

## Critical Issues (must fix)
- [issue]: [explanation] [line reference if applicable]
  Suggestion: [how to fix]

## Minor Issues (should fix)
- [issue]: [explanation]
  Suggestion: [how to fix]

## Nits (optional)
- [style/preference items]

## Positives
- [things done well — always include at least one]
```

## Tone and Approach

- **Be specific** — "this could be cleaner" is not useful; explain what and why
- **Explain the why** — don't just flag issues, explain why they matter
- **Suggest, don't dictate** — for style/preference: "consider X" not "do X"
- **Acknowledge good work** — point out what's done well, not just problems
- **Prioritize** — distinguish blocking issues from minor suggestions

## Review Checklist

Before submitting the review, verify:
- [ ] Correctness checked for all code paths
- [ ] Security vulnerabilities checked (injection, auth, input validation, secrets)
- [ ] Performance issues checked (N+1, unnecessary computation)
- [ ] Tests are present and meaningful
- [ ] Variable/function names are clear
- [ ] No debug code, console.logs, or TODOs left in
- [ ] Breaking changes identified
- [ ] Documentation updated if needed

## Common Issues Quick Reference

| Category | Pattern to Flag |
|----------|----------------|
| Security | `eval()`, string concatenation in SQL, `innerHTML =`, hardcoded credentials |
| Performance | Query inside loop, `.find()` in inner loop, sync file I/O |
| Correctness | Missing null check, uncaught promise, off-by-one in slice |
| Maintainability | Function >50 lines, nesting >3 levels, magic number |
| Tests | No error path test, mock returning wrong shape |

## Notes for Claude

- Read the full diff before commenting — context from other changes matters
- Check if tests were updated to cover the change
- Flag security issues as Critical regardless of other context
- If reviewing a PR, understand the PR description and intended goal first

---

## Skill: `connect`

---
name: connect
description: Connect Claude to any app. Send emails, create issues, post messages, update databases - take real actions across Gmail, Slack, GitHub, Notion, and 1000+ services.
---

# Connect

Connect Claude to any app. Stop generating text about what you could do - actually do it.

## When to Use This Skill

Use this skill when you need Claude to:

- **Send that email** instead of drafting it
- **Create that issue** instead of describing it
- **Post that message** instead of suggesting it
- **Update that database** instead of explaining how

## What Changes

| Without Connect | With Connect |
|-----------------|--------------|
| "Here's a draft email..." | Sends the email |
| "You should create an issue..." | Creates the issue |
| "Post this to Slack..." | Posts it |
| "Add this to Notion..." | Adds it |

## Supported Apps

**1000+ integrations** including:

- **Email:** Gmail, Outlook, SendGrid
- **Chat:** Slack, Discord, Teams, Telegram
- **Dev:** GitHub, GitLab, Jira, Linear
- **Docs:** Notion, Google Docs, Confluence
- **Data:** Sheets, Airtable, PostgreSQL
- **CRM:** HubSpot, Salesforce, Pipedrive
- **Storage:** Drive, Dropbox, S3
- **Social:** Twitter, LinkedIn, Reddit

## Setup

### 1. Get API Key

Get your free key at [platform.composio.dev](https://platform.composio.dev/?utm_source=Github&utm_content=AwesomeSkills)

### 2. Set Environment Variable

```bash
export COMPOSIO_API_KEY="your-key"
```

### 3. Install

```bash
pip install composio          # Python
npm install @composio/core    # TypeScript
```

Done. Claude can now connect to any app.

## Examples

### Send Email
```
Email sarah@acme.com - Subject: "Shipped!" Body: "v2.0 is live, let me know if issues"
```

### Create GitHub Issue
```
Create issue in my-org/repo: "Mobile timeout bug" with label:bug
```

### Post to Slack
```
Post to #engineering: "Deploy complete - v2.4.0 live"
```

### Chain Actions
```
Find GitHub issues labeled "bug" from this week, summarize, post to #bugs on Slack
```

## How It Works

Uses Composio Tool Router:

1. **You ask** Claude to do something
2. **Tool Router finds** the right tool (1000+ options)
3. **OAuth handled** automatically
4. **Action executes** and returns result

### Code

```python
from composio import Composio
from claude_agent_sdk.client import ClaudeSDKClient
from claude_agent_sdk.types import ClaudeAgentOptions
import os

composio = Composio(api_key=os.environ["COMPOSIO_API_KEY"])
session = composio.create(user_id="user_123")

options = ClaudeAgentOptions(
    system_prompt="You can take actions in external apps.",
    mcp_servers={
        "composio": {
            "type": "http",
            "url": session.mcp.url,
            "headers": {"x-api-key": os.environ["COMPOSIO_API_KEY"]},
        }
    },
)

async with ClaudeSDKClient(options) as client:
    await client.query("Send Slack message to #general: Hello!")
```

## Auth Flow

First time using an app:
```
To send emails, I need Gmail access.
Authorize here: https://...
Say "connected" when done.
```

Connection persists after that.

## Framework Support

| Framework | Install |
|-----------|---------|
| Claude Agent SDK | `pip install composio claude-agent-sdk` |
| OpenAI Agents | `pip install composio openai-agents` |
| Vercel AI | `npm install @composio/core @composio/vercel` |
| LangChain | `pip install composio-langchain` |
| Any MCP Client | Use `session.mcp.url` |

## Troubleshooting

- **Auth required** → Click link, authorize, say "connected"
- **Action failed** → Check permissions in target app
- **Tool not found** → Be specific: "Slack #general" not "send message"

---

<p align="center">
  <b>Join 20,000+ developers building agents that ship</b>
</p>

<p align="center">
  <a href="https://platform.composio.dev/?utm_source=Github&utm_content=AwesomeSkills">
    <img src="https://img.shields.io/badge/Get_Started_Free-4F46E5?style=for-the-badge" alt="Get Started"/>
  </a>
</p>

---

## Skill: `connect-apps`

---
name: connect-apps
description: Connect Claude to external apps like Gmail, Slack, GitHub. Use this skill when the user wants to send emails, create issues, post messages, or take actions in external services.
---

# Connect Apps

Connect Claude to 1000+ apps. Actually send emails, create issues, post messages - not just generate text about it.

## Quick Start

### Step 1: Install the Plugin

```
/plugin install composio-toolrouter
```

### Step 2: Run Setup

```
/composio-toolrouter:setup
```

This will:
- Ask for your free API key (get one at [platform.composio.dev](https://platform.composio.dev/?utm_source=Github&utm_content=AwesomeSkills))
- Configure Claude's connection to 1000+ apps
- Take about 60 seconds

### Step 3: Try It!

After setup, restart Claude Code and try:

```
Send me a test email at YOUR_EMAIL@example.com
```

If it works, you're connected!

## What You Can Do

| Ask Claude to... | What happens |
|------------------|--------------|
| "Send email to sarah@acme.com about the launch" | Actually sends the email |
| "Create GitHub issue: fix login bug" | Creates the issue |
| "Post to Slack #general: deploy complete" | Posts the message |
| "Add meeting notes to Notion" | Adds to Notion |

## Supported Apps

**Email:** Gmail, Outlook, SendGrid
**Chat:** Slack, Discord, Teams, Telegram
**Dev:** GitHub, GitLab, Jira, Linear
**Docs:** Notion, Google Docs, Confluence
**Data:** Sheets, Airtable, PostgreSQL
**And 1000+ more...**

## How It Works

1. You ask Claude to do something
2. Composio Tool Router finds the right tool
3. First time? You'll authorize via OAuth (one-time)
4. Action executes and returns result

## Troubleshooting

- **"Plugin not found"** → Make sure you ran `/plugin install composio-toolrouter`
- **"Need to authorize"** → Click the OAuth link Claude provides, then say "done"
- **Action failed** → Check you have permissions in the target app

---

<p align="center">
  <b>Join 20,000+ developers building agents that ship</b>
</p>

<p align="center">
  <a href="https://platform.composio.dev/?utm_source=Github&utm_content=AwesomeSkills">
    <img src="https://img.shields.io/badge/Get_Started_Free-4F46E5?style=for-the-badge" alt="Get Started"/>
  </a>
</p>

---

## Skill: `content-research-writer`

---
name: content-research-writer
description: Assists in writing high-quality content by conducting research, adding citations, improving hooks, iterating on outlines, and providing real-time feedback on each section. Transforms your writing process from solo effort to collaborative partnership.
---

# Content Research Writer

This skill acts as your writing partner, helping you research, outline, draft, and refine content while maintaining your unique voice and style.

## When to Use This Skill

- Writing blog posts, articles, or newsletters
- Creating educational content or tutorials
- Drafting thought leadership pieces
- Researching and writing case studies
- Producing technical documentation with sources
- Writing with proper citations and references
- Improving hooks and introductions
- Getting section-by-section feedback while writing

## What This Skill Does

1. **Collaborative Outlining**: Helps you structure ideas into coherent outlines
2. **Research Assistance**: Finds relevant information and adds citations
3. **Hook Improvement**: Strengthens your opening to capture attention
4. **Section Feedback**: Reviews each section as you write
5. **Voice Preservation**: Maintains your writing style and tone
6. **Citation Management**: Adds and formats references properly
7. **Iterative Refinement**: Helps you improve through multiple drafts

## How to Use

### Setup Your Writing Environment

Create a dedicated folder for your article:
```
mkdir ~/writing/my-article-title
cd ~/writing/my-article-title
```

Create your draft file:
```
touch article-draft.md
```

Open Claude Code from this directory and start writing.

### Basic Workflow

1. **Start with an outline**:
```
Help me create an outline for an article about [topic]
```

2. **Research and add citations**:
```
Research [specific topic] and add citations to my outline
```

3. **Improve the hook**:
```
Here's my introduction. Help me make the hook more compelling.
```

4. **Get section feedback**:
```
I just finished the "Why This Matters" section. Review it and give feedback.
```

5. **Refine and polish**:
```
Review the full draft for flow, clarity, and consistency.
```

## Instructions

When a user requests writing assistance:

1. **Understand the Writing Project**
   
   Ask clarifying questions:
   - What's the topic and main argument?
   - Who's the target audience?
   - What's the desired length/format?
   - What's your goal? (educate, persuade, entertain, explain)
   - Any existing research or sources to include?
   - What's your writing style? (formal, conversational, technical)

2. **Collaborative Outlining**
   
   Help structure the content:
   
   ```markdown
   # Article Outline: [Title]
   
   ## Hook
   - [Opening line/story/statistic]
   - [Why reader should care]
   
   ## Introduction
   - Context and background
   - Problem statement
   - What this article covers
   
   ## Main Sections
   
   ### Section 1: [Title]
   - Key point A
   - Key point B
   - Example/evidence
   - [Research needed: specific topic]
   
   ### Section 2: [Title]
   - Key point C
   - Key point D
   - Data/citation needed
   
   ### Section 3: [Title]
   - Key point E
   - Counter-arguments
   - Resolution
   
   ## Conclusion
   - Summary of main points
   - Call to action
   - Final thought
   
   ## Research To-Do
   - [ ] Find data on [topic]
   - [ ] Get examples of [concept]
   - [ ] Source citation for [claim]
   ```
   
   **Iterate on outline**:
   - Adjust based on feedback
   - Ensure logical flow
   - Identify research gaps
   - Mark sections for deep dives

3. **Conduct Research**
   
   When user requests research on a topic:
   
   - Search for relevant information
   - Find credible sources
   - Extract key facts, quotes, and data
   - Add citations in requested format
   
   Example output:
   ```markdown
   ## Research: AI Impact on Productivity
   
   Key Findings:
   
   1. **Productivity Gains**: Studies show 40% time savings for 
      content creation tasks [1]
   
   2. **Adoption Rates**: 67% of knowledge workers use AI tools 
      weekly [2]
   
   3. **Expert Quote**: "AI augments rather than replaces human 
      creativity" - Dr. Jane Smith, MIT [3]
   
   Citations:
   [1] McKinsey Global Institute. (2024). "The Economic Potential 
       of Generative AI"
   [2] Stack Overflow Developer Survey (2024)
   [3] Smith, J. (2024). MIT Technology Review interview
   
   Added to outline under Section 2.
   ```

4. **Improve Hooks**
   
   When user shares an introduction, analyze and strengthen:
   
   **Current Hook Analysis**:
   - What works: [positive elements]
   - What could be stronger: [areas for improvement]
   - Emotional impact: [current vs. potential]
   
   **Suggested Alternatives**:
   
   Option 1: [Bold statement]
   > [Example]
   *Why it works: [explanation]*
   
   Option 2: [Personal story]
   > [Example]
   *Why it works: [explanation]*
   
   Option 3: [Surprising data]
   > [Example]
   *Why it works: [explanation]*
   
   **Questions to hook**:
   - Does it create curiosity?
   - Does it promise value?
   - Is it specific enough?
   - Does it match the audience?

5. **Provide Section-by-Section Feedback**
   
   As user writes each section, review for:
   
   ```markdown
   # Feedback: [Section Name]
   
   ## What Works Well ✓
   - [Strength 1]
   - [Strength 2]
   - [Strength 3]
   
   ## Suggestions for Improvement
   
   ### Clarity
   - [Specific issue] → [Suggested fix]
   - [Complex sentence] → [Simpler alternative]
   
   ### Flow
   - [Transition issue] → [Better connection]
   - [Paragraph order] → [Suggested reordering]
   
   ### Evidence
   - [Claim needing support] → [Add citation or example]
   - [Generic statement] → [Make more specific]
   
   ### Style
   - [Tone inconsistency] → [Match your voice better]
   - [Word choice] → [Stronger alternative]
   
   ## Specific Line Edits
   
   Original:
   > [Exact quote from draft]
   
   Suggested:
   > [Improved version]
   
   Why: [Explanation]
   
   ## Questions to Consider
   - [Thought-provoking question 1]
   - [Thought-provoking question 2]
   
   Ready to move to next section!
   ```

6. **Preserve Writer's Voice**
   
   Important principles:
   
   - **Learn their style**: Read existing writing samples
   - **Suggest, don't replace**: Offer options, not directives
   - **Match tone**: Formal, casual, technical, friendly
   - **Respect choices**: If they prefer their version, support it
   - **Enhance, don't override**: Make their writing better, not different
   
   Ask periodically:
   - "Does this sound like you?"
   - "Is this the right tone?"
   - "Should I be more/less [formal/casual/technical]?"

7. **Citation Management**
   
   Handle references based on user preference:
   
   **Inline Citations**:
   ```markdown
   Studies show 40% productivity improvement (McKinsey, 2024).
   ```
   
   **Numbered References**:
   ```markdown
   Studies show 40% productivity improvement [1].
   
   [1] McKinsey Global Institute. (2024)...
   ```
   
   **Footnote Style**:
   ```markdown
   Studies show 40% productivity improvement^1
   
   ^1: McKinsey Global Institute. (2024)...
   ```
   
   Maintain a running citations list:
   ```markdown
   ## References
   
   1. Author. (Year). "Title". Publication.
   2. Author. (Year). "Title". Publication.
   ...
   ```

8. **Final Review and Polish**
   
   When draft is complete, provide comprehensive feedback:
   
   ```markdown
   # Full Draft Review
   
   ## Overall Assessment
   
   **Strengths**:
   - [Major strength 1]
   - [Major strength 2]
   - [Major strength 3]
   
   **Impact**: [Overall effectiveness assessment]
   
   ## Structure & Flow
   - [Comments on organization]
   - [Transition quality]
   - [Pacing assessment]
   
   ## Content Quality
   - [Argument strength]
   - [Evidence sufficiency]
   - [Example effectiveness]
   
   ## Technical Quality
   - Grammar and mechanics: [assessment]
   - Consistency: [assessment]
   - Citations: [completeness check]
   
   ## Readability
   - Clarity score: [evaluation]
   - Sentence variety: [evaluation]
   - Paragraph length: [evaluation]
   
   ## Final Polish Suggestions
   
   1. **Introduction**: [Specific improvements]
   2. **Body**: [Specific improvements]
   3. **Conclusion**: [Specific improvements]
   4. **Title**: [Options if needed]
   
   ## Pre-Publish Checklist
   - [ ] All claims sourced
   - [ ] Citations formatted
   - [ ] Examples clear
   - [ ] Transitions smooth
   - [ ] Call to action present
   - [ ] Proofread for typos
   
   Ready to publish! 🚀
   ```

## Examples

### Example 1: Teresa Torres's Workflow

**User**: "I'm writing an article about continuous discovery. Help me create an outline."

**Process**:
1. Collaborates on outline structure
2. Identifies research needs
3. User starts writing introduction
4. Reviews and improves the hook
5. User writes each section
6. Provides feedback after each section
7. Conducts research and adds citations
8. Final review of complete draft
9. Polish and prep for publishing

**Result**: Well-researched, properly cited article written in Teresa's voice with strong structure and flow.

### Example 2: Research-Heavy Article

**User**: "I'm writing about AI's impact on product management. Help me find current data and examples."

**Output**:
```markdown
## Research Compiled

### Recent Data
- Gartner: 80% of PMs will use AI tools by 2025 [1]
- Survey: 45% report faster feature shipping [2]
- Case study: Airbnb's AI-assisted prioritization [3]

### Expert Quotes
- "AI amplifies PM judgment, not replaces it" - Marty Cagan
- [Additional quotes with citations]

### Real Examples
1. **Company A**: Used AI for user research synthesis
   - Result: 60% time savings
   - Source: [citation]

2. **Company B**: AI-powered roadmap analysis
   - Result: Better stakeholder alignment
   - Source: [citation]

All added to your outline with proper citations.
```

### Example 3: Hook Improvement

**User's Original Hook**:
> "Product management is changing because of AI. In this article, I'll discuss some ways AI affects product managers."

**Improved Options**:

**Option 1 (Data-driven)**:
> "Last month, I asked AI to analyze 500 customer interviews. It took 30 minutes instead of 3 weeks. Product management will never be the same."

**Option 2 (Question)**:
> "What if you could talk to every customer, read every review, and analyze every support ticket—all before your morning coffee?"

**Option 3 (Story)**:
> "Sarah spent two weeks building the wrong feature. Not because she didn't understand her users, but because she couldn't process the hundreds of interviews fast enough to spot the pattern."

### Example 4: Section Feedback

**User**: "Just finished my 'Common Mistakes' section. Thoughts?"

**Response**:
```markdown
# Feedback: Common Mistakes Section

## What Works Well ✓
- Strong examples (the Slack notification story)
- Clear structure (3 mistakes, clean layout)
- Practical advice for each mistake

## Suggestions

### Make It More Specific
Your second point says "Bad prioritization" but could be stronger:

Current:
> "Many teams prioritize badly by focusing on features instead of outcomes."

Suggested:
> "I've watched teams ship 14 features in a quarter yet move none of their key metrics. They prioritized activity over progress."

### Add Data
The third mistake would benefit from evidence:
> "[Add citation]: Studies show teams without regular user contact are 3x more likely to build unused features [needs source]"

### Flow Improvement
Consider reordering: Mistake 3 → Mistake 2 → Mistake 1
This builds from small to big impact.

Ready for the next section!
```

## Writing Workflows

### Blog Post Workflow
1. Outline together
2. Research key points
3. Write introduction → get feedback
4. Write body sections → feedback each
5. Write conclusion → final review
6. Polish and edit

### Newsletter Workflow
1. Discuss hook ideas
2. Quick outline (shorter format)
3. Draft in one session
4. Review for clarity and links
5. Quick polish

### Technical Tutorial Workflow
1. Outline steps
2. Write code examples
3. Add explanations
4. Test instructions
5. Add troubleshooting section
6. Final review for accuracy

### Thought Leadership Workflow
1. Brainstorm unique angle
2. Research existing perspectives
3. Develop your thesis
4. Write with strong POV
5. Add supporting evidence
6. Craft compelling conclusion

## Pro Tips

1. **Work in VS Code**: Better than web Claude for long-form writing
2. **One section at a time**: Get feedback incrementally
3. **Save research separately**: Keep a research.md file
4. **Version your drafts**: article-v1.md, article-v2.md, etc.
5. **Read aloud**: Use feedback to identify clunky sentences
6. **Set deadlines**: "I want to finish the draft today"
7. **Take breaks**: Write, get feedback, pause, revise

## File Organization

Recommended structure for writing projects:

```
~/writing/article-name/
├── outline.md          # Your outline
├── research.md         # All research and citations
├── draft-v1.md         # First draft
├── draft-v2.md         # Revised draft
├── final.md            # Publication-ready
├── feedback.md         # Collected feedback
└── sources/            # Reference materials
    ├── study1.pdf
    └── article2.md
```

## Best Practices

### For Research
- Verify sources before citing
- Use recent data when possible
- Balance different perspectives
- Link to original sources

### For Feedback
- Be specific about what you want: "Is this too technical?"
- Share your concerns: "I'm worried this section drags"
- Ask questions: "Does this flow logically?"
- Request alternatives: "What's another way to explain this?"

### For Voice
- Share examples of your writing
- Specify tone preferences
- Point out good matches: "That sounds like me!"
- Flag mismatches: "Too formal for my style"

## Related Use Cases

- Creating social media posts from articles
- Adapting content for different audiences
- Writing email newsletters
- Drafting technical documentation
- Creating presentation content
- Writing case studies
- Developing course outlines

---

## Skill: `debugging`

---
name: debugging
description: Systematically diagnose and fix bugs, errors, and unexpected behavior in code. Use this skill when the user has a bug, error message, unexpected behavior, or broken code that needs investigation and resolution.
---

# Debugging

Systematically diagnose and resolve bugs using structured investigation rather than random trial and error.

## Debugging Philosophy

Debugging is hypothesis-driven. Each step should:
1. Form a hypothesis about the root cause
2. Design a minimal test to confirm or refute it
3. Act on the result — fix or form the next hypothesis

Avoid random changes. Each change should test a specific hypothesis.

## Step 1: Understand the Bug

Before touching code, gather complete information:

- **What is the expected behavior?**
- **What is the actual behavior?**
- **When does it happen?** Always? Under specific conditions?
- **When did it start?** After a recent change? Always present?
- **What's the error?** Exact error message, stack trace, log output
- **What's the environment?** OS, runtime version, dependencies, config

Ask the user for any missing context before guessing.

## Step 2: Reproduce the Bug

Always reproduce before fixing:
- Find the minimal reproduction case
- Confirm the bug is reproducible consistently
- Rule out environment-specific issues (works on my machine?)
- If flaky: identify the conditions that trigger it

## Step 3: Locate the Source

Narrow down where the bug lives:

**Read the error message carefully:**
- Stack traces point to the line — but the bug may be higher up the call stack
- Error types (TypeError, KeyError, etc.) hint at the category of problem

**Bisect the problem:**
- Comment out / disable sections to isolate the faulty component
- Use binary search on recent commits if regression: `git bisect`
- Add logging/print statements to trace execution flow

**Check common culprits first:**
- Off-by-one errors in loops/indices
- Null/undefined/None not handled
- Type mismatches (string vs int, etc.)
- Async/timing issues (race conditions, unresolved promises)
- Scope issues (variable shadowing, closures)
- Mutation of shared state
- Wrong assumptions about external data shape

## Step 4: Fix and Verify

Once the root cause is identified:
1. Write the fix — targeted and minimal; avoid refactoring while debugging
2. Verify the original bug is gone with the reproduction case
3. Check for regressions — does anything else break?
4. Consider edge cases: what related inputs might also fail?

## Step 5: Document

After fixing:
- Add a comment explaining WHY the fix works (not just what it does)
- Add a test that would have caught this bug
- Note if there are related areas that might have the same issue

## Debugging Tools by Context

**JavaScript/TypeScript:**
```js
console.log(), console.error(), console.trace()
debugger; // pause in browser/Node
// Chrome DevTools, VS Code debugger
```

**Python:**
```python
print(), logging.debug()
import pdb; pdb.set_trace()  # or breakpoint() in Python 3.7+
# VS Code debugger, pdb, ipdb
```

**Git bisect (for regressions):**
```bash
git bisect start
git bisect bad HEAD
git bisect good <last-known-good-commit>
# Run tests, mark good/bad, git will find the culprit commit
```

## Common Bug Patterns

| Symptom | Likely Cause |
|---------|-------------|
| Works sometimes, fails sometimes | Race condition, async issue, flaky dependency |
| Only fails on specific input | Edge case, boundary condition |
| Fails only in production | Environment difference, missing config, different data |
| Was working, now broken | Recent change introduced regression |
| Wrong output, no error | Logic error, wrong algorithm, off-by-one |
| Correct output but crash later | Side effect, state mutation |

## Notes for Claude

- Read the full stack trace — the error origin is often not where the exception is thrown
- If the user has tried things already, ask what they tried — avoid repeating dead ends
- Never guess and apply multiple changes at once — test one hypothesis at a time
- If unable to reproduce locally, ask the user to add logging/print statements and share output

---

## Skill: `developer-growth-analysis`

---
name: developer-growth-analysis
description: Analyzes your recent Claude Code chat history to identify coding patterns, development gaps, and areas for improvement, curates relevant learning resources from HackerNews, and automatically sends a personalized growth report to your Slack DMs.
---

# Developer Growth Analysis

This skill provides personalized feedback on your recent coding work by analyzing your Claude Code chat interactions and identifying patterns that reveal strengths and areas for growth.

## When to Use This Skill

Use this skill when you want to:
- Understand your development patterns and habits from recent work
- Identify specific technical gaps or recurring challenges
- Discover which topics would benefit from deeper study
- Get curated learning resources tailored to your actual work patterns
- Track improvement areas across your recent projects
- Find high-quality articles that directly address the skills you're developing

This skill is ideal for developers who want structured feedback on their growth without waiting for code reviews, and who prefer data-driven insights from their own work history.

## What This Skill Does

This skill performs a six-step analysis of your development work:

1. **Reads Your Chat History**: Accesses your local Claude Code chat history from the past 24-48 hours to understand what you've been working on.

2. **Identifies Development Patterns**: Analyzes the types of problems you're solving, technologies you're using, challenges you encounter, and how you approach different kinds of tasks.

3. **Detects Improvement Areas**: Recognizes patterns that suggest skill gaps, repeated struggles, inefficient approaches, or areas where you might benefit from deeper knowledge.

4. **Generates a Personalized Report**: Creates a comprehensive report showing your work summary, identified improvement areas, and specific recommendations for growth.

5. **Finds Learning Resources**: Uses HackerNews to curate high-quality articles and discussions directly relevant to your improvement areas, providing you with a reading list tailored to your actual development work.

6. **Sends to Your Slack DMs**: Automatically delivers the complete report to your own Slack direct messages so you can reference it anytime, anywhere.

## How to Use

Ask Claude to analyze your recent coding work:

```
Analyze my developer growth from my recent chats
```

Or be more specific about which time period:

```
Analyze my work from today and suggest areas for improvement
```

The skill will generate a formatted report with:
- Overview of your recent work
- Key improvement areas identified
- Specific recommendations for each area
- Curated learning resources from HackerNews
- Action items you can focus on

## Instructions

When a user requests analysis of their developer growth or coding patterns from recent work:

1. **Access Chat History**

   Read the chat history from `~/.claude/history.jsonl`. This file is a JSONL format where each line contains:
   - `display`: The user's message/request
   - `project`: The project being worked on
   - `timestamp`: Unix timestamp (in milliseconds)
   - `pastedContents`: Any code or content pasted

   Filter for entries from the past 24-48 hours based on the current timestamp.

2. **Analyze Work Patterns**

   Extract and analyze the following from the filtered chats:
   - **Projects and Domains**: What types of projects was the user working on? (e.g., backend, frontend, DevOps, data, etc.)
   - **Technologies Used**: What languages, frameworks, and tools appear in the conversations?
   - **Problem Types**: What categories of problems are being solved? (e.g., performance optimization, debugging, feature implementation, refactoring, setup/configuration)
   - **Challenges Encountered**: What problems did the user struggle with? Look for:
     - Repeated questions about similar topics
     - Problems that took multiple attempts to solve
     - Questions indicating knowledge gaps
     - Complex architectural decisions
   - **Approach Patterns**: How does the user solve problems? (e.g., methodical, exploratory, experimental)

3. **Identify Improvement Areas**

   Based on the analysis, identify 3-5 specific areas where the user could improve. These should be:
   - **Specific** (not vague like "improve coding skills")
   - **Evidence-based** (grounded in actual chat history)
   - **Actionable** (practical improvements that can be made)
   - **Prioritized** (most impactful first)

   Examples of good improvement areas:
   - "Advanced TypeScript patterns (generics, utility types, type guards) - you struggled with type safety in [specific project]"
   - "Error handling and validation - I noticed you patched several bugs related to missing null checks"
   - "Async/await patterns - your recent work shows some race conditions and timing issues"
   - "Database query optimization - you rewrote the same query multiple times"

4. **Generate Report**

   Create a comprehensive report with this structure:

   ```markdown
   # Your Developer Growth Report

   **Report Period**: [Yesterday / Today / [Custom Date Range]]
   **Last Updated**: [Current Date and Time]

   ## Work Summary

   [2-3 paragraphs summarizing what the user worked on, projects touched, technologies used, and overall focus areas]

   Example:
   "Over the past 24 hours, you focused primarily on backend development with three distinct projects. Your work involved TypeScript, React, and deployment infrastructure. You tackled a mix of feature implementation, debugging, and architectural decisions, with a particular focus on API design and database optimization."

   ## Improvement Areas (Prioritized)

   ### 1. [Area Name]

   **Why This Matters**: [Explanation of why this skill is important for the user's work]

   **What I Observed**: [Specific evidence from chat history showing this gap]

   **Recommendation**: [Concrete step(s) to improve in this area]

   **Time to Skill Up**: [Brief estimate of effort required]

   ---

   [Repeat for 2-4 additional areas]

   ## Strengths Observed

   [2-3 bullet points highlighting things you're doing well - things to continue doing]

   ## Action Items

   Priority order:
   1. [Action item derived from highest priority improvement area]
   2. [Action item from next area]
   3. [Action item from next area]

   ## Learning Resources

   [Will be populated in next step]
   ```

5. **Search for Learning Resources**

   Use Rube MCP to search HackerNews for articles related to each improvement area:

   - For each improvement area, construct a search query targeting high-quality resources
   - Search HackerNews using RUBE_SEARCH_TOOLS with queries like:
     - "Learn [Technology/Pattern] best practices"
     - "[Technology] advanced patterns and techniques"
     - "Debugging [specific problem type] in [language]"
   - Prioritize posts with high engagement (comments, upvotes)
   - For each area, include 2-3 most relevant articles with:
     - Article title
     - Publication date
     - Brief description of why it's relevant
     - Link to the article

   Add this section to the report:

   ```markdown
   ## Curated Learning Resources

   ### For: [Improvement Area]

   1. **[Article Title]** - [Date]
      [Description of what it covers and why it's relevant to your improvement area]
      [Link]

   2. **[Article Title]** - [Date]
      [Description]
      [Link]

   [Repeat for other improvement areas]
   ```

6. **Present the Complete Report**

   Deliver the report in a clean, readable format that the user can:
   - Quickly scan for key takeaways
   - Use for focused learning planning
   - Reference over the next week as they work on improvements
   - Share with mentors if they want external feedback

7. **Send Report to Slack DMs**

   Use Rube MCP to send the complete report to the user's own Slack DMs:

   - Check if Slack connection is active via RUBE_SEARCH_TOOLS
   - If not connected, use RUBE_MANAGE_CONNECTIONS to initiate Slack auth
   - Use RUBE_MULTI_EXECUTE_TOOL to send the report as a formatted message:
     - Send the report title and period as the first message
     - Break the report into logical sections (Summary, Improvements, Strengths, Actions, Resources)
     - Format each section as a well-structured Slack message with proper markdown
     - Include clickable links for the learning resources
   - Confirm delivery in the CLI output

   This ensures the user has the report in a place they check regularly and can reference it throughout the week.

## Example Usage

### Input

```
Analyze my developer growth from my recent chats
```

### Output

```markdown
# Your Developer Growth Report

**Report Period**: November 9-10, 2024
**Last Updated**: November 10, 2024, 9:15 PM UTC

## Work Summary

Over the past two days, you focused on backend infrastructure and API development. Your primary project was an open-source showcase application, where you made significant progress on connections management, UI improvements, and deployment configuration. You worked with TypeScript, React, and Node.js, tackling challenges ranging from data security to responsive design. Your work shows a balance between implementing features and addressing technical debt.

## Improvement Areas (Prioritized)

### 1. Advanced TypeScript Patterns and Type Safety

**Why This Matters**: TypeScript is central to your work, but leveraging its advanced features (generics, utility types, conditional types, type guards) can significantly improve code reliability and reduce runtime errors. Better type safety catches bugs at compile time rather than in production.

**What I Observed**: In your recent chats, you were working with connection data structures and struggled a few times with typing auth configurations properly. You also had to iterate on union types for different connection states. There's an opportunity to use discriminated unions and type guards more effectively.

**Recommendation**: Study TypeScript's advanced type system, particularly utility types (Omit, Pick, Record), conditional types, and discriminated unions. Apply these patterns to your connection configuration handling and auth state management.

**Time to Skill Up**: 5-8 hours of focused learning and practice

### 2. Secure Data Handling and Information Hiding in UI

**Why This Matters**: You identified and fixed a security concern where sensitive connection data was being displayed in your console. Preventing information leakage is critical for applications handling user credentials and API keys. Good practices here prevent security incidents and user trust violations.

**What I Observed**: You caught that your "Your Apps" page was showing full connection data including auth configs. This shows good security instincts, and the next step is building this into your default thinking when handling sensitive information.

**Recommendation**: Review security best practices for handling sensitive data in frontend applications. Create reusable patterns for filtering/masking sensitive information before displaying it. Consider implementing a secure data layer that explicitly whitelist what can be shown in the UI.

**Time to Skill Up**: 3-4 hours

### 3. Component Architecture and Responsive UI Patterns

**Why This Matters**: You're designing UIs that need to work across different screen sizes and user interactions. Strong component architecture makes it easier to build complex UIs without bugs and improves maintainability.

**What I Observed**: You worked on the "Marketplace" UI (formerly Browse Tools), recreating it from a design image. You also identified and fixed scrolling issues where content was overflowing containers. There's an opportunity to strengthen your understanding of layout containment and responsive design patterns.

**Recommendation**: Study React component composition patterns and CSS layout best practices (especially flexbox and grid). Focus on container queries and responsive patterns that prevent overflow issues. Look into component composition libraries and design system approaches.

**Time to Skill Up**: 6-10 hours (depending on depth)

## Strengths Observed

- **Security Awareness**: You proactively identified data leakage issues before they became problems
- **Iterative Refinement**: You worked through UI requirements methodically, asking clarifying questions and improving designs
- **Full-Stack Capability**: You comfortably work across backend APIs, frontend UI, and deployment concerns
- **Problem-Solving Approach**: You break down complex tasks into manageable steps

## Action Items

Priority order:
1. Spend 1-2 hours learning TypeScript utility types and discriminated unions; apply to your connection data structures
2. Document security patterns for your project (what data is safe to display, filtering/masking functions)
3. Study one article on advanced React patterns and apply one pattern to your current UI work
4. Set up a code review checklist focused on type safety and data security for future PRs

## Curated Learning Resources

### For: Advanced TypeScript Patterns

1. **TypeScript's Advanced Types: Generics, Utility Types, and Conditional Types** - HackerNews, October 2024
   Deep dive into TypeScript's type system with practical examples and real-world applications. Covers discriminated unions, type guards, and patterns for ensuring compile-time safety in complex applications.
   [Link to discussion]

2. **Building Type-Safe APIs in TypeScript** - HackerNews, September 2024
   Practical guide to designing APIs with TypeScript that catch errors early. Particularly relevant for your connection configuration work.
   [Link to discussion]

### For: Secure Data Handling in Frontend

1. **Preventing Information Leakage in Web Applications** - HackerNews, August 2024
   Comprehensive guide to data security in frontend applications, including filtering sensitive information, secure logging, and audit trails.
   [Link to discussion]

2. **OAuth and API Key Management Best Practices** - HackerNews, July 2024
   How to safely handle authentication tokens and API keys in applications, with examples for different frameworks.
   [Link to discussion]

### For: Component Architecture and Responsive Design

1. **Advanced React Patterns: Composition Over Configuration** - HackerNews
   Explores component composition strategies that scale, with examples using modern React patterns.
   [Link to discussion]

2. **CSS Layout Mastery: Flexbox, Grid, and Container Queries** - HackerNews, October 2024
   Learn responsive design patterns that prevent overflow issues and work across all screen sizes.
   [Link to discussion]
```

## Tips and Best Practices

- Run this analysis once a week to track your improvement trajectory over time
- Pick one improvement area at a time and focus on it for a few days before moving to the next
- Use the learning resources as a study guide; work through the recommended materials and practice applying the patterns
- Revisit this report after focusing on an area for a week to see how your work patterns change
- The learning resources are intentionally curated for your actual work, not generic topics, so they'll be highly relevant to what you're building

## How Accuracy and Quality Are Maintained

This skill:
- Analyzes your actual work patterns from timestamped chat history
- Generates evidence-based recommendations grounded in real projects
- Curates learning resources that directly address your identified gaps
- Focuses on actionable improvements, not vague feedback
- Provides specific time estimates based on complexity
- Prioritizes areas that will have the most impact on your development velocity

---

## Skill: `domain-name-brainstormer`

---
name: domain-name-brainstormer
description: Generates creative domain name ideas for your project and checks availability across multiple TLDs (.com, .io, .dev, .ai, etc.). Saves hours of brainstorming and manual checking.
---

# Domain Name Brainstormer

This skill helps you find the perfect domain name for your project by generating creative options and checking what's actually available to register.

## When to Use This Skill

- Starting a new project or company
- Launching a product or service
- Creating a personal brand or portfolio site
- Rebranding an existing project
- Registering a domain for a side project
- Finding available alternatives when your first choice is taken

## What This Skill Does

1. **Understands Your Project**: Analyzes what you're building and who it's for
2. **Generates Creative Names**: Creates relevant, memorable domain options
3. **Checks Availability**: Verifies which domains are actually available across multiple TLDs
4. **Multiple Extensions**: Suggests .com, .io, .dev, .ai, .app, and more
5. **Provides Alternatives**: Offers variations if top choices are taken
6. **Branding Insights**: Explains why certain names work well

## How to Use

### Basic Brainstorming

```
I'm building a project management tool for remote teams. 
Suggest domain names.
```

```
Help me brainstorm domain names for a personal finance app
```

### Specific Preferences

```
I need a domain name for my AI writing assistant. 
Prefer short names with .ai or .io extension.
```

### With Keywords

```
Suggest domain names using the words "pixel" or "studio" 
for my design agency
```

## Example

**User**: "I'm building a tool for developers to share code snippets. Suggest creative domain names."

**Output**:
```
Analyzing your project...
Target audience: Developers
Key features: Code sharing, snippets, collaboration

🎯 Domain Name Suggestions

## Available (.com)
1. ✓ snippetbox.com - Clear, memorable, available!
   Why: Directly describes the product, easy to remember

2. ✓ codeclip.com - Short and snappy
   Why: Implies quick code sharing, only 8 characters

3. ✓ devpaste.com - Developer-focused
   Why: Familiar to devs (like pastebin), clear purpose

## Available (Alternative TLDs)
4. ✓ snippet.dev - Perfect extension for developers
   Why: .dev extension signals developer tool

5. ✓ codebox.io - Tech-forward
   Why: .io popular with tech startups, clean name

6. ✓ sharecode.app - Descriptive
   Why: .app extension, clearly states the action

## Premium/Taken (.com)
- codeshare.com (Taken, est. $2,500)
- snippets.com (Taken, premium domain)

## Recommendations

🏆 Top Pick: snippet.dev
- Perfect for developer audience
- Short and memorable  
- .dev extension adds credibility
- Available now!

🥈 Runner-up: snippetbox.com
- .com is universally recognized
- Slightly longer but descriptive
- Great brandability

Next steps:
1. Register your favorite before someone else does!
2. Want me to check more variations?
3. Need help with logo ideas for these names?
```

**Inspired by:** Ben Aiad's use case from Lenny's Newsletter

## Domain Naming Tips

### What Makes a Good Domain

✓ **Short**: Under 15 characters ideal
✓ **Memorable**: Easy to recall and spell
✓ **Pronounceable**: Can be said in conversation
✓ **Descriptive**: Hints at what you do
✓ **Brandable**: Unique enough to stand out
✓ **No hyphens**: Easier to share verbally

### TLD Guide

- **.com**: Universal, trusted, great for businesses
- **.io**: Tech startups, developer tools
- **.dev**: Developer-focused products
- **.ai**: AI/ML products
- **.app**: Mobile or web applications
- **.co**: Alternative to .com
- **.xyz**: Modern, creative projects
- **.design**: Creative/design agencies
- **.tech**: Technology companies

## Advanced Features

### Check Similar Variations

```
Check availability for "codebase" and similar variations 
across .com, .io, .dev
```

### Industry-Specific

```
Suggest domain names for a sustainable fashion brand, 
checking .eco and .fashion TLDs
```

### Multilingual Options

```
Brainstorm domain names in English and Spanish for 
a language learning app
```

### Competitor Analysis

```
Show me domain patterns used by successful project 
management tools, then suggest similar available ones
```

## Example Workflows

### Startup Launch
1. Describe your startup idea
2. Get 10-15 domain suggestions across TLDs
3. Review availability and pricing
4. Pick top 3 favorites
5. Register immediately

### Personal Brand
1. Share your name and profession
2. Get variations (firstname.com, firstnamelastname.dev, etc.)
3. Check social media handle availability too
4. Register consistent brand across platforms

### Product Naming
1. Describe product and target market
2. Get creative, brandable names
3. Check trademark conflicts
4. Verify domain and social availability
5. Test names with target audience

## Tips for Success

1. **Act Fast**: Good domains get taken quickly
2. **Register Variations**: Get .com and .io to protect brand
3. **Avoid Numbers**: Hard to communicate verbally
4. **Check Social Media**: Make sure @username is available too
5. **Say It Out Loud**: Test if it's easy to pronounce
6. **Check Trademarks**: Ensure no legal conflicts
7. **Think Long-term**: Will it still make sense in 5 years?

## Pricing Context

When suggesting domains, I'll note:
- Standard domains: ~$10-15/year
- Premium TLDs (.io, .ai): ~$30-50/year
- Taken domains: Market price if listed
- Premium domains: $hundreds to $thousands

## Related Tools

After picking a domain:
- Check logo design options
- Verify social media handles
- Research trademark availability
- Plan brand identity colors/fonts

---

## Skill: `file-organizer`

---
name: file-organizer
description: Intelligently organizes your files and folders across your computer by understanding context, finding duplicates, suggesting better structures, and automating cleanup tasks. Reduces cognitive load and keeps your digital workspace tidy without manual effort.
---

# File Organizer

This skill acts as your personal organization assistant, helping you maintain a clean, logical file structure across your computer without the mental overhead of constant manual organization.

## When to Use This Skill

- Your Downloads folder is a chaotic mess
- You can't find files because they're scattered everywhere
- You have duplicate files taking up space
- Your folder structure doesn't make sense anymore
- You want to establish better organization habits
- You're starting a new project and need a good structure
- You're cleaning up before archiving old projects

## What This Skill Does

1. **Analyzes Current Structure**: Reviews your folders and files to understand what you have
2. **Finds Duplicates**: Identifies duplicate files across your system
3. **Suggests Organization**: Proposes logical folder structures based on your content
4. **Automates Cleanup**: Moves, renames, and organizes files with your approval
5. **Maintains Context**: Makes smart decisions based on file types, dates, and content
6. **Reduces Clutter**: Identifies old files you probably don't need anymore

## How to Use

### From Your Home Directory

```
cd ~
```

Then run Claude Code and ask for help:

```
Help me organize my Downloads folder
```

```
Find duplicate files in my Documents folder
```

```
Review my project directories and suggest improvements
```

### Specific Organization Tasks

```
Organize these downloads into proper folders based on what they are
```

```
Find duplicate files and help me decide which to keep
```

```
Clean up old files I haven't touched in 6+ months
```

```
Create a better folder structure for my [work/projects/photos/etc]
```

## Instructions

When a user requests file organization help:

1. **Understand the Scope**
   
   Ask clarifying questions:
   - Which directory needs organization? (Downloads, Documents, entire home folder?)
   - What's the main problem? (Can't find things, duplicates, too messy, no structure?)
   - Any files or folders to avoid? (Current projects, sensitive data?)
   - How aggressively to organize? (Conservative vs. comprehensive cleanup)

2. **Analyze Current State**
   
   Review the target directory:
   ```bash
   # Get overview of current structure
   ls -la [target_directory]
   
   # Check file types and sizes
   find [target_directory] -type f -exec file {} \; | head -20
   
   # Identify largest files
   du -sh [target_directory]/* | sort -rh | head -20
   
   # Count file types
   find [target_directory] -type f | sed 's/.*\.//' | sort | uniq -c | sort -rn
   ```
   
   Summarize findings:
   - Total files and folders
   - File type breakdown
   - Size distribution
   - Date ranges
   - Obvious organization issues

3. **Identify Organization Patterns**
   
   Based on the files, determine logical groupings:
   
   **By Type**:
   - Documents (PDFs, DOCX, TXT)
   - Images (JPG, PNG, SVG)
   - Videos (MP4, MOV)
   - Archives (ZIP, TAR, DMG)
   - Code/Projects (directories with code)
   - Spreadsheets (XLSX, CSV)
   - Presentations (PPTX, KEY)
   
   **By Purpose**:
   - Work vs. Personal
   - Active vs. Archive
   - Project-specific
   - Reference materials
   - Temporary/scratch files
   
   **By Date**:
   - Current year/month
   - Previous years
   - Very old (archive candidates)

4. **Find Duplicates**
   
   When requested, search for duplicates:
   ```bash
   # Find exact duplicates by hash
   find [directory] -type f -exec md5 {} \; | sort | uniq -d
   
   # Find files with same name
   find [directory] -type f -printf '%f\n' | sort | uniq -d
   
   # Find similar-sized files
   find [directory] -type f -printf '%s %p\n' | sort -n
   ```
   
   For each set of duplicates:
   - Show all file paths
   - Display sizes and modification dates
   - Recommend which to keep (usually newest or best-named)
   - **Important**: Always ask for confirmation before deleting

5. **Propose Organization Plan**
   
   Present a clear plan before making changes:
   
   ```markdown
   # Organization Plan for [Directory]
   
   ## Current State
   - X files across Y folders
   - [Size] total
   - File types: [breakdown]
   - Issues: [list problems]
   
   ## Proposed Structure
   
   ```
   [Directory]/
   ├── Work/
   │   ├── Projects/
   │   ├── Documents/
   │   └── Archive/
   ├── Personal/
   │   ├── Photos/
   │   ├── Documents/
   │   └── Media/
   └── Downloads/
       ├── To-Sort/
       └── Archive/
   ```
   
   ## Changes I'll Make
   
   1. **Create new folders**: [list]
   2. **Move files**:
      - X PDFs → Work/Documents/
      - Y images → Personal/Photos/
      - Z old files → Archive/
   3. **Rename files**: [any renaming patterns]
   4. **Delete**: [duplicates or trash files]
   
   ## Files Needing Your Decision
   
   - [List any files you're unsure about]
   
   Ready to proceed? (yes/no/modify)
   ```

6. **Execute Organization**
   
   After approval, organize systematically:
   
   ```bash
   # Create folder structure
   mkdir -p "path/to/new/folders"
   
   # Move files with clear logging
   mv "old/path/file.pdf" "new/path/file.pdf"
   
   # Rename files with consistent patterns
   # Example: "YYYY-MM-DD - Description.ext"
   ```
   
   **Important Rules**:
   - Always confirm before deleting anything
   - Log all moves for potential undo
   - Preserve original modification dates
   - Handle filename conflicts gracefully
   - Stop and ask if you encounter unexpected situations

7. **Provide Summary and Maintenance Tips**
   
   After organizing:
   
   ```markdown
   # Organization Complete! ✨
   
   ## What Changed
   
   - Created [X] new folders
   - Organized [Y] files
   - Freed [Z] GB by removing duplicates
   - Archived [W] old files
   
   ## New Structure
   
   [Show the new folder tree]
   
   ## Maintenance Tips
   
   To keep this organized:
   
   1. **Weekly**: Sort new downloads
   2. **Monthly**: Review and archive completed projects
   3. **Quarterly**: Check for new duplicates
   4. **Yearly**: Archive old files
   
   ## Quick Commands for You
   
   ```bash
   # Find files modified this week
   find . -type f -mtime -7
   
   # Sort downloads by type
   [custom command for their setup]
   
   # Find duplicates
   [custom command]
   ```
   
   Want to organize another folder?
   ```

## Examples

### Example 1: Organizing Downloads (From Justin Dielmann)

**User**: "My Downloads folder is a mess with 500+ files. Help me organize it."

**Process**:
1. Analyzes Downloads folder
2. Finds patterns: work docs, personal photos, installers, random PDFs
3. Proposes structure:
   - Downloads/
     - Work/
     - Personal/
     - Installers/ (DMG, PKG files)
     - Archive/
     - ToSort/ (things needing decisions)
4. Asks for confirmation
5. Moves files intelligently based on content and names
6. Results: 500 files → 5 organized folders

### Example 2: Finding and Removing Duplicates

**User**: "Find duplicate files in my Documents and help me decide which to keep."

**Output**:
```markdown
# Found 23 Sets of Duplicates (156 MB total)

## Duplicate Set 1: "proposal.pdf"
- `/Documents/proposal.pdf` (2.3 MB, modified: 2024-03-15)
- `/Documents/old/proposal.pdf` (2.3 MB, modified: 2024-03-15)
- `/Desktop/proposal.pdf` (2.3 MB, modified: 2024-03-10)

**Recommendation**: Keep `/Documents/proposal.pdf` (most recent in correct location)
Delete the other 2 copies?

[Continue for all duplicates...]
```

### Example 3: Restructuring Projects Folder

**User**: "Review my ~/Projects directory and suggest improvements."

**Output**:
```markdown
# Analysis of ~/Projects

## Current Structure Issues
- Mix of active and archived projects (3+ years old)
- No consistent naming convention
- Some projects at root, others in random subfolders
- Duplicate folders (project-name, project-name-old, project-name-v2)

## Proposed Structure

```
Projects/
├── Active/
│   ├── client-work/
│   ├── side-projects/
│   └── learning/
├── Archive/
│   ├── 2022/
│   ├── 2023/
│   └── 2024/
└── Templates/
```

## Specific Changes
1. Move 12 projects not touched since 2022 → Archive/
2. Consolidate 4 duplicate project folders
3. Rename projects to consistent format: "client-name-project-name"
4. Create Archive for old work

Want me to implement this?
```

### Example 4: Organizing Photos by Date

**User**: "Organize my photo folders by year and month."

**Output**: Creates structure like:
```
Photos/
├── 2023/
│   ├── 01-January/
│   ├── 02-February/
│   └── ...
├── 2024/
│   ├── 01-January/
│   └── ...
└── Unsorted/
```

Then moves photos based on EXIF data or file modification dates.

## Common Organization Tasks

### Downloads Cleanup
```
Organize my Downloads folder - move documents to Documents, 
images to Pictures, keep installers separate, and archive files 
older than 3 months.
```

### Project Organization
```
Review my Projects folder structure and help me separate active 
projects from old ones I should archive.
```

### Duplicate Removal
```
Find all duplicate files in my Documents folder and help me 
decide which ones to keep.
```

### Desktop Cleanup
```
My Desktop is covered in files. Help me organize everything into 
my Documents folder properly.
```

### Photo Organization
```
Organize all photos in this folder by date (year/month) based 
on when they were taken.
```

### Work/Personal Separation
```
Help me separate my work files from personal files across my 
Documents folder.
```

## Pro Tips

1. **Start Small**: Begin with one messy folder (like Downloads) to build trust
2. **Regular Maintenance**: Run weekly cleanup on Downloads
3. **Consistent Naming**: Use "YYYY-MM-DD - Description" format for important files
4. **Archive Aggressively**: Move old projects to Archive instead of deleting
5. **Keep Active Separate**: Maintain clear boundaries between active and archived work
6. **Trust the Process**: Let Claude handle the cognitive load of where things go

## Best Practices

### Folder Naming
- Use clear, descriptive names
- Avoid spaces (use hyphens or underscores)
- Be specific: "client-proposals" not "docs"
- Use prefixes for ordering: "01-current", "02-archive"

### File Naming
- Include dates: "2024-10-17-meeting-notes.md"
- Be descriptive: "q3-financial-report.xlsx"
- Avoid version numbers in names (use version control instead)
- Remove download artifacts: "document-final-v2 (1).pdf" → "document.pdf"

### When to Archive
- Projects not touched in 6+ months
- Completed work that might be referenced later
- Old versions after migration to new systems
- Files you're hesitant to delete (archive first)

## Related Use Cases

- Setting up organization for a new computer
- Preparing files for backup/archiving
- Cleaning up before storage cleanup
- Organizing shared team folders
- Structuring new project directories

---

## Skill: `frontend-design`

---
name: frontend-design
description: Create distinctive, production-grade frontend interfaces with high design quality. Use this skill when the user asks to build web components, pages, or applications. Generates creative, polished code that avoids generic AI aesthetics.
license: Complete terms in LICENSE.txt
---

This skill guides creation of distinctive, production-grade frontend interfaces that avoid generic "AI slop" aesthetics. Implement real working code with exceptional attention to aesthetic details and creative choices.

The user provides frontend requirements: a component, page, application, or interface to build. They may include context about the purpose, audience, or technical constraints.

## Design Thinking

Before coding, understand the context and commit to a BOLD aesthetic direction:
- **Purpose**: What problem does this interface solve? Who uses it?
- **Tone**: Pick an extreme: brutally minimal, maximalist chaos, retro-futuristic, organic/natural, luxury/refined, playful/toy-like, editorial/magazine, brutalist/raw, art deco/geometric, soft/pastel, industrial/utilitarian, etc. There are so many flavors to choose from. Use these for inspiration but design one that is true to the aesthetic direction.
- **Constraints**: Technical requirements (framework, performance, accessibility).
- **Differentiation**: What makes this UNFORGETTABLE? What's the one thing someone will remember?

**CRITICAL**: Choose a clear conceptual direction and execute it with precision. Bold maximalism and refined minimalism both work - the key is intentionality, not intensity.

Then implement working code (HTML/CSS/JS, React, Vue, etc.) that is:
- Production-grade and functional
- Visually striking and memorable
- Cohesive with a clear aesthetic point-of-view
- Meticulously refined in every detail

## Frontend Aesthetics Guidelines

Focus on:
- **Typography**: Choose fonts that are beautiful, unique, and interesting. Avoid generic fonts like Arial and Inter; opt instead for distinctive choices that elevate the frontend's aesthetics; unexpected, characterful font choices. Pair a distinctive display font with a refined body font.
- **Color & Theme**: Commit to a cohesive aesthetic. Use CSS variables for consistency. Dominant colors with sharp accents outperform timid, evenly-distributed palettes.
- **Motion**: Use animations for effects and micro-interactions. Prioritize CSS-only solutions for HTML. Use Motion library for React when available. Focus on high-impact moments: one well-orchestrated page load with staggered reveals (animation-delay) creates more delight than scattered micro-interactions. Use scroll-triggering and hover states that surprise.
- **Spatial Composition**: Unexpected layouts. Asymmetry. Overlap. Diagonal flow. Grid-breaking elements. Generous negative space OR controlled density.
- **Backgrounds & Visual Details**: Create atmosphere and depth rather than defaulting to solid colors. Add contextual effects and textures that match the overall aesthetic. Apply creative forms like gradient meshes, noise textures, geometric patterns, layered transparencies, dramatic shadows, decorative borders, custom cursors, and grain overlays.

NEVER use generic AI-generated aesthetics like overused font families (Inter, Roboto, Arial, system fonts), cliched color schemes (particularly purple gradients on white backgrounds), predictable layouts and component patterns, and cookie-cutter design that lacks context-specific character.

Interpret creatively and make unexpected choices that feel genuinely designed for the context. No design should be the same. Vary between light and dark themes, different fonts, different aesthetics. NEVER converge on common choices (Space Grotesk, for example) across generations.

**IMPORTANT**: Match implementation complexity to the aesthetic vision. Maximalist designs need elaborate code with extensive animations and effects. Minimalist or refined designs need restraint, precision, and careful attention to spacing, typography, and subtle details. Elegance comes from executing the vision well.

Remember: Claude is capable of extraordinary creative work. Don't hold back, show what can truly be created when thinking outside the box and committing fully to a distinctive vision.

---

## Skill: `git-worktrees`

---
name: git-worktrees
description: Manage multiple Git working trees to work on multiple branches simultaneously without stashing or switching. Use this skill when the user wants to work on multiple branches at the same time, review code in one branch while developing in another, or set up parallel development workflows.
---

# Git Worktrees

Work on multiple branches simultaneously using `git worktree` — each branch gets its own working directory.

## What is a Worktree?

A Git worktree is an additional working directory linked to the same repository. Each worktree:
- Has its own checked-out branch
- Has its own working directory and index
- Shares the same `.git` object store (efficient — no duplication)

Use case: work on a feature in one worktree while hotfixing in another, without stashing or losing context.

## Core Commands

### List existing worktrees
```bash
git worktree list
```

### Add a new worktree
```bash
# Checkout existing branch into new directory
git worktree add ../feature-branch feature-branch

# Create new branch and worktree together
git worktree add -b new-feature ../new-feature main

# Add worktree at a specific path
git worktree add /path/to/directory branch-name
```

### Remove a worktree
```bash
# After you're done with the worktree
git worktree remove ../feature-branch

# Force remove (if worktree has uncommitted changes)
git worktree remove --force ../feature-branch

# Prune stale worktree references
git worktree prune
```

### Move a worktree
```bash
git worktree move ../old-path ../new-path
```

## Common Workflows

### Workflow 1: Parallel Feature Development

```bash
# Main work: currently on feature-a
cd ~/projects/my-app

# Start working on feature-b in parallel
git worktree add ../my-app-feature-b feature-b

# Open feature-b in editor
code ../my-app-feature-b

# Later, clean up
git worktree remove ../my-app-feature-b
```

### Workflow 2: Hotfix While Feature is In Progress

```bash
# You're deep in feature work — don't stash, use a worktree
git worktree add ../hotfix-123 main

cd ../hotfix-123
git checkout -b hotfix/critical-bug-123

# Fix the bug, commit, push, open PR
git commit -am "fix: resolve critical login bug"
git push origin hotfix/critical-bug-123

# Back to feature work without losing context
cd ../my-app
```

### Workflow 3: Code Review Without Leaving Current Work

```bash
# Review a PR branch without disrupting your work
git fetch origin
git worktree add ../review-pr-456 origin/feature/some-feature

# Review the code in ../review-pr-456
# Run tests, inspect changes

# Clean up after review
git worktree remove ../review-pr-456
```

### Workflow 4: Testing Multiple Versions

```bash
# Compare behavior between main and a branch
git worktree add ../test-main main
git worktree add ../test-feature feature/new-algorithm

# Run both side by side
cd ../test-main && npm test
cd ../test-feature && npm test
```

## Directory Naming Convention

Keep worktrees organized with a consistent naming pattern:
```
~/projects/
  my-app/              # main worktree (primary branch)
  my-app-feature-x/   # feature worktree
  my-app-hotfix/      # hotfix worktree
  my-app-review/      # PR review worktree
```

Or use a subdirectory approach:
```
~/projects/
  my-app/
    .git/
    src/
  worktrees/
    my-app-feature-x/
    my-app-hotfix/
```

## Important Notes

- **One branch per worktree** — you cannot check out the same branch in two worktrees simultaneously
- **Shared objects** — all worktrees share the `.git` database; disk usage is minimal
- **Independent index** — each worktree has its own staging area (index)
- **Node modules / builds** — each worktree needs its own `node_modules`, `.venv`, build artifacts, etc. Run install commands after creating each worktree
- **IDE project files** — some IDEs may need to be opened separately for each worktree

## Cleanup Reminders

Orphaned worktrees (deleted directory without `git worktree remove`) leave stale metadata:
```bash
# Clean up stale references
git worktree prune

# View all worktrees including stale ones
git worktree list --porcelain
```

## Integration with Claude Code

When working in Claude Code across multiple worktrees:
- Each worktree is a separate project directory — open them independently
- Use `git worktree list` to see all active worktrees and their branches
- Prefer worktrees over stashing for context-switch heavy workflows

---

## Skill: `image-enhancer`

---
name: image-enhancer
description: Improves the quality of images, especially screenshots, by enhancing resolution, sharpness, and clarity. Perfect for preparing images for presentations, documentation, or social media posts.
---

# Image Enhancer

This skill takes your images and screenshots and makes them look better—sharper, clearer, and more professional.

## When to Use This Skill

- Improving screenshot quality for blog posts or documentation
- Enhancing images before sharing on social media
- Preparing images for presentations or reports
- Upscaling low-resolution images
- Sharpening blurry photos
- Cleaning up compressed images

## What This Skill Does

1. **Analyzes Image Quality**: Checks resolution, sharpness, and compression artifacts
2. **Enhances Resolution**: Upscales images intelligently
3. **Improves Sharpness**: Enhances edges and details
4. **Reduces Artifacts**: Cleans up compression artifacts and noise
5. **Optimizes for Use Case**: Adjusts based on intended use (web, print, social media)

## How to Use

### Basic Enhancement

```
Improve the image quality of screenshot.png
```

```
Enhance all images in this folder
```

### Specific Improvements

```
Upscale this image to 4K resolution
```

```
Sharpen this blurry screenshot
```

```
Reduce compression artifacts in this image
```

### Batch Processing

```
Improve the quality of all PNG files in this directory
```

## Example

**User**: "Improve the image quality of screenshot-2024.png"

**Output**:
```
Analyzing screenshot-2024.png...

Current specs:
- Resolution: 1920x1080
- Format: PNG
- Quality: Good, but slight blur

Enhancements applied:
✓ Upscaled to 2560x1440 (retina)
✓ Sharpened edges
✓ Enhanced text clarity
✓ Optimized file size

Saved as: screenshot-2024-enhanced.png
Original preserved as: screenshot-2024-original.png
```

**Inspired by:** Lenny Rachitsky's workflow from his newsletter - used for screenshots in his articles

## Tips

- Always keeps original files as backup
- Works best with screenshots and digital images
- Can batch process entire folders
- Specify output format if needed (PNG for quality, JPG for smaller size)
- For social media, mention the platform for optimal sizing

## Common Use Cases

- **Blog Posts**: Enhance screenshots before publishing
- **Documentation**: Make UI screenshots crystal clear
- **Social Media**: Optimize images for Twitter, LinkedIn, Instagram
- **Presentations**: Upscale images for large screens
- **Print Materials**: Increase resolution for physical media

---

## Skill: `instagram-fetch`

---
name: instagram-fetch
description: Fetch and analyze Instagram posts, reels, and stories. Use when a user shares an Instagram URL (post, reel, or story) and wants to extract content, captions, metadata, or download media. Uses yt-dlp for media download and metadata extraction. Requires yt-dlp and optionally Instagram credentials for private content.
---

# Instagram Fetch Skill

Fetch metadata, captions, and media from Instagram posts, reels, and stories using yt-dlp.

## When to Use This Skill

Activate when the user shares an Instagram URL such as:
- `https://www.instagram.com/reel/...`
- `https://www.instagram.com/p/...`
- `https://www.instagram.com/stories/...`
- Any Instagram URL and asks to "fetch", "download", "analyze", or "summarize" it

## Prerequisites

### Install yt-dlp
```bash
pip install yt-dlp
# or
brew install yt-dlp
# or
sudo apt install yt-dlp
```

**Verify:**
```bash
yt-dlp --version
```

### (Optional) Instagram Login for Private Content
For private accounts or stories that require login:
```bash
# Login via browser cookies (recommended - no password needed)
yt-dlp --cookies-from-browser chrome "INSTAGRAM_URL"

# Or using username/password
yt-dlp -u YOUR_USERNAME -p YOUR_PASSWORD "INSTAGRAM_URL"
```

## Core Workflows

### Workflow 1: Fetch Reel/Post Metadata Only

**When user shares a URL and wants caption/info without downloading:**

```bash
yt-dlp --dump-json --no-download "INSTAGRAM_URL" 2>/dev/null
```

**Parse and report:**
1. `title` / `description` — caption text
2. `uploader` / `uploader_id` — account name
3. `timestamp` — post date
4. `like_count`, `comment_count`, `view_count` — engagement
5. `duration` — video length (reels)
6. `thumbnail` — cover image URL

**Example response format:**
```
Instagram Reel — @username

Caption: "Check out this amazing sunset! 🌅 #travel #photography"

Stats:
- Views: 1.2M
- Likes: 45,000
- Comments: 892
- Duration: 0:32
- Posted: 2025-03-10

Direct URL: https://www.instagram.com/reel/ABC123/
```

---

### Workflow 2: Download Reel/Post Video

**When user wants to save the video:**

```bash
# Download best quality to current directory
yt-dlp -o "%(uploader)s_%(id)s.%(ext)s" "INSTAGRAM_URL"

# Download to specific output folder
yt-dlp -o "/mnt/user-data/outputs/%(uploader)s_%(id)s.%(ext)s" "INSTAGRAM_URL"

# Download with cookies from browser (for private content)
yt-dlp --cookies-from-browser chrome -o "%(uploader)s_%(id)s.%(ext)s" "INSTAGRAM_URL"
```

**Report:**
```
Downloaded: username_DVwYONVAVfj.mp4
Size: 12.4 MB
Quality: 1080x1920 (1080p)
Saved to: /mnt/user-data/outputs/
```

---

### Workflow 3: Extract Caption/Text Only

**When user wants just the caption text:**

```bash
yt-dlp --dump-json --no-download "INSTAGRAM_URL" 2>/dev/null | python3 -c "
import json, sys
data = json.load(sys.stdin)
print('Caption:', data.get('description', data.get('title', 'No caption found')))
print('Posted by:', data.get('uploader', 'Unknown'))
print('Date:', data.get('upload_date', 'Unknown'))
"
```

---

### Workflow 4: Download Thumbnail/Cover Image

**When user wants the cover image:**

```bash
yt-dlp --write-thumbnail --skip-download -o "%(uploader)s_%(id)s" "INSTAGRAM_URL"
```

---

### Workflow 5: Batch Fetch Multiple URLs

**When user provides multiple Instagram links:**

```bash
# Save URLs to a file
cat > instagram_urls.txt << 'EOF'
https://www.instagram.com/reel/URL1/
https://www.instagram.com/reel/URL2/
https://www.instagram.com/p/URL3/
EOF

# Fetch metadata for all
yt-dlp --dump-json --no-download -a instagram_urls.txt 2>/dev/null
```

---

## Handling Common Issues

### 403 Forbidden / Login Required

Instagram often blocks unauthenticated requests. Solutions:

```bash
# Option 1: Use browser cookies (best method)
yt-dlp --cookies-from-browser chrome "INSTAGRAM_URL"
yt-dlp --cookies-from-browser firefox "INSTAGRAM_URL"

# Option 2: Export cookies manually and use cookie file
# In Chrome: use a cookies.txt extension, save to cookies.txt
yt-dlp --cookies cookies.txt "INSTAGRAM_URL"

# Option 3: Username/password (less reliable due to 2FA)
yt-dlp -u your@email.com -p yourpassword "INSTAGRAM_URL"
```

### Rate Limiting

```bash
# Add delays between requests
yt-dlp --sleep-interval 3 --max-sleep-interval 10 "INSTAGRAM_URL"
```

### Private Content

```bash
# Must use cookies from a logged-in browser session
yt-dlp --cookies-from-browser chrome "INSTAGRAM_URL"
```

### CSRF Token Warning

The warning `No csrf token set by Instagram API` is common and usually harmless. The download often still succeeds.

---

## Output Parsing (Python Helper)

When you get JSON from `--dump-json`, parse it like this:

```python
import json, subprocess

result = subprocess.run(
    ["yt-dlp", "--dump-json", "--no-download", "INSTAGRAM_URL"],
    capture_output=True, text=True
)

if result.returncode == 0:
    data = json.loads(result.stdout)
    print(f"Title: {data.get('title', 'N/A')}")
    print(f"Caption: {data.get('description', 'N/A')}")
    print(f"Uploader: {data.get('uploader', 'N/A')} (@{data.get('uploader_id', 'N/A')})")
    print(f"Views: {data.get('view_count', 'N/A'):,}")
    print(f"Likes: {data.get('like_count', 'N/A'):,}")
    print(f"Comments: {data.get('comment_count', 'N/A'):,}")
    print(f"Duration: {data.get('duration', 0)}s")
    print(f"Upload date: {data.get('upload_date', 'N/A')}")
    print(f"Thumbnail: {data.get('thumbnail', 'N/A')}")
else:
    print("Error:", result.stderr)
```

---

## Quick Reference

```bash
# Metadata only (no download)
yt-dlp --dump-json --no-download "URL"

# Download video
yt-dlp "URL"

# Download with browser cookies
yt-dlp --cookies-from-browser chrome "URL"

# Caption only
yt-dlp --dump-json --no-download "URL" | python3 -c "import json,sys; d=json.load(sys.stdin); print(d.get('description',''))"

# Thumbnail only
yt-dlp --write-thumbnail --skip-download "URL"

# Save to specific folder
yt-dlp -o "/path/to/folder/%(uploader)s_%(id)s.%(ext)s" "URL"
```

---

## Notes for Claude

- Always try `--dump-json --no-download` first to avoid unnecessary downloads
- If 403 error occurs, suggest using `--cookies-from-browser chrome` or `firefox`
- Instagram blocks sandbox/server environments — this skill works best when run locally by the user
- For reels: key fields are `description` (caption), `uploader`, `view_count`, `like_count`
- The reel ID is in the URL: `instagram.com/reel/{REEL_ID}/`
- Always show the extracted caption prominently — that's usually what users want
- If network is blocked (proxy/sandbox), explain this clearly and provide the commands for the user to run locally

---

**Version:** 1.0.0
**Requires:** yt-dlp (`pip install yt-dlp`)
**Works with:** Instagram Reels, Posts (photos & carousels), IGTV
**Does NOT work with:** Instagram Stories (requires login + they expire)

---

## Skill: `instagram-prompt-extractor`

---
name: instagram-prompt-extractor
description: Extract the AI prompt or creative brief behind an Instagram post — reverse-engineer what prompt or concept was used to create AI-generated images, designs, or content. Use this skill when the user shares an Instagram post (image or caption) and wants to know the likely prompt or creative direction behind it.
---

# Instagram Prompt Extractor

Reverse-engineer the AI prompt or creative brief behind Instagram content.

## When to Use

Use when the user:
- Shares an Instagram image or post and asks "what prompt was used for this?"
- Wants to recreate a visual style they saw on Instagram
- Asks "how would I recreate this?" for AI-generated content
- Wants to understand the creative direction behind a post

## Process

### Step 1: Analyze the Visual Content

When an image is provided, analyze:

**Subject & Composition:**
- Main subject (person, object, scene, abstract)
- Composition style (rule of thirds, centered, symmetrical, dynamic)
- Foreground/background relationship
- Camera angle (eye-level, aerial, low-angle, POV)

**Lighting & Mood:**
- Lighting type (natural, studio, golden hour, neon, moody)
- Shadows and highlights
- Overall mood (dramatic, soft, cheerful, mysterious)

**Style & Aesthetic:**
- Photography style vs AI-generated vs illustration
- Art style if applicable (hyperrealistic, cinematic, anime, oil painting, etc.)
- Color grading (warm, cool, desaturated, high contrast, pastel)
- Post-processing style (film grain, vignette, sharp, soft focus)

**Technical Details:**
- Apparent camera/lens (wide angle, telephoto, macro, fisheye)
- Depth of field (shallow bokeh vs everything in focus)
- Resolution/clarity impression

### Step 2: Analyze the Caption (if provided)

Extract from caption:
- Key themes and concepts
- Brand voice and tone
- Hashtags as topic signals
- Product or service context
- Target audience cues

### Step 3: Construct the Likely Prompt

Build the reverse-engineered prompt in layers:

**For AI Image Generation (Midjourney, DALL-E, Stable Diffusion):**
```
[Subject description], [style/aesthetic], [lighting], [mood], [technical specs], [quality modifiers]
```

Example:
```
A young woman in a flowing white dress standing in a field of sunflowers at golden hour,
cinematic photography, warm soft lighting, bokeh background, shot on Canon 5D,
8k resolution, hyperrealistic, editorial style
```

**For Midjourney specifically:**
```
/imagine [subject] [style] [mood] [lighting] --ar 4:5 --style raw --v 6
```

**For content/caption prompts:**
```
Write an Instagram caption for [subject] with [tone] voice targeting [audience].
Include relevant hashtags for [niche]. Keep it [length].
```

### Step 4: Provide Recreation Instructions

Give the user:
1. **Extracted prompt** — ready to copy-paste into an AI image tool
2. **Style parameters** — specific settings for the tool (aspect ratio, style version)
3. **Key elements** — the most important visual elements to preserve
4. **Variations to try** — tweaks that might improve results

## Output Format

```
## Prompt Analysis: [Post description]

### Likely AI Tool
[Midjourney / DALL-E / Stable Diffusion / Not AI-generated / Unclear]

### Reverse-Engineered Prompt

**Ready to use:**
```
[Full prompt ready to copy-paste]
```

**For Midjourney:**
```
/imagine [prompt] --ar 4:5 --v 6
```

### Key Visual Elements
- **Subject**: [description]
- **Style**: [aesthetic description]
- **Lighting**: [lighting description]
- **Color**: [color grading]
- **Mood**: [emotional quality]

### Recreation Tips
1. [Specific tip for getting the same result]
2. [Another tip]
3. [Variation to try]

### Caption Prompt (if applicable)
```
[Prompt to generate a similar caption]
```
```

## Visual Style Vocabulary

Use these terms when constructing prompts:

**Photography styles:** editorial, documentary, fine art, street photography, fashion photography, product photography, portrait, landscape, macro

**Lighting:** golden hour, blue hour, studio lighting, rembrandt lighting, dramatic side lighting, flat lay, backlit, neon, cinematic

**Moods:** ethereal, moody, dark academia, cottagecore, minimalist, maximalist, retro, futuristic, dreamy, raw

**Technical:** bokeh, shallow depth of field, wide angle, telephoto compression, film grain, 35mm, medium format, drone shot, fisheye

**AI art styles:** hyperrealistic, photorealistic, cinematic, oil painting, watercolor, digital art, concept art, anime, illustration, 3D render

## Notes

- Be clear when a post is likely NOT AI-generated (real photography)
- For real photography, describe it as a "creative brief" rather than an "AI prompt"
- Include both the image generation prompt AND the caption prompt if both are relevant
- If image is not provided, work from caption and hashtag analysis only

---

## Skill: `internal-comms`

---
name: internal-comms
description: A set of resources to help me write all kinds of internal communications, using the formats that my company likes to use. Claude should use this skill whenever asked to write some sort of internal communications (status reports, leadership updates, 3P updates, company newsletters, FAQs, incident reports, project updates, etc.).
license: Complete terms in LICENSE.txt
---

## When to use this skill
To write internal communications, use this skill for:
- 3P updates (Progress, Plans, Problems)
- Company newsletters
- FAQ responses
- Status reports
- Leadership updates
- Project updates
- Incident reports

## How to use this skill

To write any internal communication:

1. **Identify the communication type** from the request
2. **Load the appropriate guideline file** from the `examples/` directory:
    - `examples/3p-updates.md` - For Progress/Plans/Problems team updates
    - `examples/company-newsletter.md` - For company-wide newsletters
    - `examples/faq-answers.md` - For answering frequently asked questions
    - `examples/general-comms.md` - For anything else that doesn't explicitly match one of the above
3. **Follow the specific instructions** in that file for formatting, tone, and content gathering

If the communication type doesn't match any existing guideline, ask for clarification or more context about the desired format.

## Keywords
3P updates, company newsletter, company comms, weekly update, faqs, common questions, updates, internal comms

---

## Skill: `invoice-organizer`

---
name: invoice-organizer
description: Automatically organizes invoices and receipts for tax preparation by reading messy files, extracting key information, renaming them consistently, and sorting them into logical folders. Turns hours of manual bookkeeping into minutes of automated organization.
---

# Invoice Organizer

This skill transforms chaotic folders of invoices, receipts, and financial documents into a clean, tax-ready filing system without manual effort.

## When to Use This Skill

- Preparing for tax season and need organized records
- Managing business expenses across multiple vendors
- Organizing receipts from a messy folder or email downloads
- Setting up automated invoice filing for ongoing bookkeeping
- Archiving financial records by year or category
- Reconciling expenses for reimbursement
- Preparing documentation for accountants

## What This Skill Does

1. **Reads Invoice Content**: Extracts information from PDFs, images, and documents:
   - Vendor/company name
   - Invoice number
   - Date
   - Amount
   - Product or service description
   - Payment method

2. **Renames Files Consistently**: Creates standardized filenames:
   - Format: `YYYY-MM-DD Vendor - Invoice - ProductOrService.pdf`
   - Examples: `2024-03-15 Adobe - Invoice - Creative Cloud.pdf`

3. **Organizes by Category**: Sorts into logical folders:
   - By vendor
   - By expense category (software, office, travel, etc.)
   - By time period (year, quarter, month)
   - By tax category (deductible, personal, etc.)

4. **Handles Multiple Formats**: Works with:
   - PDF invoices
   - Scanned receipts (JPG, PNG)
   - Email attachments
   - Screenshots
   - Bank statements

5. **Maintains Originals**: Preserves original files while organizing copies

## How to Use

### Basic Usage

Navigate to your messy invoice folder:
```
cd ~/Desktop/receipts-to-sort
```

Then ask Claude Code:
```
Organize these invoices for taxes
```

Or more specifically:
```
Read all invoices in this folder, rename them to 
"YYYY-MM-DD Vendor - Invoice - Product.pdf" format, 
and organize them by vendor
```

### Advanced Organization

```
Organize these invoices:
1. Extract date, vendor, and description from each file
2. Rename to standard format
3. Sort into folders by expense category (Software, Office, Travel, etc.)
4. Create a CSV spreadsheet with all invoice details for my accountant
```

## Instructions

When a user requests invoice organization:

1. **Scan the Folder**
   
   Identify all invoice files:
   ```bash
   # Find all invoice-related files
   find . -type f \( -name "*.pdf" -o -name "*.jpg" -o -name "*.png" \) -print
   ```
   
   Report findings:
   - Total number of files
   - File types
   - Date range (if discernible from names)
   - Current organization (or lack thereof)

2. **Extract Information from Each File**
   
   For each invoice, extract:
   
   **From PDF invoices**:
   - Use text extraction to read invoice content
   - Look for common patterns:
     - "Invoice Date:", "Date:", "Issued:"
     - "Invoice #:", "Invoice Number:"
     - Company name (usually at top)
     - "Amount Due:", "Total:", "Amount:"
     - "Description:", "Service:", "Product:"
   
   **From image receipts**:
   - Read visible text from images
   - Identify vendor name (often at top)
   - Look for date (common formats)
   - Find total amount
   
   **Fallback for unclear files**:
   - Use filename clues
   - Check file creation/modification date
   - Flag for manual review if critical info missing

3. **Determine Organization Strategy**
   
   Ask user preference if not specified:
   
   ```markdown
   I found [X] invoices from [date range].
   
   How would you like them organized?
   
   1. **By Vendor** (Adobe/, Amazon/, Stripe/, etc.)
   2. **By Category** (Software/, Office Supplies/, Travel/, etc.)
   3. **By Date** (2024/Q1/, 2024/Q2/, etc.)
   4. **By Tax Category** (Deductible/, Personal/, etc.)
   5. **Custom** (describe your structure)
   
   Or I can use a default structure: Year/Category/Vendor
   ```

4. **Create Standardized Filename**
   
   For each invoice, create a filename following this pattern:
   
   ```
   YYYY-MM-DD Vendor - Invoice - Description.ext
   ```
   
   Examples:
   - `2024-03-15 Adobe - Invoice - Creative Cloud.pdf`
   - `2024-01-10 Amazon - Receipt - Office Supplies.pdf`
   - `2023-12-01 Stripe - Invoice - Monthly Payment Processing.pdf`
   
   **Filename Best Practices**:
   - Remove special characters except hyphens
   - Capitalize vendor names properly
   - Keep descriptions concise but meaningful
   - Use consistent date format (YYYY-MM-DD) for sorting
   - Preserve original file extension

5. **Execute Organization**
   
   Before moving files, show the plan:
   
   ```markdown
   # Organization Plan
   
   ## Proposed Structure
   ```
   Invoices/
   ├── 2023/
   │   ├── Software/
   │   │   ├── Adobe/
   │   │   └── Microsoft/
   │   ├── Services/
   │   └── Office/
   └── 2024/
       ├── Software/
       ├── Services/
       └── Office/
   ```
   
   ## Sample Changes
   
   Before: `invoice_adobe_march.pdf`
   After: `2024-03-15 Adobe - Invoice - Creative Cloud.pdf`
   Location: `Invoices/2024/Software/Adobe/`
   
   Before: `IMG_2847.jpg`
   After: `2024-02-10 Staples - Receipt - Office Supplies.jpg`
   Location: `Invoices/2024/Office/Staples/`
   
   Process [X] files? (yes/no)
   ```
   
   After approval:
   ```bash
   # Create folder structure
   mkdir -p "Invoices/2024/Software/Adobe"
   
   # Copy (don't move) to preserve originals
   cp "original.pdf" "Invoices/2024/Software/Adobe/2024-03-15 Adobe - Invoice - Creative Cloud.pdf"
   
   # Or move if user prefers
   mv "original.pdf" "new/path/standardized-name.pdf"
   ```

6. **Generate Summary Report**
   
   Create a CSV file with all invoice details:
   
   ```csv
   Date,Vendor,Invoice Number,Description,Amount,Category,File Path
   2024-03-15,Adobe,INV-12345,Creative Cloud,52.99,Software,Invoices/2024/Software/Adobe/2024-03-15 Adobe - Invoice - Creative Cloud.pdf
   2024-03-10,Amazon,123-4567890-1234567,Office Supplies,127.45,Office,Invoices/2024/Office/Amazon/2024-03-10 Amazon - Receipt - Office Supplies.pdf
   ...
   ```
   
   This CSV is useful for:
   - Importing into accounting software
   - Sharing with accountants
   - Expense tracking and reporting
   - Tax preparation

7. **Provide Completion Summary**
   
   ```markdown
   # Organization Complete! 📊
   
   ## Summary
   - **Processed**: [X] invoices
   - **Date range**: [earliest] to [latest]
   - **Total amount**: $[sum] (if amounts extracted)
   - **Vendors**: [Y] unique vendors
   
   ## New Structure
   ```
   Invoices/
   ├── 2024/ (45 files)
   │   ├── Software/ (23 files)
   │   ├── Services/ (12 files)
   │   └── Office/ (10 files)
   └── 2023/ (12 files)
   ```
   
   ## Files Created
   - `/Invoices/` - Organized invoices
   - `/Invoices/invoice-summary.csv` - Spreadsheet for accounting
   - `/Invoices/originals/` - Original files (if copied)
   
   ## Files Needing Review
   [List any files where information couldn't be extracted completely]
   
   ## Next Steps
   1. Review the `invoice-summary.csv` file
   2. Check files in "Needs Review" folder
   3. Import CSV into your accounting software
   4. Set up auto-organization for future invoices
   
   Ready for tax season! 🎉
   ```

## Examples

### Example 1: Tax Preparation (From Martin Merschroth)

**User**: "I have a messy folder of invoices for taxes. Sort them and rename properly."

**Process**:
1. Scans folder: finds 147 PDFs and images
2. Reads each invoice to extract:
   - Date
   - Vendor name
   - Invoice number
   - Product/service description
3. Renames all files: `YYYY-MM-DD Vendor - Invoice - Product.pdf`
4. Organizes into: `2024/Software/`, `2024/Travel/`, etc.
5. Creates `invoice-summary.csv` for accountant
6. Result: Tax-ready organized invoices in minutes

### Example 2: Monthly Expense Reconciliation

**User**: "Organize my business receipts from last month by category."

**Output**:
```markdown
# March 2024 Receipts Organized

## By Category
- Software & Tools: $847.32 (12 invoices)
- Office Supplies: $234.18 (8 receipts)
- Travel & Meals: $1,456.90 (15 receipts)
- Professional Services: $2,500.00 (3 invoices)

Total: $5,038.40

All receipts renamed and filed in:
`Business-Receipts/2024/03-March/[Category]/`

CSV export: `march-2024-expenses.csv`
```

### Example 3: Multi-Year Archive

**User**: "I have 3 years of random invoices. Organize them by year, then by vendor."

**Output**: Creates structure:
```
Invoices/
├── 2022/
│   ├── Adobe/
│   ├── Amazon/
│   └── ...
├── 2023/
│   ├── Adobe/
│   ├── Amazon/
│   └── ...
└── 2024/
    ├── Adobe/
    ├── Amazon/
    └── ...
```

Each file properly renamed with date and description.

### Example 4: Email Downloads Cleanup

**User**: "I download invoices from Gmail. They're all named 'invoice.pdf', 'invoice(1).pdf', etc. Fix this mess."

**Output**:
```markdown
Found 89 files all named "invoice*.pdf"

Reading each file to extract real information...

Renamed examples:
- invoice.pdf → 2024-03-15 Shopify - Invoice - Monthly Subscription.pdf
- invoice(1).pdf → 2024-03-14 Google - Invoice - Workspace.pdf
- invoice(2).pdf → 2024-03-10 Netlify - Invoice - Pro Plan.pdf

All files renamed and organized by vendor.
```

## Common Organization Patterns

### By Vendor (Simple)
```
Invoices/
├── Adobe/
├── Amazon/
├── Google/
└── Microsoft/
```

### By Year and Category (Tax-Friendly)
```
Invoices/
├── 2023/
│   ├── Software/
│   ├── Hardware/
│   ├── Services/
│   └── Travel/
└── 2024/
    └── ...
```

### By Quarter (Detailed Tracking)
```
Invoices/
├── 2024/
│   ├── Q1/
│   │   ├── Software/
│   │   ├── Office/
│   │   └── Travel/
│   └── Q2/
│       └── ...
```

### By Tax Category (Accountant-Ready)
```
Invoices/
├── Deductible/
│   ├── Software/
│   ├── Office/
│   └── Professional-Services/
├── Partially-Deductible/
│   └── Meals-Travel/
└── Personal/
```

## Automation Setup

For ongoing organization:

```
Create a script that watches my ~/Downloads/invoices folder 
and auto-organizes any new invoice files using our standard 
naming and folder structure.
```

This creates a persistent solution that organizes invoices as they arrive.

## Pro Tips

1. **Scan emails to PDF**: Use Preview or similar to save email invoices as PDFs first
2. **Consistent downloads**: Save all invoices to one folder for batch processing
3. **Monthly routine**: Organize invoices monthly, not annually
4. **Backup originals**: Keep original files before reorganizing
5. **Include amounts in CSV**: Useful for budget tracking
6. **Tag by deductibility**: Note which expenses are tax-deductible
7. **Keep receipts 7 years**: Standard audit period

## Handling Special Cases

### Missing Information
If date/vendor can't be extracted:
- Flag file for manual review
- Use file modification date as fallback
- Create "Needs-Review/" folder

### Duplicate Invoices
If same invoice appears multiple times:
- Compare file hashes
- Keep highest quality version
- Note duplicates in summary

### Multi-Page Invoices
For invoices split across files:
- Merge PDFs if needed
- Use consistent naming for parts
- Note in CSV if invoice is split

### Non-Standard Formats
For unusual receipt formats:
- Extract what's possible
- Standardize what you can
- Flag for review if critical info missing

## Related Use Cases

- Creating expense reports for reimbursement
- Organizing bank statements
- Managing vendor contracts
- Archiving old financial records
- Preparing for audits
- Tracking subscription costs over time

---

## Skill: `keybindings`

---
name: keybindings
description: Customize Claude Code keyboard shortcuts — add, change, or remove keybindings in ~/.claude/keybindings.json. Use this skill when the user wants to rebind keys, add chord shortcuts, change the submit key, or customize any Claude Code keyboard shortcuts.
---

# Keybindings

Customize Claude Code keyboard shortcuts by editing `~/.claude/keybindings.json`.

## Keybindings File Location

```
~/.claude/keybindings.json
```

Create it if it doesn't exist.

## File Format

```json
[
  {
    "key": "ctrl+enter",
    "command": "sendMessage"
  },
  {
    "key": "ctrl+shift+n",
    "command": "newChat"
  }
]
```

## Available Commands

| Command | Description |
|---------|-------------|
| `sendMessage` | Send the current message |
| `newChat` | Start a new chat session |
| `clearChat` | Clear the current chat |
| `cancelMessage` | Cancel the current in-progress response |
| `focusInput` | Focus the message input |
| `toggleSidebar` | Toggle the sidebar |

## Key Format

Keys are specified as strings with modifiers separated by `+`:

**Modifiers:**
- `ctrl` — Control key
- `cmd` — Command key (macOS)
- `shift` — Shift key
- `alt` — Alt/Option key
- `meta` — Meta/Windows key

**Examples:**
- `"ctrl+enter"` — Ctrl + Enter
- `"cmd+shift+k"` — Cmd + Shift + K
- `"ctrl+k ctrl+c"` — Chord: Ctrl+K then Ctrl+C (two-key sequence)

## Common Customizations

### Change submit key to Ctrl+Enter (keep Enter for newlines)
```json
[
  {
    "key": "ctrl+enter",
    "command": "sendMessage"
  }
]
```

### Add chord shortcut
```json
[
  {
    "key": "ctrl+k n",
    "command": "newChat"
  }
]
```

### Multiple custom bindings
```json
[
  {
    "key": "ctrl+enter",
    "command": "sendMessage"
  },
  {
    "key": "escape",
    "command": "cancelMessage"
  },
  {
    "key": "ctrl+shift+c",
    "command": "clearChat"
  }
]
```

## Process for Updating Keybindings

1. Read the current `~/.claude/keybindings.json` (or note it doesn't exist)
2. Apply the requested changes
3. Write the updated file
4. Confirm with the user what was changed

## Notes

- Changes take effect after restarting Claude Code
- If the file doesn't exist, create it with just the new bindings
- Multiple keys can bind to the same command
- Chord bindings (two-key sequences) are supported with a space: `"ctrl+k n"`
- On macOS, prefer `cmd` over `ctrl` for Mac-native feel

---

## Skill: `keybindings-help`

---
name: keybindings-help
description: Helps you customize keyboard shortcuts in Claude Code. Rebind keys, add chord bindings, change the submit key, or modify ~/.claude/keybindings.json.
---

## keybindings-help
**Category:** Utility

**What it does:**
Helps you customize keyboard shortcuts in Claude Code. You can rebind keys, add chord bindings (multi-key sequences), change the submit key, or modify `~/.claude/keybindings.json` directly.

**When to trigger:**
- "Rebind Ctrl+S"
- "Add a chord shortcut"
- "Change the submit key"
- "Customize keybindings"

**How to install:**
Bundled with Superpowers:
```bash
npx claude install superpowers
```

**Trigger phrase:** Ask Claude Code to customize, rebind, or modify keyboard shortcuts.

---

## Skill: `langsmith-fetch`

---
name: langsmith-fetch
description: Debug LangChain and LangGraph agents by fetching execution traces from LangSmith Studio. Use when debugging agent behavior, investigating errors, analyzing tool calls, checking memory operations, or examining agent performance. Automatically fetches recent traces and analyzes execution patterns. Requires langsmith-fetch CLI installed.
---

# LangSmith Fetch - Agent Debugging Skill

Debug LangChain and LangGraph agents by fetching execution traces directly from LangSmith Studio in your terminal.

## When to Use This Skill

Automatically activate when user mentions:
- 🐛 "Debug my agent" or "What went wrong?"
- 🔍 "Show me recent traces" or "What happened?"
- ❌ "Check for errors" or "Why did it fail?"
- 💾 "Analyze memory operations" or "Check LTM"
- 📊 "Review agent performance" or "Check token usage"
- 🔧 "What tools were called?" or "Show execution flow"

## Prerequisites

### 1. Install langsmith-fetch
```bash
pip install langsmith-fetch
```

### 2. Set Environment Variables
```bash
export LANGSMITH_API_KEY="your_langsmith_api_key"
export LANGSMITH_PROJECT="your_project_name"
```

**Verify setup:**
```bash
echo $LANGSMITH_API_KEY
echo $LANGSMITH_PROJECT
```

## Core Workflows

### Workflow 1: Quick Debug Recent Activity

**When user asks:** "What just happened?" or "Debug my agent"

**Execute:**
```bash
langsmith-fetch traces --last-n-minutes 5 --limit 5 --format pretty
```

**Analyze and report:**
1. ✅ Number of traces found
2. ⚠️ Any errors or failures
3. 🛠️ Tools that were called
4. ⏱️ Execution times
5. 💰 Token usage

**Example response format:**
```
Found 3 traces in the last 5 minutes:

Trace 1: ✅ Success
- Agent: memento
- Tools: recall_memories, create_entities
- Duration: 2.3s
- Tokens: 1,245

Trace 2: ❌ Error
- Agent: cypher
- Error: "Neo4j connection timeout"
- Duration: 15.1s
- Failed at: search_nodes tool

Trace 3: ✅ Success
- Agent: memento
- Tools: store_memory
- Duration: 1.8s
- Tokens: 892

💡 Issue found: Trace 2 failed due to Neo4j timeout. Recommend checking database connection.
```

---

### Workflow 2: Deep Dive Specific Trace

**When user provides:** Trace ID or says "investigate that error"

**Execute:**
```bash
langsmith-fetch trace <trace-id> --format json
```

**Analyze JSON and report:**
1. 🎯 What the agent was trying to do
2. 🛠️ Which tools were called (in order)
3. ✅ Tool results (success/failure)
4. ❌ Error messages (if any)
5. 💡 Root cause analysis
6. 🔧 Suggested fix

**Example response format:**
```
Deep Dive Analysis - Trace abc123

Goal: User asked "Find all projects in Neo4j"

Execution Flow:
1. ✅ search_nodes(query: "projects")
   → Found 24 nodes

2. ❌ get_node_details(node_id: "proj_123")
   → Error: "Node not found"
   → This is the failure point

3. ⏹️ Execution stopped

Root Cause:
The search_nodes tool returned node IDs that no longer exist in the database,
possibly due to recent deletions.

Suggested Fix:
1. Add error handling in get_node_details tool
2. Filter deleted nodes in search results
3. Update cache invalidation strategy

Token Usage: 1,842 tokens ($0.0276)
Execution Time: 8.7 seconds
```

---

### Workflow 3: Export Debug Session

**When user says:** "Save this session" or "Export traces"

**Execute:**
```bash
# Create session folder with timestamp
SESSION_DIR="langsmith-debug/session-$(date +%Y%m%d-%H%M%S)"
mkdir -p "$SESSION_DIR"

# Export traces
langsmith-fetch traces "$SESSION_DIR/traces" --last-n-minutes 30 --limit 50 --include-metadata

# Export threads (conversations)
langsmith-fetch threads "$SESSION_DIR/threads" --limit 20
```

**Report:**
```
✅ Session exported successfully!

Location: langsmith-debug/session-20251224-143022/
- Traces: 42 files
- Threads: 8 files

You can now:
1. Review individual trace files
2. Share folder with team
3. Analyze with external tools
4. Archive for future reference

Session size: 2.3 MB
```

---

### Workflow 4: Error Detection

**When user asks:** "Show me errors" or "What's failing?"

**Execute:**
```bash
# Fetch recent traces
langsmith-fetch traces --last-n-minutes 30 --limit 50 --format json > recent-traces.json

# Search for errors
grep -i "error\|failed\|exception" recent-traces.json
```

**Analyze and report:**
1. 📊 Total errors found
2. ❌ Error types and frequency
3. 🕐 When errors occurred
4. 🎯 Which agents/tools failed
5. 💡 Common patterns

**Example response format:**
```
Error Analysis - Last 30 Minutes

Total Traces: 50
Failed Traces: 7 (14% failure rate)

Error Breakdown:
1. Neo4j Connection Timeout (4 occurrences)
   - Agent: cypher
   - Tool: search_nodes
   - First occurred: 14:32
   - Last occurred: 14:45
   - Pattern: Happens during peak load

2. Memory Store Failed (2 occurrences)
   - Agent: memento
   - Tool: store_memory
   - Error: "Pinecone rate limit exceeded"
   - Occurred: 14:38, 14:41

3. Tool Not Found (1 occurrence)
   - Agent: sqlcrm
   - Attempted tool: "export_report" (doesn't exist)
   - Occurred: 14:35

💡 Recommendations:
1. Add retry logic for Neo4j timeouts
2. Implement rate limiting for Pinecone
3. Fix sqlcrm tool configuration
```

---

## Common Use Cases

### Use Case 1: "Agent Not Responding"

**User says:** "My agent isn't doing anything"

**Steps:**
1. Check if traces exist:
   ```bash
   langsmith-fetch traces --last-n-minutes 5 --limit 5
   ```

2. **If NO traces found:**
   - Tracing might be disabled
   - Check: `LANGCHAIN_TRACING_V2=true` in environment
   - Check: `LANGCHAIN_API_KEY` is set
   - Verify agent actually ran

3. **If traces found:**
   - Review for errors
   - Check execution time (hanging?)
   - Verify tool calls completed

---

### Use Case 2: "Wrong Tool Called"

**User says:** "Why did it use the wrong tool?"

**Steps:**
1. Get the specific trace
2. Review available tools at execution time
3. Check agent's reasoning for tool selection
4. Examine tool descriptions/instructions
5. Suggest prompt or tool config improvements

---

### Use Case 3: "Memory Not Working"

**User says:** "Agent doesn't remember things"

**Steps:**
1. Search for memory operations:
   ```bash
   langsmith-fetch traces --last-n-minutes 10 --limit 20 --format raw | grep -i "memory\|recall\|store"
   ```

2. Check:
   - Were memory tools called?
   - Did recall return results?
   - Were memories actually stored?
   - Are retrieved memories being used?

---

### Use Case 4: "Performance Issues"

**User says:** "Agent is too slow"

**Steps:**
1. Export with metadata:
   ```bash
   langsmith-fetch traces ./perf-analysis --last-n-minutes 30 --limit 50 --include-metadata
   ```

2. Analyze:
   - Execution time per trace
   - Tool call latencies
   - Token usage (context size)
   - Number of iterations
   - Slowest operations

3. Identify bottlenecks and suggest optimizations

---

## Output Format Guide

### Pretty Format (Default)
```bash
langsmith-fetch traces --limit 5 --format pretty
```
**Use for:** Quick visual inspection, showing to users

### JSON Format
```bash
langsmith-fetch traces --limit 5 --format json
```
**Use for:** Detailed analysis, syntax-highlighted review

### Raw Format
```bash
langsmith-fetch traces --limit 5 --format raw
```
**Use for:** Piping to other commands, automation

---

## Advanced Features

### Time-Based Filtering
```bash
# After specific timestamp
langsmith-fetch traces --after "2025-12-24T13:00:00Z" --limit 20

# Last N minutes (most common)
langsmith-fetch traces --last-n-minutes 60 --limit 100
```

### Include Metadata
```bash
# Get extra context
langsmith-fetch traces --limit 10 --include-metadata

# Metadata includes: agent type, model, tags, environment
```

### Concurrent Fetching (Faster)
```bash
# Speed up large exports
langsmith-fetch traces ./output --limit 100 --concurrent 10
```

---

## Troubleshooting

### "No traces found matching criteria"

**Possible causes:**
1. No agent activity in the timeframe
2. Tracing is disabled
3. Wrong project name
4. API key issues

**Solutions:**
```bash
# 1. Try longer timeframe
langsmith-fetch traces --last-n-minutes 1440 --limit 50

# 2. Check environment
echo $LANGSMITH_API_KEY
echo $LANGSMITH_PROJECT

# 3. Try fetching threads instead
langsmith-fetch threads --limit 10

# 4. Verify tracing is enabled in your code
# Check for: LANGCHAIN_TRACING_V2=true
```

### "Project not found"

**Solution:**
```bash
# View current config
langsmith-fetch config show

# Set correct project
export LANGSMITH_PROJECT="correct-project-name"

# Or configure permanently
langsmith-fetch config set project "your-project-name"
```

### Environment variables not persisting

**Solution:**
```bash
# Add to shell config file (~/.bashrc or ~/.zshrc)
echo 'export LANGSMITH_API_KEY="your_key"' >> ~/.bashrc
echo 'export LANGSMITH_PROJECT="your_project"' >> ~/.bashrc

# Reload shell config
source ~/.bashrc
```

---

## Best Practices

### 1. Regular Health Checks
```bash
# Quick check after making changes
langsmith-fetch traces --last-n-minutes 5 --limit 5
```

### 2. Organized Storage
```
langsmith-debug/
├── sessions/
│   ├── 2025-12-24/
│   └── 2025-12-25/
├── error-cases/
└── performance-tests/
```

### 3. Document Findings
When you find bugs:
1. Export the problematic trace
2. Save to `error-cases/` folder
3. Note what went wrong in a README
4. Share trace ID with team

### 4. Integration with Development
```bash
# Before committing code
langsmith-fetch traces --last-n-minutes 10 --limit 5

# If errors found
langsmith-fetch trace <error-id> --format json > pre-commit-error.json
```

---

## Quick Reference

```bash
# Most common commands

# Quick debug
langsmith-fetch traces --last-n-minutes 5 --limit 5 --format pretty

# Specific trace
langsmith-fetch trace <trace-id> --format pretty

# Export session
langsmith-fetch traces ./debug-session --last-n-minutes 30 --limit 50

# Find errors
langsmith-fetch traces --last-n-minutes 30 --limit 50 --format raw | grep -i error

# With metadata
langsmith-fetch traces --limit 10 --include-metadata
```

---

## Resources

- **LangSmith Fetch CLI:** https://github.com/langchain-ai/langsmith-fetch
- **LangSmith Studio:** https://smith.langchain.com/
- **LangChain Docs:** https://docs.langchain.com/
- **This Skill Repo:** https://github.com/OthmanAdi/langsmith-fetch-skill

---

## Notes for Claude

- Always check if `langsmith-fetch` is installed before running commands
- Verify environment variables are set
- Use `--format pretty` for human-readable output
- Use `--format json` when you need to parse and analyze data
- When exporting sessions, create organized folder structures
- Always provide clear analysis and actionable insights
- If commands fail, help troubleshoot configuration issues

---

**Version:** 0.1.0
**Author:** Ahmad Othman Ammar Adi
**License:** MIT
**Repository:** https://github.com/OthmanAdi/langsmith-fetch-skill

---

## Skill: `lead-research-assistant`

---
name: lead-research-assistant
description: Identifies high-quality leads for your product or service by analyzing your business, searching for target companies, and providing actionable contact strategies. Perfect for sales, business development, and marketing professionals.
---

# Lead Research Assistant

This skill helps you identify and qualify potential leads for your business by analyzing your product/service, understanding your ideal customer profile, and providing actionable outreach strategies.

## When to Use This Skill

- Finding potential customers or clients for your product/service
- Building a list of companies to reach out to for partnerships
- Identifying target accounts for sales outreach
- Researching companies that match your ideal customer profile
- Preparing for business development activities

## What This Skill Does

1. **Understands Your Business**: Analyzes your product/service, value proposition, and target market
2. **Identifies Target Companies**: Finds companies that match your ideal customer profile based on:
   - Industry and sector
   - Company size and location
   - Technology stack and tools they use
   - Growth stage and funding
   - Pain points your product solves
3. **Prioritizes Leads**: Ranks companies based on fit score and relevance
4. **Provides Contact Strategies**: Suggests how to approach each lead with personalized messaging
5. **Enriches Data**: Gathers relevant information about decision-makers and company context

## How to Use

### Basic Usage

Simply describe your product/service and what you're looking for:

```
I'm building [product description]. Find me 10 companies in [location/industry] 
that would be good leads for this.
```

### With Your Codebase

For even better results, run this from your product's source code directory:

```
Look at what I'm building in this repository and identify the top 10 companies 
in [location/industry] that would benefit from this product.
```

### Advanced Usage

For more targeted research:

```
My product: [description]
Ideal customer profile:
- Industry: [industry]
- Company size: [size range]
- Location: [location]
- Current pain points: [pain points]
- Technologies they use: [tech stack]

Find me 20 qualified leads with contact strategies for each.
```

## Instructions

When a user requests lead research:

1. **Understand the Product/Service**
   - If in a code directory, analyze the codebase to understand the product
   - Ask clarifying questions about the value proposition
   - Identify key features and benefits
   - Understand what problems it solves

2. **Define Ideal Customer Profile**
   - Determine target industries and sectors
   - Identify company size ranges
   - Consider geographic preferences
   - Understand relevant pain points
   - Note any technology requirements

3. **Research and Identify Leads**
   - Search for companies matching the criteria
   - Look for signals of need (job postings, tech stack, recent news)
   - Consider growth indicators (funding, expansion, hiring)
   - Identify companies with complementary products/services
   - Check for budget indicators

4. **Prioritize and Score**
   - Create a fit score (1-10) for each lead
   - Consider factors like:
     - Alignment with ICP
     - Signals of immediate need
     - Budget availability
     - Competitive landscape
     - Timing indicators

5. **Provide Actionable Output**
   
   For each lead, provide:
   - **Company Name** and website
   - **Why They're a Good Fit**: Specific reasons based on their business
   - **Priority Score**: 1-10 with explanation
   - **Decision Maker**: Role/title to target (e.g., "VP of Engineering")
   - **Contact Strategy**: Personalized approach suggestions
   - **Value Proposition**: How your product solves their specific problem
   - **Conversation Starters**: Specific points to mention in outreach
   - **LinkedIn URL**: If available, for easy connection

6. **Format the Output**

   Present results in a clear, scannable format:

   ```markdown
   # Lead Research Results
   
   ## Summary
   - Total leads found: [X]
   - High priority (8-10): [X]
   - Medium priority (5-7): [X]
   - Average fit score: [X]
   
   ---
   
   ## Lead 1: [Company Name]
   
   **Website**: [URL]
   **Priority Score**: [X/10]
   **Industry**: [Industry]
   **Size**: [Employee count/revenue range]
   
   **Why They're a Good Fit**:
   [2-3 specific reasons based on their business]
   
   **Target Decision Maker**: [Role/Title]
   **LinkedIn**: [URL if available]
   
   **Value Proposition for Them**:
   [Specific benefit for this company]
   
   **Outreach Strategy**:
   [Personalized approach - mention specific pain points, recent company news, or relevant context]
   
   **Conversation Starters**:
   - [Specific point 1]
   - [Specific point 2]
   
   ---
   
   [Repeat for each lead]
   ```

7. **Offer Next Steps**
   - Suggest saving results to a CSV for CRM import
   - Offer to draft personalized outreach messages
   - Recommend prioritization based on timing
   - Suggest follow-up research for top leads

## Examples

### Example 1: From Lenny's Newsletter

**User**: "I'm building a tool that masks sensitive data in AI coding assistant queries. Find potential leads."

**Output**: Creates a prioritized list of companies that:
- Use AI coding assistants (Copilot, Cursor, etc.)
- Handle sensitive data (fintech, healthcare, legal)
- Have evidence in their GitHub repos of using coding agents
- May have accidentally exposed sensitive data in code
- Includes LinkedIn URLs of relevant decision-makers

### Example 2: Local Business

**User**: "I run a consulting practice for remote team productivity. Find me 10 companies in the Bay Area that recently went remote."

**Output**: Identifies companies that:
- Recently posted remote job listings
- Announced remote-first policies
- Are hiring distributed teams
- Show signs of remote work challenges
- Provides personalized outreach strategies for each

## Tips for Best Results

- **Be specific** about your product and its unique value
- **Run from your codebase** if applicable for automatic context
- **Provide context** about your ideal customer profile
- **Specify constraints** like industry, location, or company size
- **Request follow-up** research on promising leads for deeper insights

## Related Use Cases

- Drafting personalized outreach emails after identifying leads
- Building a CRM-ready CSV of qualified prospects
- Researching specific companies in detail
- Analyzing competitor customer bases
- Identifying partnership opportunities

---

## Skill: `loop`

---
name: loop
description: Run a prompt or slash command on a recurring interval. Use this skill when the user wants to set up a recurring task, poll for status, or run something repeatedly (e.g., "/loop 5m /foo", "check the deploy every 5 minutes", "keep running /babysit-prs"). Do NOT invoke for one-off tasks.
---

# Loop

Run a command or prompt repeatedly on a timed interval.

## Syntax

```
/loop [interval] [command or prompt]
```

**Examples:**
- `/loop 5m /check-deploy` — run `/check-deploy` every 5 minutes
- `/loop 10m check if any new PRs need review` — check for PRs every 10 minutes
- `/loop 30s run tests and report results` — run tests every 30 seconds
- `/loop /my-skill` — run `/my-skill` every 10 minutes (default interval)

## Interval Format

| Format | Example | Meaning |
|--------|---------|---------|
| `Xs` | `30s` | Every 30 seconds |
| `Xm` | `5m` | Every 5 minutes |
| `Xh` | `1h` | Every 1 hour |
| (none) | — | Default: 10 minutes |

## How to Run a Loop

When the user invokes `/loop`:

1. **Parse the interval** — extract time from the command (default 10m if not specified)
2. **Parse the command** — everything after the interval is the recurring task
3. **Execute the task** immediately (first run)
4. **Report results** from the first run
5. **Wait** for the specified interval
6. **Execute again** and report
7. **Continue** until the user stops it (Ctrl+C or says "stop")

## Loop Execution Pattern

```
[Loop started: every 5m]

━━━ Run 1 — 14:32:00 ━━━
[Execute command and report results]

━━━ Run 2 — 14:37:00 ━━━
[Execute command and report results]

━━━ Run 3 — 14:42:00 ━━━
[Execute command and report results — highlight any changes from previous run]
```

## Change Detection

On each run after the first:
- Compare results to the previous run
- Highlight **changes** clearly: new items, resolved items, status changes
- If nothing changed: report "No changes since last run"

## Common Use Cases

**Monitor CI/CD:**
```
/loop 2m check if the GitHub Actions build has finished
```

**Watch for PR reviews:**
```
/loop 15m check if any PRs are waiting for my review
```

**Monitor a deployment:**
```
/loop 1m check if the deployment to staging is complete
```

**Poll an API or service:**
```
/loop 30s check the status of the background job
```

**Run tests repeatedly:**
```
/loop 5m run the test suite and report any failures
```

## Stopping a Loop

The loop stops when:
- User types "stop", "cancel", or "quit"
- User presses Ctrl+C
- A completion condition is met (optional — specify in the prompt)

To add a stop condition:
```
/loop 1m check if deploy is done — stop when status is "success" or "failed"
```

## Notes

- Loops should be used for genuinely recurring monitoring tasks
- Do not use for one-time tasks (just run the command directly)
- Keep loop intervals reasonable — very short intervals (< 10s) may rate-limit APIs
- If the recurring task takes longer than the interval, skip the next scheduled run and warn the user

---

## Skill: `meeting-insights-analyzer`

---
name: meeting-insights-analyzer
description: Analyzes meeting transcripts and recordings to uncover behavioral patterns, communication insights, and actionable feedback. Identifies when you avoid conflict, use filler words, dominate conversations, or miss opportunities to listen. Perfect for professionals seeking to improve their communication and leadership skills.
---

# Meeting Insights Analyzer

This skill transforms your meeting transcripts into actionable insights about your communication patterns, helping you become a more effective communicator and leader.

## When to Use This Skill

- Analyzing your communication patterns across multiple meetings
- Getting feedback on your leadership and facilitation style
- Identifying when you avoid difficult conversations
- Understanding your speaking habits and filler words
- Tracking improvement in communication skills over time
- Preparing for performance reviews with concrete examples
- Coaching team members on their communication style

## What This Skill Does

1. **Pattern Recognition**: Identifies recurring behaviors across meetings like:
   - Conflict avoidance or indirect communication
   - Speaking ratios and turn-taking
   - Question-asking vs. statement-making patterns
   - Active listening indicators
   - Decision-making approaches

2. **Communication Analysis**: Evaluates communication effectiveness:
   - Clarity and directness
   - Use of filler words and hedging language
   - Tone and sentiment patterns
   - Meeting control and facilitation

3. **Actionable Feedback**: Provides specific, timestamped examples with:
   - What happened
   - Why it matters
   - How to improve

4. **Trend Tracking**: Compares patterns over time when analyzing multiple meetings

## How to Use

### Basic Setup

1. Download your meeting transcripts to a folder (e.g., `~/meetings/`)
2. Navigate to that folder in Claude Code
3. Ask for the analysis you want

### Quick Start Examples

```
Analyze all meetings in this folder and tell me when I avoided conflict.
```

```
Look at my meetings from the past month and identify my communication patterns.
```

```
Compare my facilitation style between these two meeting folders.
```

### Advanced Analysis

```
Analyze all transcripts in this folder and:
1. Identify when I interrupted others
2. Calculate my speaking ratio
3. Find moments I avoided giving direct feedback
4. Track my use of filler words
5. Show examples of good active listening
```

## Instructions

When a user requests meeting analysis:

1. **Discover Available Data**
   - Scan the folder for transcript files (.txt, .md, .vtt, .srt, .docx)
   - Check if files contain speaker labels and timestamps
   - Confirm the date range of meetings
   - Identify the user's name/identifier in transcripts

2. **Clarify Analysis Goals**
   
   If not specified, ask what they want to learn:
   - Specific behaviors (conflict avoidance, interruptions, filler words)
   - Communication effectiveness (clarity, directness, listening)
   - Meeting facilitation skills
   - Speaking patterns and ratios
   - Growth areas for improvement
   
3. **Analyze Patterns**

   For each requested insight:
   
   **Conflict Avoidance**:
   - Look for hedging language ("maybe", "kind of", "I think")
   - Indirect phrasing instead of direct requests
   - Changing subject when tension arises
   - Agreeing without commitment ("yeah, but...")
   - Not addressing obvious problems
   
   **Speaking Ratios**:
   - Calculate percentage of meeting spent speaking
   - Count interruptions (by and of the user)
   - Measure average speaking turn length
   - Track question vs. statement ratios
   
   **Filler Words**:
   - Count "um", "uh", "like", "you know", "actually", etc.
   - Note frequency per minute or per speaking turn
   - Identify situations where they increase (nervous, uncertain)
   
   **Active Listening**:
   - Questions that reference others' previous points
   - Paraphrasing or summarizing others' ideas
   - Building on others' contributions
   - Asking clarifying questions
   
   **Leadership & Facilitation**:
   - Decision-making approach (directive vs. collaborative)
   - How disagreements are handled
   - Inclusion of quieter participants
   - Time management and agenda control
   - Follow-up and action item clarity

4. **Provide Specific Examples**

   For each pattern found, include:
   
   ```markdown
   ### [Pattern Name]
   
   **Finding**: [One-sentence summary of the pattern]
   
   **Frequency**: [X times across Y meetings]
   
   **Examples**:
   
   1. **[Meeting Name/Date]** - [Timestamp]
      
      **What Happened**:
      > [Actual quote from transcript]
      
      **Why This Matters**:
      [Explanation of the impact or missed opportunity]
      
      **Better Approach**:
      [Specific alternative phrasing or behavior]
   
   [Repeat for 2-3 strongest examples]
   ```

5. **Synthesize Insights**

   After analyzing all patterns, provide:
   
   ```markdown
   # Meeting Insights Summary
   
   **Analysis Period**: [Date range]
   **Meetings Analyzed**: [X meetings]
   **Total Duration**: [X hours]
   
   ## Key Patterns Identified
   
   ### 1. [Primary Pattern]
   - **Observed**: [What you saw]
   - **Impact**: [Why it matters]
   - **Recommendation**: [How to improve]
   
   ### 2. [Second Pattern]
   [Same structure]
   
   ## Communication Strengths
   
   1. [Strength 1 with example]
   2. [Strength 2 with example]
   3. [Strength 3 with example]
   
   ## Growth Opportunities
   
   1. **[Area 1]**: [Specific, actionable advice]
   2. **[Area 2]**: [Specific, actionable advice]
   3. **[Area 3]**: [Specific, actionable advice]
   
   ## Speaking Statistics
   
   - Average speaking time: [X% of meeting]
   - Questions asked: [X per meeting average]
   - Filler words: [X per minute]
   - Interruptions: [X given / Y received per meeting]
   
   ## Next Steps
   
   [3-5 concrete actions to improve communication]
   ```

6. **Offer Follow-Up Options**
   - Track these same metrics in future meetings
   - Deep dive into specific meetings or patterns
   - Compare to industry benchmarks
   - Create a personal communication development plan
   - Generate a summary for performance reviews

## Examples

### Example 1: Conflict Avoidance Analysis (Inspired by Dan Shipper)

**User**: "I download all of my meeting recordings and put them in a folder. Tell me all the times I've subtly avoided conflict."

**Output**: 
```markdown
# Conflict Avoidance Patterns

Found 23 instances across 15 meetings where you used indirect 
communication or avoided addressing tensions directly.

## Pattern: Hedging on Critical Feedback

**Frequency**: 8 times across 7 meetings

**Example 1: 1:1 with Sarah** - 00:14:32

**What Happened**:
> "So, I was thinking... maybe we could, like, potentially 
> consider looking at the timeline again? I mean, if you 
> think that makes sense. But whatever you think is best!"

**Why This Matters**:
You needed to address that Sarah's project was behind schedule, 
but the hedging language ("maybe", "potentially", "if you think") 
and the deflection at the end ("whatever you think") made it easy 
for her to miss the urgency.

**Better Approach**:
"Sarah, the project is two weeks behind schedule. We need to 
discuss what's blocking progress and create a new timeline 
today."

[Additional examples...]

## Recommendations

1. **Name the issue directly** in the first sentence
2. **Remove hedging words** like "maybe," "kind of," "sort of"
3. **Ask specific questions** instead of hinting
4. **Schedule difficult conversations** instead of raising them casually
```

### Example 2: Leadership Facilitation

**User**: "Analyze my team meetings and tell me about my facilitation style."

**Output**: Provides insights on:
- How much you speak vs. team members (60% vs. 40%)
- Whether you ask questions or make statements (3:1 ratio)
- How you handle disagreements (tendency to resolve too quickly)
- Who speaks least and whether you draw them in
- Examples of good and missed facilitation moments

### Example 3: Personal Development Tracking

**User**: "Compare my meetings from Q1 vs. Q2 to see if I've improved my listening skills."

**Output**: Creates a comparative analysis showing:
- Decrease in interruptions (8 per meeting → 3 per meeting)
- Increase in clarifying questions (2 → 7 per meeting)
- Improvement in building on others' ideas
- Specific examples showing the difference
- Remaining areas for growth

## Setup Tips

### Getting Meeting Transcripts

**From Granola** (free with Lenny's newsletter subscription):
- Granola auto-transcribes your meetings
- Export transcripts to a folder: [Instructions on how]
- Point Claude Code to that folder

**From Zoom**:
- Enable cloud recording with transcription
- Download VTT or SRT files after meetings
- Store in a dedicated folder

**From Google Meet**:
- Use Google Docs auto-transcription
- Save transcript docs to a folder
- Download as .txt files or give Claude Code access

**From Fireflies.ai, Otter.ai, etc.**:
- Export transcripts in bulk
- Store in a local folder
- Run analysis on the folder

### Best Practices

1. **Consistent naming**: Use `YYYY-MM-DD - Meeting Name.txt` format
2. **Regular analysis**: Review monthly or quarterly for trends
3. **Specific queries**: Ask about one behavior at a time for depth
4. **Privacy**: Keep sensitive meeting data local
5. **Action-oriented**: Focus on one improvement area at a time

## Common Analysis Requests

- "When do I avoid difficult conversations?"
- "How often do I interrupt others?"
- "What's my speaking vs. listening ratio?"
- "Do I ask good questions?"
- "How do I handle disagreement?"
- "Am I inclusive of all voices?"
- "Do I use too many filler words?"
- "How clear are my action items?"
- "Do I stay on agenda or get sidetracked?"
- "How has my communication changed over time?"

## Related Use Cases

- Creating a personal development plan from insights
- Preparing performance review materials with examples
- Coaching direct reports on their communication
- Analyzing customer calls for sales or support patterns
- Studying negotiation tactics and outcomes

---

## Skill: `mintlify`

---
name: mintlify
description: Build, manage, and optimize Mintlify documentation sites. Use this skill when the user wants to create or update documentation using Mintlify — adding pages, configuring navigation, writing MDX content, customizing themes, or deploying a Mintlify docs site.
---

# Mintlify

Build and manage documentation sites using Mintlify.

## What is Mintlify?

Mintlify is a modern documentation platform that:
- Converts MDX files into beautiful docs sites
- Supports API reference generation (OpenAPI)
- Has built-in search, analytics, and theming
- Deploys automatically from Git

## Project Structure

```
docs/
  mint.json              # Main configuration file
  introduction.mdx       # Pages as MDX files
  quickstart.mdx
  api-reference/
    introduction.mdx
    endpoint/
      get-users.mdx
  guides/
    authentication.mdx
  _snippets/             # Reusable content snippets
    common-params.mdx
  images/                # Static assets
  logo/
    light.svg
    dark.svg
```

## mint.json Configuration

The `mint.json` file controls everything:

```json
{
  "$schema": "https://mintlify.com/schema.json",
  "name": "Your Docs",
  "logo": {
    "dark": "/logo/dark.svg",
    "light": "/logo/light.svg"
  },
  "favicon": "/favicon.svg",
  "colors": {
    "primary": "#2563EB",
    "light": "#3B82F6",
    "dark": "#1D4ED8"
  },
  "topbarLinks": [
    { "name": "Support", "url": "mailto:support@yourcompany.com" }
  ],
  "topbarCtaButton": {
    "name": "Get Started",
    "url": "https://yourapp.com/signup"
  },
  "navigation": [
    {
      "group": "Get Started",
      "pages": ["introduction", "quickstart", "installation"]
    },
    {
      "group": "Guides",
      "pages": ["guides/authentication", "guides/webhooks"]
    },
    {
      "group": "API Reference",
      "pages": ["api-reference/introduction", "api-reference/endpoint/get-users"]
    }
  ],
  "footerSocials": {
    "twitter": "https://twitter.com/yourcompany",
    "github": "https://github.com/yourcompany"
  }
}
```

## MDX Page Format

Every page is an MDX file with frontmatter:

```mdx
---
title: 'Page Title'
description: 'Short description for SEO and card previews'
icon: 'rocket'
---

# Introduction

Content goes here. MDX supports React components inline.

## Section Heading

Regular markdown works as expected.

<Note>
  This is a callout note.
</Note>

<Warning>
  This is a warning callout.
</Warning>

<Tip>
  This is a tip callout.
</Tip>

<Info>
  This is an info callout.
</Info>
```

## Mintlify Components

### Callouts
```mdx
<Note>Informational note</Note>
<Warning>Warning message</Warning>
<Tip>Helpful tip</Tip>
<Info>General info</Info>
```

### Code Blocks
````mdx
```python
def hello():
    print("Hello, world!")
```
````

With filename:
````mdx
```python hello.py
def hello():
    print("Hello, world!")
```
````

### Tabs
```mdx
<Tabs>
  <Tab title="npm">
    ```bash
    npm install package-name
    ```
  </Tab>
  <Tab title="yarn">
    ```bash
    yarn add package-name
    ```
  </Tab>
</Tabs>
```

### Cards
```mdx
<CardGroup cols={2}>
  <Card title="Quickstart" icon="bolt" href="/quickstart">
    Get up and running in 5 minutes.
  </Card>
  <Card title="API Reference" icon="code" href="/api-reference">
    Explore the full API.
  </Card>
</CardGroup>
```

### Steps
```mdx
<Steps>
  <Step title="Install the SDK">
    ```bash
    npm install @yourcompany/sdk
    ```
  </Step>
  <Step title="Initialize">
    Create your client with your API key.
  </Step>
  <Step title="Make your first call">
    Use the SDK to make your first API call.
  </Step>
</Steps>
```

### API Reference Pages (OpenAPI)
```mdx
---
title: 'Get Users'
openapi: 'GET /users'
---
```

Configure OpenAPI source in mint.json:
```json
{
  "openapi": "https://yourapi.com/openapi.json"
}
```

## Local Development

```bash
# Install Mintlify CLI
npm install -g mintlify

# Start local dev server (run from docs directory)
mintlify dev

# Opens at http://localhost:3000
```

## Deployment

Mintlify deploys automatically from Git:
1. Connect GitHub/GitLab repo at dashboard.mintlify.com
2. Point to docs directory in settings
3. Every push to main triggers a deploy

Manual deploy:
```bash
mintlify deploy
```

## Writing Good Documentation

Structure docs pages as:
1. **What it is** — one clear sentence
2. **Why use it** — the problem it solves
3. **Prerequisites** — what they need first
4. **Steps** — numbered, actionable
5. **Examples** — real code that works
6. **Troubleshooting** — common errors and solutions
7. **Next steps** — where to go from here

## Navigation Best Practices

- Group pages logically: "Get Started" → "Guides" → "API Reference"
- Keep navigation shallow (max 2 levels deep)
- Put the most important pages first
- Use clear, descriptive group names

## Notes for Claude

- Always check `mint.json` exists before adding pages — the page must be listed in `navigation`
- MDX files must be referenced in `mint.json` navigation or they won't appear
- Icons use Fontawesome names (e.g., `"rocket"`, `"code"`, `"database"`)
- Images go in the `/images/` or `/logo/` directory and are referenced with absolute paths

---

## Skill: `mintlify-mintlify`

---
name: mintlify:mintlify
description: Comprehensive reference for building Mintlify documentation sites. Covers creating pages, configuring docs.json, adding components, navigation, and API references.
---

## mintlify:mintlify
**Category:** Mintlify

**What it does:**
Comprehensive reference for building Mintlify documentation sites. Routes to detailed reference files for all components and configuration options. Covers:
- Creating pages
- Configuring `docs.json`
- Adding components
- Setting up navigation
- Working with API references

**When to trigger:**
- Working on a Mintlify docs site
- "How do I add X to Mintlify?"
- Configuring docs.json
- Building API reference pages

**How to install:**
```bash
npx claude install mintlify
```

**Trigger phrase:** Any Mintlify documentation work — building pages, configuring navigation, adding components.

---

## Skill: `planning`

---
name: planning
description: Create structured, actionable plans for projects, tasks, or goals. Use this skill when the user needs to plan a project, break down a goal into steps, create a roadmap, or organize work before execution.
---

# Planning

Create clear, structured, and actionable plans that bridge goals and execution.

## Planning Philosophy

Good plans are:
- **Specific** — concrete actions, not vague intentions
- **Sequenced** — ordered by dependency and priority
- **Scoped** — right level of detail for the time horizon
- **Adaptable** — built with checkpoints for course correction

## Planning Process

### Step 1: Clarify the Goal
Before planning, ensure the goal is well-defined:
- What does success look like? Define the end state concretely.
- What are the hard constraints? (deadline, budget, resources, tech)
- What are the unknowns? Flag assumptions that need validation.
- What's the planning horizon? Day/week/month/quarter?

### Step 2: Decompose into Phases
Break the goal into logical phases:
- Each phase should have a clear deliverable or milestone
- Phases should be sequenced by dependency (what must come first?)
- Identify the critical path — what's blocking everything else?

### Step 3: Define Tasks
For each phase, define concrete tasks:
- Each task should be completable in a single focused session
- Tasks should have clear done criteria (not "work on X", but "complete X")
- Assign owners if multiple people are involved
- Add time estimates where helpful

### Step 4: Identify Risks
For each plan, surface:
- **Blockers** — things that would stop progress entirely
- **Dependencies** — external inputs or decisions needed
- **Assumptions** — things assumed true that could be wrong
- **Mitigations** — how to reduce or recover from each risk

### Step 5: Define Success Metrics
How will progress be tracked?
- What are the key milestones?
- What signals indicate the plan is on/off track?
- What are the go/no-go decision points?

## Output Formats

### Quick Plan (for shorter horizons)
```
Goal: [one sentence]

Phase 1: [Name] — [deliverable]
  - [ ] Task 1
  - [ ] Task 2

Phase 2: [Name] — [deliverable]
  - [ ] Task 1
  - [ ] Task 2

Risks: [top 2-3 risks]
First step: [the single next action]
```

### Full Project Plan (for complex projects)
Provide a structured document with:
- Executive summary
- Goals and success criteria
- Phased roadmap with milestones
- Task breakdown per phase
- Risk register
- Assumptions log
- Next immediate actions

## Common Planning Mistakes to Avoid

- **Planning too far ahead in detail** — only detail the next 1-2 phases; future phases should stay high-level until closer
- **Missing dependencies** — always ask "what needs to be true for this step to happen?"
- **Underestimating setup** — environment, research, and coordination tasks are real work
- **No review cadence** — build in checkpoints to reassess the plan itself

## After the Plan

Once the plan is ready:
1. Identify the single next action (SNA) — what happens in the next 30 minutes?
2. Set the first checkpoint — when will the plan be reviewed?
3. Communicate the plan to all stakeholders if applicable

---

## Skill: `raffle-winner-picker`

---
name: raffle-winner-picker
description: Picks random winners from lists, spreadsheets, or Google Sheets for giveaways, raffles, and contests. Ensures fair, unbiased selection with transparency.
---

# Raffle Winner Picker

This skill randomly selects winners from lists, spreadsheets, or Google Sheets for giveaways and contests.

## When to Use This Skill

- Running social media giveaways
- Picking raffle winners at events
- Randomly selecting participants for surveys or tests
- Choosing winners from contest submissions
- Fair distribution of limited spots or resources
- Random team assignments

## What This Skill Does

1. **Random Selection**: Uses cryptographically random selection
2. **Multiple Sources**: Works with CSV, Excel, Google Sheets, or plain lists
3. **Multiple Winners**: Can pick one or multiple winners
4. **Duplicate Prevention**: Ensures the same person can't win twice
5. **Transparent Results**: Shows the selection process clearly
6. **Winner Details**: Displays all relevant information about winners

## How to Use

### From Google Sheets

```
Pick a random row from this Google Sheet to select a winner 
for a giveaway: [Sheet URL]
```

### From Local File

```
Pick 3 random winners from entries.csv
```

### From List

```
Pick a random winner from this list:
- Alice (alice@email.com)
- Bob (bob@email.com)
- Carol (carol@email.com)
...
```

### Multiple Winners

```
Pick 5 random winners from contest-entries.xlsx, 
make sure no duplicates
```

## Example

**User**: "Pick a random row from this Google Sheet to select a winner for a giveaway."

**Output**:
```
Accessing Google Sheet...
Total entries found: 247

Randomly selecting winner...

🎉 WINNER SELECTED! 🎉

Row #142
Name: Sarah Johnson
Email: sarah.j@email.com
Entry Date: March 10, 2024
Comment: "Love your newsletter!"

Selection method: Cryptographically random
Timestamp: 2024-03-15 14:32:18 UTC

Would you like to:
- Pick another winner (excluding Sarah)?
- Export winner details?
- Pick runner-ups?
```

**Inspired by:** Lenny's use case - picking a Sora 2 giveaway winner from his subscriber Slack community

## Features

### Fair Selection
- Uses secure random number generation
- No bias or patterns
- Transparent process
- Repeatable with seed (for verification)

### Exclusions
```
Pick a random winner excluding previous winners: 
Alice, Bob, Carol
```

### Weighted Selection
```
Pick a winner with weighted probability based on 
the "entries" column (1 entry = 1 ticket)
```

### Runner-ups
```
Pick 1 winner and 3 runner-ups from the list
```

## Example Workflows

### Social Media Giveaway
1. Export entries from Google Form to Sheets
2. "Pick a random winner from [Sheet URL]"
3. Verify winner details
4. Announce publicly with timestamp

### Event Raffle
1. Create CSV of attendee names and emails
2. "Pick 10 random winners from attendees.csv"
3. Export winner list
4. Email winners directly

### Team Assignment
1. Have list of participants
2. "Randomly split this list into 4 equal teams"
3. Review assignments
4. Share team rosters

## Tips

- **Document the process**: Save the timestamp and method
- **Public announcement**: Share selection details for transparency
- **Check eligibility**: Verify winner meets contest rules
- **Have backups**: Pick runner-ups in case winner is ineligible
- **Export results**: Save winner list for records

## Privacy & Fairness

✓ Uses cryptographically secure randomness
✓ No manipulation possible
✓ Timestamp recorded for verification
✓ Can provide seed for third-party verification
✓ Respects data privacy

## Common Use Cases

- Newsletter subscriber giveaways
- Product launch raffles
- Conference ticket drawings
- Beta tester selection
- Focus group participant selection
- Random prize distribution at events

---

## Skill: `simplify`

---
name: simplify
description: Review recently changed code for reuse, quality, and efficiency — then fix any issues found. Use this skill when the user wants to simplify or improve code they just wrote, or asks for a quality pass on their changes.
---

# Simplify

Review changed code for quality, then apply targeted improvements.

## When to Use

Use after writing or changing code when:
- The user asks to "simplify this" or "clean this up"
- Code was written quickly and needs a quality pass
- Refactoring opportunities are visible but not worth a full rewrite

## Review Checklist

Run through this checklist on the changed code:

### Duplication
- [ ] Is similar logic repeated that could be extracted into a function?
- [ ] Are there copy-pasted blocks that differ only in a variable?
- [ ] Could a loop or `.map()` replace repeated statements?

### Complexity
- [ ] Is there nesting deeper than 3 levels that could be flattened?
- [ ] Could early returns reduce nesting (guard clauses)?
- [ ] Is there a simpler algorithm or built-in that achieves the same result?
- [ ] Are there unnecessary variables or intermediate values?

### Naming
- [ ] Do variable and function names clearly describe what they hold/do?
- [ ] Are there single-letter variables (outside loops/lambdas) that should be named?
- [ ] Are there misleading names (e.g., `data`, `result`, `temp`)?

### Reuse
- [ ] Does this reimplement something that already exists in the codebase?
- [ ] Does this reimplement a standard library function?
- [ ] Could an existing utility or helper be used?

### Efficiency
- [ ] Are there unnecessary loops (O(n²) where O(n) is possible)?
- [ ] Are expensive operations repeated inside a loop that could be hoisted?
- [ ] Are there unnecessary re-renders or recomputations?

### Dead Code
- [ ] Are there unused variables or imports?
- [ ] Are there commented-out code blocks that should be removed?
- [ ] Are there debug `console.log` / `print` statements left in?

## Fix Strategy

For each issue found:
1. Make the smallest change that addresses it
2. Verify the behavior is unchanged (run tests if available)
3. Don't refactor parts of the code that weren't changed

## Output Format

Present improvements as:

```
## Simplification Review

### Issues Found

**Duplication** (lines 12-24, 40-52):
The same validation logic is repeated. Extracted into `validateInput()`.

**Naming** (line 8):
`d` renamed to `dueDate` for clarity.

**Dead code** (line 67):
Removed commented-out code block.

### Changes Applied
[List of specific changes made]

### Not Changed
[Note anything that could be improved but was left alone to stay in scope]
```

## Scope Boundaries

Only modify:
- The code the user recently changed (not the whole file)
- Code directly related to the user's change

Do not:
- Refactor unrelated code
- Change architecture or add features
- Add error handling for scenarios not in scope
- Add comments or docstrings unless the logic is non-obvious

---

## Skill: `skill-creator`

---
name: skill-creator
description: Guide for creating effective skills. This skill should be used when users want to create a new skill (or update an existing skill) that extends Claude's capabilities with specialized knowledge, workflows, or tool integrations.
license: Complete terms in LICENSE.txt
---

# Skill Creator

This skill provides guidance for creating effective skills.

## About Skills

Skills are modular, self-contained packages that extend Claude's capabilities by providing
specialized knowledge, workflows, and tools. Think of them as "onboarding guides" for specific
domains or tasks—they transform Claude from a general-purpose agent into a specialized agent
equipped with procedural knowledge that no model can fully possess.

### What Skills Provide

1. Specialized workflows - Multi-step procedures for specific domains
2. Tool integrations - Instructions for working with specific file formats or APIs
3. Domain expertise - Company-specific knowledge, schemas, business logic
4. Bundled resources - Scripts, references, and assets for complex and repetitive tasks

### Anatomy of a Skill

Every skill consists of a required SKILL.md file and optional bundled resources:

```
skill-name/
├── SKILL.md (required)
│   ├── YAML frontmatter metadata (required)
│   │   ├── name: (required)
│   │   └── description: (required)
│   └── Markdown instructions (required)
└── Bundled Resources (optional)
    ├── scripts/          - Executable code (Python/Bash/etc.)
    ├── references/       - Documentation intended to be loaded into context as needed
    └── assets/           - Files used in output (templates, icons, fonts, etc.)
```

#### SKILL.md (required)

**Metadata Quality:** The `name` and `description` in YAML frontmatter determine when Claude will use the skill. Be specific about what the skill does and when to use it. Use the third-person (e.g. "This skill should be used when..." instead of "Use this skill when...").

#### Bundled Resources (optional)

##### Scripts (`scripts/`)

Executable code (Python/Bash/etc.) for tasks that require deterministic reliability or are repeatedly rewritten.

- **When to include**: When the same code is being rewritten repeatedly or deterministic reliability is needed
- **Example**: `scripts/rotate_pdf.py` for PDF rotation tasks
- **Benefits**: Token efficient, deterministic, may be executed without loading into context
- **Note**: Scripts may still need to be read by Claude for patching or environment-specific adjustments

##### References (`references/`)

Documentation and reference material intended to be loaded as needed into context to inform Claude's process and thinking.

- **When to include**: For documentation that Claude should reference while working
- **Examples**: `references/finance.md` for financial schemas, `references/mnda.md` for company NDA template, `references/policies.md` for company policies, `references/api_docs.md` for API specifications
- **Use cases**: Database schemas, API documentation, domain knowledge, company policies, detailed workflow guides
- **Benefits**: Keeps SKILL.md lean, loaded only when Claude determines it's needed
- **Best practice**: If files are large (>10k words), include grep search patterns in SKILL.md
- **Avoid duplication**: Information should live in either SKILL.md or references files, not both. Prefer references files for detailed information unless it's truly core to the skill—this keeps SKILL.md lean while making information discoverable without hogging the context window. Keep only essential procedural instructions and workflow guidance in SKILL.md; move detailed reference material, schemas, and examples to references files.

##### Assets (`assets/`)

Files not intended to be loaded into context, but rather used within the output Claude produces.

- **When to include**: When the skill needs files that will be used in the final output
- **Examples**: `assets/logo.png` for brand assets, `assets/slides.pptx` for PowerPoint templates, `assets/frontend-template/` for HTML/React boilerplate, `assets/font.ttf` for typography
- **Use cases**: Templates, images, icons, boilerplate code, fonts, sample documents that get copied or modified
- **Benefits**: Separates output resources from documentation, enables Claude to use files without loading them into context

### Progressive Disclosure Design Principle

Skills use a three-level loading system to manage context efficiently:

1. **Metadata (name + description)** - Always in context (~100 words)
2. **SKILL.md body** - When skill triggers (<5k words)
3. **Bundled resources** - As needed by Claude (Unlimited*)

*Unlimited because scripts can be executed without reading into context window.

## Skill Creation Process

To create a skill, follow the "Skill Creation Process" in order, skipping steps only if there is a clear reason why they are not applicable.

### Step 1: Understanding the Skill with Concrete Examples

Skip this step only when the skill's usage patterns are already clearly understood. It remains valuable even when working with an existing skill.

To create an effective skill, clearly understand concrete examples of how the skill will be used. This understanding can come from either direct user examples or generated examples that are validated with user feedback.

For example, when building an image-editor skill, relevant questions include:

- "What functionality should the image-editor skill support? Editing, rotating, anything else?"
- "Can you give some examples of how this skill would be used?"
- "I can imagine users asking for things like 'Remove the red-eye from this image' or 'Rotate this image'. Are there other ways you imagine this skill being used?"
- "What would a user say that should trigger this skill?"

To avoid overwhelming users, avoid asking too many questions in a single message. Start with the most important questions and follow up as needed for better effectiveness.

Conclude this step when there is a clear sense of the functionality the skill should support.

### Step 2: Planning the Reusable Skill Contents

To turn concrete examples into an effective skill, analyze each example by:

1. Considering how to execute on the example from scratch
2. Identifying what scripts, references, and assets would be helpful when executing these workflows repeatedly

Example: When building a `pdf-editor` skill to handle queries like "Help me rotate this PDF," the analysis shows:

1. Rotating a PDF requires re-writing the same code each time
2. A `scripts/rotate_pdf.py` script would be helpful to store in the skill

Example: When designing a `frontend-webapp-builder` skill for queries like "Build me a todo app" or "Build me a dashboard to track my steps," the analysis shows:

1. Writing a frontend webapp requires the same boilerplate HTML/React each time
2. An `assets/hello-world/` template containing the boilerplate HTML/React project files would be helpful to store in the skill

Example: When building a `big-query` skill to handle queries like "How many users have logged in today?" the analysis shows:

1. Querying BigQuery requires re-discovering the table schemas and relationships each time
2. A `references/schema.md` file documenting the table schemas would be helpful to store in the skill

To establish the skill's contents, analyze each concrete example to create a list of the reusable resources to include: scripts, references, and assets.

### Step 3: Initializing the Skill

At this point, it is time to actually create the skill.

Skip this step only if the skill being developed already exists, and iteration or packaging is needed. In this case, continue to the next step.

When creating a new skill from scratch, always run the `init_skill.py` script. The script conveniently generates a new template skill directory that automatically includes everything a skill requires, making the skill creation process much more efficient and reliable.

Usage:

```bash
scripts/init_skill.py <skill-name> --path <output-directory>
```

The script:

- Creates the skill directory at the specified path
- Generates a SKILL.md template with proper frontmatter and TODO placeholders
- Creates example resource directories: `scripts/`, `references/`, and `assets/`
- Adds example files in each directory that can be customized or deleted

After initialization, customize or remove the generated SKILL.md and example files as needed.

### Step 4: Edit the Skill

When editing the (newly-generated or existing) skill, remember that the skill is being created for another instance of Claude to use. Focus on including information that would be beneficial and non-obvious to Claude. Consider what procedural knowledge, domain-specific details, or reusable assets would help another Claude instance execute these tasks more effectively.

#### Start with Reusable Skill Contents

To begin implementation, start with the reusable resources identified above: `scripts/`, `references/`, and `assets/` files. Note that this step may require user input. For example, when implementing a `brand-guidelines` skill, the user may need to provide brand assets or templates to store in `assets/`, or documentation to store in `references/`.

Also, delete any example files and directories not needed for the skill. The initialization script creates example files in `scripts/`, `references/`, and `assets/` to demonstrate structure, but most skills won't need all of them.

#### Update SKILL.md

**Writing Style:** Write the entire skill using **imperative/infinitive form** (verb-first instructions), not second person. Use objective, instructional language (e.g., "To accomplish X, do Y" rather than "You should do X" or "If you need to do X"). This maintains consistency and clarity for AI consumption.

To complete SKILL.md, answer the following questions:

1. What is the purpose of the skill, in a few sentences?
2. When should the skill be used?
3. In practice, how should Claude use the skill? All reusable skill contents developed above should be referenced so that Claude knows how to use them.

### Step 5: Packaging a Skill

Once the skill is ready, it should be packaged into a distributable zip file that gets shared with the user. The packaging process automatically validates the skill first to ensure it meets all requirements:

```bash
scripts/package_skill.py <path/to/skill-folder>
```

Optional output directory specification:

```bash
scripts/package_skill.py <path/to/skill-folder> ./dist
```

The packaging script will:

1. **Validate** the skill automatically, checking:
   - YAML frontmatter format and required fields
   - Skill naming conventions and directory structure
   - Description completeness and quality
   - File organization and resource references

2. **Package** the skill if validation passes, creating a zip file named after the skill (e.g., `my-skill.zip`) that includes all files and maintains the proper directory structure for distribution.

If validation fails, the script will report the errors and exit without creating a package. Fix any validation errors and run the packaging command again.

### Step 6: Iterate

After testing the skill, users may request improvements. Often this happens right after using the skill, with fresh context of how the skill performed.

**Iteration workflow:**
1. Use the skill on real tasks
2. Notice struggles or inefficiencies
3. Identify how SKILL.md or bundled resources should be updated
4. Implement changes and test again

---

## Skill: `skill-share`

---
name: skill-share
description: A skill that creates new Claude skills and automatically shares them on Slack using Rube for seamless team collaboration and skill discovery.
license: Complete terms in LICENSE.txt
---

## When to use this skill

Use this skill when you need to:
- **Create new Claude skills** with proper structure and metadata
- **Generate skill packages** ready for distribution
- **Automatically share created skills** on Slack channels for team visibility
- **Validate skill structure** before sharing
- **Package and distribute** skills to your team

Also use this skill when:
- **User says he wants to create/share his skill** 

This skill is ideal for:
- Creating skills as part of team workflows
- Building internal tools that need skill creation + team notification
- Automating the skill development pipeline
- Collaborative skill creation with team notifications

## Key Features

### 1. Skill Creation
- Creates properly structured skill directories with SKILL.md
- Generates standardized scripts/, references/, and assets/ directories
- Auto-generates YAML frontmatter with required metadata
- Enforces naming conventions (hyphen-case)

### 2. Skill Validation
- Validates SKILL.md format and required fields
- Checks naming conventions
- Ensures metadata completeness before packaging

### 3. Skill Packaging
- Creates distributable zip files
- Includes all skill assets and documentation
- Runs validation automatically before packaging

### 4. Slack Integration via Rube
- Automatically sends created skill information to designated Slack channels
- Shares skill metadata (name, description, link)
- Posts skill summary for team discovery
- Provides direct links to skill files

## How It Works

1. **Initialization**: Provide skill name and description
2. **Creation**: Skill directory is created with proper structure
3. **Validation**: Skill metadata is validated for correctness
4. **Packaging**: Skill is packaged into a distributable format
5. **Slack Notification**: Skill details are posted to your team's Slack channel

## Example Usage

```
When you ask Claude to create a skill called "pdf-analyzer":
1. Creates /skill-pdf-analyzer/ with SKILL.md template
2. Generates structured directories (scripts/, references/, assets/)
3. Validates the skill structure
4. Packages the skill as a zip file
5. Posts to Slack: "New Skill Created: pdf-analyzer - Advanced PDF analysis and extraction capabilities"
```

## Integration with Rube

This skill leverages Rube for:
- **SLACK_SEND_MESSAGE**: Posts skill information to team channels
- **SLACK_POST_MESSAGE_WITH_BLOCKS**: Shares rich formatted skill metadata
- **SLACK_FIND_CHANNELS**: Discovers target channels for skill announcements

## Requirements

- Slack workspace connection via Rube
- Write access to skill creation directory
- Python 3.7+ for skill creation scripts
- Target Slack channel for skill notifications

---

## Skill: `slack-gif-creator`

---
name: slack-gif-creator
description: Toolkit for creating animated GIFs optimized for Slack, with validators for size constraints and composable animation primitives. This skill applies when users request animated GIFs or emoji animations for Slack from descriptions like "make me a GIF for Slack of X doing Y".
license: Complete terms in LICENSE.txt
---

# Slack GIF Creator - Flexible Toolkit

A toolkit for creating animated GIFs optimized for Slack. Provides validators for Slack's constraints, composable animation primitives, and optional helper utilities. **Apply these tools however needed to achieve the creative vision.**

## Slack's Requirements

Slack has specific requirements for GIFs based on their use:

**Message GIFs:**
- Max size: ~2MB
- Optimal dimensions: 480x480
- Typical FPS: 15-20
- Color limit: 128-256
- Duration: 2-5s

**Emoji GIFs:**
- Max size: 64KB (strict limit)
- Optimal dimensions: 128x128
- Typical FPS: 10-12
- Color limit: 32-48
- Duration: 1-2s

**Emoji GIFs are challenging** - the 64KB limit is strict. Strategies that help:
- Limit to 10-15 frames total
- Use 32-48 colors maximum
- Keep designs simple
- Avoid gradients
- Validate file size frequently

## Toolkit Structure

This skill provides three types of tools:

1. **Validators** - Check if a GIF meets Slack's requirements
2. **Animation Primitives** - Composable building blocks for motion (shake, bounce, move, kaleidoscope)
3. **Helper Utilities** - Optional functions for common needs (text, colors, effects)

**Complete creative freedom is available in how these tools are applied.**

## Core Validators

To ensure a GIF meets Slack's constraints, use these validators:

```python
from core.gif_builder import GIFBuilder

# After creating your GIF, check if it meets requirements
builder = GIFBuilder(width=128, height=128, fps=10)
# ... add your frames however you want ...

# Save and check size
info = builder.save('emoji.gif', num_colors=48, optimize_for_emoji=True)

# The save method automatically warns if file exceeds limits
# info dict contains: size_kb, size_mb, frame_count, duration_seconds
```

**File size validator**:
```python
from core.validators import check_slack_size

# Check if GIF meets size limits
passes, info = check_slack_size('emoji.gif', is_emoji=True)
# Returns: (True/False, dict with size details)
```

**Dimension validator**:
```python
from core.validators import validate_dimensions

# Check dimensions
passes, info = validate_dimensions(128, 128, is_emoji=True)
# Returns: (True/False, dict with dimension details)
```

**Complete validation**:
```python
from core.validators import validate_gif, is_slack_ready

# Run all validations
all_pass, results = validate_gif('emoji.gif', is_emoji=True)

# Or quick check
if is_slack_ready('emoji.gif', is_emoji=True):
    print("Ready to upload!")
```

## Animation Primitives

These are composable building blocks for motion. Apply these to any object in any combination:

### Shake
```python
from templates.shake import create_shake_animation

# Shake an emoji
frames = create_shake_animation(
    object_type='emoji',
    object_data={'emoji': '😱', 'size': 80},
    num_frames=20,
    shake_intensity=15,
    direction='both'  # or 'horizontal', 'vertical'
)
```

### Bounce
```python
from templates.bounce import create_bounce_animation

# Bounce a circle
frames = create_bounce_animation(
    object_type='circle',
    object_data={'radius': 40, 'color': (255, 100, 100)},
    num_frames=30,
    bounce_height=150
)
```

### Spin / Rotate
```python
from templates.spin import create_spin_animation, create_loading_spinner

# Clockwise spin
frames = create_spin_animation(
    object_type='emoji',
    object_data={'emoji': '🔄', 'size': 100},
    rotation_type='clockwise',
    full_rotations=2
)

# Wobble rotation
frames = create_spin_animation(rotation_type='wobble', full_rotations=3)

# Loading spinner
frames = create_loading_spinner(spinner_type='dots')
```

### Pulse / Heartbeat
```python
from templates.pulse import create_pulse_animation, create_attention_pulse

# Smooth pulse
frames = create_pulse_animation(
    object_data={'emoji': '❤️', 'size': 100},
    pulse_type='smooth',
    scale_range=(0.8, 1.2)
)

# Heartbeat (double-pump)
frames = create_pulse_animation(pulse_type='heartbeat')

# Attention pulse for emoji GIFs
frames = create_attention_pulse(emoji='⚠️', num_frames=20)
```

### Fade
```python
from templates.fade import create_fade_animation, create_crossfade

# Fade in
frames = create_fade_animation(fade_type='in')

# Fade out
frames = create_fade_animation(fade_type='out')

# Crossfade between two emojis
frames = create_crossfade(
    object1_data={'emoji': '😊', 'size': 100},
    object2_data={'emoji': '😂', 'size': 100}
)
```

### Zoom
```python
from templates.zoom import create_zoom_animation, create_explosion_zoom

# Zoom in dramatically
frames = create_zoom_animation(
    zoom_type='in',
    scale_range=(0.1, 2.0),
    add_motion_blur=True
)

# Zoom out
frames = create_zoom_animation(zoom_type='out')

# Explosion zoom
frames = create_explosion_zoom(emoji='💥')
```

### Explode / Shatter
```python
from templates.explode import create_explode_animation, create_particle_burst

# Burst explosion
frames = create_explode_animation(
    explode_type='burst',
    num_pieces=25
)

# Shatter effect
frames = create_explode_animation(explode_type='shatter')

# Dissolve into particles
frames = create_explode_animation(explode_type='dissolve')

# Particle burst
frames = create_particle_burst(particle_count=30)
```

### Wiggle / Jiggle
```python
from templates.wiggle import create_wiggle_animation, create_excited_wiggle

# Jello wobble
frames = create_wiggle_animation(
    wiggle_type='jello',
    intensity=1.0,
    cycles=2
)

# Wave motion
frames = create_wiggle_animation(wiggle_type='wave')

# Excited wiggle for emoji GIFs
frames = create_excited_wiggle(emoji='🎉')
```

### Slide
```python
from templates.slide import create_slide_animation, create_multi_slide

# Slide in from left with overshoot
frames = create_slide_animation(
    direction='left',
    slide_type='in',
    overshoot=True
)

# Slide across
frames = create_slide_animation(direction='left', slide_type='across')

# Multiple objects sliding in sequence
objects = [
    {'data': {'emoji': '🎯', 'size': 60}, 'direction': 'left', 'final_pos': (120, 240)},
    {'data': {'emoji': '🎪', 'size': 60}, 'direction': 'right', 'final_pos': (240, 240)}
]
frames = create_multi_slide(objects, stagger_delay=5)
```

### Flip
```python
from templates.flip import create_flip_animation, create_quick_flip

# Horizontal flip between two emojis
frames = create_flip_animation(
    object1_data={'emoji': '😊', 'size': 120},
    object2_data={'emoji': '😂', 'size': 120},
    flip_axis='horizontal'
)

# Vertical flip
frames = create_flip_animation(flip_axis='vertical')

# Quick flip for emoji GIFs
frames = create_quick_flip('👍', '👎')
```

### Morph / Transform
```python
from templates.morph import create_morph_animation, create_reaction_morph

# Crossfade morph
frames = create_morph_animation(
    object1_data={'emoji': '😊', 'size': 100},
    object2_data={'emoji': '😂', 'size': 100},
    morph_type='crossfade'
)

# Scale morph (shrink while other grows)
frames = create_morph_animation(morph_type='scale')

# Spin morph (3D flip-like)
frames = create_morph_animation(morph_type='spin_morph')
```

### Move Effect
```python
from templates.move import create_move_animation

# Linear movement
frames = create_move_animation(
    object_type='emoji',
    object_data={'emoji': '🚀', 'size': 60},
    start_pos=(50, 240),
    end_pos=(430, 240),
    motion_type='linear',
    easing='ease_out'
)

# Arc movement (parabolic trajectory)
frames = create_move_animation(
    object_type='emoji',
    object_data={'emoji': '⚽', 'size': 60},
    start_pos=(50, 350),
    end_pos=(430, 350),
    motion_type='arc',
    motion_params={'arc_height': 150}
)

# Circular movement
frames = create_move_animation(
    object_type='emoji',
    object_data={'emoji': '🌍', 'size': 50},
    motion_type='circle',
    motion_params={
        'center': (240, 240),
        'radius': 120,
        'angle_range': 360  # full circle
    }
)

# Wave movement
frames = create_move_animation(
    motion_type='wave',
    motion_params={
        'wave_amplitude': 50,
        'wave_frequency': 2
    }
)

# Or use low-level easing functions
from core.easing import interpolate, calculate_arc_motion

for i in range(num_frames):
    t = i / (num_frames - 1)
    x = interpolate(start_x, end_x, t, easing='ease_out')
    # Or: x, y = calculate_arc_motion(start, end, height, t)
```

### Kaleidoscope Effect
```python
from templates.kaleidoscope import apply_kaleidoscope, create_kaleidoscope_animation

# Apply to a single frame
kaleido_frame = apply_kaleidoscope(frame, segments=8)

# Or create animated kaleidoscope
frames = create_kaleidoscope_animation(
    base_frame=my_frame,  # or None for demo pattern
    num_frames=30,
    segments=8,
    rotation_speed=1.0
)

# Simple mirror effects (faster)
from templates.kaleidoscope import apply_simple_mirror

mirrored = apply_simple_mirror(frame, mode='quad')  # 4-way mirror
# modes: 'horizontal', 'vertical', 'quad', 'radial'
```

**To compose primitives freely, follow these patterns:**
```python
# Example: Bounce + shake for impact
for i in range(num_frames):
    frame = create_blank_frame(480, 480, bg_color)

    # Bounce motion
    t_bounce = i / (num_frames - 1)
    y = interpolate(start_y, ground_y, t_bounce, 'bounce_out')

    # Add shake on impact (when y reaches ground)
    if y >= ground_y - 5:
        shake_x = math.sin(i * 2) * 10
        x = center_x + shake_x
    else:
        x = center_x

    draw_emoji(frame, '⚽', (x, y), size=60)
    builder.add_frame(frame)
```

## Helper Utilities

These are optional helpers for common needs. **Use, modify, or replace these with custom implementations as needed.**

### GIF Builder (Assembly & Optimization)

```python
from core.gif_builder import GIFBuilder

# Create builder with your chosen settings
builder = GIFBuilder(width=480, height=480, fps=20)

# Add frames (however you created them)
for frame in my_frames:
    builder.add_frame(frame)

# Save with optimization
builder.save('output.gif',
             num_colors=128,
             optimize_for_emoji=False)
```

Key features:
- Automatic color quantization
- Duplicate frame removal
- Size warnings for Slack limits
- Emoji mode (aggressive optimization)

### Text Rendering

For small GIFs like emojis, text readability is challenging. A common solution involves adding outlines:

```python
from core.typography import draw_text_with_outline, TYPOGRAPHY_SCALE

# Text with outline (helps readability)
draw_text_with_outline(
    frame, "BONK!",
    position=(240, 100),
    font_size=TYPOGRAPHY_SCALE['h1'],  # 60px
    text_color=(255, 68, 68),
    outline_color=(0, 0, 0),
    outline_width=4,
    centered=True
)
```

To implement custom text rendering, use PIL's `ImageDraw.text()` which works fine for larger GIFs.

### Color Management

Professional-looking GIFs often use cohesive color palettes:

```python
from core.color_palettes import get_palette

# Get a pre-made palette
palette = get_palette('vibrant')  # or 'pastel', 'dark', 'neon', 'professional'

bg_color = palette['background']
text_color = palette['primary']
accent_color = palette['accent']
```

To work with colors directly, use RGB tuples - whatever works for the use case.

### Visual Effects

Optional effects for impact moments:

```python
from core.visual_effects import ParticleSystem, create_impact_flash, create_shockwave_rings

# Particle system
particles = ParticleSystem()
particles.emit_sparkles(x=240, y=200, count=15)
particles.emit_confetti(x=240, y=200, count=20)

# Update and render each frame
particles.update()
particles.render(frame)

# Flash effect
frame = create_impact_flash(frame, position=(240, 200), radius=100)

# Shockwave rings
frame = create_shockwave_rings(frame, position=(240, 200), radii=[30, 60, 90])
```

### Easing Functions

Smooth motion uses easing instead of linear interpolation:

```python
from core.easing import interpolate

# Object falling (accelerates)
y = interpolate(start=0, end=400, t=progress, easing='ease_in')

# Object landing (decelerates)
y = interpolate(start=0, end=400, t=progress, easing='ease_out')

# Bouncing
y = interpolate(start=0, end=400, t=progress, easing='bounce_out')

# Overshoot (elastic)
scale = interpolate(start=0.5, end=1.0, t=progress, easing='elastic_out')
```

Available easings: `linear`, `ease_in`, `ease_out`, `ease_in_out`, `bounce_out`, `elastic_out`, `back_out` (overshoot), and more in `core/easing.py`.

### Frame Composition

Basic drawing utilities if you need them:

```python
from core.frame_composer import (
    create_gradient_background,  # Gradient backgrounds
    draw_emoji_enhanced,         # Emoji with optional shadow
    draw_circle_with_shadow,     # Shapes with depth
    draw_star                    # 5-pointed stars
)

# Gradient background
frame = create_gradient_background(480, 480, top_color, bottom_color)

# Emoji with shadow
draw_emoji_enhanced(frame, '🎉', position=(200, 200), size=80, shadow=True)
```

## Optimization Strategies

When your GIF is too large:

**For Message GIFs (>2MB):**
1. Reduce frames (lower FPS or shorter duration)
2. Reduce colors (128 → 64 colors)
3. Reduce dimensions (480x480 → 320x320)
4. Enable duplicate frame removal

**For Emoji GIFs (>64KB) - be aggressive:**
1. Limit to 10-12 frames total
2. Use 32-40 colors maximum
3. Avoid gradients (solid colors compress better)
4. Simplify design (fewer elements)
5. Use `optimize_for_emoji=True` in save method

## Example Composition Patterns

### Simple Reaction (Pulsing)
```python
builder = GIFBuilder(128, 128, 10)

for i in range(12):
    frame = Image.new('RGB', (128, 128), (240, 248, 255))

    # Pulsing scale
    scale = 1.0 + math.sin(i * 0.5) * 0.15
    size = int(60 * scale)

    draw_emoji_enhanced(frame, '😱', position=(64-size//2, 64-size//2),
                       size=size, shadow=False)
    builder.add_frame(frame)

builder.save('reaction.gif', num_colors=40, optimize_for_emoji=True)

# Validate
from core.validators import check_slack_size
check_slack_size('reaction.gif', is_emoji=True)
```

### Action with Impact (Bounce + Flash)
```python
builder = GIFBuilder(480, 480, 20)

# Phase 1: Object falls
for i in range(15):
    frame = create_gradient_background(480, 480, (240, 248, 255), (200, 230, 255))
    t = i / 14
    y = interpolate(0, 350, t, 'ease_in')
    draw_emoji_enhanced(frame, '⚽', position=(220, int(y)), size=80)
    builder.add_frame(frame)

# Phase 2: Impact + flash
for i in range(8):
    frame = create_gradient_background(480, 480, (240, 248, 255), (200, 230, 255))

    # Flash on first frames
    if i < 3:
        frame = create_impact_flash(frame, (240, 350), radius=120, intensity=0.6)

    draw_emoji_enhanced(frame, '⚽', position=(220, 350), size=80)

    # Text appears
    if i > 2:
        draw_text_with_outline(frame, "GOAL!", position=(240, 150),
                              font_size=60, text_color=(255, 68, 68),
                              outline_color=(0, 0, 0), outline_width=4, centered=True)

    builder.add_frame(frame)

builder.save('goal.gif', num_colors=128)
```

### Combining Primitives (Move + Shake)
```python
from templates.shake import create_shake_animation

# Create shake animation
shake_frames = create_shake_animation(
    object_type='emoji',
    object_data={'emoji': '😰', 'size': 70},
    num_frames=20,
    shake_intensity=12
)

# Create moving element that triggers the shake
builder = GIFBuilder(480, 480, 20)
for i in range(40):
    t = i / 39

    if i < 20:
        # Before trigger - use blank frame with moving object
        frame = create_blank_frame(480, 480, (255, 255, 255))
        x = interpolate(50, 300, t * 2, 'linear')
        draw_emoji_enhanced(frame, '🚗', position=(int(x), 300), size=60)
        draw_emoji_enhanced(frame, '😰', position=(350, 200), size=70)
    else:
        # After trigger - use shake frame
        frame = shake_frames[i - 20]
        # Add the car in final position
        draw_emoji_enhanced(frame, '🚗', position=(300, 300), size=60)

    builder.add_frame(frame)

builder.save('scare.gif')
```

## Philosophy

This toolkit provides building blocks, not rigid recipes. To work with a GIF request:

1. **Understand the creative vision** - What should happen? What's the mood?
2. **Design the animation** - Break it into phases (anticipation, action, reaction)
3. **Apply primitives as needed** - Shake, bounce, move, effects - mix freely
4. **Validate constraints** - Check file size, especially for emoji GIFs
5. **Iterate if needed** - Reduce frames/colors if over size limits

**The goal is creative freedom within Slack's technical constraints.**

## Dependencies

To use this toolkit, install these dependencies only if they aren't already present:

```bash
pip install pillow imageio numpy
```

---

## Skill: `tailored-resume-generator`

---
name: tailored-resume-generator
description: Analyzes job descriptions and generates tailored resumes that highlight relevant experience, skills, and achievements to maximize interview chances
---

# Tailored Resume Generator

## When to Use This Skill

- Applying for a specific job position
- Customizing your resume for different industries or roles
- Highlighting relevant experience for career transitions
- Optimizing your resume for ATS (Applicant Tracking Systems)
- Creating multiple resume versions for different job applications
- Emphasizing specific skills mentioned in job postings

## What This Skill Does

1. **Analyzes Job Descriptions**: Extracts key requirements, skills, qualifications, and keywords from job postings
2. **Identifies Priorities**: Determines what employers value most based on the job description language and structure
3. **Tailors Content**: Reorganizes and emphasizes relevant experience, skills, and achievements
4. **Optimizes Keywords**: Incorporates ATS-friendly keywords naturally throughout the resume
5. **Formats Professionally**: Creates clean, professional resume layouts suitable for various formats
6. **Provides Recommendations**: Suggests improvements and highlights gaps to address

## How to Use

### Basic Usage
Provide a job description and your background information:

```
I'm applying for this job:

[paste job description]

Here's my background:
- 5 years as software engineer at TechCorp
- Led team of 3 developers on mobile app project
- Expert in Python, JavaScript, React
- Computer Science degree from State University
```

### With Existing Resume
Upload or paste your current resume along with the job description:

```
Please tailor my resume for this position:

Job Description:
[paste job description]

My Current Resume:
[paste resume content]
```

### Career Transition
When changing industries or roles:

```
I'm transitioning from marketing to product management.
Here's the job I'm applying for:

[paste job description]

My transferable experience:
- 7 years in digital marketing
- Led cross-functional teams
- Managed product launches
- Data analysis and A/B testing
```

## Example

**User Request:**
```
I need a tailored resume for this job:

Senior Data Analyst Position

Requirements:
- 5+ years experience in data analysis
- Expert in SQL, Python, and data visualization tools
- Experience with A/B testing and statistical analysis
- Strong communication skills to present findings
- Healthcare industry experience preferred

My background:
- Data Analyst at RetailCo (2019-2024)
- Created dashboards using Tableau and Power BI
- Built Python scripts for data automation
- Worked with marketing team on campaign analysis
- Business Analytics degree
- Also did 1 year internship at HealthPlus clinic
```

**Generated Output:**

```markdown
# JOHN DOE
Email: john.doe@email.com | Phone: (555) 123-4567 | LinkedIn: linkedin.com/in/johndoe

## PROFESSIONAL SUMMARY
Results-driven Data Analyst with 5+ years of experience leveraging SQL, Python, and advanced
visualization tools to deliver actionable insights. Proven track record in statistical analysis,
A/B testing, and cross-functional collaboration. Healthcare industry experience with strong
ability to communicate complex data findings to stakeholders.

## TECHNICAL SKILLS
- **Data Analysis & Programming**: SQL, Python, Statistical Analysis, A/B Testing
- **Visualization Tools**: Tableau, Power BI, Advanced Dashboard Development
- **Data Management**: Data Automation, ETL Processes, Database Optimization
- **Business Intelligence**: Campaign Analytics, Performance Metrics, KPI Tracking

## PROFESSIONAL EXPERIENCE

**Data Analyst** | RetailCo | 2019 - 2024
- Designed and implemented 50+ SQL queries and Python automation scripts, reducing manual
  data processing time by 60%
- Conducted rigorous A/B testing and statistical analysis for marketing campaigns,
  improving campaign ROI by 35%
- Built interactive Tableau and Power BI dashboards for executive team, enabling
  data-driven decision making
- Presented analytical findings to cross-functional stakeholders including marketing,
  operations, and executive leadership
- Collaborated with marketing team to analyze customer behavior patterns and optimize
  targeting strategies

**Data Analysis Intern** | HealthPlus Clinic | 2018 - 2019
- Supported healthcare analytics initiatives by analyzing patient data and operational metrics
- Gained exposure to healthcare industry data management and HIPAA compliance requirements
- Assisted in creating reports for clinical staff to improve patient care workflows

## EDUCATION

**Bachelor of Science in Business Analytics**
State University | Graduated 2018

## KEY ACHIEVEMENTS
- Reduced data processing time by 60% through Python automation
- Improved marketing campaign ROI by 35% through A/B testing and optimization
- Created data visualization system now used across entire organization
```

**Additional Recommendations:**
- Consider adding any specific healthcare projects or certifications
- Quantify more achievements with metrics when possible
- If you have experience with R or advanced statistical methods, add them
- Consider mentioning any familiarity with healthcare regulations (HIPAA, etc.)

---

## Instructions

When a user requests resume tailoring:

### 1. Gather Information

**Job Description Analysis**:
- Request the full job description if not provided
- Ask for the company name and job title

**Candidate Background**:
- If user provides existing resume, use it as the foundation
- If not, request:
  - Work history (job titles, companies, dates, responsibilities)
  - Education background
  - Key skills and technical proficiencies
  - Notable achievements and metrics
  - Certifications or awards
  - Any other relevant information

### 2. Analyze Job Requirements

Extract and prioritize:
- **Must-have qualifications**: Years of experience, required skills, education
- **Key skills**: Technical tools, methodologies, competencies
- **Soft skills**: Communication, leadership, teamwork
- **Industry knowledge**: Domain-specific experience
- **Keywords**: Repeated terms, phrases, and buzzwords for ATS optimization
- **Company values**: Cultural fit indicators from job description

Create a mental map of:
- Priority 1: Critical requirements (deal-breakers)
- Priority 2: Important qualifications (strongly desired)
- Priority 3: Nice-to-have skills (bonus points)

### 3. Map Candidate Experience to Requirements

For each job requirement:
- Identify matching experience from candidate's background
- Find transferable skills if no direct match
- Note gaps that need to be addressed or de-emphasized
- Identify unique strengths to highlight

### 4. Structure the Tailored Resume

**Professional Summary** (3-4 lines):
- Lead with years of experience in the target role/field
- Include top 3-4 required skills from job description
- Mention industry experience if relevant
- Highlight unique value proposition

**Technical/Core Skills Section**:
- Group skills by category matching job requirements
- List required tools and technologies first
- Use exact terminology from job description
- Only include skills you can substantiate with experience

**Professional Experience**:
- For each role, emphasize responsibilities and achievements aligned with job requirements
- Use action verbs: Led, Developed, Implemented, Optimized, Managed, Created, Analyzed
- **Quantify achievements**: Include numbers, percentages, timeframes, scale
- Reorder bullet points to prioritize most relevant experience
- Use keywords naturally from job description
- Format: **[Action Verb] + [What] + [How/Why] + [Result/Impact]**

**Education**:
- List degrees, certifications relevant to position
- Include relevant coursework if early career
- Add certifications that match job requirements

**Optional Sections** (if applicable):
- Certifications & Licenses
- Publications or Speaking Engagements
- Awards & Recognition
- Volunteer Work (if relevant to role)
- Projects (especially for technical roles)

### 5. Optimize for ATS (Applicant Tracking Systems)

- Use standard section headings (Professional Experience, Education, Skills)
- Incorporate exact keywords from job description naturally
- Avoid tables, graphics, headers/footers, or complex formatting
- Use standard fonts and bullet points
- Include both acronyms and full terms (e.g., "SQL (Structured Query Language)")
- Match job title terminology where truthful

### 6. Format and Present

**Format Options**:
- **Markdown**: Clean, readable, easy to copy
- **Plain Text**: ATS-optimized, safe for all systems
- **Tips for Word/PDF**: Provide formatting guidance

**Resume Structure Guidelines**:
- Keep to 1 page for <10 years experience, 2 pages for 10+ years
- Use consistent formatting and spacing
- Ensure contact information is prominent
- Use reverse chronological order (most recent first)
- Maintain clean, scannable layout with white space

### 7. Provide Strategic Recommendations

After presenting the tailored resume, offer:

**Strengths Analysis**:
- What makes this candidate competitive
- Unique qualifications to emphasize in cover letter or interview

**Gap Analysis**:
- Requirements not fully met
- Suggestions for addressing gaps (courses, projects, reframing experience)

**Interview Preparation Tips**:
- Key talking points aligned with resume
- Stories to prepare based on job requirements
- Questions to ask that demonstrate fit

**Cover Letter Hooks**:
- Suggest 2-3 opening lines for cover letter
- Key achievements to expand upon

### 8. Iterate and Refine

Ask if user wants to:
- Adjust emphasis or tone
- Add or remove sections
- Generate alternative versions for different roles
- Create format variations (traditional vs. modern)
- Develop role-specific versions (if applying to multiple similar positions)

### 9. Best Practices to Follow

**Do**:
- Be truthful and accurate - never fabricate experience
- Use industry-standard terminology
- Quantify achievements with specific metrics
- Tailor each resume to specific job
- Proofread for grammar and consistency
- Keep language concise and impactful

**Don't**:
- Include personal information (age, marital status, photo unless requested)
- Use first-person pronouns (I, me, my)
- Include references ("available upon request" is outdated)
- List every job if career is 20+ years (focus on relevant, recent experience)
- Use generic templates without customization
- Exceed 2 pages unless very senior role

### 10. Special Considerations

**Career Changers**:
- Use functional or hybrid resume format
- Emphasize transferable skills
- Create compelling narrative in summary
- Focus on relevant projects and coursework

**Recent Graduates**:
- Lead with education
- Include relevant coursework, projects, internships
- Emphasize leadership in student organizations
- Include GPA if 3.5+

**Senior Executives**:
- Lead with executive summary
- Focus on leadership and strategic impact
- Include board memberships, speaking engagements
- Emphasize revenue growth, team building, vision

**Technical Roles**:
- Include technical skills section prominently
- List programming languages, frameworks, tools
- Include GitHub, portfolio, or project links
- Mention methodologies (Agile, Scrum, etc.)

**Creative Roles**:
- Include link to portfolio
- Highlight creative achievements and campaigns
- Mention tools and software proficiencies
- Consider more creative formatting (while maintaining ATS compatibility)

---

## Tips for Best Results

- **Be specific**: Provide complete job descriptions and detailed background information
- **Share metrics**: Include numbers, percentages, and quantifiable achievements when describing your experience
- **Indicate format preference**: Let the skill know if you need ATS-optimized, creative, or traditional format
- **Mention constraints**: Share any specific requirements (page limits, sections to include/exclude)
- **Iterate**: Don't hesitate to ask for revisions or alternative approaches
- **Multiple applications**: Generate separate tailored versions for different roles

## Privacy Note

This skill processes your personal and professional information to generate tailored resumes. Always review the output before submitting to ensure accuracy and appropriateness. Remove or modify any information you prefer not to share with potential employers.

---

## Skill: `theme-factory`

---
name: theme-factory
description: Toolkit for styling artifacts with a theme. These artifacts can be slides, docs, reportings, HTML landing pages, etc. There are 10 pre-set themes with colors/fonts that you can apply to any artifact that has been creating, or can generate a new theme on-the-fly.
license: Complete terms in LICENSE.txt
---


# Theme Factory Skill

This skill provides a curated collection of professional font and color themes themes, each with carefully selected color palettes and font pairings. Once a theme is chosen, it can be applied to any artifact.

## Purpose

To apply consistent, professional styling to presentation slide decks, use this skill. Each theme includes:
- A cohesive color palette with hex codes
- Complementary font pairings for headers and body text
- A distinct visual identity suitable for different contexts and audiences

## Usage Instructions

To apply styling to a slide deck or other artifact:

1. **Show the theme showcase**: Display the `theme-showcase.pdf` file to allow users to see all available themes visually. Do not make any modifications to it; simply show the file for viewing.
2. **Ask for their choice**: Ask which theme to apply to the deck
3. **Wait for selection**: Get explicit confirmation about the chosen theme
4. **Apply the theme**: Once a theme has been chosen, apply the selected theme's colors and fonts to the deck/artifact

## Themes Available

The following 10 themes are available, each showcased in `theme-showcase.pdf`:

1. **Ocean Depths** - Professional and calming maritime theme
2. **Sunset Boulevard** - Warm and vibrant sunset colors
3. **Forest Canopy** - Natural and grounded earth tones
4. **Modern Minimalist** - Clean and contemporary grayscale
5. **Golden Hour** - Rich and warm autumnal palette
6. **Arctic Frost** - Cool and crisp winter-inspired theme
7. **Desert Rose** - Soft and sophisticated dusty tones
8. **Tech Innovation** - Bold and modern tech aesthetic
9. **Botanical Garden** - Fresh and organic garden colors
10. **Midnight Galaxy** - Dramatic and cosmic deep tones

## Theme Details

Each theme is defined in the `themes/` directory with complete specifications including:
- Cohesive color palette with hex codes
- Complementary font pairings for headers and body text
- Distinct visual identity suitable for different contexts and audiences

## Application Process

After a preferred theme is selected:
1. Read the corresponding theme file from the `themes/` directory
2. Apply the specified colors and fonts consistently throughout the deck
3. Ensure proper contrast and readability
4. Maintain the theme's visual identity across all slides

## Create your Own Theme
To handle cases where none of the existing themes work for an artifact, create a custom theme. Based on provided inputs, generate a new theme similar to the ones above. Give the theme a similar name describing what the font/color combinations represent. Use any basic description provided to choose appropriate colors/fonts. After generating the theme, show it for review and verification. Following that, apply the theme as described above.

---

## Skill: `twitter-algorithm-optimizer`

---
name: twitter-algorithm-optimizer
description: Analyze and optimize tweets for maximum reach using Twitter's open-source algorithm insights. Rewrite and edit user tweets to improve engagement and visibility based on how the recommendation system ranks content.
license: AGPL-3.0 (referencing Twitter's algorithm source)
---

# Twitter Algorithm Optimizer

## When to Use This Skill

Use this skill when you need to:
- **Optimize tweet drafts** for maximum reach and engagement
- **Understand why** a tweet might not perform well algorithmically
- **Rewrite tweets** to align with Twitter's ranking mechanisms
- **Improve content strategy** based on the actual ranking algorithms
- **Debug underperforming content** and increase visibility
- **Maximize engagement signals** that Twitter's algorithms track

## What This Skill Does

1. **Analyzes tweets** against Twitter's core recommendation algorithms
2. **Identifies optimization opportunities** based on engagement signals
3. **Rewrites and edits tweets** to improve algorithmic ranking
4. **Explains the "why"** behind recommendations using algorithm insights
5. **Applies Real-graph, SimClusters, and TwHIN principles** to content strategy
6. **Provides engagement-boosting tactics** grounded in Twitter's actual systems

## How It Works: Twitter's Algorithm Architecture

Twitter's recommendation system uses multiple interconnected models:

### Core Ranking Models

**Real-graph**: Predicts interaction likelihood between users
- Determines if your followers will engage with your content
- Affects how widely Twitter shows your tweet to others
- Key signal: Will followers like, reply, or retweet this?

**SimClusters**: Community detection with sparse embeddings
- Identifies communities of users with similar interests
- Determines if your tweet resonates within specific communities
- Key strategy: Make content that appeals to tight communities who will engage

**TwHIN**: Knowledge graph embeddings for users and posts
- Maps relationships between users and content topics
- Helps Twitter understand if your tweet fits your follower interests
- Key strategy: Stay in your niche or clearly signal topic shifts

**Tweepcred**: User reputation/authority scoring
- Higher-credibility users get more distribution
- Your past engagement history affects current tweet reach
- Key strategy: Build reputation through consistent engagement

### Engagement Signals Tracked

Twitter's **Unified User Actions** service tracks both explicit and implicit signals:

**Explicit Signals** (high weight):
- Likes (direct positive signal)
- Replies (indicates valuable content worth discussing)
- Retweets (strongest signal - users want to share it)
- Quote tweets (engaged discussion)

**Implicit Signals** (also weighted):
- Profile visits (curiosity about the author)
- Clicks/link clicks (content deemed useful enough to explore)
- Time spent (users reading/considering your tweet)
- Saves/bookmarks (plan to return later)

**Negative Signals**:
- Block/report (Twitter penalizes this heavily)
- Mute/unfollow (person doesn't want your content)
- Skip/scroll past quickly (low engagement)

### The Feed Generation Process

Your tweet reaches users through this pipeline:

1. **Candidate Retrieval** - Multiple sources find candidate tweets:
   - Search Index (relevant keyword matches)
   - UTEG (timeline engagement graph - following relationships)
   - Tweet-mixer (trending/viral content)

2. **Ranking** - ML models rank candidates by predicted engagement:
   - Will THIS user engage with THIS tweet?
   - How quickly will engagement happen?
   - Will it spread to non-followers?

3. **Filtering** - Remove blocked content, apply preferences

4. **Delivery** - Show ranked feed to user

## Optimization Strategies Based on Algorithm Insights

### 1. Maximize Real-graph (Follower Engagement)

**Strategy**: Make content your followers WILL engage with

- **Know your audience**: Reference topics they care about
- **Ask questions**: Direct questions get more replies than statements
- **Create controversy (safely)**: Debate attracts engagement (but avoid blocks/reports)
- **Tag related creators**: Increases visibility through networks
- **Post when followers are active**: Better early engagement means better ranking

**Example Optimization**:
- ❌ "I think climate policy is important"
- ✅ "Hot take: Current climate policy ignores nuclear energy. Thoughts?" (triggers replies)

### 2. Leverage SimClusters (Community Resonance)

**Strategy**: Find and serve tight communities deeply interested in your topic

- **Pick ONE clear topic**: Don't confuse the algorithm with mixed messages
- **Use community language**: Reference shared memes, inside jokes, terminology
- **Provide value to the niche**: Be genuinely useful to that specific community
- **Encourage community-to-community sharing**: Quotes that spark discussion
- **Build in your lane**: Consistency helps algorithm understand your topic

**Example Optimization**:
- ❌ "I use many programming languages"
- ✅ "Rust's ownership system is the most underrated feature. Here's why..." (targets specific dev community)

### 3. Improve TwHIN Mapping (Content-User Fit)

**Strategy**: Make your content clearly relevant to your established identity

- **Signal your expertise**: Lead with domain knowledge
- **Consistency matters**: Stay in your lanes (or clearly announce a new direction)
- **Use specific terminology**: Helps algorithm categorize you correctly
- **Reference your past wins**: "Following up on my tweet about X..."
- **Build topical authority**: Multiple tweets on same topic strengthen the connection

**Example Optimization**:
- ❌ "I like lots of things" (vague, confuses algorithm)
- ✅ "My 3rd consecutive framework review as a full-stack engineer" (establishes authority)

### 4. Boost Tweepcred (Authority/Credibility)

**Strategy**: Build reputation through engagement consistency

- **Reply to top creators**: Interaction with high-credibility accounts boosts visibility
- **Quote interesting tweets**: Adds value and signals engagement
- **Avoid engagement bait**: Doesn't build real credibility
- **Be consistent**: Regular quality posting beats sporadic viral attempts
- **Engage deeply**: Quality replies and discussions matter more than volume

**Example Optimization**:
- ❌ "RETWEET IF..." (engagement bait, damages credibility over time)
- ✅ "Thoughtful critique of the approach in [linked tweet]" (builds authority)

### 5. Maximize Engagement Signals

**Explicit Signal Triggers**:

**For Likes**:
- Novel insights or memorable phrasing
- Validation of audience beliefs
- Useful/actionable information
- Strong opinions with supporting evidence

**For Replies**:
- Ask a direct question
- Create a debate
- Request opinions
- Share incomplete thoughts (invites completion)

**For Retweets**:
- Useful information people want to share
- Representational value (tweet speaks for them)
- Entertainment that entertains their followers
- Information advantage (breaking news first)

**For Bookmarks/Saves**:
- Tutorials or how-tos
- Data/statistics they'll reference later
- Inspiration or motivation
- Jokes/entertainment they'll want to see again

**Example Optimization**:
- ❌ "Check out this tool" (passive)
- ✅ "This tool saved me 5 hours this week. Here's how to set it up..." (actionable, retweet-worthy)

### 6. Prevent Negative Signals

**Avoid**:
- Inflammatory content likely to be reported
- Targeted harassment (gets algorithmic penalty)
- Misleading/false claims (damages credibility)
- Off-brand pivots (confuses the algorithm)
- Reply-guy syndrome (too many low-value replies)

## How to Optimize Your Tweets

### Step 1: Identify the Core Message
- What's the single most important thing this tweet communicates?
- Who should care about this?
- What action/engagement do you want?

### Step 2: Map to Algorithm Strategy
- Which Real-graph follower segment will engage? (Followers who care about X)
- Which SimCluster community? (Niche interested in Y)
- How does this fit your TwHIN identity? (Your established expertise)
- Does this boost or hurt Tweepcred?

### Step 3: Optimize for Signals
- Does it trigger replies? (Ask a question, create debate)
- Is it retweet-worthy? (Usefulness, entertainment, representational value)
- Will followers like it? (Novel, validating, actionable)
- Could it go viral? (Community resonance + network effects)

### Step 4: Check Against Negatives
- Any blocks/reports risk?
- Any confusion about your identity?
- Any engagement bait that damages credibility?
- Any inflammatory language that hurts Tweepcred?

## Example Optimizations

### Example 1: Developer Tweet

**Original**:
> "I fixed a bug today"

**Algorithm Analysis**:
- No clear audience - too generic
- No engagement signals - statements don't trigger replies
- No Real-graph trigger - followers won't engage strongly
- No SimCluster resonance - could apply to any developer

**Optimized**:
> "Spent 2 hours debugging, turned out I was missing one semicolon. The best part? The linter didn't catch it.
>
> What's your most embarrassing bug? Drop it in replies 👇"

**Why It Works**:
- SimCluster trigger: Specific developer community
- Real-graph trigger: Direct question invites replies
- Tweepcred: Relatable vulnerability builds connection
- Engagement: Likely replies (others share embarrassing bugs)

### Example 2: Product Launch Tweet

**Original**:
> "We launched a new feature today. Check it out."

**Algorithm Analysis**:
- Passive voice - doesn't indicate impact
- No specific benefit - followers don't know why to care
- No community resonance - generic
- Engagement bait risk if it feels like self-promotion

**Optimized**:
> "Spent 6 months on the one feature our users asked for most: export to PDF.
>
> 10x improvement in report generation time. Already live.
>
> What export format do you want next?"

**Why It Works**:
- Real-graph: Followers in your product space will engage
- Specificity: "PDF export" + "10x improvement" triggers bookmarks (useful info)
- Question: Ends with engagement trigger
- Authority: You spent 6 months (shows credibility)
- SimCluster: Product management/SaaS community resonates

### Example 3: Opinion Tweet

**Original**:
> "I think remote work is better than office work"

**Algorithm Analysis**:
- Vague opinion - doesn't invite engagement
- Could be debated either way - no clear position
- No Real-graph hooks - followers unclear if they should care
- Generic topic - dilutes your personal brand

**Optimized**:
> "Hot take: remote work works great for async tasks but kills creative collaboration.
>
> We're now hybrid: deep focus days remote, collab days in office.
>
> What's your team's balance? Genuinely curious what works."

**Why It Works**:
- Clear position: Not absolutes, nuanced stance
- Debate trigger: "Hot take" signals discussion opportunity
- Question: Direct engagement request
- Real-graph: Followers in your industry will have opinions
- SimCluster: CTOs, team leads, engineering managers will relate
- Tweepcred: Nuanced thinking builds authority

## Best Practices for Algorithm Optimization

1. **Quality Over Virality**: Consistent engagement from your community beats occasional viral moments
2. **Community First**: Deep resonance with 100 engaged followers beats shallow reach to 10,000
3. **Authenticity Matters**: The algorithm rewards genuine engagement, not manipulation
4. **Timing Helps**: Engage early when tweet is fresh (first hour critical)
5. **Build Threads**: Threaded tweets often get more engagement than single tweets
6. **Follow Up**: Reply to replies quickly - Twitter's algorithm favors active conversation
7. **Avoid Spam**: Engagement pods and bots hurt long-term credibility
8. **Track Your Performance**: Notice what YOUR audience engages with and iterate

## Common Pitfalls to Avoid

- **Generic statements**: Doesn't trigger algorithm (too vague)
- **Pure engagement bait**: "Like if you agree" - hurts credibility long-term
- **Unclear audience**: Who should care? If unclear, algorithm won't push it far
- **Off-brand pivots**: Confuses algorithm about your identity
- **Over-frequency**: Spamming hurts engagement rate metrics
- **Toxicity**: Blocks/reports heavily penalize future reach
- **No calls to action**: Passive tweets underperform

## When to Ask for Algorithm Optimization

Use this skill when:
- You've drafted a tweet and want to maximize reach
- A tweet underperformed and you want to understand why
- You're launching important content and want algorithm advantage
- You're building audience in a specific niche
- You want to become known for something specific
- You're debugging inconsistent engagement rates

Use Claude without this skill for:
- General writing and grammar fixes
- Tone adjustments not related to algorithm
- Off-Twitter content (LinkedIn, Medium, blogs, etc.)
- Personal conversations and casual tweets

---

## Skill: `video-downloader`

---
name: youtube-downloader
description: Download YouTube videos with customizable quality and format options. Use this skill when the user asks to download, save, or grab YouTube videos. Supports various quality settings (best, 1080p, 720p, 480p, 360p), multiple formats (mp4, webm, mkv), and audio-only downloads as MP3.
---

# YouTube Video Downloader

Download YouTube videos with full control over quality and format settings.

## Quick Start

The simplest way to download a video:

```bash
python scripts/download_video.py "https://www.youtube.com/watch?v=VIDEO_ID"
```

This downloads the video in best available quality as MP4 to `/mnt/user-data/outputs/`.

## Options

### Quality Settings

Use `-q` or `--quality` to specify video quality:

- `best` (default): Highest quality available
- `1080p`: Full HD
- `720p`: HD
- `480p`: Standard definition
- `360p`: Lower quality
- `worst`: Lowest quality available

Example:
```bash
python scripts/download_video.py "URL" -q 720p
```

### Format Options

Use `-f` or `--format` to specify output format (video downloads only):

- `mp4` (default): Most compatible
- `webm`: Modern format
- `mkv`: Matroska container

Example:
```bash
python scripts/download_video.py "URL" -f webm
```

### Audio Only

Use `-a` or `--audio-only` to download only audio as MP3:

```bash
python scripts/download_video.py "URL" -a
```

### Custom Output Directory

Use `-o` or `--output` to specify a different output directory:

```bash
python scripts/download_video.py "URL" -o /path/to/directory
```

## Complete Examples

1. Download video in 1080p as MP4:
```bash
python scripts/download_video.py "https://www.youtube.com/watch?v=dQw4w9WgXcQ" -q 1080p
```

2. Download audio only as MP3:
```bash
python scripts/download_video.py "https://www.youtube.com/watch?v=dQw4w9WgXcQ" -a
```

3. Download in 720p as WebM to custom directory:
```bash
python scripts/download_video.py "https://www.youtube.com/watch?v=dQw4w9WgXcQ" -q 720p -f webm -o /custom/path
```

## How It Works

The skill uses `yt-dlp`, a robust YouTube downloader that:
- Automatically installs itself if not present
- Fetches video information before downloading
- Selects the best available streams matching your criteria
- Merges video and audio streams when needed
- Supports a wide range of YouTube video formats

## Important Notes

- Downloads are saved to `/mnt/user-data/outputs/` by default
- Video filename is automatically generated from the video title
- The script handles installation of yt-dlp automatically
- Only single videos are downloaded (playlists are skipped by default)
- Higher quality videos may take longer to download and use more disk space

---

## Skill: `webapp-testing`

---
name: webapp-testing
description: Toolkit for interacting with and testing local web applications using Playwright. Supports verifying frontend functionality, debugging UI behavior, capturing browser screenshots, and viewing browser logs.
license: Complete terms in LICENSE.txt
---

# Web Application Testing

To test local web applications, write native Python Playwright scripts.

**Helper Scripts Available**:
- `scripts/with_server.py` - Manages server lifecycle (supports multiple servers)

**Always run scripts with `--help` first** to see usage. DO NOT read the source until you try running the script first and find that a customized solution is abslutely necessary. These scripts can be very large and thus pollute your context window. They exist to be called directly as black-box scripts rather than ingested into your context window.

## Decision Tree: Choosing Your Approach

```
User task → Is it static HTML?
    ├─ Yes → Read HTML file directly to identify selectors
    │         ├─ Success → Write Playwright script using selectors
    │         └─ Fails/Incomplete → Treat as dynamic (below)
    │
    └─ No (dynamic webapp) → Is the server already running?
        ├─ No → Run: python scripts/with_server.py --help
        │        Then use the helper + write simplified Playwright script
        │
        └─ Yes → Reconnaissance-then-action:
            1. Navigate and wait for networkidle
            2. Take screenshot or inspect DOM
            3. Identify selectors from rendered state
            4. Execute actions with discovered selectors
```

## Example: Using with_server.py

To start a server, run `--help` first, then use the helper:

**Single server:**
```bash
python scripts/with_server.py --server "npm run dev" --port 5173 -- python your_automation.py
```

**Multiple servers (e.g., backend + frontend):**
```bash
python scripts/with_server.py \
  --server "cd backend && python server.py" --port 3000 \
  --server "cd frontend && npm run dev" --port 5173 \
  -- python your_automation.py
```

To create an automation script, include only Playwright logic (servers are managed automatically):
```python
from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=True) # Always launch chromium in headless mode
    page = browser.new_page()
    page.goto('http://localhost:5173') # Server already running and ready
    page.wait_for_load_state('networkidle') # CRITICAL: Wait for JS to execute
    # ... your automation logic
    browser.close()
```

## Reconnaissance-Then-Action Pattern

1. **Inspect rendered DOM**:
   ```python
   page.screenshot(path='/tmp/inspect.png', full_page=True)
   content = page.content()
   page.locator('button').all()
   ```

2. **Identify selectors** from inspection results

3. **Execute actions** using discovered selectors

## Common Pitfall

❌ **Don't** inspect the DOM before waiting for `networkidle` on dynamic apps
✅ **Do** wait for `page.wait_for_load_state('networkidle')` before inspection

## Best Practices

- **Use bundled scripts as black boxes** - To accomplish a task, consider whether one of the scripts available in `scripts/` can help. These scripts handle common, complex workflows reliably without cluttering the context window. Use `--help` to see usage, then invoke directly. 
- Use `sync_playwright()` for synchronous scripts
- Always close the browser when done
- Use descriptive selectors: `text=`, `role=`, CSS selectors, or IDs
- Add appropriate waits: `page.wait_for_selector()` or `page.wait_for_timeout()`

## Reference Files

- **examples/** - Examples showing common patterns:
  - `element_discovery.py` - Discovering buttons, links, and inputs on a page
  - `static_html_automation.py` - Using file:// URLs for local HTML
  - `console_logging.py` - Capturing console logs during automation

---
