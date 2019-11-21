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
driver.implicitly_wait(60)  # 隐式等待60秒

print(driver.title)

qxls = driver.find_element_by_id('defectTypeName')  # 缺陷类型
gxms = driver.find_element_by_id('defectDesc')  # 缺陷描述
qxry = driver.find_element_by_xpath('//*[@id="defectcause-select-btn"]')  # 缺陷原因


rq = driver.find_element_by_xpath('//*[@id="dealTime"]/div/a')  # 日期
t = qxls.get_attribute('value')
b = gxms.get_attribute('value')
print(t)
print(b)
# c = re.findall(r'(.+?)广告', b)
# print(type(c[0]))
# -----------------------加图片----------------------
driver.find_element_by_xpath('//*[@id="attachment-container-before"]/div/div[1]/div[1]/div').click()

