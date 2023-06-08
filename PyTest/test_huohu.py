import pytest
from selenium import webdriver

driver = webdriver.Chrome()


def test_huohu():
    driver.get('https://www.baidu.com/')
    driver.find_element_by_id('kw').send_keys('火狐')
    driver.find_element_by_id('su').click()
    print('火狐用例执行了')
@pytest.mark.run
def test_guge():
    driver.get('https://www.baidu.com/')
    driver.find_element_by_id('kw').send_keys('谷歌')
    driver.find_element_by_id('su').click()
    print('谷歌用例执行了')