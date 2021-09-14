import os,sys
sys.path.append(os.getcwd())
from selenium.webdriver.common.by import By
from base.base_action import BaseAction

class NetworkPage(BaseAction):
    #网络按钮
    network_button = By.XPATH,"//*[contains(@text,'Network & Internet')]"
    #移动网络按钮
    mobile_button = By.XPATH,"//*[contains(@text,'Mobile network')]"
    #网络类型按钮
    network_type_button = By.XPATH,"//*[contains(@text,'Preferred network type')]"
    #2g按钮
    network_2g_button = By.XPATH,"//*[contains(@text,'2G')]"
    #3g按钮
    network_3g_button = By.XPATH,"//*[contains(@text,'3G')]"

    # def __init__(self,driver):
    #     BaseAction.__init__(self,driver)
        #self.driver = driver

    def click_network(self):
        #self.driver.find_element_by_xpath("//*[contains(@text,'Network & Internet')]").click()
        #self.find_element(self.network_button).click()
        self.click(self.network_button)


    def click_mobile_net(self):
        #self.driver.find_element_by_xpath("//*[contains(@text,'Mobile network')]").click()
        #self.find_element(self.mobile_button).click()
        self.click(self.mobile_button)

    def click_network_type(self):
        #self.driver.find_element_by_xpath("//*[contains(@text,'Preferred network type')]").click()
        #self.find_element(self.network_type_button).click()
        self.click(self.network_type_button)

    def click_2g(self):
        #self.driver.find_element_by_xpath("//*[contains(@text,'2G')]").click()
        #self.find_element(self.network_2g_button).click()
        self.click(self.network_2g_button)

    def click_3g(self):
        #self.driver.find_element_by_xpath("//*[contains(@text,'3G')]").click()
        self.find_element(self.network_3g_button).click()
        #self.click(self.network_3g_button)

    # def find_element(self,loc):
    #     return self.driver.find_element(loc[0],loc[1])