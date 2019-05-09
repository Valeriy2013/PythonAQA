import time
import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from JiraSelenium.Pages.BasePage import BasePage
from JiraSelenium.Pages.CreateIssuePage import CreateIssuePage
from JiraSelenium.Pages.CreateIssuePage import Issue


class IssuesPage(BasePage):
    SEARCH_INPUT = (By.ID, 'quickSearchInput')
    SEARCH_MENU_ITEM = (By.ID, 'find_link')
    SEARCH_FOR_ISSUES = (By.ID, 'issues_new_search_link_lnk')
    USER_DETAILS = (By.ID, 'header-details-user-fullname')
    CREATE_BTN = (By.ID, 'create_link')
    ISSUE_CREATED_ALERT = (By.CSS_SELECTOR, 'a.issue-created-key.issue-link')
    EDIT_BTN = (By.ID, 'edit-issue')

    SEARCH_BTN = (By.XPATH, '//*[@original-title="Search for issues"]')
    SEARCH_CRITERIA_PROJECT_DIV = (By.XPATH, '//div[@data-id="project"]')
    SEARCH_CRITERIA_PROJECT = (By.ID, 'searcher-pid-input')
    SEARCH_CRITERIA_ISSUE_TYPE_DIV = (By.XPATH, '//div[@data-id="issuetype"]')
    SEARCH_CRITERIA_ISSUE_TYPE = (By.ID, 'searcher-type-input')
    SEARCH_CRITERIA_ASSIGNEE_DIV = (By.XPATH, '//div[@data-id="assignee"]')
    SEARCH_CRITERIA_ASSIGNEE = (By.ID, 'assignee-input')
    SEARCH_CRITERIA_TEXT = (By.ID, 'searcher-query')

    SEARCH_RESULTS = (By.CSS_SELECTOR, 'tr.issuerow')
    SEARCH_NO_RESULTS = (By.XPATH, '//*[@id="content"]//h2[text()="No issues were found to match your search"]')

    SWITCH_LAYOUT = (By.ID, 'layout-switcher-button')
    LIST_VIEW = (By.XPATH, '//*[@id="layout-switcher-options"]//a[text()="List View"]')
    DETAIL_VIEW = (By.XPATH, '//*[@id="layout-switcher-options"]//a[text()="Detail View"]')

    def is_user_details_visible(self):
        self.is_visible(*self.USER_DETAILS)
        return self._driver.find_element(*self.USER_DETAILS).is_displayed()

    @allure.step('Create|Update issue form')
    def create_update_issue(self, issue: Issue, create_or_update='create'):
        create_issue_page = CreateIssuePage(self._driver)
        if create_or_update == 'create':
            self.click_element(*self.CREATE_BTN)
            create_issue_page.fill_form(issue, 'create')
        elif create_or_update == 'update':
            self.click_element(*self.EDIT_BTN)
            create_issue_page.fill_form(issue, 'update')

    @allure.step('Create|Update issue')
    def is_issue_created(self):
        self.is_visible(*self.ISSUE_CREATED_ALERT)
        is_created = self._driver.find_element(*self.ISSUE_CREATED_ALERT).is_displayed()
        issue_link = self._driver.find_element(*self.ISSUE_CREATED_ALERT).get_attribute("href")
        self.is_not_visible(*self.ISSUE_CREATED_ALERT)
        return is_created, issue_link

    def switch_view(self, view='List'):
        self.click_element(*self.SWITCH_LAYOUT)
        if view == 'List':
            self.click_element(*self.LIST_VIEW)
        elif view == 'Detail':
            self.click_element(*self.DETAIL_VIEW)

    @allure.step('Check "No results" message')
    def no_results(self):
        return self.is_visible(*self.SEARCH_NO_RESULTS)

    def get_results(self):
        self.is_present(*self.SEARCH_RESULTS)
        return self._driver.find_elements(*self.SEARCH_RESULTS)

    def get_row_content(self, row: int):
        attempts = 0
        result = {}
        while attempts < 3:
            try:
                result = self.get_results()[row].text
                break
            except IndexError:
                print('Caught out of range here')
            attempts += 1
        return result

    def get_results_count(self):
        return len(self.get_results())

    @allure.step('Search issue')
    def search(self, criteria: Issue):
        self.click_element(*self.SEARCH_MENU_ITEM)
        self.click_element(*self.SEARCH_FOR_ISSUES)
        if criteria.issue_type != '':
            self.click_element(*self.SEARCH_CRITERIA_ISSUE_TYPE_DIV)
            self.send_keys(*self.SEARCH_CRITERIA_ISSUE_TYPE, text=criteria.issue_type)
            self.send_keys(*self.SEARCH_CRITERIA_ISSUE_TYPE, text=Keys.ENTER)
        if criteria.assignee != '':
            self.click_element(*self.SEARCH_CRITERIA_ASSIGNEE_DIV)
            self.send_keys(*self.SEARCH_CRITERIA_ASSIGNEE, text=criteria.assignee)
            self.send_keys(*self.SEARCH_CRITERIA_ASSIGNEE, text=Keys.ENTER)
        if criteria.project != '':
            self.click_element(*self.SEARCH_CRITERIA_PROJECT_DIV)
            self.send_keys(*self.SEARCH_CRITERIA_PROJECT, text=criteria.project)
            self.send_keys(*self.SEARCH_CRITERIA_PROJECT, text=Keys.ENTER)
        if criteria.summary != '':
            # self.click_element(*self.SEARCH_CRITERIA_TEXT)
            self.send_keys(*self.SEARCH_CRITERIA_TEXT, text=criteria.summary)
        self.click_element(*self.SEARCH_BTN)
        time.sleep(2)
