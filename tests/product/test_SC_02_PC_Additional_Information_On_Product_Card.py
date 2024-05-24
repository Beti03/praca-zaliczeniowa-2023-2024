import pytest
import allure
from allure_commons.types import AttachmentType
from selenium.webdriver.common.by import By
from beti03_source.pages.locators import Product_Page_Locators

@allure.epic('Product card')
@allure.suite("Additional information on product card")
@pytest.mark.usefixtures("set_side_on_product_page")
class Test_SC_02_PC_Additional_Information_On_Product_Card:
    TAB_DESCRIPTION = (By.XPATH, Product_Page_Locators.TAB_DESCRIPTION)
    TAB_ADDITIONAL = (By.XPATH, Product_Page_Locators.TAB_ADDITIONAL)
    TAB_TABREVIEWS = (By.XPATH, Product_Page_Locators.TAB_TABREVIEWS)
    TAB_TAGS = (By.XPATH, Product_Page_Locators.TAB_TAGS)
    TAB_PRODUCT_CMS_BLOCK1 = (By.XPATH, Product_Page_Locators.TAB_PRODUCT_CMS_BLOCK1)
    EXPECTED_RESULT_TAB_DESCRIPTION = "Opis produktu"
    EXPECTED_RESULT_TAB_ADDITIONAL = "Informacje dodatkowe"
    EXPECTED_RESULT_TAB_TABREVIEWS = "Recenzje"
    EXPECTED_RESULT_TAB_TAGS = "Tagi produktu"
    EXPECTED_RESULT_TAB_PRODUCT_CMS_BLOCK1 = "Dodatkowe opcje znakowania"

    @allure.testcase('', 'SC_03_PC_TC_01 Visible product description tab')
    @allure.severity(allure.severity_level.NORMAL)
    @allure.label("owner", "Beti03")
    @allure.severity(allure.severity_level.NORMAL)
    def test_SC_02_PC_TC_01_Visible_Product_Description_Tab(self):
        """
        CEL: Sprawdzenie czy wyświetla się na zakładce napis "Opis produktu"
            WARUNKI WSTĘPNE:
            1. Strona ustawiona na http://www.kubki-reklamowe.eu/polska-ceramika-reklamowa/kubek-ceramiczny-handy-supreme-r-300ml.html
            KROKI:
            1. Znajdź zakłądkę na dole strony o tytule "Opis produktu"
            REZULTAT:
            1. Na stronie jest widoczna zakładka o tytule "Opis produktu"
        """
        description_tab = self.driver.find_element(*self.TAB_DESCRIPTION)
        assert description_tab.text == self.EXPECTED_RESULT_TAB_DESCRIPTION
        allure.attach(self.driver.get_screenshot_as_png(), name='Visible Product Description Tab',
                      attachment_type=AttachmentType.PNG)
    @allure.testcase('', 'SC_03_PC_TC_02 Visible additional information tab')
    @allure.severity(allure.severity_level.NORMAL)
    @allure.label("owner", "Beti03")
    @allure.severity(allure.severity_level.NORMAL)
    def test_SC_02_PC_TC_02_Visible_Additional_Information_Tab(self):
        """
        CEL: Sprawdzenie czy wyświetla się na zakładce napis "Informacje dodatkowe"
            WARUNKI WSTĘPNE:
            1. Strona ustawiona na http://www.kubki-reklamowe.eu/polska-ceramika-reklamowa/kubek-ceramiczny-handy-supreme-r-300ml.html
            KROKI:
            1. Znajdź zakłądkę na dole strony o tytule "Informacje dodatkowe"
            REZULTAT:
            1. Na stronie jest widoczna zakładka o tytule "Informacje dodatkowe"
        """
        additional_information_tab = self.driver.find_element(*self.TAB_ADDITIONAL)
        assert additional_information_tab.text == self.EXPECTED_RESULT_TAB_ADDITIONAL
        allure.attach(self.driver.get_screenshot_as_png(), name='Visible Additional Information Tab',
                      attachment_type=AttachmentType.PNG)
    @allure.testcase('', 'SC_03_PC_TC_03 Visible reviews tab')
    @allure.severity(allure.severity_level.NORMAL)
    @allure.label("owner", "Beti03")
    @allure.severity(allure.severity_level.NORMAL)
    def test_SC_02_PC_TC_03_Visible_Reviews_Tab(self):
        """
        CEL: Sprawdzenie czy wyświetla się na zakładce napis "Recenzje"
            WARUNKI WSTĘPNE:
            1. Strona ustawiona na http://www.kubki-reklamowe.eu/polska-ceramika-reklamowa/kubek-ceramiczny-handy-supreme-r-300ml.html
            KROKI:
            1. Znajdź zakłądkę na dole strony o tytule "Recenzje"
            REZULTAT:
            1. Na stronie jest widoczna zakładka o tytule "Recenzje"
        """
        reviews_tab = self.driver.find_element(*self.TAB_TABREVIEWS)
        assert reviews_tab.text == self.EXPECTED_RESULT_TAB_TABREVIEWS
        allure.attach(self.driver.get_screenshot_as_png(), name='Visible Reviews Tab',
                      attachment_type=AttachmentType.PNG)

    @allure.testcase('', 'SC_03_PC_TC_05 Visible product description sheet product tags')
    @allure.severity(allure.severity_level.NORMAL)
    @allure.label("owner", "Beti03")
    @allure.severity(allure.severity_level.NORMAL)
    def test_SC_02_PC_TC_04_Visible_Product_Description_Sheet_Product_Tags(self):
        """
        CEL: Sprawdzenie czy wyświetla się na zakładce napis "Tagi produktu"
            WARUNKI WSTĘPNE:
            1. Strona ustawiona na http://www.kubki-reklamowe.eu/polska-ceramika-reklamowa/kubek-ceramiczny-handy-supreme-r-300ml.html
            KROKI:
            1. Znajdź zakłądkę na dole strony o tytule "Tagi produktu"
            REZULTAT:
            1. Na stronie jest widoczna zakładka o tytule "Tagi produktu"
        """
        product_tags_tab = self.driver.find_element(*self.TAB_TAGS)
        assert product_tags_tab.text == self.EXPECTED_RESULT_TAB_TAGS
        allure.attach(self.driver.get_screenshot_as_png(), name='Visible Product Description Sheet Product Tags',
                      attachment_type=AttachmentType.PNG)
    @allure.testcase('', 'SC_03_PC_TC_05 Visible description card add mark options')
    @allure.severity(allure.severity_level.NORMAL)
    @allure.label("owner", "Beti03")
    @allure.severity(allure.severity_level.NORMAL)
    def test_SC_02_PC_TC_05_Visible_Description_Card_Add_Mark_Options(self):
        """
        CEL: Sprawdzenie czy wyświetla się na zakładce napis "Dodatkow opcje znakowania"
            WARUNKI WSTĘPNE:
            1. Strona ustawiona na http://www.kubki-reklamowe.eu/polska-ceramika-reklamowa/kubek-ceramiczny-handy-supreme-r-300ml.html
            KROKI:
            1. Znajdź zakłądkę na dole strony o tytule "Dodatkow opcje znakowania"
            REZULTAT:
            1. Na stronie jest widoczna zakładka o tytule "Dodatkow opcje znakowania"
        """
        add_mark_options_tab = self.driver.find_element(*self.TAB_PRODUCT_CMS_BLOCK1)
        assert add_mark_options_tab.text == self.EXPECTED_RESULT_TAB_PRODUCT_CMS_BLOCK1
        allure.attach(self.driver.get_screenshot_as_png(), name='Visible Description Card Add Mark Options',
                      attachment_type=AttachmentType.PNG)
