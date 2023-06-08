import pytest
from selenium import webdriver

driver = webdriver.Chrome()

@pytest.mark.skip
def test():
    driver.get('https://www.baidu.com/')
    driver.find_element_by_id('kw').send_keys('lk')
    driver.find_element_by_id('su').click()
