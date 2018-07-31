#! /usr/bin/env python
# _*_ coding: utf-8 _*_
# __author__ = 'bill'
# create on 2018/7/31

from selenium import webdriver

driver=webdriver.Chrome()
driver.get("https://www.baidu.com")
print(driver.page_source)
driver.close()