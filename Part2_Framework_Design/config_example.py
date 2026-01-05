"""
Sample Configuration File
=========================
Shows how config would work in the framework.
"""

import os

class Config:
    """Main configuration class"""
    
    # Environment selection
    ENV = os.getenv("ENV", "staging")  # Can be: dev, staging, prod
    
    # Browser selection
    BROWSER = os.getenv("BROWSER", "chrome")  # Can be: chrome, firefox, safari
    
    # Execution mode
    HEADLESS = os.getenv("HEADLESS", "true").lower() == "true"
    
    # Timeouts (in milliseconds)
    DEFAULT_TIMEOUT = 10000
    SLOW_TIMEOUT = 30000  # For large data loads
    
    # Parallel execution
    PARALLEL_WORKERS = int(os.getenv("WORKERS", "4"))


class Environments:
    """URLs for different environments"""
    
    ENVIRONMENTS = {
        "dev": {
            "web_url": "https://dev.workflowpro.com",
            "api_url": "https://api-dev.workflowpro.com"
        },
        "staging": {
            "web_url": "https://staging.workflowpro.com",
            "api_url": "https://api-staging.workflowpro.com"
        },
        "prod": {
            "web_url": "https://workflowpro.com",
            "api_url": "https://api.workflowpro.com"
        }
    }
    
    @staticmethod
    def get_url(env, url_type="web"):
        """Get URL for environment"""
        return Environments.ENVIRONMENTS[env][f"{url_type}_url"]


class Tenants:
    """Settings for different companies"""
    
    TENANTS = {
        "company1": {
            "subdomain": "company1",
            "url": "https://company1.workflowpro.com",
            "users": {
                "admin": {
                    "email": "admin@company1.com",
                    "password": os.getenv("COMPANY1_ADMIN_PASS", "password123")
                },
                "manager": {
                    "email": "manager@company1.com",
                    "password": os.getenv("COMPANY1_MANAGER_PASS", "password123")
                },
                "employee": {
                    "email": "employee@company1.com",
                    "password": os.getenv("COMPANY1_EMP_PASS", "password123")
                }
            }
        },
        "company2": {
            "subdomain": "company2",
            "url": "https://company2.workflowpro.com",
            "users": {
                "admin": {
                    "email": "admin@company2.com",
                    "password": os.getenv("COMPANY2_ADMIN_PASS", "password123")
                },
                "manager": {
                    "email": "manager@company2.com",
                    "password": os.getenv("COMPANY2_MANAGER_PASS", "password123")
                },
                "employee": {
                    "email": "employee@company2.com",
                    "password": os.getenv("COMPANY2_EMP_PASS", "password123")
                }
            }
        }
    }
    
    @staticmethod
    def get_user(tenant, role):
        """Get user email and password"""
        return Tenants.TENANTS[tenant]["users"][role]


class BrowserStackConfig:
    """Settings for BrowserStack (mobile testing)"""
    
    # Login info (from environment variables)
    USERNAME = os.getenv("BROWSERSTACK_USERNAME")
    ACCESS_KEY = os.getenv("BROWSERSTACK_ACCESS_KEY")
    
    # Desktop browsers
    DESKTOP_BROWSERS = [
        {
            "os": "Windows",
            "os_version": "11",
            "browser": "Chrome",
            "browser_version": "latest"
        },
        {
            "os": "OS X",
            "os_version": "Ventura",
            "browser": "Safari",
            "browser_version": "16"
        }
    ]
    
    # Mobile devices
    MOBILE_DEVICES = [
        {
            "device": "iPhone 14",
            "os_version": "16",
            "browserName": "safari"
        },
        {
            "device": "Samsung Galaxy S22",
            "os_version": "12",
            "browserName": "chrome"
        }
    ]


# How to use:
# ===========

# Get URL:
# url = Environments.get_url(Config.ENV)

# Get user:
# user = Tenants.get_user("company1", "admin")
# email = user["email"]

# Check headless:
# if Config.HEADLESS:
#     print("Browser hidden")
