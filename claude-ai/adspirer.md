# Skills: Adspirer — Ads & Marketing

This file contains 4 skill(s) for the **Adspirer — Ads & Marketing** category.
Follow the relevant skill's instructions when the user's request matches.

---

## Skill: `adspirer`

---
name: adspirer
description: Manage Google Ads and Meta (Facebook/Instagram) advertising campaigns — create, analyze, and optimize ads. Use this skill when the user wants to work with Google Ads or Meta Ads: creating campaigns, analyzing performance, writing ad copy, optimizing budgets, or troubleshooting ad issues.
---

# Adspirer — Google & Meta Ads Management

Manage and optimize Google Ads and Meta Ads campaigns.

## Capabilities

- Analyze campaign performance and surface insights
- Write high-converting ad copy (headlines, descriptions, CTAs)
- Recommend targeting, bidding, and budget strategies
- Diagnose underperforming campaigns
- Build campaign structures for new products/promotions
- Interpret ad metrics and suggest optimizations

## Key Metrics Reference

### Google Ads
| Metric | Good benchmark |
|--------|---------------|
| CTR (Search) | > 3-5% |
| CTR (Display) | > 0.35% |
| Quality Score | 7-10 |
| Conversion Rate | Varies by industry; compare vs account average |
| ROAS | Depends on margins; typically target > 3x |
| CPA | Below target CPA set for campaign |

### Meta Ads
| Metric | Good benchmark |
|--------|---------------|
| CTR (Link) | > 1% |
| CPM | Varies by audience/placement |
| Frequency | Keep < 3-4 for conversion campaigns |
| ROAS | Target varies; compare vs blended |
| Relevance Score / Quality Ranking | Above average |

## Campaign Structure

### Google Ads
```
Account
  └── Campaign (budget, bidding, location, device targets)
        └── Ad Group (keyword/audience theme)
              ├── Keywords (match types: broad, phrase, exact)
              └── Ads (RSA, Performance Max, Display)
```

### Meta Ads
```
Account
  └── Campaign (objective: Awareness, Traffic, Conversions, etc.)
        └── Ad Set (audience, budget, schedule, placement)
              └── Ads (creative: image, video, carousel)
```

## Ad Copywriting

### Google Search Ad (RSA)
- **Headlines**: Up to 15 headlines (30 chars each) — include keyword, benefit, CTA
- **Descriptions**: Up to 4 descriptions (90 chars each) — expand on benefits, USP
- **Best practices**: Pin headline 1 to brand/keyword, use all 15 headlines

Example:
```
Headline 1: [Keyword-based] "Buy Running Shoes Online"
Headline 2: [Benefit] "Free Shipping on Orders $50+"
Headline 3: [CTA] "Shop Top Brands Today"
Headline 4: [Social proof] "50,000+ Happy Customers"

Description 1: "Discover our wide selection of running shoes from top brands. Find your perfect fit with free returns."
Description 2: "Shop Nike, Adidas, Brooks & more. Fast shipping available. Order by 3pm for same-day dispatch."
```

### Meta Ad
- **Primary text**: 125 chars visible before "See more" (key message first)
- **Headline**: 40 chars — punchy benefit or offer
- **Description**: 30 chars — supporting detail
- **CTA button**: Match to action (Shop Now, Learn More, Sign Up, etc.)

## Audience Targeting

### Google Ads
- **Search**: Keywords define audience intent — use negative keywords to exclude irrelevant traffic
- **Performance Max**: Asset-based; uses Google's signals
- **Audiences**: Remarketing, Customer Match, Similar Audiences, In-Market, Affinity

### Meta Ads
- **Core audiences**: Demographics, interests, behaviors
- **Custom audiences**: Website visitors (pixel), email lists, app users, video views
- **Lookalike audiences**: 1-10% lookalike from Custom Audience source
- **Best practice**: Start with 3-5% lookalike from buyers; narrow with interest stacking

## Optimization Workflow

When asked to optimize a campaign:

1. **Audit performance** — identify top/bottom performers at campaign, ad set, and ad level
2. **Budget allocation** — shift budget toward top performers
3. **Bid adjustments** — device, location, time-of-day adjustments
4. **Pause underperformers** — cut ad sets/ads below CPA threshold (after sufficient data)
5. **Test new creative** — if CTR low, test new headlines/images
6. **Audience refinement** — narrow or expand based on performance data
7. **Negative keywords** (Google) — review Search Terms report weekly

## Troubleshooting Common Issues

| Issue | Likely Cause | Fix |
|-------|-------------|-----|
| High CPC, low CTR | Low Quality Score / irrelevant audience | Improve ad relevance to keywords; tighten targeting |
| Good CTR, low conversions | Landing page issue | A/B test landing page; check tracking |
| Ads not delivering | Low budget, disapproved ads, narrow audience | Increase budget; fix policy issues; broaden audience |
| ROAS declining | Audience fatigue / increased competition | Refresh creative; test new audiences |
| Meta ads approved but no delivery | Audience too small, bid too low | Broaden audience; use Advantage+ placements |

