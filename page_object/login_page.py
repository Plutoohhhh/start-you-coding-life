from selenium.webdriver.common.by import By
from commom.base_page import BasePage
from commom.config_reader import get_config

class LoginPage(BasePage):
    _username_input = (By.ID,"user-name")
    _password_input = (By.ID,"password")
    _login_button = (By.ID,"login-button")
    _error_message = (By.CSS_SELECTOR,"h3[data-test='error']")

    def __init__(self,driver):
        base_url = get_config("web","base_url")
        driver.get(base_url)
        super().__init__(driver)




    def login(self,username,password):

        self.send_keys(self._username_input,username)
        self.send_keys(self._password_input,password)
        self.click(self._login_button)

    def get_error_message(self):
        element = self.find_element(self._error_message)
        return element.text if element else None