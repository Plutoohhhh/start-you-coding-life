import pytest
from commom.driver_factory import get_driver
from commom.config_reader import get_config
from page_object.login_page import LoginPage

@pytest.fixture(scope="function")
#scope表示每一个测试函数都会执行一次这个fixture
def driver():
    #为每一个测试函数都创建一个实例
    web_driver = get_driver()
    yield web_driver
    print("——————测试结束，关闭浏览器——————")
    web_driver.quit()

@pytest.fixture
def loggin_in_driver(driver):
    username = get_config("users","standard_user")
    password = get_config("users","standard_password")
    login_page = LoginPage(driver)
    login_page.login(username,password)

    yield driver

    print("\n测试用例执行完毕，可以执行清理操作，如退出登录")
