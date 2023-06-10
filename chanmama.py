from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
import time

# browser = webdriver.Chrome()
browser = webdriver.Firefox()
# url = 'https://www.chanmama.com/promotionRank?keyword=&category_id=162&has_jx_commission=0'
url = 'https://www.chanmama.com/login'
browser.get(url)
time.sleep(3)
phone_input = browser.find_element('id', 'e2e-login-username')
phone_input.send_keys('18682962409')

passwd_input = browser.find_element('id', 'e2e-login-password')
passwd_input.send_keys('xiaolou766')
time.sleep(2)
submit_button = browser.find_element('id', 'e2e-login-submit')
submit_button.click()

try:
    close_box = browser.find_element('class name', 'close_box')
    close_box.click()
except NoSuchElementException:
    print('not FOUND, continue')

time.sleep(3)
food_url = 'https://www.chanmama.com/promotionRank?keyword=&category_id=162&has_jx_commission=0'
browser.get(food_url)
time.sleep(5)

baihuo = browser.find_element('xpath', '//span[@class="el-tooltip item" and text()="日用百货"]')
baihuo.click()

# 获取最上层领域链接
print(browser.current_url)
with open('baihuo.html', 'w', encoding='utf-8') as f:
    f.write(browser.page_source)
time.sleep(2)

# 获取某个细分领域的链接
clearing_span = browser.find_element('xpath', '//span[@class="el-tooltip text ellipsis-1" and text()="家庭清洁"]')
clearing_span.click()
time.sleep(1)

# 下拉刷新界面，加载更多内容
for i in range(3):  # 下拉3次
    body = browser.find_element('tag name', 'body')
    body.send_keys(Keys.PAGE_DOWN)
    time.sleep(1)

# 获取到商品信息
food_list = browser.find_elements('xpath', '//a[@class="el-tooltip ellipsis-2 text-decoration-none fs12 c333 link-hover cursor-pointer"]')
print(food_list)

# 将商品信息的禅妈妈解析地址和名称打印出来
for food in food_list:
    link = food.get_attribute('href')
    text = food.text
    print(link, text)
    time.sleep(1)

with open('chanmama.html', 'w', encoding='utf-8') as f:
    f.write(browser.page_source)
browser.quit()
exit(0)
time.sleep(90)
# print(browser.find_element_by_name('td'))
browser.quit()
