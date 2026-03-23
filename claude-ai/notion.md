# Skills: Notion Integration

This file contains 10 skill(s) for the **Notion Integration** category.
Follow the relevant skill's instructions when the user's request matches.

---

## Skill: `notion-create-database-row`

---
name: Notion:create-database-row
description: Inserts a new row into a specified Notion database using natural-language property values. You describe the row in plain English and Claude handles the property mapping.
---

## Notion:create-database-row
**Category:** Notion Integration

**What it does:**
Inserts a new row into a specified Notion database using natural-language property values. You describe the row in plain English and Claude handles the property mapping.

**When to trigger:**
- "Add a row to my [database name] in Notion"

**How to install:**
```bash
npx claude install superpowers
```
Also requires the **Notion MCP server** connected.

**Trigger phrase:** Ask Claude to add a row or entry to a specific Notion database.

---

## Skill: `notion-create-page`

---
name: notion-create-page
description: Create a new Notion page with content. Use this skill when the user wants to create a new page in Notion, add a document, write a note, or create a wiki entry.
---

# Notion: Create Page

Create a new Notion page with a title and content.

## When to Use

Use when the user:
- Says "create a page in Notion"
- Wants to add a new note, document, or wiki entry
- Needs to write content to Notion
- Wants to create a sub-page under an existing page

## Process

### Step 1: Determine Where to Create the Page

Ask or infer:
- **Parent page**: Should this live under an existing page? If yes, get the parent page ID using `notion-find`.
- **Workspace root**: If no parent is specified, create at the workspace level.
- **Database**: If it should be an entry in a database, use `notion-create-task` instead.

### Step 2: Prepare the Content

Gather from the user:
- **Title**: The page title (required)
- **Content**: Body text, structured content, etc.

### Step 3: Create the Page

Use `API-post-page`:

**Create at workspace root:**
```json
{
  "parent": { "type": "workspace" },
  "properties": {
    "title": {
      "title": [{ "type": "text", "text": { "content": "Page Title" } }]
    }
  }
}
```

**Create under a parent page:**
```json
{
  "parent": { "page_id": "parent-page-id" },
  "properties": {
    "title": {
      "title": [{ "type": "text", "text": { "content": "Page Title" } }]
    }
  }
}
```

### Step 4: Add Content (if any)

The `API-post-page` endpoint creates the page with a title. To add body content, use `API-patch-block-children` with the new page's ID:

**Add paragraph blocks:**
```json
{
  "block_id": "new-page-id",
  "children": [
    {
      "type": "paragraph",
      "paragraph": {
        "rich_text": [{ "type": "text", "text": { "content": "Your content here." } }]
      }
    }
  ]
}
```

**Add bulleted list:**
```json
{
  "block_id": "new-page-id",
  "children": [
    {
      "type": "bulleted_list_item",
      "bulleted_list_item": {
        "rich_text": [{ "type": "text", "text": { "content": "List item" } }]
      }
    }
  ]
}
```

## Response Format

On success:
```
✅ Page created: **[Title]**
URL: [notion url]
ID: [page-id]
```

## Multi-Block Content

For pages with multiple sections, append blocks sequentially. Keep each `API-patch-block-children` call to <100 blocks.

## Notes

- The Notion API only supports `paragraph` and `bulleted_list_item` block types in this integration
- For richer content (headings, code blocks, etc.), the page can be edited manually in Notion after creation
- Always confirm with the user before creating the page if the intent was ambiguous
- Page IDs are UUIDs — save them if the user will want to reference the page again

---

## Skill: `notion-create-task`

---
name: notion-create-task
description: Create a new task or entry in a Notion database. Use this skill when the user wants to add a task, to-do item, project entry, or any record to a Notion database.
---

# Notion: Create Task

Add a new entry (task, to-do, record) to a Notion database.

## When to Use

Use when the user:
- Says "add a task to Notion" or "create a to-do in Notion"
- Wants to add an entry to a specific Notion database
- Needs to log something (a bug, a lead, a project entry)

## Process

### Step 1: Identify the Target Database

Ask or infer which database the task should go into:
- "Which database should this go in? (e.g., Tasks, Projects, Backlog)"
- Or search for it: use `API-post-search` with `filter: { value: "data_source" }`

Get the database ID.

### Step 2: Retrieve Database Schema

Before creating an entry, understand what properties the database has:

