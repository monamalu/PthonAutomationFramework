import pytest
from selenium import webdriver


@pytest.fixture(scope="class")
def setup(request):
    driver = webdriver.Chrome(executable_path="/Users/macbook/Downloads/chromedriver.exe")
    driver.get("https://practice.automationtesting.in/")
#    driver.get("https://www.tripadvisor.in/")
    driver.maximize_window()
    request.cls.driver = driver
    yield driver
    driver.close()


@pytest.fixture(params=["chrome", "Firefox", "IE"])
def cross_browser(request):
    return request.param


