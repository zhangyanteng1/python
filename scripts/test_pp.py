import pytest
from selenium import webdriver
from time import sleep
import allure
class TestGaoTu:

    @allure.step(title='高途')
    def test_gaotu(self):
        driver = webdriver.Chrome()
        driver.get("http://www.gaotu100.com")
        driver.maximize_window()
        sleep(3)
        driver.quit()
