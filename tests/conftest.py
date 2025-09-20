import pytest
from commom.driver_factory import get_driver
from commom.config_reader import get_config
from page_object.login_page import LoginPage

@pytest.fixture
def loggin_in_driver(driver):
    username = get_config("users","standard_user")
    password = get_config("users","standard_password")
    login_page = LoginPage(driver)
    login_page.login(username,password)

    yield driver

    print("\n测试用例执行完毕，可以执行清理操作，如退出登录")