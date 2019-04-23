# import unittest
# import os
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from JiraSelenium.Pages.LoginPage import LoginPage


class TestTemplate:
    # def setUpClass(self) -> None: ...

    # def tearDownClass(self) -> None: ...

    def setup_method(self):
        # chrome_driver = os.path.join(os.path.dirname(os.path.abspath(__file__)), "chromedriver.exe")
        # os.environ["webdriver.chrome.driver"] = chrome_driver
        # self.driver = webdriver.Chrome(chrome_driver)
        # self.driver.implicitly_wait(10)
        self.driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
        self.login_page = LoginPage(self.driver)
        self.login_page.navigate('https://jira.hillel.it/projects/WEBINAR')
        self.login_page.login_to_jira('ValeriiSokolovskyi', 'ValeriiSokolovskyi')

    def teardown_method(self):
        self.driver.quit()


# if __name__ == "__main__":
#    unittest.main()
