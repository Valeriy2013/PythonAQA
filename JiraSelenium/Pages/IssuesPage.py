from JiraSelenium.Pages.BasePage import BasePage
from selenium.webdriver.common.by import By
from JiraSelenium.Pages.CreateIssuePage import CreateIssuePage


class IssuesPage(BasePage):
    SEARCH_INPUT = (By.ID, 'quickSearchInput')
    USER_DETAILS = (By.ID, 'header-details-user-fullname')
    CREATE_BTN = (By.ID, 'create_link')

    def is_search_visible(self):
        self.is_visible(*self.SEARCH_INPUT)
        return self._driver.find_element(*self.SEARCH_INPUT).is_displayed()

    def is_user_details_visible(self):
        self.is_visible(*self.USER_DETAILS)
        return self._driver.find_element(*self.USER_DETAILS).is_displayed()

    def create_issue(self, issue):
        self.click_create()
        create_issue_page = CreateIssuePage(self._driver)
        create_issue_page.fill_form(issue)

    def click_create(self):
        self.is_visible(*self.CREATE_BTN)
        self._driver.find_element(*self.CREATE_BTN).click()
