# Test Plan - Debugging Flaky Tests

**Goal:** Find and fix all the flaky issues in the test code

---

## My Approach

### Step 1: Read the code (5 min)
- Go through the flaky_code.py line by line
- Look for common problems that cause flakiness
- Make notes of suspicious lines

### Step 2: Find the issues (10 min)
Using a checklist:
- Are there waits after clicks?
- Are elements checked before they load?
- Is 2FA handled?
- Does browser cleanup happen?
- Are there hardcoded credentials?

### Step 3: Understand WHY they fail (5 min)
For each issue:
- Why does it cause random failures?
- When does it fail (local vs CI/CD)?
- How to fix it?

### Step 4: Write fixes (10 min)
- Add proper waits
- Use pytest fixtures
- Handle 2FA flow
- Test data from JSON

---

## What I'm Looking For

**Race Conditions:**
- Actions followed immediately by checks
- No waits after navigation

**Dynamic Content:**
- Getting elements without waiting
- AJAX calls not handled

**2FA Flow:**
- Code doesn't handle optional 2FA step

**Cleanup:**
- Browser not closing properly

**Data Issues:**
- Same credentials everywhere
- No timeout for large data

---

## Success Checklist

- Found 7+ issues
- Each issue explained
- Fixed code written
- Uses pytest fixtures
- Handles 2FA
- Works for both small and large companies
