# Test Plan - Integration Test

**Plan for testing API + UI together**

---

## What I'm Testing

Complete flow:
1. API creates project
2. UI shows project
3. Works on mobile
4. Secure (other companies can't see)

---

## Approach

**Step 1: API Call (5 min)**
- Create project via API
- Save the project ID

**Step 2: UI Verification (10 min)**
- Login to dashboard
- Check if project appears

**Step 3: Mobile Test (10 min)**
- Switch to mobile view
- Verify mobile works

**Step 4: Security Test (10 min)**
- Login as different company
- Verify project NOT visible

---

## Tools

- pytest - Run tests
- Playwright - Browser automation
- requests - API calls (simulated)

---

## Test Data

Using 2 companies:
- **Company1** - Creates project
- **Company2** - Tries to see it (should fail)

---

## Expected Results

All checks pass:
- Project created via API
- Project visible in UI
- Works on mobile
- Tenant isolation working

---

## Edge Cases

1. API-UI sync delay (wait 10s)
2. Network issues (timeouts)
3. Mobile viewport different size

---

## Notes

- API responses simulated (no real environment)
- Would use BrowserStack for real mobile test
- Shows correct structure for actual implementation
- Both with known credentials

Project data:
- Name: "Test Project - Integration"
- Description: "Created for integration testing"

---

## Success Criteria

- API returns project with ID
- Project visible in UI
- Mobile view works
- Tenant isolation confirmed
- Cleanup successful
