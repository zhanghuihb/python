from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait

EMAIL = "zhanghuihb@126.com"
PASSWORD = "123456"

class CrackGeetest():
    def __init__(self):
        self.url = "https://account.geetest.com/login"
        self.browser = webdriver.Chrome()
        self.wait = WebDriverWait(self.browser, 20)
        self.email = EMAIL
        self.password = PASSWORD