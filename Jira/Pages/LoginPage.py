from Jira.Pages.BasePage import BasePage
from selenium.webdriver.common.by import By
import allure


class LoginPage(BasePage):
    LOGIN_INPUT = (By.ID, 'login-form-username')
    PASS_INPUT = (By.ID, 'login-form-password')
    LOGIN_BTN = (By.ID, 'login-form-submit')
    LOGIN_ERR = (By.CSS_SELECTOR, '.aui-message.aui-message-error')

    @allure.step('Login to Jira')
    def login_to_jira(self, name, passw):
        self.set_username(name)
        self.set_password(passw)
        self.click_login()

    @allure.step('Set username')
    def set_username(self, username: str):
        self.is_visible(*self.LOGIN_INPUT)
        self._driver.find_element(*self.LOGIN_INPUT).clear()
        self._driver.find_element(*self.LOGIN_INPUT).send_keys(username)

    @allure.step('Set password')
    def set_password(self, password: str):
        self.is_visible(*self.PASS_INPUT)
        self._driver.find_element(*self.PASS_INPUT).clear()
        self._driver.find_element(*self.PASS_INPUT).send_keys(password)

    @allure.step('Submit login')
    def click_login(self):
        self.is_visible(*self.LOGIN_BTN)
        self._driver.find_element(*self.LOGIN_BTN).click()

    @allure.step('Does login error occur?')
    def is_login_error_visible(self):
        self.is_visible(*self.LOGIN_ERR)
        return self._driver.find_element(*self.LOGIN_ERR).is_displayed()
