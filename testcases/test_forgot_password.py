import pytest
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from pageObjects.forgot_password_page import ForgotPasswordPage
from utilities.customLogger import LogGen
from utilities.readProperties import ReadProperties
import time

@pytest.mark.usefixtures("setup")  # Use fixture from conftest.py
class TestForgotPassword:
    baseURL = ReadProperties.get_application_url()  # Get URL from config.ini
    username = ReadProperties.get_username()  # Get username from config.ini
    logger = LogGen.loggen()  # Logger instance

    @pytest.mark.regression
    def test_forgot_password_functionality(self):
        """Test Case: Forgot Password Reset Link Functionality"""
        self.logger.info("********** Test Forgot Password Functionality **********")
        driver = self.driver
        forgot_password_page = ForgotPasswordPage(driver)

        try:
            # ✅ Click Forgot Password
            self.logger.info("👉 Clicking 'Forgot your password?' link")
            forgot_password_page.click_forgot_password_link()
            time.sleep(2)

            # ✅ Verify username field is visible
            assert forgot_password_page.is_username_field_visible(), "❌ Username field is not visible!"
            self.logger.info("✅ Username field is visible")

            # ✅ Enter username from config.ini
            self.logger.info(f"👉 Entering username: {self.username}")
            forgot_password_page.enter_username(self.username)

            # ✅ Click Reset Password
            self.logger.info("👉 Clicking 'Reset Password' button")
            forgot_password_page.click_reset_password()
            time.sleep(2)

            # ✅ Verify success message
            success_msg = forgot_password_page.get_success_message().strip()
            expected_msg = "Reset Password link sent successfully"
            assert expected_msg in success_msg, f"❌ Expected '{expected_msg}', but got '{success_msg}'"
            self.logger.info("✅ Forgot Password Test Passed Successfully!")

        except TimeoutException:
            self.logger.error("❌ Forgot Password test failed due to timeout.")
            assert False, "Forgot Password process took too long!"

        except NoSuchElementException:
            self.logger.error("❌ Required element not found on the page.")
            assert False, "One or more elements are missing!"

        except Exception as e:
            self.logger.error(f"❌ Test case failed due to error: {str(e)}")
            assert False, f"Test case failed: {str(e)}"