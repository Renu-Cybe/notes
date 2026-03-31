---
name: review
description: |
  Staff Engineer code review. Find bugs that pass CI but blow up in production.
  Auto-fixes obvious issues. Flags completeness gaps.
argument-hint: "[optional: branch name or PR number]"
---

# Code Review

Find bugs that pass CI but blow up in production.

## Review Personas

| Persona | Focus |
|---------|-------|
| **Correctness** | Logic errors, edge cases, state bugs |
| **Testing** | Coverage gaps, weak assertions |
| **Maintainability** | Coupling, complexity, naming, dead code |
| **Security** | Auth, injection, exposure risks |
| **Performance** | N+1 queries, unnecessary work |

## Severity Scale

| Level | Meaning | Action |
|-------|---------|--------|
| **P0** | Critical breakage, data loss, security hole | Must fix before merge |
| **P1** | High-impact defect in normal usage | Should fix |
| **P2** | Moderate issue, edge case, perf regression | Fix if straightforward |
| **P3** | Low-impact, minor improvement | User's discretion |

## Execution Flow

### Phase 1: Determine Scope

```bash
# Get current branch
git branch --show-current

# Get diff
git diff --name-only origin/main
git diff origin/main
```

### Phase 2: Intent Discovery

Understand what the change is trying to accomplish:
```bash
git log --oneline origin/main..HEAD
```

Write 2-3 line intent summary.

### Phase 3: Run Reviews

Check each dimension:

**Correctness:**
- [ ] Logic errors in happy path
- [ ] Edge cases handled
- [ ] State management correct
- [ ] Error propagation sensible

**Testing:**
- [ ] New behavior has tests
- [ ] Changed behavior has updated tests
- [ ] Edge cases covered
- [ ] Assertions are specific

**Maintainability:**
- [ ] Naming is clear
- [ ] No obvious duplication
- [ ] Complexity justified
- [ ] Dead code removed

**Security:**
- [ ] Input validated
- [ ] Auth checks present
- [ ] No injection risks
- [ ] Secrets not exposed

**Performance:**
- [ ] No N+1 queries
- [ ] No unnecessary work
- [ ] Async where appropriate

### Phase 4: Auto-Fix

Apply safe fixes automatically:
- Obvious typos
- Missing awaits
- Simple refactors
- Import cleanup

### Phase 5: Report Findings

```markdown
## Review Report

### Intent
[2-3 line summary]

### Files Changed
- file1.ts
- file2.ts

### Findings

#### P0 — Critical
| File | Issue | Suggested Fix |
|------|-------|---------------|
| | | |

#### P1 — High
| File | Issue | Suggested Fix |
|------|-------|---------------|
| | | |

#### P2 — Moderate
...

#### P3 — Low
...

### Auto-Fixed
- [x] Issue 1
- [x] Issue 2

### Completeness Gaps
[What's missing from the implementation?]

### Verdict
- [ ] Ready to merge
- [ ] Ready with fixes
- [ ] Needs more work
```

## Output

- Categorized findings (P0-P3)
- Auto-fixed issues
- Completeness gaps
- Clear verdict

## Trigger Phrases

- "Check my code"
- "Review this"
- "Code review"
- PR review
