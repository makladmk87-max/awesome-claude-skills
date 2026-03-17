---
name: ccpm-issue-show
description: Display detailed information about a CCPM-tracked GitHub issue including description, local task file mapping, sub-issues, dependencies, recent activity, and acceptance criteria progress. Part of the CCPM spec-driven development workflow.
---

# CCPM: Issue Show

Display comprehensive information about a GitHub issue and its local task file.

## Usage

```
/pm:issue-show <issue_number>
```

## Instructions

### 1. Fetch Issue Data

```bash
gh issue view $ARGUMENTS --json number,title,state,body,labels,assignees,createdAt,updatedAt
```

- Look for local task file at `.claude/epics/*/$ARGUMENTS.md`
- If not found, search for `github:.*issues/$ARGUMENTS` in frontmatter

### 2. Display Issue Overview

```
🎫 Issue #$ARGUMENTS: {Issue Title}
   Status: {open/closed}
   Labels: {labels}
   Assignee: {assignee}
   Created: {creation_date}
   Updated: {last_update}

📝 Description:
{issue_description}
```

### 3. Show Local File Mapping

If local task file exists:
```
📁 Local Files:
   Task file: .claude/epics/{epic_name}/{task_file}
   Updates: .claude/epics/{epic_name}/updates/$ARGUMENTS/
   Last local update: {timestamp}
```

### 4. Show Dependencies

```
🔗 Related Issues:
   Parent Epic: #{epic_issue_number}
   Dependencies: #{dep1}, #{dep2}
   Blocking: #{blocked1}, #{blocked2}
   Sub-tasks: #{sub1}, #{sub2}
```

### 5. Show Recent Activity

```bash
gh issue view $ARGUMENTS --comments --json comments -q '.comments[-3:]'
```

```
💬 Recent Activity:
   {timestamp} - {author}: {comment_preview}

   View full thread: gh issue view #$ARGUMENTS --comments
```

### 6. Show Acceptance Criteria Progress

If task file exists, parse acceptance criteria:
```
✅ Acceptance Criteria:
   ✅ Criterion 1 (completed)
   🔄 Criterion 2 (in progress)
   ⏸️ Criterion 3 (blocked)
   □  Criterion 4 (not started)
```

### 7. Quick Actions

```
🚀 Quick Actions:
   Start work:   /pm:issue-start $ARGUMENTS
   Sync updates: /pm:issue-sync $ARGUMENTS
   Close issue:  /pm:issue-close $ARGUMENTS
   Add comment:  gh issue comment #$ARGUMENTS --body "your comment"
   View in browser: gh issue view #$ARGUMENTS --web
```

### 8. Error Handling

- Handle invalid issue numbers gracefully
- Provide helpful message if not authenticated: `gh auth login`
- Suggest `/pm:import` if no local task file found

## Notes

Provides a single-pane view combining GitHub data with local CCPM state, saving context switching between GitHub and the local workspace.
