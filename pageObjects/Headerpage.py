from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class AdminPage:
    def __init__(self, driver, logger):
        self.driver = driver
        self.logger = logger  # Use the logger passed from the test class

        # XPath locators for various headers
        self.admin_menu_xpath = "//li[1]//a[1]//span[1]"
        self.user_management_xpath = "//span[normalize-space()='User Management']"
        self.job_xpath = "//span[normalize-space()='Job']"
        self.organization_xpath = "//span[normalize-space()='Organization']"
        self.qualification_xpath = "//span[normalize-space()='Qualifications']"
        self.more_button_xpath = "//i[@class='oxd-icon bi-three-dots-vertical']"
        self.nationalities_xpath = "//a[normalize-space()='Nationalities']"
        self.corporate_branding_xpath = "//a[normalize-space()='Corporate Branding']"
        self.configuration_xpath = "//a[normalize-space()='Configuration']"

    def click_admin_menu(self):
        """Clicks on the Admin menu to ensure it's displayed."""
        try:
            admin_menu = WebDriverWait(self.driver, 5).until(
                EC.presence_of_element_located((By.XPATH, self.admin_menu_xpath))
            )
            self.logger.info("👉 Admin menu item is present. Clicking on it.")
            admin_menu.click()
        except Exception as e:
            self.logger.error(f"⚠️ Admin menu not found. {str(e)}")
            raise

    def check_header_visible(self, header_xpath, header_name):
        """Checks if a specific header is visible on the page."""
        try:
            WebDriverWait(self.driver, 5).until(
                EC.presence_of_element_located((By.XPATH, header_xpath))
            )
            self.logger.info(f"✅ '{header_name}' header is visible on the page.")
        except Exception as e:
            self.logger.error(f"❌ '{header_name}' header is not visible: {str(e)}")
            raise

    def click_more_if_present(self):
        """Clicks 'More' button if it appears to reveal hidden headers."""
        try:
            more_button = WebDriverWait(self.driver, 5).until(
                EC.presence_of_element_located((By.XPATH, self.more_button_xpath))
            )
            if more_button.is_displayed():
                self.logger.info("👉 Clicking 'More' button to reveal hidden headers.")
                more_button.click()
                # Wait for new headers to appear after clicking "More"
                WebDriverWait(self.driver, 5).until(
                    EC.presence_of_element_located((By.XPATH, self.nationalities_xpath))
                )
        except Exception as e:
            self.logger.warning(f"⚠️ More button not found or not needed. {str(e)}")

    def minimize_window(self):
        """Minimizes the browser window."""
        self.driver.minimize_window()
        self.logger.info("👉 Browser window minimized.")

    def validate_all_headers(self):
        """Validate all headers (visible and hidden)."""
        self.click_admin_menu()

        # Validate first set of headers (User Management, Job, Organization, Qualifications)
        self.check_header_visible(self.user_management_xpath, "User Management")
        self.check_header_visible(self.job_xpath, "Job")
        self.check_header_visible(self.organization_xpath, "Organization")
        self.check_header_visible(self.qualification_xpath, "Qualifications")

        # Click "More" button and validate remaining headers
        self.click_more_if_present()

        # Validate remaining headers (Nationalities, Corporate Branding, Configuration)
        self.check_header_visible(self.nationalities_xpath, "Nationalities")
        self.check_header_visible(self.corporate_branding_xpath, "Corporate Branding")
        self.check_header_visible(self.configuration_xpath, "Configuration")
