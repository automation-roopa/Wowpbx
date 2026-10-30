from playwright.sync_api import Page, expect
import pytest
from pages.loginPage import loginPage
from pages.resultPage import resultPage  # Import the login page object

@pytest.mark.regression
@pytest.mark.smoke
@pytest.mark.results
def test_validateTheresultsUI(page: Page, navigate_to_login_page):
    # 1. Initialize the Login Page Object
    login_page_obj = loginPage(page)
    results_page_obj = resultPage(page)

    # 2. Perform login actions using the Page Object Model method
    login_page_obj.username_input.fill("ram@rirabh.com")
    login_page_obj.password_input.fill("Admin@7192")
    login_page_obj.login_button.click()

    # 3. Validate results/dashboard using the resultPage object method
    result_page_obj.verify_dashboard_loaded() # pyright: ignore[reportUndefinedVariable]