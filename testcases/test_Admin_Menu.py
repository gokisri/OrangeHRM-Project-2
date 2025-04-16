import pytest
from pageObjects.Admin_Menu import AdminPage
from utilities.customLogger import LogGen
from pageObjects.LoginPage import LoginPage
from utilities.readProperties import ReadProperties

@pytest.mark.usefixtures("setup")  # Uses WebDriver fixture from conftest.py
class TestAdminPage:
    logger = LogGen.loggen()  # Initialize logger

    @pytest.mark.regression
    def test_validate_admin_headers(self):
        """Test Case: Validate Headers on Admin Page"""
        self.logger.info("********** Test: Admin Page Header Validation **********")
        driver = self.driver
        login_page = LoginPage(driver)
        admin_page = AdminPage(driver, self.logger)

        try:
            # Retrieve login credentials from config.ini
            username = ReadProperties.get_username()
            password = ReadProperties.get_password()

            # Perform login
            login_page.setUserName(username)
            login_page.setPassword(password)
            login_page.clickLogin()
            self.logger.info("✅ Successfully logged into OrangeHRM.")

            # Minimize the browser window before starting validation
            admin_page.minimize_window()

            # Validate all headers (visible and hidden)
            admin_page.validate_all_headers()

            self.logger.info("✅ All headers validated successfully!")

        except Exception as e:
            self.logger.error(f"❌ Test case failed due to error: {str(e)}")
            assert False, f"Test case failed: {str(e)}"
