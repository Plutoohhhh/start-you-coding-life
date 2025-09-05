import pytest

from page_object.home_page import HomePage
import time

from page_object.inventory_page import InventoryPage
from page_object.login_page import LoginPage
from page_object.register_page import RegisterPage
from commom.config_reader import get_config

@pytest.mark.skip
def test_navigation_to_register_page(driver):
    "测试目标：验证用户可以从首页到注册页面"
    #步骤：1.打开首页 2.打开注册连接 3.验证是否是注册页面
    base_url = get_config("web","base_url")
    driver.get(base_url)
    home_page = HomePage(driver)
    home_page.click_resgister_link()
    time.sleep(1)

    expecte_title = "TriCis.com is for sale | HugeDomains"
    actual_title = home_page.get_title()

    assert actual_title == expecte_title,f"页面标题错误！预期为{expecte_title},实际为：{actual_title}"

@pytest.mark.skip
def test_successful_registration(driver):
    base_url = get_config("web","base_url")
    driver.get(base_url)
    unique_email = f"testuser_{int(time.time())}@example.com"
    home_page = HomePage(driver)
    home_page.click_resgister_link()

    register_page = RegisterPage(driver)
    register_page.register_user("Test","User",unique_email,"paswword123")
    success_msg = register_page.get_success_meassge()
    assert success_msg == "Your resgistration completed"

def test_successful_login(driver):
    username = get_config("users","standard_user")
    password = get_config("users","standard_password")

    login_page = LoginPage(driver)
    login_page.login(username,password)

    inventory_page = InventoryPage(driver)
    page_title = inventory_page.get_title()

    assert page_title == "PRODUCTS", f"登录后的页面标题不正确！实际为{page_title}"