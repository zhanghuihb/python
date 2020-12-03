import random
import time

from pyquery import PyQuery
from selenium.webdriver.chrome import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Recogniton():
    def __init__(self):
        """
        类初始化
        """
        # 无界面模式
        self.chrome_options = webdriver.ChromeOptions()
        # self.chrome_options.add_argument('--headless')

        # self.browser = webdriver.Chrome()
        self.browser = webdriver.Chrome(chrome_options=self.chrome_options)

        self.wait = WebDriverWait(self.browser, 10)

    def recognition_verification_code(self, url):
        """
        识别验证码
        :return:
        """
        try:
            self.browser.get(url)
            self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, ".reviews-items ul li")))

            return True
        except:
            print("待识别验证码未出现，识别成功")
            return True