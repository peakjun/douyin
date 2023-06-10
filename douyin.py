from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
import time

browser = webdriver.Firefox()
url = 'https://www.douyin.com'
browser.get(url)
time.sleep(3)
try:
    login_in = browser.find_element('xpath', '//p[@class="lqiPv8cB" and text()="登录"]')
    login_in.click()
    time.sleep(1)
except:
    print('error, but no problem')

passwd_login = browser.find_element('xpath', '//li[@class="web-login-tab-list__item" and text()="密码登录"]')
passwd_login.click()
time.sleep(1)

phone_input = browser.find_element('xpath', '//input[@placeholder="手机号"]')
phone_input.send_keys('19339933537')
time.sleep(1)

passwd_input = browser.find_element('xpath', '//input[@placeholder="请输入密码"]')
passwd_input.send_keys('xiaolou766')

time.sleep(1)
submit_button = browser.find_element('xpath', '//button[@class="web-login-button"]')
submit_button.click()
time.sleep(2)

browser.get('https://www.douyin.com/search/%E5%85%83%E6%B0%94%E6%BB%A1%E6%BB%A1%E5%9E%83%E5%9C%BE%E8%A2%8B?publish_time=0&sort_type=0&source=switch_tab&type=video')
time.sleep(2)





