# My Testing Approach

**How I debugged the flaky tests**

---

## Step 1: Read the case study

I started by understanding what the app does:
- B2B SaaS platform (WorkflowPro)
- Multi-tenant (different companies use it)
- Has 2FA for some users
- Uses AJAX to load data

This helped me know what problems to look for.

---

## Step 2: Look for common flaky patterns

I went through the code looking for these issues:

**Race conditions:** Code that checks things too quickly
- Found: Click → immediate assert (no wait)

**Dynamic loading:** Assuming AJAX is instant
- Found: Getting elements before they load

**2FA:** Some users have it, some don't
- Found: Code doesn't handle both cases

**Cleanup:** Browser not closing properly
- Found: browser.close() at end (doesn't run if test fails)

**Different data sizes:** Small vs large companies
- Found: No timeout consideration

---

## Step 3: Fix each issue

For each problem, I:
1. Understood WHY it fails
2. Added proper wait
3. Tested the fix

### Main fixes:
- Added `wait_for_url()` after clicks
- Added `wait_for_selector()` before getting elements
- Added 2FA handling with if statement
- Used pytest fixture for cleanup
- Used 30s timeout for large companies

---

## Why I made these choices

### Choice 1: pytest fixtures
I used fixtures instead of try/finally because:
- Simpler code
- Cleanup ALWAYS runs
- Standard practice

### Choice 2: Explicit waits
I used `wait_for_selector()` instead of just hoping elements exist because:
- More reliable
- Clear what I'm waiting for
- Can set different timeouts

### Choice 3: 30 second timeout
For large companies (50,000 projects), loading takes 4+ seconds. 30s gives enough buffer.
**Important:** It waits UP TO 30s, not always 30s!

---

## What I learned

1. **Most flaky tests = timing issues** - Code checks before things are ready
2. **CI/CD is slower** - What works locally might fail there
3. **Always wait before asserting** - Click → Wait → Assert
4. **Handle all flows** - Don't assume happy path (2FA example)

---

## Key takeaways

**Do:**
- Wait for what you're checking
- Use pytest fixtures for cleanup
- Handle conditional flows (2FA)
- Test with large data

**Don't:**
- Assert immediately after action
- Assume elements are ready
- Forget cleanup
- Use same test data everywhere
