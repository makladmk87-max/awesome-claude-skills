# Skills: Figma Integration

This file contains 5 skill(s) for the **Figma Integration** category.
Follow the relevant skill's instructions when the user's request matches.

---

## Skill: `figma-code-connect`

---
name: figma-code-connect
description: Set up and manage Figma Code Connect — link Figma components to real code components so devs see actual code snippets in Figma Dev Mode. Use this skill when the user wants to connect their Figma design system to their React/other framework component library using Figma's Code Connect feature.
---

# Figma: Code Connect

Link Figma components to real code components using Figma Code Connect.

## What is Code Connect?

Figma Code Connect maps Figma design components to their code implementations. When developers inspect a component in Figma Dev Mode, they see real code snippets from the actual codebase instead of generated CSS.

## Prerequisites

- Figma account with Dev Mode access
- Node.js project with a component library
- Figma personal access token

## Installation

```bash
npm install --save-dev @figma/code-connect
# or
npx figma connect
```

## Setup

### 1. Authenticate

```bash
npx figma connect login
# Enter your Figma personal access token when prompted
# Token: https://www.figma.com/settings → Personal access tokens
```

Or set via environment variable:
```bash
export FIGMA_ACCESS_TOKEN=figd_...
```

### 2. Initialize

```bash
npx figma connect create
```

This creates a `figma.config.json`:
```json
{
  "codeConnect": {
    "include": ["src/**/*.figma.tsx"],
    "exclude": ["node_modules/**"]
  }
}
```

## Creating Code Connect Files

For each Figma component, create a `.figma.tsx` (or `.figma.ts`) file:

### Basic Example — Button

```tsx
// src/components/Button/Button.figma.tsx
import figma from '@figma/code-connect'
import { Button } from './Button'

figma.connect(Button, 'https://www.figma.com/design/FILE_ID/DESIGN_NAME?node-id=COMPONENT_NODE_ID', {
  props: {
    variant: figma.enum('Variant', {
      Default: 'default',
      Primary: 'primary',
      Destructive: 'destructive',
    }),
    size: figma.enum('Size', {
      Small: 'sm',
      Medium: 'md',
      Large: 'lg',
    }),
    disabled: figma.boolean('Disabled'),
    label: figma.string('Label'),
  },
  example: ({ variant, size, disabled, label }) => (
    <Button variant={variant} size={size} disabled={disabled}>
      {label}
    </Button>
  ),
})
```

### Input Component Example

```tsx
import figma from '@figma/code-connect'
import { Input } from './Input'

figma.connect(Input, 'FIGMA_URL?node-id=NODE_ID', {
  props: {
    placeholder: figma.string('Placeholder'),
    disabled: figma.boolean('Disabled'),
    error: figma.boolean('Error'),
  },
  example: ({ placeholder, disabled, error }) => (
    <Input
      placeholder={placeholder}
      disabled={disabled}
      className={error ? 'input-error' : ''}
    />
  ),
})
```

## Figma URL Format

Get the component URL from Figma:
1. Open Figma file
2. Right-click the component in the canvas
3. "Copy link to selection"
4. URL format: `https://www.figma.com/design/FILE_ID/NAME?node-id=X-Y`

## Publishing Code Connect

```bash
# Preview what will be published
npx figma connect publish --dry-run

# Publish to Figma
npx figma connect publish
```

## Prop Mappers Reference

| Figma Prop Type | Code Connect Mapper |
|----------------|---------------------|
| Enum/Variant | `figma.enum('Prop Name', { FigmaOption: 'codeValue' })` |
| Boolean | `figma.boolean('Prop Name')` |
| String | `figma.string('Prop Name')` |
| Number | `figma.number('Prop Name')` |
| Instance swap | `figma.instance('Prop Name')` |
| Nested instance | `figma.nestedProps('Layer Name', { ... })` |

## CI Integration

Add to CI pipeline to keep Code Connect up to date:
```yaml
# .github/workflows/figma-code-connect.yml
- name: Publish Code Connect
  run: npx figma connect publish
  env:
    FIGMA_ACCESS_TOKEN: ${{ secrets.FIGMA_ACCESS_TOKEN }}
```

## Process for Connecting a Component Library

1. Get component node IDs from Figma (right-click → copy link)
2. Create `.figma.tsx` file for each component
3. Map Figma property names to code prop names
4. Write the `example` render function
5. Run `npx figma connect publish --dry-run` to verify
6. Run `npx figma connect publish` to push live

## Notes

- Component node IDs change if components are moved between files
- Keep `.figma.tsx` files co-located with their components
- Test locally with `--dry-run` before publishing
- Figma Dev Mode must be enabled on the file to see Code Connect snippets

---

## Skill: `figma-code-connect-components`

---
name: figma:code-connect-components
description: Connects Figma design components to code components using Code Connect. Creates mappings between Figma designs and code implementations so design tools show the real code.
---

