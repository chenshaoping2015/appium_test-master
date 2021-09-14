#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 主页
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.remote.webdriver import WebDriver

from base.base_action import BaseAction
from page.contact_list_page import ContactListPage


class MainPage(BaseAction):
    # 首页-通讯录
    _contact_list = (MobileBy.XPATH, "//*[@text='通讯录']")

    def goto_contactlist(self):
        '''
        进入到通讯录
        '''
        # 点击【通讯录】

        self.click(*self._contact_list)
        return ContactListPage(self.driver)