## Notes for Claude

- Always ask for the user's goal before recommending (awareness vs leads vs sales vs ROAS)
- Ask for current metrics before optimization — don't recommend without data
- Budgets, bids, and targeting should be treated as hypotheses to test, not permanent decisions
- Follow platform policies — flag any creative that risks disapproval (misleading claims, restricted categories)

---

## Skill: `adspirer-ad-campaign-best-practices`

---
name: adspirer-ads-agent:ad-campaign-best-practices
description: Best practices for creating and managing ad campaigns across Google Ads, Meta Ads, LinkedIn Ads, and TikTok Ads. Covers planning, budgets, targeting, and optimization.
---

## adspirer-ads-agent:ad-campaign-best-practices
**Category:** Adspirer Ads Agent

**What it does:**
Best practices for creating and managing ad campaigns across Google Ads, Meta Ads, LinkedIn Ads, and TikTok Ads. Covers planning campaigns, setting budgets, choosing targeting, and optimizing performance.

**When to trigger:**
- Planning any paid ad campaign
- Setting budgets or targeting
- Optimizing campaign performance

**How to install:**
```bash
npx claude install adspirer-ads-agent
```

**Trigger phrase:** Ask about ad campaign strategy, budgets, or targeting on any major ad platform.

---

## Skill: `adspirer-keyword-research`

---
name: adspirer-ads-agent:keyword-research
description: Researches Google Ads keywords with real CPC data, search volumes, and competition analysis. Gives you data-driven keyword intelligence for ad campaigns.
---

## adspirer-ads-agent:keyword-research
**Category:** Adspirer Ads Agent

**What it does:**
Researches Google Ads keywords with real CPC data, search volumes, and competition analysis. Gives you data-driven keyword intelligence for ad campaigns.

**When to trigger:**
- Planning Google Ads campaigns
- Researching keywords with real cost and volume data

**How to install:**
```bash
npx claude install adspirer-ads-agent
```

**Trigger phrase:** Ask Claude to research keywords for Google Ads, or invoke `/adspirer-ads-agent:keyword-research`.

---

## Skill: `competitive-ads-extractor`

---
name: competitive-ads-extractor
description: Extracts and analyzes competitors' ads from ad libraries (Facebook, LinkedIn, etc.) to understand what messaging, problems, and creative approaches are working. Helps inspire and improve your own ad campaigns.
---

# Competitive Ads Extractor

This skill extracts your competitors' ads from ad libraries and analyzes what's working—the problems they're highlighting, use cases they're targeting, and copy/creative that's resonating.

## When to Use This Skill

- Researching competitor ad strategies
- Finding inspiration for your own ads
- Understanding market positioning
- Identifying successful ad patterns
- Analyzing messaging that works
- Discovering new use cases or pain points
- Planning ad campaigns with proven concepts

## What This Skill Does

1. **Extracts Ads**: Scrapes ads from Facebook Ad Library, LinkedIn, etc.
2. **Captures Screenshots**: Saves visual copies of all ads
3. **Analyzes Messaging**: Identifies problems, use cases, and value props
4. **Categorizes Ads**: Groups by theme, audience, or format
5. **Identifies Patterns**: Finds common successful approaches
6. **Provides Insights**: Explains why certain ads likely perform well

## How to Use

### Basic Extraction

```
Extract all current ads from [Competitor Name] on Facebook Ad Library
```

```
Scrape ads from [Company] and analyze their messaging
```

### Specific Analysis

```
Get all ads from [Competitor] focusing on their messaging 
about [specific problem]. What pain points are they highlighting?
```

### Competitive Set

```
Extract ads from these 5 competitors: [list]. 
Compare their approaches and tell me what's working.
```

### Specific Platform

```
Get LinkedIn ads from [Competitor] and analyze their 
B2B positioning strategy
```

## Example

**User**: "Extract ads from Notion on Facebook Ad Library and tell me what messaging is working for them."

**Process**:
```
Accessing Facebook Ad Library...
Searching for: Notion
Found: 23 active ads

Extracting screenshots...
[████████████████████] 100%

Saved to: competitor-ads/notion/
- ad-001-collaboration.png
- ad-002-productivity.png
- ad-003-templates.png
...

Analyzing messaging...
```

