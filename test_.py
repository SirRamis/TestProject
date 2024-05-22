import time

from selenium import webdriver
from selenium.webdriver.common.by import By

def test_ferst():
    options = webdriver.ChromeOptions()
    binary_yandex_driver_file = 'yandexdriver.exe'
    browser = webdriver.Chrome()
    browser.get('https://ya.ru')
    browser.find_element(By.XPATH, '//*[@id="text"]').send_keys('рбаота в яндексе')
    assert browser.find_element("css selector", "button[tabindex='-1']")

def test_second():
    options = webdriver.ChromeOptions()
    binary_yandex_driver_file = 'yandexdriver.exe'
    browser = webdriver.Chrome()
    browser.get('https://ya.ru')
    time.sleep(15)
    browser.find_element(By.XPATH, '//*[@id="text"]').send_keys('рбаота в яндексе')
    browser.find_element("css selector", "button[tabindex='-1']").click()
    assert browser.find_element(By.XPATH, "/html/body/main/div[2]/div[2]/div/div/div[1]/div[1]/div/div")



