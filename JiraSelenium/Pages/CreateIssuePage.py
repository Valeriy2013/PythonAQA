import time
import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from JiraSelenium.Pages.BasePage import BasePage


class CreateIssuePage(BasePage):
    PROJECT = (By.ID, 'project-field')
    PROJECT_SELECT = (By.ID, 'project-single-select')
    ISSUE_TYPE = (By.ID, 'issuetype-field')
    ISSUE_TYPE_SELECT = (By.ID, 'issuetype-single-select')
    PRIORITY = (By.ID, 'priority-field')
    PRIORITY_SELECT = (By.ID, 'priority-single-select')
    ASSIGNEE = (By.ID, 'assignee-field')
    ASSIGNEE_SELECT = (By.ID, 'assignee-single-select')
    SUMMARY = (By.ID, 'summary')
    UPDATE_ISSUE_BTN = (By.ID, 'edit-issue-submit')
    CREATE_ISSUE_BTN = (By.ID, 'create-issue-submit')
    CANCEL_BTN = (By.CSS_SELECTOR, 'a.cancel')
    SUMMARY_REQUIRED_ERROR = (By.XPATH, '//*[@class="error" and text() = "You must specify a summary of the issue."]')
    SUMMARY_TOO_LONG_ERROR = (By.XPATH, '//*[@class="error" and text() = "Summary must be less than 255 characters."]')

    SUMMARY_ISSUE_VIEW = (By.ID, 'summary-val')
    PRIORITY_ISSUE_VIEW = (By.ID, 'priority-val')
    ASSIGNEE_ISSUE_VIEW = (By.ID, 'assignee-val')
    ISSUE_TYPE_ISSUE_VIEW = (By.ID, 'type-val')

    @allure.step('Fill create|update issue form')
    def fill_form(self, issue, create_or_update='create'):
        if create_or_update == 'create':
            self.click_element(*self.PROJECT_SELECT)
            self.handle_select(*self.PROJECT, text=issue.project)

        self.send_keys(*self.SUMMARY, text=issue.summary)
        if issue.issue_type != self.get_element_value(*self.ISSUE_TYPE):
            self.click_element(*self.ISSUE_TYPE_SELECT)
            self.handle_select(*self.ISSUE_TYPE, text=issue.issue_type)
        if issue.priority != self.get_element_value(*self.PRIORITY):
            self.click_element(*self.PRIORITY_SELECT)
            self.handle_select(*self.PRIORITY, text=issue.priority)
        if issue.assignee != self.get_element_value(*self.ASSIGNEE):
            self.click_element(*self.ASSIGNEE_SELECT)
            self.handle_select(*self.ASSIGNEE, text=issue.assignee)

        if create_or_update == 'create':
            time.sleep(2)
            self.click_element(*self.CREATE_ISSUE_BTN)
        elif create_or_update == 'update':
            self.click_element(*self.UPDATE_ISSUE_BTN)
        time.sleep(2)

    def handle_select(self, *element, text: str):
        self.send_keys(*element, text=text)
        self.send_keys(*element, text=Keys.ENTER)

    def get_summary(self):
        return self.get_element_text(*self.SUMMARY_ISSUE_VIEW)

    def get_priority(self):
        return self.get_element_text(*self.PRIORITY_ISSUE_VIEW)

    def get_issue_type(self):
        return self.get_element_text(*self.ISSUE_TYPE_ISSUE_VIEW)

    def get_assignee(self):
        return self.get_element_text(*self.ASSIGNEE_ISSUE_VIEW)

    @allure.step('Check error message')
    def is_error_displayed(self, error):
        if error == "You must specify a summary of the issue.":
            return self.is_visible(*self.SUMMARY_REQUIRED_ERROR)
        elif error == "Summary must be less than 255 characters.":
            return self.is_visible(*self.SUMMARY_TOO_LONG_ERROR)


class Issue(object):
    """__init__() functions as the class constructor"""

    def __init__(self, project: str, issue_type: str, summary: str, priority: str, assignee: str):
        self.project = project
        self.issue_type = issue_type
        self.summary = summary
        self.priority = priority
        self.assignee = assignee
