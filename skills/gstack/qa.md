---
name: qa
description: |
  QA Lead testing with real browser. Test your app, find bugs, fix them with atomic
  commits, re-verify. Auto-generates regression tests for every fix.
argument-hint: "[staging URL or localhost:port]"
---

# QA Testing

Test your app with a real browser. Find bugs, fix them, verify.

## Execution Flow

### Phase 1: Scope and Navigate

```bash
# Navigate to URL
$B goto <url>

# Take initial snapshot
$B snapshot -i
```

### Phase 2: Test Core Flows

Identify user flows from codebase/context, then test each:

```bash
# For each flow:
$B goto <starting-url>
$B snapshot -i

# Click through steps
$B click @e3
$B snapshot -i

# Fill forms
$B fill @e5 "test@example.com"
$B click @submit
$B snapshot -i

# Verify outcomes
$B wait-for "success message"
$B snapshot -i
```

### Phase 3: Find and Fix Bugs

When a bug is found:
1. **Document** — screenshot + steps to reproduce
2. **Investigate** — root cause analysis
3. **Fix** — atomic commit with test
4. **Verify** — re-run the flow

### Phase 4: Generate Regression Tests

For each bug fixed, generate a regression test:

```javascript
// Example Playwright test
test('should not crash on empty input', async ({ page }) => {
  await page.goto('/form');
  await page.click('#submit'); // empty form
  await expect(page.locator('.error')).toBeVisible();
  await expect(page.locator('.crash')).not.toBeVisible();
});
```

### Phase 5: Report

```markdown
## QA Report

### Tested Flows
1. [Flow name] — ✅ PASS / ❌ FAIL
2. [Flow name] — ✅ PASS / ❌ FAIL

### Bugs Found
| # | Flow | Severity | Steps | Fixed |
|---|------|----------|-------|-------|
| 1 | | | | |

### Regression Tests Added
- test/bug-123-empty-input.test.ts

### Screenshots
[Attached]

### Verdict
- [ ] Ready for production
- [ ] Ready with fixes
- [ ] Needs more work
```

## Browser Commands Reference

```bash
$B goto <url>              # Navigate to URL
$B snapshot -i             # Take annotated screenshot
$B click @e3               # Click element by ref
$B fill @e5 "text"         # Fill input
$B select @e7 "option"     # Select dropdown
$B wait-for "text"         # Wait for text
$B scroll                  # Scroll down
$B back                    # Go back
$B console                 # Show console logs
$B network                 # Show network logs
```

## Output

- Tested flows with pass/fail status
- Documented bugs with steps
- Fixed bugs with atomic commits
- Regression tests added
- Screenshots for evidence

## Trigger Phrases

- "Test this"
- "Does this work?"
- "QA"
- "Check if it works"
