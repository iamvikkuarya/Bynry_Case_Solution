# Bynry Case Study - My Solution

**Name:** Vivek Kumar 
**Date:** January 6, 2026 

---

## What's in this repo

I've organized my case study solutions into 3 folders (one for each part):

```
Part1_Flaky_Tests/       # Debugging flaky tests (30 min)
Part2_Framework_Design/   # Framework architecture (25 min)  
Part3_Integration_Test/   # API + UI + Mobile test (35 min)
```

Each folder has:
- README - how to run/understand it
- Test scripts/code
- Test plan
- Test data
- Report of what I did
- My approach/reasoning

---

## How to check my work

**Option 1:** Just read through each folder
- Start with Part1, then Part2, then Part3
- Each README explains what I did

**Option 2:** Run the code
```bash
cd Part1_Flaky_Tests
pytest fixed_code.py

cd Part3_Integration_Test  
pytest test_integration.py
```
*(Needs Python, Playwright installed)*

---

## What I learned

This case study helped me understand:
- Why tests become flaky (race conditions, timing issues)
- How to use Playwright waits properly
- pytest fixtures for setup/cleanup
- Multi-tenant testing challenges
- Why CI/CD is different from local testing

---

## Quick Summary

**Part 1:** Found 7 issues in flaky test code, fixed all of them  
**Part 2:** Designed framework structure for web + mobile + API testing  
**Part 3:** Wrote full integration test (create via API → verify in UI → check mobile)

---

**Contact:** [Vivekkumararya2179@gmail.com]  

Thanks for reviewing! Happy to answer any questions.
