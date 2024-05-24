import pytest
import allure
from allure_commons.types import AttachmentType
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from beti03_source.pages.locators import Product_Page_Locators

@allure.epic('Product card')
@allure.suite("Display product information")
@pytest.mark.usefixtures("set_side_on_product_page")
class Test_SC_01_PC_Display_Product_Information:
    PRODUCT_TITLE = (By.XPATH, Product_Page_Locators.PRODUCT_TITLE)
    PRICE_BOX_PRICE = (By.XPATH, Product_Page_Locators.PRICE_BOX_PRICE)
    PRODUCT_STATUS = (By.XPATH, Product_Page_Locators.PRODUCT_STATUS)
    EXPECTED_PRODUCT_TITLE = "Kubek ceramiczny HANDY SUPREME ® 300ml"
    EXPECTED_PRODUCT_PRICE = "15,08 zł"
    EXPECTED_STATUS = "W magazynie"
    @allure.testcase('', 'SC_01_PC_TC_01 Product name')
    @allure.severity(allure.severity_level.NORMAL)
    @allure.label("owner", "Beti03")
    @allure.severity(allure.severity_level.NORMAL)
    def test_SC_01_PC_TC_01_Product_Name(self):
        """
        CEL: Sprawdzenie czy na stronie produktu wyświetla się nazwa produktu
            WARUNKI WSTĘPNE:
            1. Strona ustawiona na http://www.kubki-reklamowe.eu/polska-ceramika-reklamowa/kubek-ceramiczny-handy-supreme-r-300ml.html
            KROKI:
            1. Znajdź nazwę produktu "Kubek ceramiczny HANDY SUPREME ® 300ml"
            REZULTAT:
            1. Na stronie z wyświetlony produkt będize posiadał nazwę "Kubek ceramiczny HANDY SUPREME ® 300ml"
        """
        product_name_on_page = self.driver.find_element(*self.PRODUCT_TITLE)
        assert product_name_on_page.text == self.EXPECTED_PRODUCT_TITLE
        allure.attach(self.driver.get_screenshot_as_png(), name='Product Name',
                      attachment_type=AttachmentType.PNG)
    @allure.testcase('', 'SC_01_PC_TC_02 Product Price')
    @allure.severity(allure.severity_level.NORMAL)
    @allure.label("owner", "Beti03")
    @allure.severity(allure.severity_level.NORMAL)
    def test_SC_01_PC_TC_02_Product_Price(self):
        """
        CEL: Sprawdzenie czy na stronie produktu wyświetla się cena produktu
            WARUNKI WSTĘPNE:
            1. Strona ustawiona na http://www.kubki-reklamowe.eu/polska-ceramika-reklamowa/kubek-ceramiczny-handy-supreme-r-300ml.html
            KROKI:
            1. Znajdź cenę produktu "15,08 zł"
            REZULTAT:
            1. Na stronie z wyświetlony produkt będzie posiadał cenę "15,08 zł"
        """
        product_price = self.driver.find_element(*self.PRICE_BOX_PRICE)
        assert product_price.text == self.EXPECTED_PRODUCT_PRICE
        allure.attach(self.driver.get_screenshot_as_png(), name='Product Price',
                      attachment_type=AttachmentType.PNG)
    @allure.testcase('', 'SC_01_PC_TC_03 Product Availability')
    @allure.severity(allure.severity_level.NORMAL)
    @allure.label("owner", "Beti03")
    @allure.severity(allure.severity_level.NORMAL)
    def test_SC_01_PC_TC_03_Product_Availability(self):
        """
        CEL: Sprawdzenie czy na stronie produktu wyświetla stan magazynowy
            WARUNKI WSTĘPNE:
            1. Strona ustawiona na http://www.kubki-reklamowe.eu/polska-ceramika-reklamowa/kubek-ceramiczny-handy-supreme-r-300ml.html
            KROKI:
            1. Znajdź dostępność produktu
            REZULTAT:
            1. Na stronie produkt widnieć będzie informacja o dostępności towaru "W magazynie"
        """
        product_status = self.driver.find_element(*self.PRODUCT_STATUS)
        assert product_status.text == self.EXPECTED_STATUS
        allure.attach(self.driver.get_screenshot_as_png(), name='Product Availability',
                      attachment_type=AttachmentType.PNG)
    @allure.testcase('', 'SC_01_PC_TC_04 Product Image Displayed')
    @allure.severity(allure.severity_level.NORMAL)
    @allure.label("owner", "Beti03")
    @allure.severity(allure.severity_level.NORMAL)
    def test_SC_01_PC_TC_04_Product_Image_Displayed(self):
        """
        CEL: Sprawdzenie czy na stronie produktu wyświetla się zdjęcia produktu
            WARUNKI WSTĘPNE:
            1. Strona ustawiona na http://www.kubki-reklamowe.eu/polska-ceramika-reklamowa/kubek-ceramiczny-handy-supreme-r-300ml.html
            KROKI:
            1. Znajdź zdjęcie produktu
            REZULTAT:
            1. Na stronie produkt bedzie widoczne zdjęcie produkty
        """
        image = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.ID, "image-main")))
        image_src = image.get_attribute("src")
        assert image_src and image_src != ""
        allure.attach(self.driver.get_screenshot_as_png(), name='Product Image Displayed',
                      attachment_type=AttachmentType.PNG)