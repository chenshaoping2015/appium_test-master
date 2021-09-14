#!/usr/bin/env python
# -*- coding: utf-8 -*-
from appium.webdriver.common.mobileby import MobileBy
from base.base_action import BaseAction


class MemberInviteMenuPage(BaseAction):
    click_add = MobileBy.XPATH, "//*[@text='手动输入添加']"

    def add_member_manul(self):
        # 点击【手动输入添加】
        self.click(self.click_add)

        from page.contact_add_page import ContactAddPage
        return ContactAddPage(self.driver)

    def verify_toast(self):
        # result = self.find(MobileBy.XPATH, "//*[@class='android.widget.Toast']").text
        result = self.get_toast_text()
        return result
