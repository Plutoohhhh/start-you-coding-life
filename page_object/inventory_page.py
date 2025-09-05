from selenium.webdriver.common.by import By
from commom.base_page import BasePage

class InventoryPage(BasePage):

    _page_title = (By.CLASS_NAME,"title")

    def __init__(self,driver):
        super.__init__(driver)

    def get_page_title(self):
        element = self.find_element(self._page_title)
        return element.text if element else None