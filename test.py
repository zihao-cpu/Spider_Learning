#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   test.py
@Time    :   2024/12/12 15:53:32
@Author  :   Zihao Zheng 
@Email   :   zhengzihao718@163.com
'''
#自动登录ADNI
import time
import sys
sys.path.append("D:/Python_learing/pubmed_craw/MicrosoftWebDriver.exe")
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.edge.service import Service
from selenium.webdriver.common.action_chains import ActionChains

driver =  webdriver.Edge()
driver.get("https://ida.loni.usc.edu/login.jsp")  

cookies=driver.get_cookies()
for c in cookies:
    driver.add_cookie(c)
time.sleep(10)
ActionChains(driver).move_to_element(driver.find_element_by_xpath('/html/body/div[2]/div/div[1]/div[3]/div')).click().perform()
# driver.refresh()
time.sleep(10)
ActionChains(driver).move_to_element(driver.find_element_by_xpath('/html/body/div[1]/div[2]/div/div/div[2]/div[4]')).click().perform()

#登录账号

driver.find_element_by_name('userEmail').send_keys('zhengzihao718@163.com')

driver.find_element_by_name('userPassword').send_keys('zhengzihao718@163')
time.sleep(5)
ActionChains(driver).move_to_element(driver.find_element_by_xpath('/html/body/div[1]/div[2]/div/div/div[2]/div[4]/div[2]/div/div[1]/form/div[3]/span')).click().perform()