**Output**:
```
# Notion Ad Analysis

## Overview
- Total Ads: 23 active
- Primary Themes: Productivity (35%), Collaboration (30%), 
  Templates (20%), AI Features (15%)
- Ad Formats: Static images (60%), Video (40%)
- CTA Patterns: "Try for free", "Get started"

## Key Problems They're Highlighting

1. **Scattered Information** (8 ads)
   Copy: "Stop switching between 10 different tools"
   Why it works: Direct pain point many teams face

2. **Meeting Overload** (5 ads)
   Copy: "Replace unnecessary meetings with async updates"
   Why it works: Post-COVID remote work pain point

3. **Lost Documentation** (4 ads)
   Copy: "Never ask 'where is that doc?' again"
   Why it works: Universal workplace frustration

## Successful Creative Patterns

### Pattern 1: Before/After Split
- Shows chaotic tool landscape → Clean Notion workspace
- Used in 6 high-performing ads
- Visual metaphor is immediately clear

### Pattern 2: Feature Showcase
- GIF of actual product usage
- Shows specific feature in 5 seconds
- Used for new features (AI, templates)

### Pattern 3: Social Proof
- "Join 20M users" messaging
- Customer logos
- Used in 4 ads targeting enterprise

## Copy That's Working

Best Headlines:
1. "Your team's knowledge, finally in one place"
   → Benefit-focused, addresses pain directly
   
2. "The all-in-one workspace"
   → Clear positioning, broad appeal
   
3. "AI that actually helps you work"
   → Addresses AI skepticism, practical angle

Best Body Copy Patterns:
- Short sentences (under 10 words)
- Focus on outcomes not features
- Include specific numbers ("Cut meetings by 50%")

## Audience Targeting Insights

Based on ad variations:
- Startup founders: Solo productivity angle
- Team leads: Collaboration and alignment
- Enterprise: Security and compliance mentions
- Students: Free plan, templates, organization

## Recommendations for Your Ads

1. **Test the "tool sprawl" pain point**
   → Strong resonance based on their ad frequency

2. **Use product screenshots over abstract visuals**
   → All their top ads show actual UI

3. **Lead with the problem, not the solution**
   → "Tired of X?" performs better than "Introducing Y"

4. **Keep copy under 100 characters**
   → Their shortest ads seem most frequent

5. **Test before/after visual formats**
   → Proven pattern in their creative

## Files Saved
- All ads: ~/competitor-ads/notion/
- Analysis: ~/competitor-ads/notion/analysis.md
- Best performers: ~/competitor-ads/notion/top-10/
```

**Inspired by:** Sumant Subrahmanya's use case from Lenny's Newsletter

## What You Can Learn

### Messaging Analysis
- What problems they emphasize
- How they position against competition
- Value propositions that resonate
- Target audience segments

### Creative Patterns
- Visual styles that work
- Video vs. static image performance
- Color schemes and branding
- Layout patterns

### Copy Formulas
- Headline structures
- Call-to-action patterns
- Length and tone
- Emotional triggers

### Campaign Strategy
- Seasonal campaigns
- Product launch approaches
- Feature announcement tactics
- Retargeting patterns

## Best Practices

### Legal & Ethical
✓ Only use for research and inspiration
✓ Don't copy ads directly
✓ Respect intellectual property
✓ Use insights to inform original creative
✗ Don't plagiarize copy or steal designs

### Analysis Tips
1. **Look for patterns**: What themes repeat?
2. **Track over time**: Save ads monthly to see evolution
3. **Test hypotheses**: Adapt successful patterns for your brand
4. **Segment by audience**: Different messages for different targets
5. **Compare platforms**: LinkedIn vs Facebook messaging differs

## Advanced Features

### Trend Tracking
```
Compare [Competitor]'s ads from Q1 vs Q2. 
What messaging has changed?
```

### Multi-Competitor Analysis
```
Extract ads from [Company A], [Company B], [Company C]. 
What are the common patterns? Where do they differ?
```

### Industry Benchmarks
```
Show me ad patterns across the top 10 project management 
tools. What problems do they all focus on?
```

### Format Analysis
```
Analyze video ads vs static image ads from [Competitor]. 
Which gets more engagement? (if data available)
```

## Common Workflows

### Ad Campaign Planning
1. Extract competitor ads
2. Identify successful patterns
3. Note gaps in their messaging
4. Brainstorm unique angles
5. Draft test ad variations

### Positioning Research
1. Get ads from 5 competitors
2. Map their positioning
3. Find underserved angles
4. Develop differentiated messaging
5. Test against their approaches

### Creative Inspiration
1. Extract ads by theme
2. Analyze visual patterns
3. Note color and layout trends
4. Adapt successful patterns
5. Create original variations

## Tips for Success

1. **Regular Monitoring**: Check monthly for changes
2. **Broad Research**: Look at adjacent competitors too
3. **Save Everything**: Build a reference library
4. **Test Insights**: Run your own experiments
5. **Track Performance**: A/B test inspired concepts
6. **Stay Original**: Use for inspiration, not copying
7. **Multiple Platforms**: Compare Facebook, LinkedIn, TikTok, etc.

## Output Formats

- **Screenshots**: All ads saved as images
- **Analysis Report**: Markdown summary of insights
- **Spreadsheet**: CSV with ad copy, CTAs, themes
- **Presentation**: Visual deck of top performers
- **Pattern Library**: Categorized by approach

## Related Use Cases

- Writing better ad copy for your campaigns
- Understanding market positioning
- Finding content gaps in your messaging
- Discovering new use cases for your product
- Planning product marketing strategy
- Inspiring social media content

---
