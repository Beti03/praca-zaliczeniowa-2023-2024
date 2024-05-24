import pytest
import allure
from allure_commons.types import AttachmentType
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from beti03_source.pages.locators import Page_Locators, Message_Page_Locators


@allure.epic("Search Product")
@allure.suite("Product search by global search")
class Test_SC_02_PS_Product_Search_By_Global_Search:
    PAGE_TITLE = (By.XPATH, Page_Locators.PAGE_TITLE)
    NOTE_MSG = (By.XPATH, Message_Page_Locators.NOTE_MSG)
    CATEGORY_PRODUCTS_LIST = (By.XPATH, Page_Locators.CATEGORY_PRODUCTS_LIST)
    GLOBAL_SEARCH = (By.XPATH, Page_Locators.GLOBAL_SEARCH)
    PRODUCT_NAME_H2 = (By.XPATH, Page_Locators.PRODUCT_NAME_H2)
    FIND_WORD = 'kufel'
    FIND_FAKE_WORD = 'kafel'
    EXPECTED_RESULT_PRODUCT_COUNT = 9
    EXPECTED_SEARCH_MSG = 'Brak wyników wyszukiwania.'
    EXPECTED_SEARCH_RESULT = "Wyniki wyszukiwania dla 'kafel'"
    @allure.testcase('',"SC_02_PS_TC_01 Product search by word")
    @allure.severity(allure.severity_level.NORMAL)
    @allure.label("owner", "Beti03")
    @pytest.mark.usefixtures("set_side_on_home_page")
    def test_SC_02_PS_TC_01_Product_Search_By_Word(self):
        """
        CEL: Sprawdzenie czy po wpisaniu frazy "kufel" zostaną wyświetlone produkty, które mają w tytule "Kufel"
            WARUNKI WSTĘPNE:
            1. Strona ustawiona na http://www.kubki-reklamowe.eu
            KROKI:
            1. W pasku wyszukiwania wpisza frazę "kufel" i kliknij enter
            2. Sprawdź czy w zwróconych towarach jest szykane słowo
            3. Zlicz ilość wyświetlonych produktów
            REZULTAT:
            1. Każdy wyświetlony produkt posiada w nazwie słowo "kufel"
            2. Zostanie zwrócone 9 pozycji
        """
        global_search = self.driver.find_element(*self.GLOBAL_SEARCH)
        global_search.send_keys(*self.FIND_WORD)
        search_button = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//div[@class='form-search']/button[@class='button']"))
        )
        search_button.click()
        WebDriverWait(self.driver, 25).until(
            EC.presence_of_element_located((By.XPATH, "//div[@class='category-products']"))
        )
        tmp_product_names_list = []
        product_find = self.driver.find_elements(*self.PRODUCT_NAME_H2)
        for i in range(len(product_find)):
            tmp_product_names_list.append(str(product_find[i].text))
        convert_to_sting = ' '.join(tmp_product_names_list).lower()
        create_to_tmp_list = convert_to_sting.split(' ')
        create_new_product_names_list = [element for element in create_to_tmp_list if element == self.__class__.FIND_WORD]
        assert len(create_new_product_names_list) == self.EXPECTED_RESULT_PRODUCT_COUNT
        allure.attach(self.driver.get_screenshot_as_png(), name='Product Search By Word',
                      attachment_type=AttachmentType.PNG)

    @allure.testcase("","SC_02_PS_TC_02 Product search by wrong product name")
    @allure.severity(allure.severity_level.NORMAL)
    @allure.label("owner", "Beti03")
    @pytest.mark.usefixtures("set_side_on_home_page")
    def test_SC_02_PS_TC_02_Product_Search_By_Wrong_Product_Name(self):
        """
        CEL: Sprawdzenie czy po wpisaniu błędnej frazy "kafel" zostaną wyświetlone komunikat o treści "Brak wyników wyszukiwania. "
            WARUNKI WSTĘPNE:
            1. Strona ustawiona na http://www.kubki-reklamowe.eu
            KROKI:
            1. W pasku wyszukiwania wpisza frazę "kafel" i kliknij enter
            2. Sprawdź czy na wyświetlonej stronie wyświetlił się tytuł "Wyniki wyszukiwania dla 'kafel'"
            3. Sprawdź czy na stronie wyświetlił się komunikat o treści "Brak wyszukiwania. "
            REZULTAT:
            1. Po wpisaniu frazu, której nie ma w bazie zostanie wyświetlony tytuł "Wyniki wyszukiwania dla 'kafel'"
            2. Po wpisaniu frazu, której nie ma w bazie zostanie wyświetlony komunikat o treści "Brak wyszukiwania. "
        """
        global_search = self.driver.find_element(*self.GLOBAL_SEARCH)
        global_search.send_keys(*self.FIND_FAKE_WORD)
        search_button = WebDriverWait(self.driver, 25).until(
            EC.visibility_of_element_located((By.XPATH, "//div[@class='form-search']/button[@class='button']"))
        )
        search_button.click()
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, "//div[@class='page-title']"))
        )
        search_results = self.driver.find_element(*self.PAGE_TITLE)
        search_msg = self.driver.find_element(*self.NOTE_MSG)
        assert search_msg.text == self.EXPECTED_SEARCH_MSG
        assert search_results.text == self.EXPECTED_SEARCH_RESULT
        allure.attach(self.driver.get_screenshot_as_png(), name='Product Search By Wrong Product Name',
                      attachment_type=AttachmentType.PNG)
