from selenium.common.exceptions import TimeoutException
import selenium.webdriver.support.expected_conditions as ec
import selenium.webdriver.support.ui as ui


class BasePage(object):
    """Base class to initialize the base page that will be called from all pages"""

    def __init__(self, driver):
        self._driver = driver

    def is_at(self, title):
        return title in self._driver.title

    def navigate(self, url):
        self._driver.get(url)
        return self

    # return True if element is visible within 5 seconds, otherwise False
    def is_visible(self, *by_locator, timeout=5):
        try:
            ui.WebDriverWait(self._driver, timeout).until(ec.visibility_of_element_located(by_locator))
            return True
        except TimeoutException:
            return False

    # return True if element is not visible within 5 seconds, otherwise False
    def is_not_visible(self, *by_locator, timeout=5):
        try:
            ui.WebDriverWait(self._driver, timeout).until_not(ec.visibility_of_element_located(by_locator))
            return True
        except TimeoutException:
            return False

    # return True if element is visible within 5 seconds, otherwise False
    def is_clickable(self, *by_locator, timeout=5):
        try:
            ui.WebDriverWait(self._driver, timeout).until(ec.element_to_be_clickable(by_locator))
            return True
        except TimeoutException:
            return False
