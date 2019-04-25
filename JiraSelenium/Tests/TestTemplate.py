from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

from JiraSelenium.Pages.CreateIssuePage import CreateIssuePage
from JiraSelenium.Pages.IssuesPage import IssuesPage
from JiraSelenium.Pages.LoginPage import LoginPage
import JiraSelenium.config as conf


class TestTemplate:

    def setup_method(self):
        # chrome_driver = os.path.join(os.path.dirname(os.path.abspath(__file__)), "chromedriver.exe")
        # os.environ["webdriver.chrome.driver"] = chrome_driver
        # self.driver = webdriver.Chrome(chrome_driver)
        # self.driver.implicitly_wait(10)
        self.driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
        self.driver.set_window_size(1366, 768)
        self.driver.maximize_window()
        self.login_page = LoginPage(self.driver)
        self.issues_page = IssuesPage(self.driver)
        self.create_issue_page = CreateIssuePage(self.driver)
        self.login_page.navigate(conf.SETTINGS['url'])
        self.login_page.login_to_jira(conf.SETTINGS['login'], conf.SETTINGS['password'])

    def teardown_method(self):
        self.driver.quit()
