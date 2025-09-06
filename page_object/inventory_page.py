from selenium.webdriver.common.by import By
from commom.base_page import BasePage

class InventoryPage(BasePage):

    _page_title = (By.CLASS_NAME,"title")
    _shopping_cart_badge = (By.CLASS_NAME,"shopping_cart_badge")
    _add_to_cart_button = (By.ID,"add-to-cart-{product_id}")

    def __init__(self,driver):
        super().__init__(driver)

    def get_page_title(self):
        element = self.find_element(self._page_title)
        return element.text if element else None

    def add_product_to_cart(self,product_name):
        product_id = product_name.lower().replace(" ","-")
        add_button_locator = (self._add_to_cart_button[0],self._add_to_cart_button[1].format(product_id=product_id))
        self.click(add_button_locator)

    def get_shopping_cart_badge(self):
        element = self.find_element(self._shopping_cart_badge)
        return element.text if element else "0"