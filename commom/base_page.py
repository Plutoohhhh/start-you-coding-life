from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:
    def __init__(self,driver):
        self.driver = driver
        self.timeout = 10

    def find_element(self,locator):
        #寻找单个元素
        try:
            element = WebDriverWait(self.driver,self.timeout).until(EC.visibility_of_element_located(locator))
            return element
        except:
            print(f"错误：没有找到元素->{locator}")
            return None

    def click(self,locator):
        #点击
        element = self.find_element(locator)
        if element:
                element.click()

    def send_keys(self,locator,text):
        element = self.find_element(locator)
        if element:
            element.clear()
            element.sent_keys(text)

    def get_title(self):
        return self.driver.title