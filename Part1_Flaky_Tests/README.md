# Part 1: Debugging Flaky Test Code

**Time Allocated:** 30 minutes  
**Status:** Completed

---

## What's in this folder

```
Part1_Flaky_Tests/
├── README.md              # This file
├── flaky_code.py          # Original flaky code (provided)
├── fixed_code.py          # My fixed version
├── test_plan.md           # How I approached debugging
├── test_data.json         # Test user data
├── test_report.md         # Issues found & fixes
└── testing_approach.md    # My methodology
```

---

## Quick Start

### To see the problem:
```bash
# Run the flaky code multiple times
for i in {1..5}; do python -m pytest flaky_code.py; done
# You'll see it fails randomly
```

### To see the fix:
```bash
# Install dependencies
pip install pytest playwright

# Run fixed version
pytest fixed_code.py -v
```

---

## What I Found

**7 Major Issues** causing flakiness:

1.  **Race Condition** - No wait after login click
2.  **Dynamic Loading** - No wait for project cards
3.  **Variable Data Size** - Different tenants load at different speeds
4.  **No SPA Wait** - Form elements might not be ready
5.  **Missing 2FA Handling** - Some users have 2FA, test doesn't handle it
6.  **No Cleanup** - Browser stays open if test fails
7.  **Hardcoded Data** - Same credentials for parallel tests

---

## Key Fixes Applied

### Before (Flaky):
```python
page.click("#login-btn")
assert page.url == "https://app.workflowpro.com/dashboard"  # Fails!
```

### After (Reliable):
```python
page.click("#login-btn")
page.wait_for_url("**/dashboard", timeout=10000)  # Waits for redirect
assert "/dashboard" in page.url
```

---

## Files Explained

- **flaky_code.py** - Original buggy code
- **fixed_code.py** - All issues resolved  
- **test_report.md** - Detailed analysis of each issue
- **testing_approach.md** - Why I chose these fixes
- **test_plan.md** - How I debugged it
- **test_data.json** - Test users

---

## How to Run

```bash
# Original flaky version (fails randomly)
pytest flaky_code.py

# Fixed version (works every time)
pytest fixed_code.py
```

---

## What I Learned

- Always wait before checking things
- CI/CD is slower than local testing
- Use pytest fixtures for cleanup
- Handle 2FA (doesn't always appear)
- Big companies take longer to load data

---

**Time:** 30 minutes  
**Result:** All tests now reliable!