## figma:code-connect-components
**Category:** Figma

**What it does:**
Connects Figma design components to code components using Code Connect. Creates mappings between Figma designs and code implementations so design tools show the real code.

**When to trigger:**
- "Code connect this component"
- "Connect Figma to code"
- "Map this component to code"
- "Create code connect mapping"

**How to install:**
```bash
npx claude install figma
```
Also requires the **Figma MCP server** connected.

**Trigger phrase:** Ask to connect or map a Figma component to its code equivalent.

---

## Skill: `figma-create-design-system-rules`

---
name: figma:create-design-system-rules
description: Generates custom design system rules for your codebase. Establishes project-specific conventions for Figma-to-code workflows — tokens, component naming, spacing scales, etc.
---

## figma:create-design-system-rules
**Category:** Figma

**What it does:**
Generates custom design system rules for your codebase. Establishes project-specific conventions for Figma-to-code workflows — tokens, component naming, spacing scales, etc.

**When to trigger:**
- "Create design system rules"
- "Generate rules for my project"
- "Set up design rules"
- "Customize design system guidelines"

**How to install:**
```bash
npx claude install figma
```
Also requires the **Figma MCP server** connected.

**Trigger phrase:** Ask Claude to generate or set up design system rules for your project.

---

## Skill: `figma-design-system-rules`

---
name: figma-design-system-rules
description: Extract, document, and enforce design system rules from a Figma design system. Use this skill when the user wants to document their design system, create design tokens, establish component usage rules, or ensure code follows a Figma design system.
---

# Figma: Design System Rules

Extract and document design system rules from Figma for use in code implementation.

## When to Use

Use when the user:
- Wants to document their Figma design system for developers
- Needs to create a design tokens file from Figma specs
- Wants rules for how components should be used
- Is setting up a new codebase to match an existing Figma design system

## Design System Components to Document

### 1. Color Tokens

Extract all color styles from Figma:

```ts
// design-tokens/colors.ts
export const colors = {
  // Brand
  primary: {
    50: '#EFF6FF',
    100: '#DBEAFE',
    500: '#3B82F6',
    600: '#2563EB',
    700: '#1D4ED8',
  },
  // Semantic
  text: {
    primary: '#111827',
    secondary: '#6B7280',
    disabled: '#D1D5DB',
  },
  background: {
    default: '#FFFFFF',
    subtle: '#F9FAFB',
    muted: '#F3F4F6',
  },
  status: {
    success: '#10B981',
    warning: '#F59E0B',
    error: '#EF4444',
    info: '#3B82F6',
  },
} as const;
```

### 2. Typography Tokens

```ts
export const typography = {
  fonts: {
    heading: '"Inter", system-ui, sans-serif',
    body: '"Inter", system-ui, sans-serif',
    mono: '"JetBrains Mono", monospace',
  },
  sizes: {
    xs: '0.75rem',    // 12px
    sm: '0.875rem',   // 14px
    base: '1rem',     // 16px
    lg: '1.125rem',   // 18px
    xl: '1.25rem',    // 20px
    '2xl': '1.5rem',  // 24px
    '3xl': '1.875rem',// 30px
    '4xl': '2.25rem', // 36px
  },
  weights: {
    normal: 400,
    medium: 500,
    semibold: 600,
    bold: 700,
  },
  lineHeights: {
    tight: 1.25,
    normal: 1.5,
    relaxed: 1.75,
  },
} as const;
```

### 3. Spacing Scale

```ts
export const spacing = {
  0: '0',
  1: '4px',
  2: '8px',
  3: '12px',
  4: '16px',
  5: '20px',
  6: '24px',
  8: '32px',
  10: '40px',
  12: '48px',
  16: '64px',
  20: '80px',
  24: '96px',
} as const;
```

### 4. Border Radius

```ts
export const radius = {
  none: '0',
  sm: '4px',
  md: '8px',
  lg: '12px',
  xl: '16px',
  '2xl': '24px',
  full: '9999px',
} as const;
```

### 5. Shadows

```ts
export const shadows = {
  sm: '0 1px 2px 0 rgba(0, 0, 0, 0.05)',
  md: '0 4px 6px -1px rgba(0, 0, 0, 0.1)',
  lg: '0 10px 15px -3px rgba(0, 0, 0, 0.1)',
  xl: '0 20px 25px -5px rgba(0, 0, 0, 0.1)',
} as const;
```

### 6. Breakpoints

```ts
export const breakpoints = {
  sm: '640px',
  md: '768px',
  lg: '1024px',
  xl: '1280px',
  '2xl': '1536px',
} as const;
```

## Component Usage Rules

For each component in the design system, document:

### Component Rule Template
```md
## [ComponentName]

**Usage:** When to use this component
**Don't use when:** When NOT to use this component

### Variants
- `default` — Standard usage
- `primary` — Main CTA
- `destructive` — Dangerous actions

### Sizes
- `sm` — Compact layouts
- `md` — Default
- `lg` — Hero sections

### States
- `default`, `hover`, `focus`, `disabled`, `loading`

### Dos and Don'ts
✅ Do: [correct usage]
❌ Don't: [incorrect usage]
```

