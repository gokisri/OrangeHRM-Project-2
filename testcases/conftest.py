import pytest
from selenium import webdriver

from utilities.customLogger import LogGen
from utilities.readProperties import ReadProperties


@pytest.fixture(scope="class")
def setup(request):
    """Setup WebDriver instance and assign it to the test class"""
    logger = LogGen.loggen()  # Logger instance
    logger.info("🚀 Starting WebDriver setup...")

    driver = webdriver.Chrome()  # Change to Firefox/Edge if needed
    driver.maximize_window()
    driver.get(ReadProperties.get_application_url())

    request.cls.driver = driver  # Assign WebDriver to class

    yield driver  # Yield control back to test

    logger.info("📌 Closing WebDriver...")
    driver.quit()


def pytest_addoption(parser):  # This will get the value from CLI/hooks
    parser.addoption("--browser", action="store", default="chrome", help="Browser to run tests (chrome/firefox)")

@pytest.fixture()
def browser(request):  # This will return the Browser value to setup method
    return request.config.getoption("--browser")

########### pytest HTML Report ################

# Hook for adding environment info to HTML Report
def pytest_configure(config):
    config._metadata = getattr(config, "_metadata", {})
    config._metadata['Project Name'] = 'Capstone Project 1'
    config._metadata['Module Name'] = 'Customers'
    config._metadata['Tester'] = 'Pavan'

# Hook for modifying/deleting environment info in the HTML report
@pytest.hookimpl(optionalhook=True)
def pytest_metadata(metadata):
    metadata.pop("JAVA_HOME", None)
    metadata.pop("Plugins", None)
