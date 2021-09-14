import os,sys
sys.path.append(os.getcwd())
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.common.by import By
from base.base_action import BaseAction

class SearchPage(BaseAction):
    #搜索按钮
    search_button = By.ID,"com.android.settings:id/search"
    #搜索框
    input_textview = By.ID, "android:id/search_src_text"
    #返回按钮
    back_button = By.CLASS_NAME, "android.widget.ImageButton"

    def __init__(self,driver):
        BaseAction.__init__(self,driver)
        #self.driver = driver

    def click_search(self):
        #self.driver.find_element_by_accessibility_id("Search settings").click()
        #self.driver.find_element(MobileBy.ACCESSIBILITY_ID,"Search settings").click()
        #self.find_element(self.search_button).click()
        self.click(self.search_button)

    def input_search_text(self,text):
        #self.driver.find_element_by_id("android:id/search_src_text").send_keys(text)
        #self.driver.find_element(By.ID, "android:id/search_src_text").send_keys(text)
        #self.find_element(self.input_textview).send_keys(text)
        self.input_text(self.input_textview,text)

    def click_back(self):
        #self.driver.find_element_by_class_name("android.widget.ImageButton").click()
        #self.driver.find_element(By.CLASS_NAME, "android.widget.ImageButton").click()
        #self.find_element(self.back_button).click()
        self.click(self.back_button)

    # def find_element(self,loc):
    #     return self.driver.find_element(loc[0],loc[1])
