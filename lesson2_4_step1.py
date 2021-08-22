from selenium import webdriver
import time
# try:
#     browser = webdriver.Chrome('C:\\Users\\Alena\\Downloads\\chromedriver92\\chromedriver')
#     browser.implicitly_wait(5)
#     browser.get('http://suninjuly.github.io/wait1.html')
#
#     button = browser.find_element_by_id("verify")
#     button.click()
#     message = browser.find_element_by_id("verify_message")
#
#     assert "successful" in message.text
#
# finally:
#     browser.quit()

try:
    browser = webdriver.Chrome('C:\\Users\\Alena\\Downloads\\chromedriver92\\chromedriver')
    # browser.implicitly_wait(5)
    browser.get('http://suninjuly.github.io/cats.html')
    command =  browser.find_element_by_id("button")

finally:
    browser.quit()