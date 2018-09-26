#! /usr/bin/env python
# _*_ coding: utf-8 _*_
# __author__ = 'bill'
# create on 2018/9/26

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage(object):
    def __init__(self,selenium_driver,base_url):
        self.driver = selenium_driver
        self.base_url = base_url

    def on_page(self,pagetitle):
        return pagetitle in self.driver.title

    def _open(self,url):
        self.driver.get(url)
        self.driver.maximiza_window()

    def open(self):
        self._open(self.base_url,self.pagetitle)

    def find_element(self,*loc):
        try:
            WebDriverWait(self.driver,10).until(EC.visibility_of_element_located(loc))
            return self.driver.find_element(*loc)
        except:
            print ("%s 页面未能找到 %s 元素"%(self,loc))

    def script(self,src):
        self.driver.excute_script(src)

    def send_keys(self,loc,value,clear_first=True,click_first=True):
        try:
            loc = getattr(self,"_%s"% loc)
            if click_first:
                self.find_element(*loc).click()
            if clear_first:
                self.find_element(*loc).clear()
                self.find_element(*loc).send_keys(value)
        except  AttributeError:
            print ("%s 页面未能找到 %s 元素"(self,loc))