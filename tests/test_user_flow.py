from page_object.home_page import HomePage
import time

from page_object.register_page import RegisterPage
from commom.config_reader import get_config


def test_navigation_to_register_page(driver):
    "测试目标：验证用户可以从首页到注册页面"
    #步骤：1.打开首页 2.打开注册连接 3.验证是否是注册页面
    base_url = get_config("web","base_url")
    driver.get(base_url)
    home_page = HomePage(driver)
    home_page.click_resgister_link()
    time.sleep(1)

    expecte_title = "Demo WebShop.Register"
    actual_title = home_page.get_title()

    assert actual_title == expecte_title,f"页面标题错误！预期为{expecte_title},实际为：{actual_title}"

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