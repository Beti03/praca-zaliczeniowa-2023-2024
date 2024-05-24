import pytest
from selenium import webdriver

geckodriver_path = "/snap/bin/geckodriver"
driver_service = webdriver.FirefoxService(executable_path=geckodriver_path)


@pytest.fixture(scope="function", autouse=True)
def setup_driver(request):
    options = webdriver.FirefoxOptions()
    options.add_argument("--headless")
    options.headless = True
    driver = webdriver.Firefox(service=driver_service, options=options)
    driver.maximize_window()
    driver.implicitly_wait(25)
    request.cls.driver = driver
    yield
    driver.quit()

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


