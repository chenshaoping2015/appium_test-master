#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os,sys

sys.path.append(os.getcwd())
from base.base_driver import init_driver
from time import sleep
from appium.webdriver.common.mobileby import MobileBy
import allure
from page.main_page import MainPage


class TestWX:

    def setup_class(self):
        self.main_page = MainPage()
    def setup(self):
        self.main = self.main_page.goto_contactlist()

    def teardown(self):
        self.driver.quit()

    def test_contact(self):
        name = "aaaa"
        gender = "男"
        phone = "13111111111"
        result = self.main.add_member().add_member_manul().edit_contact(name, gender,phone).verify_toast()
        assert result == "添加成功"

