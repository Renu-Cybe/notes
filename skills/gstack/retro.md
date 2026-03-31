---
name: retro
description: |
  Weekly retrospective. Per-person breakdowns, shipping streaks, test health trends,
  growth opportunities. Cross-project mode supported.
argument-hint: "[optional: 'global' for cross-project retro]"
---

# Weekly Retro

Team-aware weekly retrospective.

## Retro Format

### 1. What Went Well

Review shipping highlights:
- Commits this week
- Lines changed
- Features shipped
- Bugs fixed

### 2. What Didn't Go Well

Identify friction:
- Blockers encountered
- Time sinks
- Failed attempts
- Technical debt accumulated

### 3. Metrics

```bash
# Git stats
git log --since="7 days ago" --oneline --author="$(git config user.name)"
git diff --shortstat HEAD~20..HEAD

# Test health
# Run test suite, check pass rate
```

### 4. Learnings

Document insights:
- Technical learnings
- Process improvements
- Tool discoveries
- Pattern recognition

### 5. Action Items

| Item | Owner | Priority |
|------|-------|----------|
| | | |

## Global Mode

```bash
# Cross-project retro
/retro global
```

Aggregates stats across:
- All projects
- All AI tools used (Claude Code, Codex, Gemini)
- Total commits, lines, time spent

## Output

```markdown
# Weekly Retro — YYYY-MM-DD

## Shipping Highlights
- X commits
- Y lines changed (+A, -B)
- Z features shipped

## What Went Well
- ✅ Thing 1
- ✅ Thing 2

## What Didn't Go Well
- ❌ Issue 1
- ❌ Issue 2

## Metrics
| Metric | This Week | Last Week | Trend |
|--------|-----------|-----------|-------|
| Commits | | | |
| Lines | | | |
| Test Pass Rate | | | |

## Learnings
1. [Learning 1]
2. [Learning 2]

## Action Items
| Item | Owner | Due |
|------|-------|-----|
| | | |

## Focus for Next Week
- [ ] Priority 1
- [ ] Priority 2
```

## Trigger Phrases

- "Weekly retro"
- "What did I ship?"
- "This week's summary"
