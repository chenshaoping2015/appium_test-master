from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By

class BaseAction:
    def __init__(self,driver):
        self.driver = driver

    def click(self,loc):
        self.find_element(loc).click()

    def input_text(self,loc,text):
        self.find_element(loc).send_keys(text)

    def find_element(self, loc):
        WebDriverWait(self.driver,3).until(lambda x:x.find_element(loc[0], loc[1]))
        return self.driver.find_element(loc[0], loc[1])

    def find_toast(self,message):
        #message：预期要获取的toast的部分消息
        message = "//*[contains(@text,'"+ message + "']"#使用包含的方式定位
        ele = self.find_element((By.XPATH,message))
        return ele.text

    def is_login_with_toast(self,text):
        try:
            print(self.find_toast(text))
            return True
        except Exception:
            return False
    def find_by_scroll(self,text):
        return self.driver.find_element(MobileBy.ANDROID_UIAUTOMATOR,
                                        'new UiScrollable(new UiSelector()'
                                        '.scrollable(true).instance(0))'
                                        '.scrollIntoView(new UiSelector()'
                                        f'.text("{text}").instance(0));')
    def get_toast_text(self):
        result = self.find(MobileBy.XPATH, "//*[@class='android.widget.Toast']").text
        return result