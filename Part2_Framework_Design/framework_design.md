# My Framework Design

**How I'd organize the test automation framework**

---

## What Is a Framework?

It's the structure for organizing test code so:
- Tests don't repeat code
- Easy to add new tests
- Easy to run on different browsers/devices
- Easy for team to understand

---

## My Setup

**Tools I'd use:**
- Python + pytest - For running tests
- Playwright - For browser automation
- Requests - For API testing
- BrowserStack - For mobile devices

---

## Folder Structure

```
framework/
├── config/          # Settings (URLs, browsers, etc.)
├── pages/           # Page objects (login_page.py, dashboard_page.py)
├── tests/           # Actual test files
│   ├── ui/         # Web tests
│   ├── api/        # API tests
│   └── mobile/     # Mobile tests
├── utils/           # Helper functions
└── data/            # Test data (JSON files)
```

See [folder_structure.txt](folder_structure.txt) for full structure.

---

## Main Ideas

### 1. Page Object Pattern

Instead of this (messy):
```python
def test_login():
    page.fill("#email", "test@test.com")
    page.fill("#password", "pass123")
    page.click("#login-btn")
```

Do this (clean):
```python
def test_login():
    login_page.login("test@test.com", "pass123")
```

All the selectors (#email, #password) go in `pages/login_page.py`.

### 2. Config File

One place for all settings:
```python
config = {
    "browser": "chrome",      # Can change to firefox
    "env": "staging",         # Can change to dev/prod
    "headless": True          # Can change to False
}
```

Run tests on different environments without changing test code.

### 3. Reusable Fixtures

Setup browser once, use in all tests:
```python
@pytest.fixture
def browser():
    browser = launch()
    yield browser
    browser.close()  # Always closes
```

---

## Handling Requirements

**Multiple browsers (Chrome, Firefox, Safari):**
- Config file has browser setting
- BrowserFactory creates the right browser

**Mobile (iOS, Android):**
- Use BrowserStack
- Config has device settings (iPhone 14, Galaxy S22)

**Multiple tenants (company1, company2):**
- Config file has tenant URLs
- Tests pick which tenant to use

**Different user roles (Admin, Manager, Employee):**
- Data file has users with roles
- Tests log in as needed user

---

## Example Files

See working examples:
- [config_example.py](config_example.py) - Shows config structure
- [base_test_example.py](base_test_example.py) - Shows base classes

---

## CI/CD Integration

Tests run automatically on GitHub:
```yaml
on: push
run: pytest
```

When code is pushed → Tests run → Results emailed

---

## What Makes This Good

1. **Organized** - Everything has a place
2. **No duplication** - Common code in one place
3. **Easy to change** - Change config, not every test
4. **Scales** - Easy to add more tests

---

## What I'd Ask Before Building

See [missing_requirements.md](missing_requirements.md) for full list of questions about:
- Where to store test data
- What info to include in reports
- How many tests to run at once
- How to handle passwords/secrets
