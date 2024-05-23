import pytest
import allure
from selenium.webdriver.common.by import By
from beti03_source.pages.locators import Products_Locators


@allure.suite("Dodatkowe zakładki na karcie produktu")
@pytest.mark.usefixtures("set_side_on_product_page")
class Test_SC_03_AI_Additional_Information_On_Product_Card:
    TAB_DESCRIPTION = (By.XPATH, Products_Locators.TAB_DESCRIPTION)
    TAB_ADDITIONAL = (By.XPATH, Products_Locators.TAB_ADDITIONAL)
    TAB_TABREVIEWS = (By.XPATH, Products_Locators.TAB_TABREVIEWS)
    TAB_TAGS = (By.XPATH, Products_Locators.TAB_TAGS)
    TAB_PRODUCT_CMS_BLOCK1 = (By.XPATH, Products_Locators.TAB_PRODUCT_CMS_BLOCK1)
    EXPECTED_RESULT_TAB_DESCRIPTION = "Opis produktu"
    EXPECTED_RESULT_TAB_ADDITIONAL = "Informacje dodatkowe"
    EXPECTED_RESULT_TAB_TABREVIEWS = "Recenzje"
    EXPECTED_RESULT_TAB_TAGS = "Tagi produktu"
    EXPECTED_RESULT_TAB_PRODUCT_CMS_BLOCK1 = "Dodatkowe opcje znakowania"
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
    @allure.description("TC-01")
    @allure.severity(allure.severity_level.NORMAL)
    def test_SC_03_AI_TC_01_Visible_Product_Description_Tab(self):
        description_tab = self.driver.find_element(*self.TAB_DESCRIPTION)
        assert description_tab.text == self.EXPECTED_RESULT_TAB_DESCRIPTION
    @allure.description("TC-02")
    @allure.severity(allure.severity_level.NORMAL)
    def test_SC_03_AI_TC_02_Visible_Additional_Information_Tab(self):
        additional_information_tab = self.driver.find_element(*self.TAB_ADDITIONAL)
        assert additional_information_tab.text == self.EXPECTED_RESULT_TAB_ADDITIONAL
    @allure.description("TC-03")
    @allure.severity(allure.severity_level.NORMAL)
    def test_SC_03_AI_TC_03_Visible_Reviews_Tab(self):
        reviews_tab = self.driver.find_element(*self.TAB_TABREVIEWS)
        assert reviews_tab.text == self.EXPECTED_RESULT_TAB_TABREVIEWS
    @allure.description("TC-04")
    @allure.severity(allure.severity_level.NORMAL)
    def test_SC_03_AI_TC_05_Visible_Product_Description_Sheet_Product_Tags(self):
        product_tags_tab = self.driver.find_element(*self.TAB_TAGS)
        assert product_tags_tab.text == self.EXPECTED_RESULT_TAB_TAGS
    @allure.description("TC-05")
    @allure.severity(allure.severity_level.NORMAL)
    def test_SC_03_AI_TC_06_Visible_Description_Card_Add_Mark_Options(self):
        add_mark_options_tab = self.driver.find_element(*self.TAB_PRODUCT_CMS_BLOCK1)
        assert add_mark_options_tab.text == self.EXPECTED_RESULT_TAB_PRODUCT_CMS_BLOCK1
