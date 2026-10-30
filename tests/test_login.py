
from playwright.sync_api import Page, expect
import pytest
from pages.loginPage import loginPage

@pytest.mark.login
@pytest.mark.smoke
def test_valid_login(page: Page, navigate_to_login_page):
    """Test login with valid credentials (success scenario)"""
    login_page = loginPage(page)
    
    # Fill valid credentials and click login
    login_page.login("ram@rirabh.com", "Admin@7192")
    
    # Assert successful redirect to dashboard
    page.wait_for_timeout(5000)
    expect(page).to_have_url("https://app.wowpbx.com/dashboard", timeout=30000)
    page.wait_for_timeout(10000)


@pytest.mark.login
@pytest.mark.regression
def test_invalid_login(page: Page, navigate_to_login_page):
    """Test login with incorrect credentials (failure/error handling scenario)"""
    login_page = loginPage(page)
    
    # Fill invalid credentials and click login
    login_page.login("wrong_user@rirabh.com", "WrongPassword123")
    
    # Assert that an error alert appears and we stay on the login page
    expect(login_page.error_message).to_be_visible(timeout=10000)
    # Use exact string match here:
    expect(page).to_have_url("https://app.wowpbx.com/login")
    


# import pytest
# from playwright.sync_api import Page, expect
# from pages.loginPage import loginPage  # Import the Page Object class

# @pytest.mark.login
# @pytest.mark.smoke
# @pytest.mark.regression
# def test_page_components(page: Page, navigate_to_login_page):
#     # Initialize the login page object
#     login_page_obj = loginPage(page)

#     try:
#         # Filling username using the page object locator
#         login_page_obj.username_input.fill("ram@rirabh.com")
#     except Exception as e:
#         page.screenshot(path="login_failure.png")
#         raise e

#     # Filling password and clicking login via page object locators
#     login_page_obj.password_input.fill("Admin@7192")
#     login_page_obj.login_button.click()

#     # Verifying success dashboard redirection
#     expect(page).to_have_url("https://app.wowpbx.com/dashboard", timeout=30000)
#     page.wait_for_timeout(10000)