```
API-retrieve-a-data-source: { "data_source_id": "database-id" }
```

This returns the database's `properties` object, which defines:
- Property names
- Property types (title, rich_text, select, multi_select, date, checkbox, number, etc.)

### Step 3: Gather Task Details

Collect from the user what's needed based on the database schema:
- **Title** (always required)
- **Status** (if the database has a status property)
- **Due date** (if relevant)
- **Assignee** (if relevant)
- **Priority** / **Tags** / other fields

### Step 4: Create the Entry

Use `API-post-page` with the database as parent:

```json
{
  "parent": {
    "type": "database_id",
    "database_id": "database-id"
  },
  "properties": {
    "Name": {
      "title": [{ "type": "text", "text": { "content": "Task title" } }]
    },
    "Status": {
      "select": { "name": "To Do" }
    },
    "Due Date": {
      "date": { "start": "2025-03-20" }
    },
    "Priority": {
      "select": { "name": "High" }
    },
    "Tags": {
      "multi_select": [{ "name": "Engineering" }]
    }
  }
}
```

## Property Type Reference

| Type | Format |
|------|--------|
| `title` | `[{ "type": "text", "text": { "content": "..." } }]` |
| `rich_text` | `[{ "type": "text", "text": { "content": "..." } }]` |
| `select` | `{ "name": "option name" }` |
| `multi_select` | `[{ "name": "tag1" }, { "name": "tag2" }]` |
| `date` | `{ "start": "YYYY-MM-DD" }` |
| `checkbox` | `true` or `false` |
| `number` | `42` |
| `url` | `"https://..."` |

## Response Format

On success:
```
✅ Task created: **[Task Title]**
Database: [database name]
URL: [notion url]
```

Include any relevant properties that were set (status, due date, etc.).

## Notes

- Always retrieve the database schema first — property names are case-sensitive
- Select options must match existing options in the database (or will create new ones if allowed)
- If the user didn't provide required fields, ask before creating
- After creating, offer to add body content to the task page if needed

---

## Skill: `notion-database-query`

---
name: notion-database-query
description: Query a Notion database to retrieve, filter, and sort records. Use this skill when the user wants to list items in a Notion database, filter tasks by status/date/property, or get data out of a Notion database.
---

# Notion: Database Query

Retrieve and filter records from a Notion database.

## When to Use

Use when the user:
- Says "show me all my tasks in Notion"
- Wants to filter database entries ("show me tasks that are In Progress")
- Wants to sort database records
- Needs to read data out of a Notion database

## Process

### Step 1: Identify the Database

Find the database ID:
- Ask the user which database (by name)
- Use `API-post-search` with `filter: { value: "data_source" }` to find it
- Or use a known database ID if the user provides one

### Step 2: (Optional) Retrieve Schema

To understand what properties are filterable/sortable:
```
API-retrieve-a-data-source: { "data_source_id": "database-id" }
```

### Step 3: Query the Database

Use `API-query-data-source`:

**Basic query (all records):**
```json
{
  "data_source_id": "database-id"
}
```

**Filter by select property:**
```json
{
  "data_source_id": "database-id",
  "filter": {
    "property": "Status",
    "select": { "equals": "In Progress" }
  }
}
```

**Filter by checkbox:**
```json
{
  "data_source_id": "database-id",
  "filter": {
    "property": "Done",
    "checkbox": { "equals": false }
  }
}
```

**Filter by date:**
```json
{
  "data_source_id": "database-id",
  "filter": {
    "property": "Due Date",
    "date": { "on_or_before": "2025-03-31" }
  }
}
```

**Sort results:**
```json
{
  "data_source_id": "database-id",
  "sorts": [
    { "property": "Priority", "direction": "descending" },
    { "property": "Due Date", "direction": "ascending" }
  ]
}
```

**Combined filter and sort:**
```json
{
  "data_source_id": "database-id",
  "filter": {
    "and": [
      { "property": "Status", "select": { "equals": "To Do" } },
      { "property": "Priority", "select": { "equals": "High" } }
    ]
  },
  "sorts": [{ "property": "Due Date", "direction": "ascending" }]
}
```

## Filter Types Reference

