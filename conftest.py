import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import pytest


def pytest_addoption(parser):
    parser.addoption('--language', action='store', default="ru", help="Choose language: ru or es")


@pytest.fixture(scope="function")
def browser(request):
    language = request.config.getoption("language")
    options = Options()
    if language == "es":
        print("\nstarting browser on ES language")
        options.add_experimental_option('prefs', {'intl.accept_languages': 'es'})
    elif language == "RU":
        print("\nstarting browser on RU language")
        options.add_experimental_option('prefs', {'intl.accept_languages': 'ru'})
    else:
        raise pytest.UsageError("--browser_language should be RU or ES")
    browser = webdriver.Chrome(options=options)
    yield browser
    print("\nquit browser..")
    browser.quit()
