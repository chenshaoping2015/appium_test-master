import os,sys
sys.path.append(os.getcwd())
from base.base_driver import init_driver
from page.network_page import NetworkPage
import allure

class TestNetwork:
    def setup(self):
        self.driver = init_driver()
        self.network_page = NetworkPage(self.driver)

    def teardown(self):
        self.driver.quit()

    @allure.step(title="2g")
    def test_network_2g(self):
        allure.attach("点击网络","点击网络按钮")
        self.network_page.click_network()
        allure.attach("点击移动网络", "点击移动网络按钮")
        self.network_page.click_mobile_net()
        allure.attach("点击网络类型", "点击网络类型按钮")
        self.network_page.click_network_type()
        allure.attach("点击2g", "点击2g按钮")
        self.network_page.click_2g()

    @allure.step(title="3g")
    def test_network_3g(self):
        allure.attach("点击网络", "点击网络按钮")
        self.network_page.click_network()
        allure.attach("点击移动网络", "点击移动网络按钮")
        self.network_page.click_mobile_net()
        allure.attach("点击网络类型", "点击网络类型按钮")
        self.network_page.click_network_type()
        allure.attach("点击3g", "点击3g按钮")
        self.network_page.click_3g()
