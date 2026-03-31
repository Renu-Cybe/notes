---
name: browse
description: |
  Headless browser control for QA testing. ~100ms per command. Real Chromium,
  real clicks, real screenshots. Supports refs (@e1, @c1) for element addressing.
---

# Browse

Headless browser control for QA testing.

**Performance:** ~100ms per command after first call.

## Quick Reference

```bash
$B goto <url>              # Navigate to URL
$B snapshot -i             # Annotated screenshot with refs
$B click @e3               # Click element by ref
$B fill @e5 "text"         # Fill input
$B select @e7 "option"     # Select dropdown
$B hover @e8               # Hover over element
$B scroll                  # Scroll down
$B scroll-to @e9           # Scroll to element
$B back                    # Go back
$B forward                 # Go forward
$B refresh                 # Refresh page
$B wait-for "text"         # Wait for text
$B wait-for @e5            # Wait for element
$B console                 # Show console logs
$B network                 # Show network logs
$B cookies                 # List cookies
$B pdf                     # Save as PDF
$B screenshot              # Full page screenshot
$B stop                    # Stop browser daemon
```

## Element Refs

Refs are automatically assigned in snapshots:
- `@e1`, `@e2` — ARIA tree elements (buttons, links, inputs)
- `@c1`, `@c2` — Cursor-pointer elements (clickable divs)

**Using refs:**
```bash
$B snapshot -i             # Shows: @e3 [button] "Submit"
$B click @e3               # Clicks that button
```

**Ref lifecycle:** Cleared on navigation. Always re-snapshot after page changes.

## Commands

### Navigation

```bash
$B goto https://example.com
$B goto /path              # Relative to current domain
$B back
$B forward
$B refresh
```

### Interaction

```bash
$B click @e3               # Click element
$B click -x                # Force click (skip visibility check)
$B dblclick @e3            # Double click
$B fill @e5 "text"         # Fill input
$B fill @e5 ""             # Clear input
$B select @e7 "Option 1"   # Select by text
$B select @e7 -v "value"   # Select by value
$B hover @e8               # Hover (triggers :hover, tooltips)
$B scroll                  # Scroll down
$B scroll 500              # Scroll 500px
$B scroll-to @e9           # Scroll element into view
```

### Verification

```bash
$B wait-for "text"         # Wait for text (30s timeout)
$B wait-for @e5            # Wait for element
$B wait-for -t 5 "text"    # 5 second timeout
$B console                 # Show console logs since last call
$B network                 # Show network requests
$B cookies                 # List cookie domains
```

### Capture

```bash
$B snapshot -i             # Annotated screenshot with refs
$B snapshot                # Screenshot without annotations
$B screenshot              # Full page screenshot
$B pdf                     # Save as PDF
$B html                    # Save HTML
```

### Control

```bash
$B stop                    # Stop browser daemon
$B status                  # Show daemon status
```

## Workflow

### Basic QA Flow

```bash
# Start testing
$B goto https://staging.myapp.com
$B snapshot -i

# Navigate and interact
$B click @e3               # Login button
$B wait-for @e5            # Wait for form
$B fill @e5 "user@example.com"
$B fill @e6 "password"
$B click @e7               # Submit

# Verify
$B wait-for "Welcome"
$B snapshot -i

# Check for errors
$B console | grep -i error
```

### Form Testing

```bash
$B goto /signup
$B snapshot -i

$B fill @e3 "Test User"
$B fill @e4 "test@example.com"
$B select @e5 "United States"
$B click @e6               # Terms checkbox
$B click @e7               # Submit

$B wait-for "Check your email"
$B snapshot -i
```

### Debug Mode

```bash
$B console                 # See JS errors
$B network                 # See failed requests
$B cookies                 # Check auth state
```

## Safety

- **Localhost only** — HTTP server binds to localhost, not network
- **Bearer token** — Each session has unique auth token
- **30-min timeout** — Auto-shuts down when idle
- **Read-only cookies** — Never modifies real browser's cookies

## Troubleshooting

**Refs not found:**
- Run `$B snapshot -i` again after navigation
- Check if element is in shadow DOM

**Element not clickable:**
- Try `$B click -x @e3` (force click)
- Check if element is off-screen
- Use `$B scroll-to @e3` first

**Page not loading:**
- Check `$B network` for failed requests
- Check `$B console` for JS errors
- Verify URL with `$B goto`

## Output

Every command returns structured output:
```
URL: https://example.com/dashboard
Title: Dashboard
Refs: @e1 [link] "Home", @e2 [button] "Profile", @e3 [heading] "Welcome"
```

## Trigger Phrases

- "Test this site"
- "Open the browser"
- "QA this"
- "Check if it works"
