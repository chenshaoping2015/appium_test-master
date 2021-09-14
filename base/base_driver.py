import os,sys

from page.main_page import MainPage

sys.path.append(os.getcwd())
from appium import webdriver

def init_driver(self):
    _app_package = 'com.tencent.wework'
    _app_activity = '.launch.LaunchSplashActivity'
    # server启动参数
    desired_caps = {}
    # 设备信息
    desired_caps['platformName'] = 'Android'
    desired_caps['platformVersion'] = '7.1.2'
    desired_caps['deviceName'] = '127.0.0.1:7555'
    # app信息
    desired_caps['appPackage'] = _app_package
    desired_caps['appActivity'] = _app_activity
    # 支持中文
    desired_caps['unicodeKeyboard'] = True
    desired_caps['resetKeyboard'] = True
    #保留登录状态
    desired_caps['noReset'] = 'true'

    self._driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
    self._driver.implicitly_wait(15)
    return self