| Property Type | Filter Options |
|--------------|----------------|
| `select` | `equals`, `does_not_equal`, `is_empty`, `is_not_empty` |
| `multi_select` | `contains`, `does_not_contain`, `is_empty`, `is_not_empty` |
| `checkbox` | `equals: true/false` |
| `date` | `equals`, `before`, `after`, `on_or_before`, `on_or_after`, `is_empty`, `is_not_empty` |
| `title` / `rich_text` | `equals`, `contains`, `starts_with`, `ends_with`, `is_empty`, `is_not_empty` |
| `number` | `equals`, `greater_than`, `less_than`, `greater_than_or_equal_to`, `less_than_or_equal_to` |

## Parsing Results

Results are in `results[]`, each with `properties`:
```json
{
  "results": [
    {
      "id": "page-id",
      "url": "https://notion.so/...",
      "properties": {
        "Name": { "title": [{ "plain_text": "Task title" }] },
        "Status": { "select": { "name": "In Progress" } },
        "Due Date": { "date": { "start": "2025-03-20" } }
      }
    }
  ]
}
```

## Response Format

Present results as a clear list:

```
Found X records in [Database Name]:

1. **[Title]** — Status: [status] | Due: [date]
2. **[Title]** — Status: [status] | Due: [date]
...

[If filtered]: Showing tasks filtered by [filter description].
```

## Pagination

If `has_more: true`, use `next_cursor` to get more results:
```json
{
  "data_source_id": "database-id",
  "start_cursor": "cursor-from-previous-response"
}
```

## Notes

- Filter property names are case-sensitive — match exactly what's in the schema
- Maximum page_size is 100 per request
- Combine `and`/`or` arrays for complex filters
- If the user doesn't know filter values, retrieve a few records first to see what options exist

---

## Skill: `notion-find`

---
name: notion-find
description: Find a specific Notion page by title or partial title match. Use this skill when the user wants to locate a specific Notion page, asks "find my X page in Notion", or needs the page ID of a known page.
---

# Notion: Find Page

Locate a specific Notion page by title using the Notion MCP integration.

## When to Use

Use when the user:
- Says "find my [page name] in Notion"
- Needs to retrieve a specific page to read or update it
- Wants to confirm a page exists before creating a new one

## How to Find a Page

Use the `API-post-search` tool to search by title:

```json
{
  "query": "page title or keywords",
  "filter": {
    "property": "object",
    "value": "page"
  }
}
```

## Process

1. **Extract the search query** from the user's request
2. **Call `API-post-search`** with the title keywords
3. **Review results** — check `results[].properties.title` or `results[].title` for matches
4. **Handle multiple results**:
   - If one clear match: return the page ID and title
   - If multiple matches: list them and ask the user to confirm which one
   - If no match: inform the user and suggest searching with different terms

## Result Parsing

Notion search results have this structure:
```json
{
  "results": [
    {
      "id": "page-id-here",
      "object": "page",
      "url": "https://notion.so/...",
      "properties": {
        "title": {
          "title": [{ "plain_text": "Page Title" }]
        }
      }
    }
  ]
}
```

Extract the page title with: `result.properties.title.title[0].plain_text`

## Response Format

When a page is found:
```
Found: **[Page Title]**
ID: `[page-id]`
URL: [notion url]
```

When multiple results:
```
Found multiple pages matching "[query]":
1. [Title 1] — [url]
2. [Title 2] — [url]

Which one did you mean?
```

When not found:
```
No page found matching "[query]".

Try:
- Different keywords
- Checking if the page is in a database (use notion-database-query)
- Using notion-search for broader content search
```

## Notes

- Notion search only covers pages the integration has access to
- Search matches against page titles, not content
- For content search, use the `notion-search` skill
- Always confirm the right page before making changes to it

---

## Skill: `notion-search`

---
name: notion-search
description: Search Notion for pages and databases matching a query. Use this skill when the user wants to search across their Notion workspace, find pages or databases by keyword, or explore what's available in their Notion.
---

# Notion: Search Workspace

Search across the Notion workspace for pages and databases matching a query.

## When to Use

Use when the user:
- Wants to search across all of Notion (not just find one specific page)
- Asks "search Notion for X" or "what's in my Notion about Y"
- Wants to find both pages and databases matching a term
- Is exploring what exists in their workspace

## How to Search

Use `API-post-search` with optional filters:

**Search everything:**
```json
{
  "query": "search terms"
}
```

**Search only pages:**
```json
{
  "query": "search terms",
  "filter": { "property": "object", "value": "page" }
}
```

