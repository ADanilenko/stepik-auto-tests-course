import time
import math
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

try:
    browser = webdriver.Chrome('C:\\Users\\Alena\\Downloads\\chromedriver92\\chromedriver')
    browser.get('http://suninjuly.github.io/explicit_wait2.html')

    check = WebDriverWait(browser, 12).until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, 'h5[id=price]'), '100'))
    click_book = browser.find_element_by_css_selector('button[id=book]').click()

    def calc(x):
        return str(math.log(abs(12*math.sin(int(x)))))

    x_element = browser.find_element_by_id('input_value')
    x = x_element.text
    y = calc(x)

    line = browser.find_element_by_id('answer').send_keys(y)
    click_submit = browser.find_element_by_css_selector("[type='submit']").click()

finally:
    time.sleep(10)
    browser.quit()