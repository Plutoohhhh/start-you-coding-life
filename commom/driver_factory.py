from selenium import webdriver
try:from selenium.webdriver.chrome.service import Service as ChromeService
except ImportError: raise ImportError("webdriver-manager库导入失败，请确保在环境中已经正确安装：pip install webdriver-manager")
from webdriver_manager.chrome import  ChromeDriverManager
import os


def get_driver():
    service = ChromeService(ChromeDriverManager().install())
    options = webdriver.ChromeOptions()
    if os.getenv("HEADLESS") == "true":
        print("---检测到HEADLESS环境变量，以无头模式运行chrome")
        options.add_argument("--headless")
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")
        options.add_argument("--window-size=1920,1080")
    options.add_argument("--headless") #无头模式，不会启动浏览器窗口
    options.add_argument("--start-maximized")
    driver = webdriver.Chrome(service=service,options=options)
    driver.maximize_window()
    driver.implicitly_wait(5)
    return driver

