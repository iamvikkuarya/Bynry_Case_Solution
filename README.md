# playwright-qa-framework

End-to-end QA automation framework built with Playwright and pytest, covering flaky test diagnosis, multi-layer framework design, and full integration testing across API and UI layers.

## Structure
Part1_Flaky_Tests/       # Flaky test analysis and fixes
Part2_Framework_Design/  # Framework architecture design
Part3_Integration_Test/  # API-to-UI integration test suite

## What's covered

**Part 1 — Flaky Test Diagnosis**
Identified and fixed 7 issues in an existing test suite — race conditions, improper waits, missing fixtures, and timing-dependent assertions.

**Part 2 — Framework Design**
Designed a scalable test framework architecture supporting web, mobile, and API testing layers with clear separation of concerns.

**Part 3 — Integration Testing**
Full integration test covering end-to-end flow: create entity via API → verify in UI → validate on mobile.

## Stack

Python · Playwright · pytest · GitHub Actions

## Setup & Run

```bash
# Install dependencies
pip install playwright pytest
playwright install

# Run flaky test fixes
cd Part1_Flaky_Tests
pytest fixed_code.py

# Run integration tests
cd Part3_Integration_Test
pytest test_integration.py
```

## Contact

vivekkumararya2179@gmail.com
