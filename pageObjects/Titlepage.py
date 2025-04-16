from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class AdminPage:
    def __init__(self, driver):
        self.driver = driver
        self.expected_title = "OrangeHRM"  # Expected page title

    def validate_page_title(self):
        """Validates that the page title is 'OrangeHRM'."""
        # Wait until the title is "OrangeHRM"
        WebDriverWait(self.driver, 10).until(
            EC.title_is(self.expected_title)
        )

        # Get the actual page title
        actual_title = self.driver.title
        assert actual_title == self.expected_title, f"❌ Page title mismatch! Expected: '{self.expected_title}', but got: '{actual_title}'"
        print(f"✅ Page title is validated as: {actual_title}")
