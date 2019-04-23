from JiraSelenium.Pages.LoginPage import LoginPage
from JiraSelenium.Pages.IssuesPage import IssuesPage
from JiraSelenium.Tests.TestTemplate import TestTemplate
from JiraSelenium.Pages.CreateIssuePage import Issue
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager


class TestIssuesPage(TestTemplate):

    def test_create_issue(self):
        assert self.issues_page.is_at('- Hillel IT School JIRA')
        assert self.issues_page.is_user_details_visible()
        issue = Issue('Webinar (WEBINAR)', 'Bug', 'Bug summary', 'High', 'ValeriiSokolovskyi')
        self.issues_page.create_issue(issue)
        assert True
