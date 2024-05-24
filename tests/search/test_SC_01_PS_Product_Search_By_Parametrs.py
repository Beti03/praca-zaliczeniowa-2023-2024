import pytest
import allure
from allure_commons.types import AttachmentType
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from beti03_source.pages.locators import Search_Locators, Page_Locators
from beti03_source.scripts.function import convert_data_to_a_new_temporary_list


@allure.epic('Search Product')
@allure.suite("Search for a product by parameter")
class Test_SC_01_PS_Product_Search_By_Parametrs:
    CAPACITY_LIST = (By.XPATH, Search_Locators.CAPACITY_LIST)
    CATEGORY_PRODUCTS_LIST = (By.XPATH, Page_Locators.CATEGORY_PRODUCTS_LIST)
    SWATCH_LINK_COLOR = (By.XPATH, Search_Locators.SWATCH_LINK_COLOR)
    SEARCH_CAPACITY = '130 ml'
    SAERCH_COLOR = 'czarny'
    EXPECTED_RESULT_OF_SEARCH_BY_CAPACITY_ARGUMENT = 1
    EXPECTED_RESULT_OF_SEARCH_BY_COLOR_ARGUMENT = 9

    @allure.testcase('', 'SC_01_PS_TC_01 Product search by capacity')
    @allure.severity(allure.severity_level.NORMAL)
    @allure.label("owner", "Beti03")
    @pytest.mark.usefixtures("set_side_on_cups")
    def test_SC_01_PS_TC_01_Product_Search_By_Capacity(self):
        """
        CEL: Sprawdzenie czy po wybraniu pojemności "130 ml" w menu "Szukaj po parametrze" zostanie zwrócona odpowienia liczba produktów na stronie
            WARUNKI WSTĘPNE:
            1. Strona ustawiona na http://www.kubki-reklamowe.eu/filizanki-reklamowe-z-logo.html
            KROKI:
            1. Znajdź nagłówek o nazwie "Szukaj po parametrze"
            2. Znajdź tytył "Pojemność w ml" i zaznacz parametr o wartości "130 ml" i kliknij enter
            3. Sprawdź czy na stronie zostały wyświetlone produkty
            4. Zlicz ilość wyświetlonych produktów
            REZULTAT:
            1. Na stronie zostanie wyświetlony 1 produkt
        """
        list_of_available_capacities = self.driver.find_elements(*self.CAPACITY_LIST)
        tmp_elements_list = convert_data_to_a_new_temporary_list(list_of_available_capacities)
        counter_counting_the_position_of_the_search_query = 0
        for i in range(len(tmp_elements_list)):
            if tmp_elements_list[i] != self.__class__.SEARCH_CAPACITY:
                counter_counting_the_position_of_the_search_query += 1
            else:
                capacity_item_xpath = f"//dl[@id='narrow-by-list']/dd[@class='last even']/ol/li[{counter_counting_the_position_of_the_search_query}]"
                capacity_item_id_in_the_list = self.driver.find_element(By.XPATH, capacity_item_xpath)
                self.driver.implicitly_wait(10)
                capacity_item_id_in_the_list.click()
                WebDriverWait(self.driver, 150).until(
                    EC.visibility_of_element_located((By.XPATH, "//div[@class='category-products']/ul/li"))
                )
                self.driver.implicitly_wait(50)
                products_find = self.driver.find_elements(self.__class__.CATEGORY_PRODUCTS_LIST)
                vissible_products = [item for item in products_find if item.is_displayed()]
                product_item_count = len(vissible_products)
                assert product_item_count == self.__class__.EXPECTED_RESULT_OF_SEARCH_BY_CAPACITY_ARGUMENT
                allure.attach(self.driver.get_screenshot_as_png(), name='Product Search By Capacity',
                              attachment_type=AttachmentType.PNG)

    @allure.testcase('', 'SC_01_PS_TC_02 Product search by black color')
    @allure.severity(allure.severity_level.NORMAL)
    @allure.label("owner", "Beti03")
    @pytest.mark.usefixtures("set_side_on_mugs")
    def test_SC_01_PS_TC_02_Product_Search_By_Black_Color(self):
        """
        CEL: Sprwadzenie czy zostanie zwrócony produkt/y do którego przypisany jest atrybut koloru czarnego
            WARUNKI WSTĘPNE:
            1. Strona ustawiona na http://www.kubki-reklamowe.eu/polska-ceramika-reklamowa.html
            KROKI:
            1. Znajdź nagłówek o nazwie "Szukaj po parametrze"
            2. Znajdź nagłówek o nazwie "Kolor" i kliknij w wadrat w kolorze "czarnym"
            3. Sprawdź czy na stronie zostały wyświetlone produkty
            4. Zlicz ilość wyświetlonych produktów
            REZULTAT:
            1. Na stronie zostanie wyświetlonych 9 produktów
        :return:
        """

        color_links = self.driver.find_elements(*self.SWATCH_LINK_COLOR)
        # Utwórz listę kolorów na podstawie atrybutu title
        color_titles = [link.get_attribute("title") for link in color_links]
        # # Kliknij każdy link i zweryfikuj wynik (np. załaduj stronę)
        for color in color_titles:
            if color == self.__class__.SAERCH_COLOR:
                link = WebDriverWait(self.driver, 10).until(
                    EC.presence_of_element_located((By.XPATH, f"//img[@title='{color}']/ancestor::a"))
                )
                # Kliknij link
                link.click()
                self.driver.implicitly_wait(50)
                products_find = self.driver.find_elements(*self.CATEGORY_PRODUCTS_LIST)
                vissible_products = [item for item in products_find if item.is_displayed()]
                product_item_count = len(vissible_products)
                assert product_item_count == self.__class__.EXPECTED_RESULT_OF_SEARCH_BY_COLOR_ARGUMENT
                allure.attach(self.driver.get_screenshot_as_png(), name='Product Search By Black Color',
                              attachment_type=AttachmentType.PNG)
