from page_object.home_page import HomePage
import time

def test_navigation_to_register_page(driver):
    "测试目标：验证用户可以从首页到注册页面"
    #步骤：1.打开首页 2.打开注册连接 3.验证是否是注册页面
    home_page = HomePage(driver)
    home_page.click_resgister_link()
    time.sleep(1)

    expecte_title = "Demo WebShop.Register"
    actual_title = home_page.get_title()

    assert actual_title == expecte_title,f"页面标题错误！预期为{expecte_title},实际为：{actual_title}"
