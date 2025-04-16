from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class AdminPage:
    def __init__(self, driver, logger):
        self.driver = driver
        self.logger = logger
        self.wait = WebDriverWait(driver, 10)

    # Locators for side menu headers
    menu_locators = {
        "Admin": (By.XPATH, "//a[@class='oxd-main-menu-item active']//span[1]"),
        "PIM": (By.XPATH, "//span[normalize-space()='PIM']"),
        "Leave": (By.XPATH, "//span[normalize-space()='Leave']"),
        "Time": (By.XPATH, "//span[normalize-space()='Time']"),
        "Recruitment": (By.XPATH, "//span[normalize-space()='Recruitment']"),
        "My Info": (By.XPATH, "(//span[normalize-space()='My Info'])[1]"),
        "Performance": (By.XPATH, "//span[normalize-space()='Performance']"),
        "Dashboard": (By.XPATH, "(//span[normalize-space()='Dashboard'])[1]"),
        "Directory": (By.XPATH, "(//span[normalize-space()='Directory'])[1]"),
        "Maintenance": (By.XPATH, "(//span[normalize-space()='Maintenance'])[1]"),
        "Buzz": (By.XPATH, "(//span[normalize-space()='Claim'])[1]"),
    }

    def minimize_window(self):
        """Minimizes the browser window."""
        self.driver.minimize_window()
        self.logger.info("🔻 Browser window minimized.")

    def validate_header(self, header_name):
        """Validates if a specific header is visible on the Admin page."""
        locator = self.menu_locators.get(header_name)
        if not locator:
            self.logger.error(f"❌ Locator not found for header: {header_name}")
            assert False, f"Locator not found for header: {header_name}"

        try:
            element = self.wait.until(EC.visibility_of_element_located(locator))
            assert element.is_displayed(), f"{header_name} menu is not visible!"
            self.logger.info(f"✅ {header_name} menu is displayed.")
        except Exception as e:
            self.logger.error(f"❌ Failed to validate {header_name} menu: {str(e)}")
            assert False, f"Failed to validate {header_name} menu: {str(e)}"

    def validate_all_headers(self):
        """Validates the visibility of all menu headers on the Admin page."""
        for header in self.menu_locators.keys():
            self.validate_header(header)
