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



# ---------------开始时间----------------

driver.find_element_by_xpath('//*[@name="isDealDefect"]').click()
driver.find_element_by_xpath('//*[@id="realBeginDate"]/div/a').click()
driver.find_element_by_xpath('//*[@name="timer_h"]').clear()
driver.find_element_by_xpath('//*[@name="timer_h"]').send_keys('8')
driver.find_element_by_xpath('//*[@name="timer_m"]').clear()
driver.find_element_by_xpath('//*[@name="timer_m"]').send_keys('35')
driver.find_element_by_xpath('//*[@class="cui C_CR "]/div[4]/a[2]').click()
driver.find_element_by_xpath('//*[@class="cui C_CR "]/div[4]/a[3]').click()

# ---------------完成时间----------------
# driver.find_element_by_xpath('//*[@id="realEndDate"]/div/a').click()
# driver.find_element_by_xpath('//*[@name="timer_h"]').clear()
# driver.find_element_by_xpath('//*[@class="C_CR_YM_wrap"]/div[3]/div/div[1]/table/tbody/tr/td[3]/span/input').send_keys('17')
# driver.find_element_by_xpath('//*[@name="timer_m"]').clear()
# driver.find_element_by_xpath('//*[@name="timer_m"]').send_keys('25')
# driver.find_element_by_xpath('//*[class="cui-button green-button"]').click()
# driver.find_element_by_xpath('//*[class="cui-button blue-button"]').click()


# ------------------工作结果--------------------------
driver.find_element_by_xpath('//*[@name="completionCondition"]').clear()
driver.find_element_by_xpath('//*[@name="completionCondition"]').send_keys('工作已完成。')