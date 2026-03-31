---
name: ship
description: |
  Release Engineer — Sync main, run tests, audit coverage, push, open PR.
  Bootstraps test frameworks if you don't have one.
---

# Ship It

Release engineer workflow: sync, test, audit, push, PR.

## Execution Flow

### Phase 1: Pre-Flight Checks

```bash
# Check branch
git branch --show-current

# Check for uncommitted changes
git status --porcelain
# If dirty: stop and warn

# Check if branch exists on remote
git ls-remote --heads origin <branch-name>
```

### Phase 2: Sync Main

```bash
# Fetch latest
git fetch origin main

# Check if behind
BASE=$(git merge-base HEAD origin/main)
if [ "$BASE" != "$(git rev-parse origin/main)" ]; then
  # Need to sync
  git stash
  git rebase origin/main
  git stash pop
fi
```

### Phase 3: Run Tests

```bash
# Detect test command from CLAUDE.md or ask user
test_cmd=$(grep -E "^(test|check|verify)" CLAUDE.md | head -1)

# Run tests
$test_cmd

# If no test framework: bootstrap one
```

**Bootstrap tests if missing:**
```bash
# Detect framework from package.json
if [ -f package.json ]; then
  if grep -q "jest" package.json; then
    # Jest already configured
  else
    # Add test framework
    npm install --save-dev jest
    # Create test/ directory
    mkdir -p test
  fi
fi
```

### Phase 4: Audit Coverage

Check test coverage:
```bash
# Run coverage report
npm run test:coverage

# Check if new code has tests
# Flag files without coverage
```

### Phase 5: Commit

```bash
# Stage changes
git add -A

# Conventional commit message
git commit -m "feat(scope): description

Details of what changed and why.

Closes #123"
```

### Phase 6: Push

```bash
# Push to origin
git push origin <branch-name>
```

### Phase 7: Create PR

```bash
# Create PR
gh pr create \
  --title "feat(scope): description" \
  --body-file .github/PULL_REQUEST_TEMPLATE.md \
  --base main
```

**PR Body Template:**
```markdown
## Summary
[1-2 sentences]

## Changes
- Change 1
- Change 2

## Testing
- [ ] Tests pass
- [ ] Manual QA completed
- [ ] Screenshots attached (if UI)

## Screenshots
[if applicable]

## Checklist
- [ ] Code reviewed
- [ ] Tests added/updated
- [ ] Documentation updated
- [ ] No console errors
```

## Output

```markdown
## Ship Report

### Pre-Flight
- [x] No uncommitted changes
- [x] Synced with main

### Tests
- [x] All tests pass (42 → 51)
- [x] Coverage: 78% → 82%

### Commits
- abc1234: feat(auth): add login flow

### PR
- https://github.com/user/repo/pull/42

### Next Steps
- [ ] Review requested
- [ ] CI passes
- [ ] /land-and-deploy
```

## Trigger Phrases

- "Ship it"
- "Create PR"
- "Push this"
- "Open pull request"
