import pytest
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pageObjects.LoginPage import LoginPage
from pageObjects.Titlepage import AdminPage
from utilities.customLogger import LogGen
from utilities.readProperties import ReadProperties

@pytest.mark.usefixtures("setup")  # Use fixture from conftest.py
class TestAdminPage:
    logger = LogGen.loggen()  # Logger instance

    @pytest.mark.regression
    def test_validate_admin_page_title(self):
        """Test Case: Validate Admin Page Title"""
        self.logger.info("********** Test: Admin Page Title Validation **********")
        driver = self.driver
        login_page = LoginPage(driver)
        admin_page = AdminPage(driver)

        try:
            # ✅ Retrieve username and password from config.ini
            username = ReadProperties.get_username()  # Get username from config.ini
            password = ReadProperties.get_password()  # Get password from config.ini

            # ✅ Log in to the application
            self.logger.info("👉 Logging in to the application")
            login_page.setUserName(username)  # Enter username from config.ini
            login_page.setPassword(password)  # Enter password from config.ini
            login_page.clickLogin()

            # ✅ Wait for the Admin page to load and validate title
            WebDriverWait(driver, 30).until(
                EC.title_is("OrangeHRM")  # Wait until the title is "OrangeHRM"
            )
            self.logger.info("✅ Admin page title is 'OrangeHRM'.")

            # ✅ Validate the page title directly
            admin_page.validate_page_title()  # This will assert if the title is 'OrangeHRM'

        except TimeoutException:
            self.logger.error("❌ Test failed due to timeout while waiting for Admin page title.")
            assert False, "Timeout occurred! Admin page title did not load as expected."

        except Exception as e:
            self.logger.error(f"❌ Test case failed due to error: {str(e)}")
            assert False, f"Test case failed: {str(e)}"
