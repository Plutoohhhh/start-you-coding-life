from selenium.webdriver.common.by import By
from commom.base_page import BasePage

class RegisterPage(BasePage):
    _male_gender_radio = (By.ID,"gender-male")
    _first_name_input = (By.ID,"FirstName")
    _last_name_input = (By.ID,"LastName")
    _email_input = (By.ID,"Email")
    _password_input = (By.ID,"Password")
    _confirm_password_input = (By.ID,"ConfirmPassword")
    _register_button = (By.ID,"resgister-button")
    _success_message = (By.CLASS_NAME,"result")

    def __init__(self,driver):
        self().__init__(driver)

    def register_user(self,first_name,last_name,email,password):
        self.click(self._male_gender_radio)
        self.send_keys(self._first_name_input,first_name)
        self.send_keys(self._last_name_input,last_name)
        self.send_keys(self._email_input,email)
        self.send_keys(self._password_input,password)
        self.send_keys(self._confirm_password_input,password)
        self.click(self._register_button)

    def get_success_meassge(self):
        element = self.find_element(self._success_message)
        return element.text if element else None