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
# ---------------------------处理措施--------------------
ActionChains(driver).move_to_element(driver.find_element_by_xpath('//*[@id="attachment-info-a"]')).perform()  # 页面移动到指定位置
driver.find_element_by_xpath('//*[@id="dealMeasure"]/div[1]/input').click()
time.sleep(1)
driver.find_element_by_xpath('/html/body/div[26]/div/a[7]').click()
print('处理措施')
time.sleep(1)
# ------------------缺陷原因------------------------------------------------------------------------------------------
qxry.click()
ywjd = driver.find_element_by_xpath('//*[@id="tree"]/ul/li/ul/li[3]/span/a')  # 运维阶段//DIV弹窗，先点击，后加载。
ywjd.click()
if t == '藤蔓攀爬':
    driver.find_element_by_xpath('//*[@id="keyword"]').send_keys('高温')
elif t == '飘挂物':
    driver.find_element_by_xpath('//*[@id="keyword"]').send_keys('外力破坏-违章作业（非电力施工）')
driver.find_element_by_xpath('//*[@id="query"]').click()  # 查询
time.sleep(0.5)

driver.find_element_by_xpath('//*[@id="defectstandardlibtable"]/tbody/tr/td[1]').click()  # 选择
driver.find_element_by_xpath('//*[@id="confirm"]').click()  # 确定
time.sleep(1)
print('缺陷原因')
# --------------------------已消缺------------------------------------------------------------------------
driver.find_element_by_xpath('//*[@id="dealResult"]/div/label[1]').click()  # 已消缺
time.sleep(1)
print('已消缺')
# ----------------------------消缺时间---------------------------------------
time_h = 8
time_m = 5
driver.find_element_by_xpath('//*[@id="dealTime"]/div/a').click()
driver.find_element_by_xpath('//*[@val="h"]').clear()
driver.find_element_by_xpath('//*[@val="h"]').send_keys(str(time_h))
driver.find_element_by_xpath('//*[@val="m"]').clear()
driver.find_element_by_xpath('//*[@val="m"]').send_keys(str(time_m))
driver.find_element_by_xpath('//*[@class="cui-button green-button"]').click()
driver.find_element_by_xpath('//*[@class="cui-button blue-button"]').click()

time.sleep(1)
print('消缺时间')

# -----------------------缺陷部位-----------------------
driver.find_element_by_xpath('//*[@id="defectposition-select-btn"]').click()
driver.find_element_by_xpath('//*[@id="defectstandardlibtable"]/tbody/tr/td[1]').click()
driver.find_element_by_xpath('//*[@id="confirm"]').click()
print('缺陷部位')
time.sleep(1)


# =======================遗留问题------------------------------------------
driver.find_element_by_xpath('//*[@name="legacy"]').send_keys('无')
print('遗留问题')

# ---------------------------处理情况描述-----------------------------------
if t == '飘挂物':
    text = re.findall(r'(.+?)广告', b)[0] + '广告牌，已拆除广告牌。'
    driver.find_element_by_xpath('//*[@name="dealDesc"]').clear()
    driver.find_element_by_xpath('//*[@name="dealDesc"]').send_keys(text)
    print('处理情况描述')
elif t =='藤蔓攀爬':
    text = re.findall(r'(.+?)藤蔓攀爬', b)[0] + '藤蔓攀爬，藤蔓已处理。'
    driver.find_element_by_xpath('//*[@name="dealDesc"]').clear()
    driver.find_element_by_xpath('//*[@name="dealDesc"]').send_keys(text)
    print('处理情况描述')
elif t =='警示牌缺损、错误':
    text = re.findall(r'(.+?)标志牌', b)[0] + '标志牌褪色，已更换标志牌。'
    driver.find_element_by_xpath('//*[@name="dealDesc"]').clear()
    driver.find_element_by_xpath('//*[@name="dealDesc"]').send_keys(text)
    print('处理情况描述')


#  --------------------保存---------------------------------
driver.find_element_by_xpath('//*[@id="save_btn"]').clear()


