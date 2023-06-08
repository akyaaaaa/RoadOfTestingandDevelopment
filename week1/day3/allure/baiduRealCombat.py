import time

import allure
import pytest
from selenium import webdriver


class TestDemo:
    @allure.feature('百度搜索')
    @pytest.mark.parametrize('keyword',['lk','lt','lyx'])
    def test_baidu(self,keyword):

        with allure.step('打开百度网页'):
            driver = webdriver.Chrome()
            driver.get('http://www.baidu.com')
            driver.maximize_window()

        with allure.step(f'输入搜索词{keyword}'):
            driver.find_element_by_id('kw').send_keys(keyword)
            time.sleep(2)
            driver.find_element_by_id('su').click()
            time.sleep(2)

        with allure.step('保存图片'):
            driver.save_screenshot('./result/png/screenshot.png')
            allure.attach.file('./result/png/screenshot.png',attachment_type=allure.attachment_type.PNG)
        with allure.step('关闭浏览器'):
            driver.quit()
if __name__ == '__main__':
    pytest.main()