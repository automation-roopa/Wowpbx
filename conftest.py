

import pytest

@pytest.fixture
def navigate_to_login_page(page):
    # 1. Navigate and only wait for the basic HTML content to load (faster and less prone to timeout)
    page.goto("https://app.wowpbx.com/login", wait_until="domcontentloaded", timeout=60000)
    
    # 2. Wait for a specific login element to be visible to ensure the app is interactive
    # (Using a generic selector that covers username/email fields)
    page.locator('input').first.wait_for(state="visible", timeout=15000)
    
    yield page