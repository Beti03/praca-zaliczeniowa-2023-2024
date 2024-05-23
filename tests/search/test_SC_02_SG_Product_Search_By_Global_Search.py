import pytest
import allure
from allure_commons.types import AttachmentType
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from beti03_source.pages.locators import MainPageLocators, MessagePageLocators
@allure.epic('Search Product')
@allure.suite("Dodatkowe zakładki na karcie produktu")
class Test_SC_02_S_Product_Search_By_Global_Search:
    PAGE_TITLE = (By.XPATH, MainPageLocators.PAGE_TITLE)
    NOTE_MSG = (By.XPATH, MessagePageLocators.NOTE_MSG)
    CATEGORY_PRODUCTS_LIST = (By.XPATH, MainPageLocators.CATEGORY_PRODUCTS_LIST)
    GLOBAL_SEARCH = (By.XPATH, MainPageLocators.GLOBAL_SEARCH)
    FIND_WORD = 'kufel'
    FIND_FAKE_WORD = 'kufel'
    EXPECTED_RESULT_PRODUCT_COUNT = 9
    @allure.description("TC-01")
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.usefixtures("set_side_on_home_page")
    def test_SC_01_2_TC_01_Product_Search_By_Search(self):
        """
        W pasku wyszukiwania wpisza frazę "kufel" i kliknij enter
        Sprawdź wynik wyszukiwania, powinien wyświetlić się napis "Wyniki wyszukiwania dla 'kufel'"
        Sprawdz wynik zwróconych pozycji = 9
        :return:
        """
        global_search = self.driver.find_element(By.XPATH, "//input[@id='search']")
        global_search.send_keys(self.FIND_WORD)
        search_button = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//div[@class='form-search']/button[@class='button']"))
        )
        search_button.click()
        WebDriverWait(self.driver, 25).until(
            EC.presence_of_element_located((By.XPATH, "//div[@class='category-products']"))
        )
        products_find = self.driver.find_elements(*self.CATEGORY_PRODUCTS_LIST)
        vissible_products = [item for item in products_find if item.is_displayed()]
        product_item_count = len(vissible_products)
        assert product_item_count == self.EXPECTED_RESULT_PRODUCT_COUNT
        allure.attach(self.driver.get_screenshot_as_png(), name='Product Search By Search',
                      attachment_type=AttachmentType.PNG)

    @allure.description("TC-02")
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.usefixtures("set_side_on_home_page")
    def test_SC_01_2_TC_01_Product_Search_By_Wrong_Product_Name(self):
        """
            W pasku wyszukiwania wpisza frazę "kufel" i kliknij enter
            Sprawdź wynik wyszukiwania, powinien wyświetlić się napis "Wyniki wyszukiwania dla 'kufel'"
            Sprawdz wynik zwróconych pozycji = 9
            :return:
            """
        global_search = self.driver.find_element(*self.GLOBAL_SEARCH)
        global_search.send_keys(self.FIND_FAKE_WORD)
        search_button = WebDriverWait(self.driver, 25).until(
            EC.visibility_of_element_located((By.XPATH, "//div[@class='form-search']/button[@class='button']"))
        )
        search_button.click()
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, "//div[@class='page-title']"))
        )
        search_results = self.driver.find_element(*self.PAGE_TITLE)
        search_msg = self.driver.find_element(*self.NOTE_MSG)
        # # TODO: dodać zmienną expeted search restults

        # print("Treść akapitu:", search_msg.text)
        assert search_msg.text == 'Brak wyników wyszukiwania.'
        assert search_results.text == "Wyniki wyszukiwania dla 'kufele'"
        allure.attach(self.driver.get_screenshot_as_png(), name='Product Search By Wrong Product Name',
                      attachment_type=AttachmentType.PNG)