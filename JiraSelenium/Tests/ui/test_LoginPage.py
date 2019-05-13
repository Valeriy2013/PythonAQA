from JiraSelenium.Pages.LoginPage import LoginPage
from JiraSelenium.Pages.IssuesPage import IssuesPage
import JiraSelenium.config as conf
import pytest


@pytest.mark.ui
@pytest.mark.usefixtures("get_driver")
class TestLoginPage:

    def test_login_positive(self, get_driver):
        self.login_page = LoginPage(get_driver)
        self.issues_page = IssuesPage(get_driver)
        self.login_page.navigate(conf.SETTINGS['url'])
        assert self.login_page.is_at('Log in - Hillel IT School JIRA')
        self.login_page.login_to_jira('ValeriiSokolovskyi', 'ValeriiSokolovskyi')
        assert self.issues_page.is_user_details_visible()

    def test_login_negative_wrong_username(self, get_driver):
        self.login_page = LoginPage(get_driver)
        self.login_page.navigate(conf.SETTINGS['url'])
        self.login_page.set_username('wrong_name@wrong.name')
        self.login_page.set_password('ValeriiSokolovskyi')
        self.login_page.click_login()
        assert self.login_page.is_login_error_visible()

    def test_login_negative_wrong_password(self, get_driver):
        self.login_page = LoginPage(get_driver)
        self.login_page.navigate(conf.SETTINGS['url'])
        self.login_page.set_username('ValeriiSokolovskyi')
        self.login_page.set_password('wrong_password')
        self.login_page.click_login()
        assert self.login_page.is_login_error_visible()
