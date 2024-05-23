import pytest
import re
from selenium import webdriver
from selenium.common import NoSuchElementException, ElementNotInteractableException
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

geckodriver_path = "/snap/bin/geckodriver"
driver_service = webdriver.FirefoxService(executable_path=geckodriver_path)


@pytest.fixture(scope="function", autouse=True)
def setup_driver(request):
    options = webdriver.FirefoxOptions()
    options.add_argument("--headless")
    # options.add_argument("--no-sandbox")
    # options.add_argument("--disable-gpu")
    options.headless = True
    driver = webdriver.Firefox(service=driver_service, options=options)
    driver.maximize_window()
    driver.implicitly_wait(10)
    request.cls.driver = driver
    yield
    driver.quit()


@pytest.fixture(scope="function")
def setup_shop_page(request):
    driver = request.cls.driver
    show_dropdown = driver.find_element(By.NAME, 'per_page')
    show_dropdown.click()
    option = driver.find_element(By.XPATH, "//option[@value='24']")
    option.click()
    driver.refresh()


@pytest.fixture(scope="function")
def set_side_on_cups(request):
    driver = request.cls.driver
    driver.get("http://www.kubki-reklamowe.eu/filizanki-reklamowe-z-logo.html")
    driver.implicitly_wait(20)
@pytest.fixture(scope="function")
def set_side_on_mugs(request):
    driver = request.cls.driver
    driver.get("http://www.kubki-reklamowe.eu/polska-ceramika-reklamowa.html")
    driver.implicitly_wait(20)
@pytest.fixture(scope="function")
def set_side_on_home_page(request):
    driver = request.cls.driver
    driver.get("http://www.kubki-reklamowe.eu/")
    driver.implicitly_wait(20)

@pytest.fixture(scope="function")
def set_side_on_product_page(request):
    driver = request.cls.driver
    driver.get("http://www.kubki-reklamowe.eu/polska-ceramika-reklamowa/kubek-ceramiczny-handy-supreme-r-300ml.html")
    driver.implicitly_wait(20)


