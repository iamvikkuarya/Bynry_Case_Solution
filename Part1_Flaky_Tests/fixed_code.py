"""
This is the fixed version after finding the flaky issues.

What I fixed:
1. Added waits before checking things
2. Used pytest fixture so browser always closes
3. Handle 2FA (appears sometimes)
4. Wait longer for big companies (50,000 projects)
"""

import pytest
from playwright.sync_api import sync_playwright


# Pytest fixture - ensures browser closes even if test fails
@pytest.fixture
def page():
    """Open browser before test, close after test."""
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        yield page
        browser.close()  # Always runs!


def test_user_login_fixed(page):
    """Test login with proper waits."""
    
    # Login info
    test_email = "admin@company1.com"
    test_password = "password123"
    
    # Go to login
    page.goto("https://app.workflowpro.com/login")
    
    # Wait for page to load (this was missing!)
    page.wait_for_load_state("networkidle")
    page.wait_for_selector("#email", state="visible", timeout=5000)
    
    # Fill form
    page.fill("#email", test_email)
    page.fill("#password", test_password)
    page.click("#login-btn")
    
    # Handle 2FA - sometimes appears, sometimes doesn't
    # Wait for EITHER dashboard or 2FA page
    page.wait_for_url("**/dashboard|**/2fa-verify", timeout=10000)
    
    # If we got 2FA, handle it
    if "/2fa-verify" in page.url:
        page.fill("#2fa-code", "123456")
        page.click("#verify-btn")
        page.wait_for_url("**/dashboard", timeout=10000)
    
    # Make sure we're on dashboard
    page.wait_for_url("**/dashboard", timeout=10000)
    page.wait_for_load_state("networkidle")
    
    # Wait for welcome message before checking
    page.wait_for_selector(".welcome-message", state="visible", timeout=5000)
    
    # Now check
    assert "/dashboard" in page.url
    assert page.locator(".welcome-message").is_visible()


def test_multi_tenant_access_fixed(page):
    """Test users only see their company's data."""
    
    # Company2 user
    test_email = "user@company2.com"
    test_password = "password123"
    
    page.goto("https://app.workflowpro.com/login")
    
    # Wait for form
    page.wait_for_load_state("networkidle")
    page.wait_for_selector("#email", state="visible", timeout=5000)
    
    # Login
    page.fill("#email", test_email)
    page.fill("#password", test_password)
    page.click("#login-btn")
    
    # Handle 2FA
    page.wait_for_url("**/dashboard|**/2fa-verify", timeout=10000)
    if "/2fa-verify" in page.url:
        page.fill("#2fa-code", "123456")
        page.click("#verify-btn")
        page.wait_for_url("**/dashboard", timeout=10000)
    
    # Wait for dashboard
    page.wait_for_url("**/dashboard", timeout=10000)
    page.wait_for_load_state("networkidle")
    
    # Wait longer - Company2 has 50,000 projects!
    # Takes 4+ seconds to load
    page.wait_for_selector(".project-card", state="visible", timeout=30000)
    
    # Get projects
    projects = page.locator(".project-card").all()
    
    # Check we got some
    assert len(projects) > 0, "No projects"
    
    # Check all belong to Company2
    for project in projects:
        text = project.text_content() or ""
        assert "Company2" in text
    
    print(f"All {len(projects)} projects belong to Company2")
