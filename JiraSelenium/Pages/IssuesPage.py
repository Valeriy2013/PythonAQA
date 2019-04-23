from JiraSelenium.Pages.BasePage import BasePage
from selenium.webdriver.common.by import By


class IssuesPage(BasePage):
    SEARCH_INPUT = (By.NAME, 'search')
    USER_DETAILS = (By.ID, 'header-details-user-fullname')

    def is_search_visible(self):
        self.is_visible(*self.SEARCH_INPUT)
        return self._driver.find_element(*self.SEARCH_INPUT).is_displayed()

    def is_user_details_visible(self):
        self.is_visible(*self.USER_DETAILS)
        return self._driver.find_element(*self.USER_DETAILS).is_displayed()
