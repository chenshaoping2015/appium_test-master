#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 编辑成员页面
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support.wait import WebDriverWait
from base.base_action import BaseAction
from page.member_invite_page import MemberInviteMenuPage

'''
编辑联系人页面
'''


class ContactAddPage(BaseAction):
    send_name = MobileBy.XPATH, '//*[contains(@text, "姓名")]/../android.widget.EditText'
    click_gender = MobileBy.XPATH, "//*[@text='性别']/..//*[@text='男']"
    click_men = MobileBy.XPATH, "//*[@text='男']"
    click_women = MobileBy.XPATH, "//*[@text='女']"
    send_mobilephone = MobileBy.XPATH, "//*[@text='手机号']"
    click_save = MobileBy.XPATH, "//*[@text='保存']"


    def edit_contact(self, name, gender, phonenum):
        '''
        编辑成员信息
        '''
        self.input_text(self.send_name,name)
        self.click(self.click_gender)
        if gender == "男":
            WebDriverWait(self.driver, 10).until(lambda x: x.find_element(self.click_women))
            self.click(self.click_men)
        else:
            self.click(self.click_women)

        self.input_text(self.send_mobilephone,phonenum)
        self.click(self.click_save)

        return MemberInviteMenuPage(self.driver)