## CSS Custom Properties Export

For use in CSS/Tailwind projects:
```css
:root {
  /* Colors */
  --color-primary: #2563EB;
  --color-primary-light: #DBEAFE;
  --color-text: #111827;
  --color-text-muted: #6B7280;
  --color-bg: #FFFFFF;
  --color-bg-subtle: #F9FAFB;

  /* Typography */
  --font-sans: 'Inter', system-ui, sans-serif;
  --text-sm: 0.875rem;
  --text-base: 1rem;
  --text-lg: 1.125rem;

  /* Spacing */
  --space-4: 1rem;
  --space-8: 2rem;

  /* Radius */
  --radius-md: 0.5rem;
  --radius-lg: 0.75rem;

  /* Shadows */
  --shadow-md: 0 4px 6px -1px rgba(0, 0, 0, 0.1);
}
```

## Notes

- Ask the user to share Figma design system pages, color styles, and text styles
- Create tokens as a single source of truth — import everywhere
- Document rules that are NOT obvious from the tokens (e.g., "never use red for non-error states")
- For Tailwind projects, translate tokens into `tailwind.config.js` theme extensions

---

## Skill: `figma-implement-design`

---
name: figma-implement-design
description: Implement a Figma design as production-ready frontend code. Use this skill when the user shares a Figma design link or screenshot and wants it converted to HTML/CSS, React, or another frontend framework.
---

# Figma: Implement Design

Convert a Figma design into production-ready frontend code.

## When to Use

Use when the user:
- Shares a Figma link or screenshot and asks to "implement this"
- Says "build this design" / "code this mockup"
- Wants to convert a visual design to working code

## Process

### Step 1: Gather Design Information

The user must provide one of:
- **Figma URL**: `https://www.figma.com/design/...` or `https://www.figma.com/file/...`
- **Screenshot/image**: Visual of the design to implement
- **Figma Dev Mode export**: CSS properties, component specs

If only a URL is provided and no Figma MCP is configured, ask the user to:
1. Open Figma Dev Mode (Shift+D or bottom bar → Dev)
2. Share relevant CSS properties, spacing values, colors, and font specs
3. Export relevant assets (icons, images)

### Step 2: Extract Design Tokens

Before coding, identify and document:
- **Colors**: Background, text, border, accent colors (as hex/rgb)
- **Typography**: Font family, sizes, weights, line heights
- **Spacing**: Padding, margin, gap values
- **Border radius**: Corner radius values
- **Shadows**: Box shadow values
- **Breakpoints**: Responsive design specs if provided

Example CSS variables to set up:
```css
:root {
  --color-primary: #2563EB;
  --color-text: #1F2937;
  --color-bg: #F9FAFB;
  --font-heading: 'Inter', sans-serif;
  --radius-md: 8px;
  --spacing-md: 16px;
}
```

### Step 3: Identify Components

Break the design into reusable components:
- Identify repeated UI patterns
- Define component hierarchy (what contains what)
- Note interactive states: hover, active, focus, disabled

### Step 4: Implement

Implement using the stack the user specifies. Defaults:
- **No preference**: HTML + CSS (no framework)
- **React asked**: React with CSS modules or Tailwind
- **Vue asked**: Vue 3 SFCs
- **Tailwind available**: Use Tailwind utility classes

**Implementation priorities:**
1. Layout (flexbox/grid structure matches design)
2. Typography (font, size, weight, color)
3. Colors and backgrounds
4. Spacing (padding, margin, gaps)
5. Border radius and shadows
6. Hover/interactive states
7. Responsive behavior

### Step 5: Asset Handling

For images and icons:
- Use placeholder images if real assets aren't provided: `https://placehold.co/400x300`
- For icons: use Lucide React, Heroicons, or inline SVG
- Note which assets need to be replaced with real ones

## Code Quality Standards

- Semantic HTML (`<header>`, `<nav>`, `<main>`, `<section>`, `<button>`, not `<div>` for everything)
- Accessible (ARIA labels on interactive elements, alt text on images)
- Responsive (mobile-first or explicit breakpoints)
- Pixel-accurate where possible (spacing, sizing matching design)

## When Design is Partial or Unclear

If parts of the design are unclear:
- Make reasonable assumptions and note them
- Comment `/* TODO: Confirm with designer */` for uncertain parts
- Ask about critical ambiguities (interactions, responsive behavior)

## Notes

- Without Figma MCP integration, implement from screenshots or exported specs
- Always match the design's aesthetic intent, not just layout
- For complex designs, implement the most visible/important section first and iterate
- Use the `frontend-design` skill for creative freedom; use this skill when fidelity to a specific design is the goal

---
