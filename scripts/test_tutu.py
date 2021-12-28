import pytest
from selenium import webdriver
from time import sleep
import allure

class TestTuTu:

    @allure.step(title='高途在线')
    def test_tutu(self):
        driver = webdriver.Chrome()
        driver.get("http://www.genshuixue.com/")
        driver.maximize_window()
        sleep(3)
        driver.quit()