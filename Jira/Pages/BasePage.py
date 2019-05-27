import selenium.webdriver.support.expected_conditions as ec
import selenium.webdriver.support.ui as ui
from selenium.common.exceptions import ElementNotInteractableException
from selenium.common.exceptions import StaleElementReferenceException
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import NoSuchAttributeException
import time


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
    def is_visible(self, *by_locator, timeout=10):
        try:
            ui.WebDriverWait(self._driver, timeout).until(ec.visibility_of_element_located(by_locator))
            return True
        except TimeoutException:
            return False

    # return True if element is not visible within 5 seconds, otherwise False
    def is_not_visible(self, *by_locator, timeout=10):
        try:
            ui.WebDriverWait(self._driver, timeout).until_not(ec.visibility_of_element_located(by_locator))
            return True
        except TimeoutException:
            return False

    # return True if element is visible within 5 seconds, otherwise False
    def is_clickable(self, *by_locator, timeout=10):
        try:
            ui.WebDriverWait(self._driver, timeout).until(ec.element_to_be_clickable(by_locator))
            return True
        except TimeoutException:
            return False

    def is_present(self, *by_locator, timeout=10):
        try:
            ui.WebDriverWait(self._driver, timeout).until(ec.presence_of_element_located(by_locator))
            return True
        except TimeoutException:
            return False

    def is_text_present(self, *by_locator, text, timeout=10):
        try:
            ui.WebDriverWait(self._driver, timeout).until(
                ec.text_to_be_present_in_element_value(by_locator, text_=text))
            return True
        except TimeoutException:
            return False

    def click_element(self, *locator):
        attempts = 0
        result = False
        while attempts < 3:
            try:
                print "click element: ", attempts
                self.is_visible(*locator)
                self.is_clickable(*locator)
                self._driver.find_element(*locator).click()
                result = True
                break
            except StaleElementReferenceException:
                print('Caught Stale Element here')
            attempts += 1
        return result

    def send_keys(self, *locator, text):
        attempts = 0
        result = False
        while attempts < 3:
            try:
                self.is_visible(*locator)
                self.is_clickable(*locator)
                self._driver.find_element(*locator).send_keys(text)
                result = True
                break
            except ElementNotInteractableException:
                print('Caught element not interactable here')
            attempts += 1
        return result  # and self.is_text_present(*locator, text=text)

    def get_element_text(self, *locator):
        attempts = 0
        result = ''
        while attempts < 3:
            try:
                self.is_visible(*locator)
                self.is_clickable(*locator)
                result = self._driver.find_element(*locator).text
                break
            except NoSuchAttributeException:
                print('Exception occurs while getting text')
            attempts += 1
        return result

    def get_element_value(self, *locator):
        attempts = 0
        result = ''
        while attempts < 3:
            try:
                self.is_visible(*locator)
                self.is_clickable(*locator)
                result = self._driver.find_element(*locator).get_attribute("value")
                break
            except NoSuchAttributeException:
                print('Exception occurs while getting attribute value')
            attempts += 1
        return result

    def wait_for_true(self, func, cycles=10, sleep_seconds=1):
        result = False
        count = 0
        while count < cycles and not result:
            try:
                result = func()
                break
            except Exception:
                print('Exception caught in wait_for_true method')
            count += 1
            time.sleep(sleep_seconds)

    # self._driver.execute_script("document.getElementById('" + self.ISSUE_TYPE[1] + "').value='" + issue.issue_type + "'")
