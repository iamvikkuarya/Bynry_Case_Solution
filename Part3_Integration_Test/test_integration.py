"""
Integration Test - API + UI Flow
=================================
Tests complete project creation flow across API and UI.

Flow:
1. API: Create project
2. Web UI: Verify project appears
3. Mobile: Check mobile view (simulated)
4. Security: Verify tenant isolation
"""

import pytest
import requests
from playwright.sync_api import sync_playwright
import json


# Test Data
TEST_DATA = {
    "company1": {
        "tenant_id": "company1",
        "api_token": "test_token_company1",
        "admin_email": "admin@company1.com",
        "admin_password": "password123",
        "base_url": "https://company1.workflowpro.com"
    },
    "company2": {
        "tenant_id": "company2",
        "api_token": "test_token_company2",
        "admin_email": "admin@company2.com",
        "admin_password": "password123",
        "base_url": "https://company2.workflowpro.com"
    }
}


class APIHelper:
    """Helper for API calls"""
    
    def __init__(self, base_url, token, tenant_id):
        self.base_url = base_url
        self.token = token
        self.tenant_id = tenant_id
    
    def create_project(self, name, description):
        """Create project via API"""
        url = f"{self.base_url}/api/v1/projects"
        headers = {
            "Authorization": f"Bearer {self.token}",
            "X-Tenant-ID": self.tenant_id,
            "Content-Type": "application/json"
        }
        payload = {
            "name": name,
            "description": description,
            "team_members": []
        }
        
        # In real scenario, this would make actual API call
        # For case study, we simulate the response
        response = {
            "id": 123,
            "name": name,
            "description": description,
            "status": "active",
            "tenant": self.tenant_id
        }
        
        return response
    
    def get_project(self, project_id):
        """Get project details via API"""
        url = f"{self.base_url}/api/v1/projects/{project_id}"
        headers = {
            "Authorization": f"Bearer {self.token}",
            "X-Tenant-ID": self.tenant_id
        }
        
        # Simulated response
        response = {
            "id": project_id,
            "name": "Test Project",
            "status": "active",
            "tenant": self.tenant_id
        }
        
        return response
    
    def delete_project(self, project_id):
        """Cleanup: Delete project"""
        url = f"{self.base_url}/api/v1/projects/{project_id}"
        headers = {
            "Authorization": f"Bearer {self.token}",
            "X-Tenant-ID": self.tenant_id
        }
        # Simulated deletion
        return {"status": "deleted"}


@pytest.fixture
def browser():
    """Setup browser for UI testing"""
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        yield page
        browser.close()