**Search only databases:**
```json
{
  "query": "search terms",
  "filter": { "property": "object", "value": "data_source" }
}
```

**Sort by most recently edited:**
```json
{
  "query": "search terms",
  "sort": { "direction": "descending", "timestamp": "last_edited_time" }
}
```

## Process

1. **Identify search intent** — does the user want pages, databases, or both?
2. **Run the search** with appropriate filters
3. **Parse results** — group by type (pages vs databases)
4. **Present results** clearly with titles, types, and URLs
5. **Offer next actions** — open a page, read content, etc.

## Result Parsing

```json
{
  "results": [
    {
      "object": "page",
      "id": "...",
      "url": "...",
      "properties": {
        "title": {
          "title": [{ "plain_text": "Page Title" }]
        }
      },
      "last_edited_time": "2025-01-15T10:00:00Z"
    },
    {
      "object": "database",
      "id": "...",
      "url": "...",
      "title": [{ "plain_text": "Database Name" }]
    }
  ]
}
```

For pages: `result.properties.title.title[0]?.plain_text`
For databases: `result.title[0]?.plain_text`

## Response Format

```
Search results for "[query]":

📄 Pages (X)
- [Title 1] — last edited [date] — [url]
- [Title 2] — last edited [date] — [url]

🗄 Databases (X)
- [Database Name] — [url]

No results? Try:
- Broader keywords
- Different spelling
- Checking workspace permissions
```

## Pagination

If there are many results, use `start_cursor` to paginate:
```json
{
  "query": "...",
  "start_cursor": "[cursor from previous result]",
  "page_size": 10
}
```

## Notes

- Notion search works on page/database titles, not full content
- Results are limited to pages the integration has access to
- If the user has large workspaces, suggest more specific search terms
- After finding relevant pages, offer to read their content using `API-get-block-children`

---

## Skill: `notion-tasks-build`

---
name: Notion:tasks:build
description: Builds a task from a Notion page URL. Reads the page content and structures it into an actionable task with the right properties.
---

## Notion:tasks:build
**Category:** Notion Integration — Tasks

**What it does:**
Builds a task from a Notion page URL. Reads the page content and structures it into an actionable task with the right properties.

**When to trigger:**
- "Build a task from this Notion page: [URL]"

**How to install:**
```bash
npx claude install superpowers
```
Also requires the **Notion MCP server** connected.

**Trigger phrase:** Provide a Notion page URL and ask to build a task from it.

---

## Skill: `notion-tasks-explain-diff`

---
name: Notion:tasks:explain-diff
description: Makes a Notion doc explaining a code change (diff). Useful for documenting what changed and why, directly in Notion.
---

## Notion:tasks:explain-diff
**Category:** Notion Integration — Tasks

**What it does:**
Makes a Notion doc explaining a code change (diff). Useful for documenting what changed and why, directly in Notion.

**When to trigger:**
- "Document this code change in Notion"
- "Explain this diff and save it to Notion"

**How to install:**
```bash
npx claude install superpowers
```
Also requires the **Notion MCP server** connected.

**Trigger phrase:** Ask Claude to explain a code diff and create a Notion doc for it.

---

## Skill: `notion-tasks-plan`

---
name: Notion:tasks:plan
description: Plans a task from a Notion page URL. Reads the page and produces a structured implementation plan.
---

## Notion:tasks:plan
**Category:** Notion Integration — Tasks

**What it does:**
Plans a task from a Notion page URL. Reads the page and produces a structured implementation plan.

**When to trigger:**
- "Plan the task from this Notion page: [URL]"

**How to install:**
```bash
npx claude install superpowers
```
Also requires the **Notion MCP server** connected.

**Trigger phrase:** Provide a Notion page URL and ask to plan the task.

---

## Skill: `notion-tasks-setup`

---
name: Notion:tasks:setup
description: Sets up a Notion task board for tracking tasks. Creates the database structure, views, and properties needed for a Claude Code + Notion workflow.
---

## Notion:tasks:setup
**Category:** Notion Integration — Tasks

**What it does:**
Sets up a Notion task board for tracking tasks. Creates the database structure, views, and properties needed for a Claude Code + Notion workflow.

**When to trigger:**
- "Set up a Notion task board for me"
- First-time Notion integration setup

**How to install:**
```bash
npx claude install superpowers
```
Also requires the **Notion MCP server** connected.

**Trigger phrase:** Ask Claude to set up a Notion task board.

---
