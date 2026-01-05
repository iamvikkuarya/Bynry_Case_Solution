"""
Original Flaky Test Code

Issues: Multiple flakiness problems (see test_report.md for analysis)
"""

import pytest
from playwright.sync_api import sync_playwright

def test_user_login():
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()
        
        # Navigate to login page
        page.goto("https://app.workflowpro.com/login")
        
        # Fill login form
        page.fill("#email", "admin@company1.com")
        page.fill("#password", "password123")
        page.click("#login-btn")
        
        # Verify successful login
        assert page.url == "https://app.workflowpro.com/dashboard"
        assert page.locator(".welcome-message").is_visible()
        
        browser.close()

def test_multi_tenant_access():
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()
        
        page.goto("https://app.workflowpro.com/login")
        page.fill("#email", "user@company2.com")
        page.fill("#password", "password123")
        page.click("#login-btn")
        
        # User should only see Company2 data
        projects = page.locator(".project-card").all()
        for project in projects:
            assert "Company2" in (project.text_content() or "")
        
        browser.close()
