# Part 3: Integration Test

**Time Allocated:** 35 minutes  
**Status:** Completed

---

## What's in this folder

```
Part3_Integration_Test/
├── README.md                    # This file
├── test_integration.py          # Main integration test
├── test_plan.md                 # Test approach
├── test_data.json              # Test data
├── test_report.md              # Test execution report
└── testing_approach.md         # Methodology
```

---

## What This Tests

**Full User Journey:**
1. Create user via API
2. Login via UI
3. Create project/workflow via UI
4. Verify via API

Tests that API and UI work together correctly.

---

## Quick Start

```bash
# Install dependencies
pip install pytest playwright requests

# Run the test
pytest test_integration.py -v
```

---

## Test Flow

```
API: Create User
    ↓
UI: Login with new user
    ↓
UI: Create a project
    ↓
API: Verify project exists
    ↓
PASS
```

---

**Time:** 35 minutes  
**Result:** Integration test complete
