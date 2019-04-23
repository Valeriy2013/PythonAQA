from JiraSelenium.Pages.LoginPage import LoginPage
from JiraSelenium.Pages.IssuesPage import IssuesPage
from JiraSelenium.Tests.TestTemplate import TestTemplate
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager


class TestLoginPage(TestTemplate):

    def setUp(self):
        self._driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
        self.login_page = LoginPage(self._driver)
        self.login_page.navigate('https://jira.hillel.it/projects/WEBINAR')

    def tearDown(self):
        self._driver.quit()

    def test_login_positive(self):
        assert self.login_page.is_at('Log in - Hillel IT School JIRA')
        self.login_page.login_to_jira('ValeriiSokolovskyi', 'ValeriiSokolovskyi')
        self.issue_page = IssuesPage(self._driver)
        assert self.issue_page.is_at('- Hillel IT School JIRA')
        assert self.issue_page.is_user_details_visible()

    def test_login_negative_wrong_username(self):
        self.login_page.set_username('wrong_name@wrong.name')
        self.login_page.set_password('ValeriiSokolovskyi')
        self.login_page.click_login()
        assert self.login_page.is_login_error_visible()

    def test_login_negative_wrong_password(self):
        self.login_page.set_username('ValeriiSokolovskyi')
        self.login_page.set_password('wrong_password')
        self.login_page.click_login()
        assert self.login_page.is_login_error_visible()
