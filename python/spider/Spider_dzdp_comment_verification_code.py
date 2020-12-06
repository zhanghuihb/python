import random
import time

from pyquery import PyQuery
from selenium import webdriver
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
            self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "#yodaImgCode")))

            with open('code.html', 'w', encoding='utf-8') as f:
                f.write(self.browser.page_source)

            return True
        except:
            print("待识别验证码未出现，识别成功")
            return True
if __name__ == '__main__':
    url = 'http://www.dianping.com/shop/l35tKdqLK2r6SbXm/review_all/p20'
    recogniton = Recogniton()
    recogniton.recognition_verification_code(url)