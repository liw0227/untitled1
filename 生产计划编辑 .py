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


hour = [8, 9, 10, 11, 14, 15, 16, 17]  # 8, 9, 10, 11, 14,
min = [-5, 60]
h = []
m = []
for time_h in hour:
    for time_m in min:
        while time_m < 55:
            time_m += 5
            if time_h == 17 and time_m > 30:
                continue
            elif time_h == 8 and time_m <= 30:
                continue
            elif time_h == 14 and time_m <= 30:
                continue
            else:
                h.append(time_h), m.append(time_m)

#  获取当前页面的句柄：
currentWin = driver.current_window_handle
print(currentWin)

lists = driver.find_elements_by_name('defectCodes')
for a in range(0, len(lists)):
    # 跳转到另一个新页面
    print(lists)
    print(lists[a].text)
    lists[a].click()
    time.sleep(1)

    # 获取所有窗口的句柄
    handles = driver.window_handles
    print(handles)

    for i in handles:
        if currentWin == i:
            continue
        else:
            # 将driver与新的页面绑定起来
            driver.switch_to.window(i)
    #  ------------新的页面---------------------
    print('当前页面' + driver.title)

    qxls = driver.find_element_by_id('defectTypeName')  # 缺陷类型
    gxms = driver.find_element_by_id('defectDesc')  # 缺陷描述
    qxry = driver.find_element_by_xpath('//*[@id="defectcause-select-btn"]')  # 缺陷原因

    rq = driver.find_element_by_xpath('//*[@id="dealTime"]/div/a')  # 日期
    t = qxls.get_attribute('value')
    b = gxms.get_attribute('value')
    print(t)
    print(b)

    # ---------------------------处理措施--------------------
    ActionChains(driver).move_to_element(driver.find_element_by_xpath('//*[@id="attachment-info-a"]')).perform()  # 页面移动到指定位置
    driver.find_element_by_xpath('//*[@id="dealMeasure"]/div[1]/input').click()
    time.sleep(2)
    x = driver.find_element_by_xpath('/html/body/div[26]/div/a[7]')
    if x.get_attribute('title') == '其他':
        print(x)
        x.click()
    else:
        driver.find_element_by_xpath('/html/body/div[27]/div/a[7]').click()
    print('处理措施')
    time.sleep(1)

    # ------------------缺陷原因------------------------------------------------------------------------------------------
    qxry.click()
    time.sleep(0.5)
    ywjd = driver.find_element_by_xpath('//*[@id="tree"]/ul/li/ul/li[3]/span/a')  # 运维阶段//DIV弹窗，先点击，后加载。
    ywjd.click()
    time.sleep(0.5)
    if t == '藤蔓攀爬':
        driver.find_element_by_xpath('//*[@id="keyword"]').send_keys('高温')
    elif t == '飘挂物':
        driver.find_element_by_xpath('//*[@id="keyword"]').send_keys('外力破坏-违章作业（非电力施工）')
    time.sleep(0.5)
    driver.find_element_by_xpath('//*[@id="query"]').click()  # 查询
    time.sleep(1)
    driver.find_element_by_xpath('//*[@id="defectstandardlibtable"]/tbody/tr/td[1]').click()  # 选择
    time.sleep(0.5)
    driver.find_element_by_xpath('//*[@id="confirm"]').click()  # 确定
    time.sleep(1)
    print('缺陷原因')
    # --------------------------已消缺------------------------------------------------------------------------
    driver.find_element_by_xpath('//*[@id="dealResult"]/div/label[1]').click()  # 已消缺
    time.sleep(1)
    print('已消缺')
    # ----------------------------消缺时间---------------------------------------


    driver.find_element_by_xpath('//*[@id="dealTime"]/div/a').click()
    driver.find_element_by_xpath('//*[@val="h"]').clear()
    driver.find_element_by_xpath('//*[@val="h"]').send_keys(str(h[a]))
    time.sleep(0.5)
    driver.find_element_by_xpath('//*[@val="m"]').clear()
    driver.find_element_by_xpath('//*[@val="m"]').send_keys(str(m[a]))
    time.sleep(0.5)
    driver.find_element_by_xpath('//*[@class="cui-button green-button"]').click()
    time.sleep(0.5)
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
    driver.find_element_by_xpath('//*[@name="legacy"]').clear()
    driver.find_element_by_xpath('//*[@name="legacy"]').send_keys('无')
    print('遗留问题')

    # ---------------------------处理情况描述-----------------------------------
    if t == '飘挂物':
        text = re.findall(r'(.+?)广告', b)[0] + '广告牌，已拆除广告牌。'
        driver.find_element_by_xpath('//*[@name="dealDesc"]').clear()
        driver.find_element_by_xpath('//*[@name="dealDesc"]').send_keys(text)
        print('处理情况描述')
    elif t == '藤蔓攀爬':
        text = re.findall(r'(.+?)藤蔓攀爬', b)[0] + '藤蔓攀爬，藤蔓已处理。'
        driver.find_element_by_xpath('//*[@name="dealDesc"]').clear()
        driver.find_element_by_xpath('//*[@name="dealDesc"]').send_keys(text)
        print('处理情况描述')
    elif t == '警示牌缺损、错误':
        text = re.findall(r'(.+?)标志牌', b)[0] + '标志牌褪色，已更换标志牌。'
        driver.find_element_by_xpath('//*[@name="dealDesc"]').clear()
        driver.find_element_by_xpath('//*[@name="dealDesc"]').send_keys(text)
        print('处理情况描述')

    # --------------------保存---------------------------------
    driver.find_element_by_xpath('//*[@id="save_btn"]').click()
    print(driver.find_element_by_xpath('//*[@id="save_btn"]').get_attribute('tip'))
    time.sleep(1)
    print('保存')
    print(driver.title)
    driver.close()  # 关闭新打开的窗口
    driver.switch_to.window(currentWin)  # 转到首页
    print(len(lists), a+1)
    print('时间', h[a], m[a])
print('完成')