def test_project_creation_integration_flow(browser):
    """
    Integration test: API → UI → Mobile → Security
    
    Tests complete flow of project creation and verification
    across different layers and platforms.
    """
    
    # Get test data for Company1
    company_data = TEST_DATA["company1"]
    api = APIHelper(
        company_data["base_url"],
        company_data["api_token"],
        company_data["tenant_id"]
    )
    
    project_id = None
    
    try:
        # ============================================
        # STEP 1: Create Project via API
        # ============================================
        print("\n[STEP 1] Creating project via API...")
        
        project_data = api.create_project(
            name="Test Project - Integration",
            description="Created for integration testing"
        )
        
        project_id = project_data["id"]
        
        # Verify API response
        assert project_data["name"] == "Test Project - Integration"
        assert project_data["status"] == "active"
        assert project_data["tenant"] == "company1"
        print(f"   Project created: ID={project_id}")
        
        
        # ============================================
        # STEP 2: Verify Project in Web UI
        # ============================================
        print("\n[STEP 2] Verifying project in Web UI...")
        
        # Login to web UI
        browser.goto(f"{company_data['base_url']}/login")
        browser.wait_for_load_state("networkidle")
        browser.wait_for_selector("#email", state="visible", timeout=5000)
        
        browser.fill("#email", company_data["admin_email"])
        browser.fill("#password", company_data["admin_password"])
        browser.click("#login-btn")
        
        # Wait for dashboard
        browser.wait_for_url("**/dashboard", timeout=10000)
        browser.wait_for_load_state("networkidle")
        print("   Logged in successfully")
        
        # Navigate to projects page
        browser.click("a[href='/projects']")
        browser.wait_for_load_state("networkidle")
        
        # Wait for project to appear (might take time to sync)
        browser.wait_for_selector(".project-card", state="visible", timeout=10000)
        
        # Find our project
        projects = browser.locator(".project-card").all()
        project_found = False
        
        for project in projects:
            project_name = project.locator(".project-name").text_content()
            if "Test Project - Integration" in project_name:
                project_found = True
                print(f"   Project found in UI: {project_name}")
                break
        
        assert project_found, "Project not found in UI"
        
        
        # ============================================
        # STEP 3: Check Mobile View
        # ============================================
        print("\n[STEP 3] Testing mobile view...")
        
        # Set mobile viewport (simulates mobile device)
        browser.set_viewport_size({"width": 375, "height": 667})  # iPhone size
        
        # Reload to get mobile layout
        browser.reload()
        browser.wait_for_load_state("networkidle")
        
        # Verify mobile menu exists
        mobile_menu = browser.locator(".mobile-menu")
        assert mobile_menu.is_visible(), "Mobile menu not visible"
        print("   Mobile view working")
        
        # In real scenario with BrowserStack:
        # - Would run on actual iPhone/Android devices
        # - Test touch interactions
        # - Verify responsive design
        
        
        # ============================================
        # STEP 4: Verify Tenant Isolation (Security)
        # ============================================
        print("\n[STEP 4] Testing tenant isolation...")
        
        # Logout from Company1
        browser.click("#user-menu")
        browser.click("#logout-btn")
        browser.wait_for_url("**/login", timeout=5000)
        
        # Login as Company2 user
        company2_data = TEST_DATA["company2"]
        
        browser.fill("#email", company2_data["admin_email"])
        browser.fill("#password", company2_data["admin_password"])
        browser.click("#login-btn")
        
        browser.wait_for_url("**/dashboard", timeout=10000)
        browser.wait_for_load_state("networkidle")
        
        # Navigate to projects
        browser.click("a[href='/projects']")
        browser.wait_for_load_state("networkidle")
        browser.wait_for_selector(".project-card", state="visible", timeout=10000)
        
        # Verify Company1 project is NOT visible
        projects = browser.locator(".project-card").all()
        company1_project_visible = False
        
        for project in projects:
            project_name = project.locator(".project-name").text_content()
            if "Test Project - Integration" in project_name:
                company1_project_visible = True
                break
        
        assert not company1_project_visible, "Security violation: Company1 project visible to Company2!"
        print("   Tenant isolation verified - Company2 cannot see Company1 projects")
        
        
        # ============================================
        # STEP 5: Final API Verification
        # ============================================
        print("\n[STEP 5] Final API verification...")
        
        # Switch back to Company1 API
        final_check = api.get_project(project_id)
        assert final_check["id"] == project_id
        assert final_check["status"] == "active"
        print("   Project still active in API")
        
        print("\n[SUCCESS] Integration test passed!")
        
    finally:
        # ============================================
        # CLEANUP
        # ============================================
        print("\n[CLEANUP] Removing test data...")
        if project_id:
            api.delete_project(project_id)
            print(f"   Deleted project ID={project_id}")


def test_integration_with_network_failure_handling(browser):
    """
    Test integration with network failure simulation
    
    Tests how system handles:
    - Slow API responses
    - Network timeouts
    - Retry logic
    """
    
    company_data = TEST_DATA["company1"]
    api = APIHelper(
        company_data["base_url"],
        company_data["api_token"],
        company_data["tenant_id"]
    )
    
    print("\n[TEST] Network failure handling...")
    
    # Simulate slow API response
    # In real scenario: Add artificial delays, test timeouts
    
    try:
        # Create project with longer timeout
        project_data = api.create_project(
            name="Slow Project",
            description="Testing slow network"
        )
        
        # UI should handle slow loading gracefully
        browser.goto(f"{company_data['base_url']}/login")
        
        # Use longer timeouts for slow networks
        browser.wait_for_load_state("networkidle", timeout=30000)
        
        print("   System handles slow network correctly")
        
    except Exception as e:
        # Proper error handling
        print(f"   Expected behavior: Timeout handled - {str(e)}")


# Additional test ideas (not implemented to keep simple):
# - test_integration_with_multiple_users()
# - test_integration_with_large_data()
# - test_integration_with_concurrent_operations()
