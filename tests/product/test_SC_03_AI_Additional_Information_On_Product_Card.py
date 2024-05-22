import pytest
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.locators import Search_Locators, Products_Locators, MainPageLocators, MessagePageLocators

@pytest.mark.usefixtures("set_side_on_product_page")
class Test_SC_03_AI_Additional_Information_On_Product_Card:
    """
    :TODO uzupełnie przypadki testowe o opis
        dodać  do lokatorów
    informacje dodatkowe na karcie produktu
    Czy widoczna jest zakładka "Opis produktu" a w niej opis
    Czy widoczna jest zakładka "Informacje dodatkow" a w niej opis
    Czy widoczna jest zakładka "Recenzja":
        - walidacja formularza wszystkie pola nie uzupełnione, powinien wyświetlić się komunikacj to błędach
    Czy widoczna jest zakładka "Tagi produktu":
        - dodanie taga i kliknięcie Dodaj tagi, po kliknięciu zostanie użytkownik przeniesionyc na stronę logowanie
        Założenie: Nie zalogowany użytkownik nie może dodać taga
    Czy widoczna jest zakładka "Dodatkow opcje znakowe": a nie opis - nagłówek
    Visible product description sheet product tags
    """

    def test_SC_03_AI_TC_01_Visible_Product_Description_Tab(self):
        description_tab = self.driver.find_element(By.XPATH, "//div[@id='product-tabs']/ul/li[@id='tab-description']")
        assert description_tab.text == "Opis produktu"
    def test_SC_03_AI_TC_02_Visible_Additional_Information_Tab(self):
        additional_information_tab = self.driver.find_element(By.XPATH, "//div[@id='product-tabs']/ul/li[@id='tab-additional']")
        assert additional_information_tab.text == "Informacje dodatkowe"

    def test_SC_03_AI_TC_03_Visible_Reviews_Tab(self):
        reviews_tab = self.driver.find_element(By.XPATH, "//div[@id='product-tabs']/ul/li[@id='tab-tabreviews']")
        assert reviews_tab.text == "Recenzje"


    def test_SC_03_AI_TC_05_Visible_Product_Description_Sheet_Product_Tags(self):
        product_tags_tab = self.driver.find_element(By.XPATH, "//div[@id='product-tabs']/ul/li[@id='tab-tags']")
        assert product_tags_tab.text == "Tagi produktu"
    def test_SC_03_AI_TC_06_Visible_Description_Card_Add_Mark_Options(self):
        add_mark_options_tab = self.driver.find_element(By.XPATH, "//div[@id='product-tabs']/ul/li[@id='tab-product_cms_block1']")
        assert add_mark_options_tab.text == "Dodatkowe opcje znakowania"
