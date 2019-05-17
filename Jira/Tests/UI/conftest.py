import pytest
import allure
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture(scope="function")
def get_driver(request):
    _driver: webdriver = None
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument('--disable-extensions')
    chrome_options.add_argument("--disable-notifications")
    chrome_options.add_argument("--enable-automation")
    # chrome_options.add_argument("--headless")
    chrome_options.add_argument('--disable-infobars')
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--disable-xss-auditor")
    # chrome_options.add_argument("--window-size=1920,1080")
    chrome_options.add_argument("--start-maximized")
    _driver = webdriver.Chrome(executable_path=ChromeDriverManager().install(), options=chrome_options)
    request.cls.driver = _driver

    def close_driver():
        _driver.quit()

    request.addfinalizer(close_driver)
    return _driver
