from playwright.sync_api import Page, expect

class resultPage:
    def __init__(self, page: Page):
        self.page = page
        
        # Define locators for elements on the dashboard/results page
        # Example: Dashboard header, welcome message, or a profile element
        self.dashboard_header = page.locator("h1, .dashboard-title, .header-title")
        self.user_profile_icon = page.locator(".user-profile, .avatar")

    def verify_dashboard_loaded(self):
        """Validates that the dashboard URL and key UI components are visible"""
        expect(self.page).to_have_url(r".*wowpbx\.com/dashboard.*", timeout=30000)