---
name: office-hours
description: |
  YC Office Hours — Start here for any new product or feature. Six forcing questions that
  reframe your product before you write code. Pushes back on framing, challenges premises,
  generates implementation alternatives. Writes design doc for downstream skills.
---

# YC Office Hours

Start here for any new product or feature idea.

## The Six Forcing Questions

1. **What is the specific pain?**
   - Who feels it? When? How often?
   - Get concrete examples, not hypotheticals

2. **Who has this pain?**
   - Be specific (not "developers", "React devs at startups with 10-50 people")
   - How many of them are there?

3. **What are they doing now?**
   - Current workaround = your real competition
   - Why is the workaround insufficient?

4. **Why you?**
   - What do you know that others don't?
   - Why will you win?

5. **What's the narrowest wedge?**
   - What can you ship tomorrow that tests the core assumption?
   - Don't build the 3-month vision first

6. **How will you know it worked?**
   - What metric moves?
   - What's the success criteria?

## Execution Flow

### Phase 1: Extract Pain

Ask the user to describe their idea. Then probe for specifics:
- "Give me a concrete example of when this happened"
- "Who specifically has this problem?"
- "What did they do instead?"

### Phase 2: Challenge Framing

Push back on the user's framing:
- "You said 'daily briefing app' — but what you described is a personal chief of staff AI"
- Extract capabilities they didn't realize they were describing
- Challenge 3-4 premises

### Phase 3: Generate Alternatives

Propose 2-3 implementation approaches with effort estimates:
- Narrow wedge (ship tomorrow)
- Medium scope (2-4 weeks)
- Full vision (3+ months)

**Recommendation:** Ship the narrowest wedge first.

### Phase 4: Write Design Doc

Create design document that feeds into downstream skills:

```markdown
# Design: [Title]

## Problem Statement
[Specific pain, who feels it, frequency]

## Target User
[Specific persona, market size]

## Current Workarounds
[What they do now, why it fails]

## Proposed Solution
[Core capabilities]

## Success Criteria
[Metrics that move]

## Implementation Approaches

### Approach 1: Narrow Wedge ([time estimate])
[Description, what's included, what's excluded]

### Approach 2: Medium Scope ([time estimate])
...

### Approach 3: Full Vision ([time estimate])
...

## Recommendation
[Approach X] — ship tomorrow, learn from real usage

## Next Steps
- [ ] /plan-ceo-review
- [ ] /plan-eng-review
```

Save to: `docs/designs/YYYY-MM-DD-<topic>-design.md`

## Output

- Design document with specific pain identified
- 3 implementation approaches with estimates
- Clear recommendation (usually narrow wedge)
- Next steps mapped to gstack skills

## Trigger Phrases

- "I want to build..."
- "What should I build?"
- "I have an idea..."
- "Is this worth building?"
