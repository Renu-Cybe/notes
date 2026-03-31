---
name: cso
description: |
  Chief Security Officer — OWASP Top 10 + STRIDE threat model. Zero-noise security audit
  with concrete exploit scenarios.
---

# Chief Security Officer (CSO)

OWASP Top 10 + STRIDE threat model audit.

## STRIDE Framework

| Threat | Question |
|--------|----------|
| **S**poofing | Can someone pretend to be someone else? |
| **T**ampering | Can data be modified in transit or at rest? |
| **R**epudiation | Can actions be denied? |
| **I**nformation Disclosure | Can unauthorized data be read? |
| **D**enial of Service | Can the service be overwhelmed? |
| **E**levation of Privilege | Can someone do what they shouldn't? |

## OWASP Top 10

1. Broken Access Control
2. Cryptographic Failures
3. Injection
4. Insecure Design
5. Security Misconfiguration
6. Vulnerable Components
7. Authentication Failures
8. Software/Data Integrity Failures
9. Security Logging Failures
10. Server-Side Request Forgery

## Execution Flow

### Phase 1: Read Code

Identify security-critical files:
- Authentication/authorization code
- API endpoints
- Data access layer
- Configuration
- Dependencies

### Phase 2: STRIDE Analysis

For each component, ask STRIDE questions:

**Authentication:**
- S: Can users spoof identities?
- T: Can tokens be tampered?
- I: Can tokens be read by unauthorized parties?
- E: Can privileges be escalated?

**Data Access:**
- T: Can data be modified by unauthorized users?
- I: Can sensitive data be read?
- R: Are data modifications logged?

**APIs:**
- I: Can unauthorized data be accessed?
- D: Can APIs be overwhelmed?
- E: Can users access other users' data?

### Phase 3: Findings

For each finding, include:
- Severity (Critical/High/Medium/Low)
- STRIDE category
- Concrete exploit scenario
- Remediation

```markdown
### Finding 1: SQL Injection Risk

**Severity:** Critical
**STRIDE:** Tampering, Information Disclosure
**Location:** `app/controllers/users.rb:42`

**Exploit Scenario:**
Attacker submits `id=1 OR 1=1` to `/users?id=1` endpoint.
Query becomes: `SELECT * FROM users WHERE id=1 OR 1=1`
Result: All user records exposed.

**Remediation:**
```ruby
# Before (vulnerable)
User.where("id = #{params[:id]}")

# After (safe)
User.where(id: params[:id])
```
```

### Phase 4: Report

```markdown
## Security Audit Report

### Executive Summary
- Findings: X Critical, Y High, Z Medium, W Low
- Overall Risk: [Critical/High/Medium/Low]

### Critical Findings
[Must fix before production]

### High Findings
[Should fix within 1 week]

### Medium Findings
[Fix within 30 days]

### Low Findings
[Address as time permits]

### Recommendations
1. Enable 2FA for admin accounts
2. Add rate limiting to auth endpoints
3. Implement security headers
4. Set up security logging

### Compliance Notes
- [ ] GDPR data handling
- [ ] SOC 2 requirements
- [ ] PCI DSS (if applicable)
```

## Trigger Phrases

- "Security check"
- "Is this safe?"
- "Security audit"
- "Threat model"
