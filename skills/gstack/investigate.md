---
name: investigate
description: |
  Systematic root-cause debugging. Iron Law: no fixes without investigation.
  Traces data flow, tests hypotheses, stops after 3 failed fixes.
argument-hint: "[bug description or error message]"
---

# Investigate

Systematic root-cause debugging.

**Iron Law:** No fixes without investigation.

## The 5 Whys

1. What happened? (symptom)
2. Why did it happen? (direct cause)
3. Why did that happen? (contributing cause)
4. Why did that happen? (systemic cause)
5. Why did that happen? (root cause)

## Execution Flow

### Phase 1: Capture Evidence

```bash
# Get error logs
grep -i "error\|exception\|fail" logs/*.log | tail -50

# Check recent changes
git log --oneline -10
git diff HEAD~5 --stat

# Check system status
# (memory, disk, connections)
```

### Phase 2: Form Hypotheses

Generate 3-5 hypotheses about root cause:

1. **Hypothesis A:** Recent change in X caused Y
2. **Hypothesis B:** Data corruption in Z
3. **Hypothesis C:** Race condition in W
4. **Hypothesis D:** Configuration error
5. **Hypothesis E:** External dependency failure

### Phase 3: Test Hypotheses

For each hypothesis, design a test:

```bash
# Hypothesis A: Revert recent change
git stash
git checkout HEAD~1 -- path/to/file
# Test if issue persists

# Hypothesis B: Check data integrity
# Run data validation queries

# Hypothesis C: Add logging
# Reproduce with verbose logging

# Hypothesis D: Check config
# Compare with known good config

# Hypothesis E: Check external service
# Test API endpoints
```

### Phase 4: Trace Data Flow

Follow the data from input to error:

```
User Input → API → Validation → Processing → Database
                ↑
            Error occurs here
```

Check at each step:
- Is data what we expect?
- Are transformations correct?
- Are error handlers catching?

### Phase 5: Root Cause

Document root cause:

```markdown
## Investigation Report

### Symptom
[What the user sees]

### Investigation Steps
1. Checked logs → Found X
2. Reproduced locally → Confirmed Y
3. Added logging → Discovered Z
4. Traced data flow → Root cause identified

### Root Cause
[The actual problem]

### Contributing Factors
- Factor 1
- Factor 2

### Fix
[What needs to change]

### Prevention
- How to prevent this in future
- Tests to add
- Monitoring to implement
```

## Stop Conditions

**STOP after 3 failed fix attempts.** Escalate if:
- 3 fixes attempted, none worked
- Issue spans multiple systems
- Security implications unclear
- Root cause unknown after 30 minutes

## Output

- Investigation steps taken
- Evidence gathered
- Root cause identified
- Fix recommendation
- Prevention strategy

## Trigger Phrases

- "Something's broken"
- "Debug this"
- "Why is this failing?"
- "Investigate"
- Error message or stack trace
