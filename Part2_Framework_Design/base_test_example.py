"""Base Classes Example

Shows how base classes make code reusable.
"""

import pytest
from playwright.sync_api import sync_playwright


class BasePage:
    """
    Base class for all page objects.
    Has common methods so we don't repeat code.
    """
    
    def __init__(self, page):
        self.page = page
    
    def goto(self, url):
        """Navigate to URL"""
        self.page.goto(url)
        self.page.wait_for_load_state("networkidle")
    
    def click(self, selector):
        """Wait then click"""
        self.page.wait_for_selector(selector, state="visible")
        self.page.click(selector)
    
    def fill(self, selector, text):
        """Wait then fill input"""
        self.page.wait_for_selector(selector, state="visible")
        self.page.fill(selector, text)
    
    def get_text(self, selector):
        """Get text from element"""
        self.page.wait_for_selector(selector, state="visible")
        return self.page.locator(selector).text_content()
    
    def is_visible(self, selector):
        """Check if element visible"""
        return self.page.locator(selector).is_visible()
    
    def wait_for_url(self, url_pattern):
        """Wait for URL change"""
        self.page.wait_for_url(url_pattern)


class LoginPage(BasePage):
    """
    Login page object.
    Inherits common methods from BasePage.
    """
    
    def __init__(self, page):
        super().__init__(page)
        # Locators
        self.email_input = "#email"
        self.password_input = "#password"
        self.login_btn = "#login-btn"
        self.error_msg = ".error-message"
    
    def login(self, email, password):
        """Perform login"""
        self.fill(self.email_input, email)
        self.fill(self.password_input, password)
        self.click(self.login_btn)
    
    def get_error(self):
        """Get error message"""
        return self.get_text(self.error_msg)


class BaseTest:
    """
    Base test class.
    Handles browser setup and cleanup.
    """
    
    @pytest.fixture(autouse=True)
    def setup(self):
        """Setup before each test"""
        # Launch browser
        with sync_playwright() as p:
            self.browser = p.chromium.launch(headless=True)
            self.page = self.browser.new_page()
            
            yield  # Test runs here
            
            # Always cleanup
            self.browser.close()


# Example Test
class TestLogin(BaseTest):
    """
    Example test - inherits from BaseTest.
    Gets browser setup/cleanup automatically.
    """
    
    def test_valid_login(self):
        """Test login with valid credentials"""
        # Create page object
        login_page = LoginPage(self.page)
        
        # Perform actions
        login_page.goto("https://staging.workflowpro.com/login")
        login_page.login("admin@company1.com", "password123")
        
        # Verify
        login_page.wait_for_url("**/dashboard")
        assert "/dashboard" in self.page.url
    
    def test_invalid_login(self):
        """Test login with invalid credentials"""
        login_page = LoginPage(self.page)
        
        login_page.goto("https://staging.workflowpro.com/login")
        login_page.login("wrong@email.com", "wrongpass")
        
        # Verify error appears
        error = login_page.get_error()
        assert "Invalid credentials" in error


# Why this design?
# ================
# 1. BasePage has all common stuff (click, fill, etc)
# 2. LoginPage only has login stuff
# 3. BaseTest sets up browser automatically
# 4. TestLogin has clean test code

# Benefits:
# =========
# - No repeated code
# - Easy to maintain
# - Change selector once, works everywhere
# - Easy to understand
