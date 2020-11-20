from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

browser = webdriver.Chrome()
try:
    browser.get('https://zhihu.com/explore')
    browser.implicitly_wait(10)
    input = browser.find_element_by_class_name('Input')
    print(input.text)
    # logo_element = browser.find_element(By.CSS_SELECTOR,'.ZhihuLogoLink')
    # print(logo_element.text)
    # browser.get('https://www.taobao.com')
    # list = browser.find_elements(By.CSS_SELECTOR,'.service-bd li')
    # print(list)
    # input = browser.find_element_by_id('kw')
    # input.send_keys('Python')
    # input.send_keys(Keys.ENTER)
    # wait = WebDriverWait(browser, 10)
    # wait.until(EC.presence_of_element_located((By.ID, 'content_left')))
    # print(browser.current_url)
    # print(browser.get_cookies())
    # print(browser.page_source)

    # input_first = browser.find_element_by_id('q')
    # input_second = browser.find_element_by_css_selector('#q')
    # input_third = browser.find_element_by_xpath('//*[@id="q"]')
    # print(input_first, input_third,input_second)
finally:
    browser.close()