import pytest
from selenium import webdriver


def pytest_addoption(parser):
    parser.addoption(
        "--browsername", action="store", default="chrome", help="my option: type1 or type2"
    )


@pytest.fixture(scope='class')  # for prereq of any test like opening a browser,db connection, selenium webdriver
def driver_fix(request):
    browser_value = request.config.getoption("browsername")
    # driver = webdriver.Chrome()
    if browser_value == 'chrome':
        driver = webdriver.Chrome()
    elif browser_value == 'firefox':
        driver = webdriver.Firefox()
    elif browser_value == 'edge':
        driver = webdriver.Edge()

    driver.get("https://rahulshettyacademy.com/angularpractice/")
    driver.maximize_window()
    request.cls.driver = driver
    yield
    driver.close()
