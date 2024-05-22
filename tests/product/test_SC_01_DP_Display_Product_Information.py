import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.locators import Search_Locators, Products_Locators, MainPageLocators, MessagePageLocators

@pytest.mark.usefixtures("set_side_on_product_page")
class TestProductInformation:
    """ TODO: Dokończyc opisy przypakdów testowych
        Sprawdzenie, czy nazwa produktu, opis, cena i dostępność są wyświetlane poprawnie.
        Weryfikacja, czy zdjęcia produktu są wyświetlane.
    """
    def test_nazwa_produktu(self):
        product_name_on_page = self.driver.find_element(By.XPATH, "//div[@class='product-name']")
        assert product_name_on_page.text == "Kubek ceramiczny HANDY SUPREME ® 300ml"

    def test_cena_produktu(self):
        product_price = self.driver.find_element(By.XPATH, "//div[@class='price-box']/span/span[@class='price']")
        new_product_price = product_price.text
        replace_string_on_new_product_price = new_product_price.replace(' zł','')
        assert replace_string_on_new_product_price == "15,08"

    def test_dostępności_produktu(self):
        # Pobierze opis o statusie
        product_status = self.driver.find_element(By.XPATH, "//div[@itemprop='offers']/div[@class='product-type-data']/p/span")
        # Sprawdź,czy resulta jest zgodny z oczekiwanym
        assert product_status.text == "W magazynie"

    def test_product_image_displayed(self):
        # Czekaj, aż element img z id "image-main" będzie obecny w DOM i widoczny
        image = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.ID, "image-main")))
        # Sprawdź, czy element img ma atrybut src z poprawną wartością
        image_src = image.get_attribute("src")
        assert image_src and image_src != "", "Zdjęcie nie ma atrybutu src lub jest puste."