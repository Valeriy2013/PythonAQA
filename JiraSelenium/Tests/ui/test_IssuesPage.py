import pytest

from JiraSelenium.Tests.ui.TestTemplate import TestTemplate
from JiraSelenium.Pages.CreateIssuePage import Issue


class TestIssuesPage(TestTemplate):

    @pytest.mark.flaky(reruns=3)
    def test_create_issue_negative_required_field_missing(self):
        assert self.issues_page.is_at('- Hillel IT School JIRA')
        assert self.issues_page.is_user_details_visible()
        issue = Issue('Webinar (WEBINAR)', 'Bug', '', 'High', 'ValeriiSokolovskyi')
        self.issues_page.create_update_issue(issue, create_or_update='create')
        assert self.create_issue_page.is_error_displayed("You must specify a summary of the issue.")

    @pytest.mark.flaky(reruns=3)
    def test_create_issue_negative_long_field(self):
        assert self.issues_page.is_at('- Hillel IT School JIRA')
        assert self.issues_page.is_user_details_visible()
        issue = Issue('Webinar (WEBINAR)',
                      'Bug',
                      'Very long summary textttttttttttttttttttttttttttttttt'
                      'ttttttttttttttttttttttttttttttttttttttttttttttttttttt'
                      'ttttttttttttttttttttttttttttttttttttttttttttttttttttt'
                      'ttttttttttttttttttttttttttttttttttttttttttttttttttttt'
                      'ttttttttttttttttttttttttttttttttttttttttttttttttttttt'
                      'ttttttttttttttttttttttttttttttttttttttttttttttttttttt'
                      'ttttttttttttttttttttttttttttttttttttttttttttttttttttt',
                      'High',
                      'ValeriiSokolovskyi')
        self.issues_page.create_update_issue(issue, create_or_update='create')
        assert self.create_issue_page.is_error_displayed("Summary must be less than 255 characters.")

    @pytest.mark.flaky(reruns=3)
    def test_create_issue_positive(self):
        assert self.issues_page.is_at('- Hillel IT School JIRA')
        assert self.issues_page.is_user_details_visible()
        issue = Issue('Webinar (WEBINAR)', 'Bug', 'Bug for create test', 'High', 'ValeriiSokolovskyi')
        self.issues_page.create_update_issue(issue, create_or_update='create')
        assert self.issues_page.is_issue_created()[0]

    @pytest.mark.flaky(reruns=3)
    def test_search_issue(self):
        assert self.issues_page.is_at('- Hillel IT School JIRA')
        assert self.issues_page.is_user_details_visible()
        criteria = Issue('Webinar (WEBINAR)', 'Bug', 'For search test', 'High', 'ValeriiSokolovskyi')
        self.issues_page.create_update_issue(criteria, create_or_update='create')
        assert self.issues_page.is_issue_created()[0]
        self.issues_page.search(criteria)
        # self.issues_page.switch_view('List')
        assert criteria.summary in self.issues_page.get_row_content(0)
        # assert self.issues_page.get_results_count() == 1

    @pytest.mark.flaky(reruns=3)
    def test_search_no_issue_found(self):
        criteria = Issue('Webinar (WEBINAR)', 'Bug', '###WILL NOT BE FOUND###', '', '')
        self.issues_page.search(criteria)
        # self.issues_page.switch_view('List')
        assert self.issues_page.no_results()

    @pytest.mark.parametrize('updated_issue', [
        Issue('Webinar (WEBINAR)', 'Bug', 'Updated Summary', 'Highest', 'ValeriiSokolovskyi'),
        Issue('Webinar (WEBINAR)', 'Bug', 'Bug for update test', 'Low', 'ValeriiSokolovskyi'),
        Issue('Webinar (WEBINAR)', 'Bug', 'Bug for update test', 'Highest', 'Unassigned')
    ])
    @pytest.mark.flaky(reruns=3)
    def test_update_issue(self, updated_issue):
        issue = Issue('Webinar (WEBINAR)', 'Bug', 'Bug for update test', 'Highest', '')
        self.issues_page.create_update_issue(issue, create_or_update='create')
        assert self.issues_page.is_issue_created()[0]
        issue_link = self.issues_page.is_issue_created()[1]
        self.issues_page.navigate(issue_link)
        self.issues_page.create_update_issue(updated_issue, create_or_update='update')
        self.issues_page.navigate(issue_link)
        assert updated_issue.summary == self.create_issue_page.get_summary()
        assert updated_issue.priority == self.create_issue_page.get_priority()
        assert updated_issue.assignee == self.create_issue_page.get_assignee()
