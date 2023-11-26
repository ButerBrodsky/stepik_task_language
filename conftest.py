from selenium import webdriver
from selenium.webdriver.chrome.options import Options

options = Options()
options.add_experimental_option("--language=ru")
browser = webdriver.Chrome(options=options)

def pytest_addoption(parser):
    parser.addoption('--language', action='store', default="ES",
                     help="Choose language: RU or ES")

@pytest.fixture(scope="function")
def browser(request):
    language_name = request.config.getoption("language_name")
    browser = None
    if language_name == "ES":
        print("\nstarting browser on ES language")
        browser = webdriver.Chrome()
    elif language_name == "RU":
        print("\nstarting browser on RU language")
        browser = webdriver.Chrome()
    else:
        raise pytest.UsageError("--browser_language should be RU or ES")
    yield browser
    print("\nquit browser..")
    browser.quit()
