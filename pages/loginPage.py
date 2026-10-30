from playwright.sync_api import Page, expect

class loginPage:
    def __init__(self, page: Page):
        self.page = page
        
        # Locators
        self.username_input = page.get_by_placeholder("user name or email", exact=False)
        self.password_input = page.locator('input[type="password"]')
        self.login_button = page.locator("button.login-form-button")
        
        # Locator for login error message/toast
        self.error_message = page.locator(".ant-message-error, .error-notification, .alert-danger")

    def login(self, username: str, password: str):
        self.username_input.fill(username)
        self.password_input.fill(password)
        self.login_button.click()





# from playwright.sync_api import Page, expect

# class loginPage:
#     def __init__(self, page: Page):
#         self.page = page
        
#         # 1. Define page locators
#         self.username_input = page.get_by_placeholder("user name or email", exact=False)
#         self.password_input = page.locator('input[type="password"]')
#         self.login_button = page.locator("button.login-form-button")

#     # 2. Define action methods
#     def enter_username(self, username: str):
#         self.username_input.fill(username)

#     def enter_password(self, password: str):
#         self.password_input.fill(password)

#     def click_login(self):
#         self.login_button.click()

#     def login_to_application(self, username: str, password: str):
#         """Combined method to perform end-to-end login"""
#         self.enter_username(username)
#         self.enter_password(password)
#         self.click_login()