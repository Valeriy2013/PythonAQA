from JiraSelenium.Pages.BasePage import BasePage
from selenium.webdriver.common.by import By


class CreateIssuePage(BasePage):
    PROJECT = (By.ID, 'project-field')
    ISSUE_TYPE = (By.ID, 'issuetype-field')
    SUMMARY = (By.ID, 'summary')
    PRIORITY = (By.ID, 'priority-field')
    ASSIGNEE = (By.ID, 'assignee-field')
    CREATE_ISSUE_BTN = (By.ID, 'create-issue-submit')
    CANCEL_BTN = (By.CSS_SELECTOR, 'a.cancel')

    def fill_form(self, issue):
        self.is_visible(*self.PROJECT)
        self._driver\
            .execute_script("document.getElementById('" + self.PROJECT[1] + "').value='" + issue.project + "'")
        self._driver\
            .execute_script("document.getElementById('" + self.ISSUE_TYPE[1] + "').value='" + issue.issue_type + "'")
        self._driver\
            .execute_script("document.getElementById('" + self.PRIORITY[1] + "').value='" + issue.priority + "'")
        self._driver\
            .execute_script("document.getElementById('" + self.ASSIGNEE[1] + "').value='" + issue.assignee + "'")
        self._driver.find_element(*self.SUMMARY).send_keys(issue.summary)
        self._driver.find_element(*self.CREATE_ISSUE_BTN).click()


class Issue(object):
    """__init__() functions as the class constructor"""

    def __init__(self, project: str, issue_type: str, summary: str, priority: str, assignee: str):
        self.project = project
        self.issue_type = issue_type
        self.summary = summary
        self.priority = priority
        self.assignee = assignee
