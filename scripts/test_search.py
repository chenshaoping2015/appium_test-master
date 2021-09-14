import os,sys
import allure
sys.path.append(os.getcwd())

from base.base_driver import init_driver
from page.search_page import SearchPage
from base.base_yml import get_data_with_file
import pytest

def data_with_key(key):
    return get_data_with_file('search_data')[key]

class TestSearch:

    def setup(self):
       self.driver = init_driver()
       self.search_page = SearchPage(self.driver)

    def teardown(self):
        self.driver.quit()

    @pytest.mark.parametrize("content",data_with_key('test_search'))
    @allure.step(title="搜索关键字")
    def test_search(self,content):
        #点击放大镜
        allure.attach("点击放大镜","点击放大镜按钮")
        self.search_page.click_search()
        #输入文字
        allure.attach("输入文字","输入3个参数")
        self.search_page.input_search_text(content)
        #点击返回
        allure.attach("点击返回","点击返回按钮")
        self.search_page.click_back()
