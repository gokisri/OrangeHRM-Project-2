from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class ForgotPasswordPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)  # Explicit Wait for Stability

    # Locators
    FORGOT_PASSWORD_LINK = (By.XPATH, "//div[@class='orangehrm-login-forgot']")
    USERNAME_FIELD = (By.XPATH, "//input[@placeholder='Username']")
    RESET_BUTTON = (By.XPATH, "(//button[normalize-space()='Reset Password'])[1]")
    SUCCESS_MESSAGE = (By.XPATH, "//h6")  # More generic to match dynamic success messages

    def click_forgot_password_link(self):
        """Click the 'Forgot your password?' link"""
        self.wait.until(EC.element_to_be_clickable(self.FORGOT_PASSWORD_LINK)).click()

    def enter_username(self, username):
        """Enter the username in the forgot password field"""
        self.wait.until(EC.visibility_of_element_located(self.USERNAME_FIELD)).send_keys(username)

    def click_reset_password(self):
        """Click the Reset Password button"""
        self.wait.until(EC.element_to_be_clickable(self.RESET_BUTTON)).click()

    def get_success_message(self):
        """Get the success message after reset request"""
        return self.wait.until(EC.visibility_of_element_located(self.SUCCESS_MESSAGE)).text.strip()

    def is_username_field_visible(self):
        """Verify if username field is visible"""
        return self.wait.until(EC.visibility_of_element_located(self.USERNAME_FIELD)) is not None
