# Questions I'd Ask

**Before building the framework, I need to know:**

---

## 1. Test Data

**Where should test data come from?**
- JSON files in the repo?
- Database?
- Create fresh data via API each time?

**How to handle cleanup?**
- Delete after each test?
- Reset database daily?

**My guess:** Use JSON files for now, create unique data per test

---

## 2. Reports

**What info should reports have?**
- Pass/fail count?
- Screenshots when test fails?
- How long tests took?

**Who sees them?**
- Just QA team?
- Developers too?
- Management?

**My guess:** Email report after test run with screenshots

---

## 3. Running Tests

**How many tests at once?**
- Run all in parallel?
- Run one at a time?
- How many workers?

**Which tests run when?**
- All tests on every commit?
- Only smoke tests on commit, full suite nightly?

**My guess:** 4 parallel workers, smoke tests on commit

---

## 4. BrowserStack

**Which devices to test?**
- iPhone 14, 15?
- Samsung Galaxy S22, S23?
- Tablets?

**How often?**
- Every test run?
- Only before release?

**My guess:** iPhone 14 + Galaxy S22, run before release (to save cost)

---

## 5. Passwords & Secrets

**Where to store passwords?**
- Environment variables?
- Secret management tool?

**API keys for BrowserStack?**
- How to keep them safe in code?

**My guess:** Use environment variables, never commit to git

---

## 6. Environments

**How many environments?**
- Dev, Staging, Prod?
- Separate URLs for each?

**Can we test on production?**
- Or only dev/staging?

**My guess:** Test on dev/staging only, never prod

---

## 7. Test Maintenance

**Who maintains tests?**
- QA team only?
- Developers help?

**When tests fail?**
- Who gets notified?
- How quickly to fix?

**My guess:** QA owns tests, devs help when needed

---

## 8. Flaky Tests

**How to handle flaky tests?**
- Retry automatically?
- Mark as known issue?
- How many retries?

**My guess:** Retry once, if still fails then real failure

---

## 9. Different User Roles

**How to test different permissions?**
- Admin can do everything
- Manager can do some things
- Employee limited access

**Do we have test accounts for each role?**

**My guess:** Create test users for each role in test data

---

## 10. CI/CD Pipeline

**Which CI tool?**
- GitHub Actions?
- Jenkins?
- Other?

**When to run tests?**
- On every push?
- Only on pull requests?

**My guess:** GitHub Actions, run on pull requests

---

## Summary

These are the main things I'd need to know before building the framework. Without answers, I'd make reasonable assumptions and ask for feedback.

**My Recommendation:**
- Use Allure reports (visual, detailed)
- Screenshot on failure
- Keep last 30 days of reports
- Send summary to Slack

---

## 3. Parallel Execution

**Questions:**

1. **How many tests run in parallel?**
   - 4 workers? 8 workers?
   - Based on available machines?

2. **Test isolation strategy?**
   - Each test uses different user?
   - Each test uses different browser instance?
   - How to prevent race conditions?

3. **Database handling in parallel?**
   - Shared database?
   - Each worker gets own database?
   - Row-level locking?

4. **BrowserStack parallel limits?**
   - How many parallel sessions allowed?
   - Cost implications?

**My Recommendation:**
- Start with 4 parallel workers
- Each test uses unique user email
- Increase parallelism after stability proven

---

## 4. Environment Management

**Questions:**

1. **How many environments?**
   - Dev, Staging, Prod?
   - Per-developer environments?

2. **Environment differences?**
   - Different URLs?
   - Different features enabled?
   - Different data?

3. **Environment refresh frequency?**
   - Staging reset daily? Weekly?
   - When to run tests against prod?

4. **Environment access?**
   - VPN required?
   - IP whitelisting?
   - Authentication tokens?

**My Recommendation:**
- Focus on Staging for now
- Dev for quick testing
- Prod only for smoke tests

---

## 5. Browser & Device Coverage

**Questions:**

1. **Which browser versions?**
   - Latest only?
   - Last 2 versions?
   - Specific version requirements?

2. **Mobile device priorities?**
   - Which iOS versions?
   - Which Android versions?
   - Real devices or emulators?

3. **Test frequency per platform?**
   - Chrome daily, others weekly?
   - Mobile on release only?

4. **BrowserStack costs?**
   - Budget limits?
   - When to use local vs BrowserStack?

**My Recommendation:**
- Chrome (latest) - every run
- Firefox, Safari - weekly
- Mobile - before releases

---

## 6. CI/CD Integration

**Questions:**

1. **When to run tests?**
   - Every commit?
   - Every PR?
   - Nightly builds?

2. **Test failure handling?**
   - Block deployment if tests fail?
   - Allow override?
   - Who gets notified?

3. **Test execution time limits?**
   - Max time for PR checks (10 min)?
   - Full suite acceptable time (2 hrs)?

4. **Retry strategy for flaky tests?**
   - Retry failed tests automatically?
   - How many retries?
   - Mark as flaky vs failed?

**My Recommendation:**
- Smoke tests on every PR (5 min)
- Full suite nightly
- Retry failed tests once

---

## 7. User Role Testing

**Questions:**

1. **How many roles to test?**
   - Admin, Manager, Employee only?
   - More roles?

2. **Permission differences?**
   - Specific list of permissions per role?
   - Can permissions change?

3. **Role switching in tests?**
   - Test role changes within one test?
   - Separate tests per role?

4. **Role-based test data?**
   - Pre-created users for each role?
   - Create on-the-fly?

**My Recommendation:**
- Test 3 main roles: Admin, Manager, Employee
- Separate tests per role
- Pre-defined test users in config

---

## 8. API Testing Scope

**Questions:**

1. **Which APIs to test?**
   - All endpoints?
   - Critical paths only?
   - Public APIs only?

2. **API test types?**
   - Functional testing?
   - Performance testing?
   - Security testing?

3. **API authentication?**
   - OAuth? JWT? API keys?
   - How to get tokens for tests?

4. **Response validation level?**
   - Status codes only?
   - Full response schema validation?
   - Data integrity checks?

**My Recommendation:**
- Test critical API endpoints
- Status codes + basic schema validation
- Use JWT tokens (stored in config)

---

## 9. Test Maintenance

**Questions:**

1. **Who maintains the tests?**
   - QA team only?
   - Developers write tests too?

2. **Code review process?**
   - All test code reviewed?
   - Who approves?

3. **Test updates?**
   - When UI changes, who updates tests?
   - Update tests before or after deployment?

4. **Documentation?**
   - How detailed?
   - Where stored?

**My Recommendation:**
- QA writes tests, developers review
- Update tests with feature development
- Document in README and inline comments

---

## 10. Performance & Scalability

**Questions:**

1. **Expected test suite size?**
   - 100 tests? 1000 tests?
   - Growth projection?

2. **Execution time goals?**
   - Full suite in under 1 hour?
   - Smoke suite in under 5 minutes?

3. **Resource constraints?**
   - CI/CD machine specs?
   - Memory/CPU limits?

4. **Test data volume?**
   - Small datasets okay?
   - Need to test with production-like data?

**My Recommendation:**
- Design for 500 tests initially
- Target: Full suite in 30 min (with parallelism)
- Smoke suite under 5 min

---

## Summary

**Top Priority Questions:**
1. Test data management strategy
2. CI/CD execution timing
3. Browser/device coverage scope
4. BrowserStack budget/limits
5. Parallel execution constraints

**Why these matter:**
- Affects framework architecture
- Impacts cost and time
- Determines tool choices
- Sets success criteria
