from JiraSelenium.Tests.TestTemplate import TestTemplate
from JiraSelenium.Pages.CreateIssuePage import Issue


class TestIssuesPage(TestTemplate):

    def test_create_issue(self):
        assert self.issues_page.is_at('- Hillel IT School JIRA')
        assert self.issues_page.is_user_details_visible()
        issue = Issue('Webinar (WEBINAR)', 'Bug', 'Bug summary', 'High', 'ValeriiSokolovskyi')
        self.issues_page.create_issue(issue)
        assert True
