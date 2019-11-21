# 360chrome.exe --remote-debugging-port=9222
# 文件上传AutoIT
# 参考https://blog.csdn.net/weixin_42024694/article/details/80080629
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

#  获取当前页面的句柄：
currentWin = driver.current_window_handle
print(currentWin)

driver.switch_to.frame(driver.find_element_by_xpath('//*[@id="sideFrame"]'))
a = driver.find_element_by_xpath('//*[@id="generate-span"]').text
print(a)
i = 0
while i < int(a):
    i += 1
    print(i)
    driver.find_element_by_xpath('//*[@target="_blank"]').click()

    #----------