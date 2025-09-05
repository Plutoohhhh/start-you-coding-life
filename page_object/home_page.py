from selenium.webdriver.common.by import By
from commom.base_page import BasePage

class HomePage(BasePage):
    _register_link = (By.CLASS_NAME,"ico-register")
    _login_link = (By.CLASS_NAME,"ico-login")
    _search_box = (By.ID,"small-searchterms")
    _search_button = (By.CSS_SELECTOR,"input[type='submit']")

    def __init__(self,driver):
        super().__init__(driver)

    def click_resgister_link(self):
        self.click(self._register_link)

    def click_login_link(self):
        self.click(self._login_link)

    def search_product(self,porduct_name):
        self.send_keys(self._search_box,porduct_name)
        self.click(self._search_button)