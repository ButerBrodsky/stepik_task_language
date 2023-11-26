import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import pytest

def test_exercise(browser):
    link = 'https://selenium1py.pythonanywhere.com/ru/catalogue/coders-at-work_207/'
    browser.get(link)
    button_submit = browser.find_element(By.CSS_SELECTOR, 'button.btn.btn-lg.btn-primary.btn-add-to-basket').text
    assert "Добавить в корзину" == button_submit, ("Кнопки добавления в корзину нет!")
    time.sleep(3)
