from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import re
from selenium.webdriver.common.action_chains import ActionChains
import time
from selenium.webdriver.support.ui import Select

chrome_options = Options()
chrome_options.add_experimental_option("debuggerAddress", "127.0.0.1:9222")
chrome_driver = r"D:\Users\Administrator\AppData\Local\360Chrome\Chrome\Application\chromedriver.exe"
driver = webdriver.Chrome(chrome_driver, chrome_options=chrome_options)
driver.implicitly_wait(180)  # 隐式等待60秒

print(driver.title)

# ----------处理情况描述---------------
cljhms = driver.find_element_by_xpath('//*[@id="dealDesc"]').text
print(cljhms)
#--------------验收意见----------------
driver.find_element_by_xpath('//*[@id="checkNotes"]').click()
time.sleep(1)
text = cljhms + '验收合格。'
print(text)
driver.find_element_by_xpath('//*[@name="checkNotes"]').clear()
driver.find_element_by_xpath('//*[@name="checkNotes"]').send_keys(text)
time.sleep(1)
#--------------验收时间----------------
driver.find_element_by_xpath('//*[@id="checkTime"]/div/a').click()

driver.find_element_by_xpath('//*[@name="timer_h"]').clear()
driver.find_element_by_xpath('//*[@name="timer_h"]').send_keys('17')

driver.find_element_by_xpath('//*[@name="timer_m"]').clear()
driver.find_element_by_xpath('//*[@name="timer_m"]').send_keys('05')

driver.find_element_by_xpath('//*[@class="cui-button green-button"]').click()

driver.find_element_by_xpath('//*[@class="cui-button blue-button"]').click()
