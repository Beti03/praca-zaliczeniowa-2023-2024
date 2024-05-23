import pytest
import allure
from allure_commons.types import AttachmentType
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from beti03_source.pages.locators import Search_Locators, MainPageLocators
from beti03_source.scripts.function import convert_data_to_a_new_temporary_list


@allure.epic('Search Product')
@allure.suite("Search for a product by parameter")
class Test_SC_01_S_Product_Search_By_Parametrs:
    CAPACITY_LIST = (By.XPATH, Search_Locators.CAPACITY_LIST)
    CATEGORY_PRODUCTS_LIST = (By.XPATH, MainPageLocators.CATEGORY_PRODUCTS_LIST)
    SWATCH_LINK_COLOR = (By.XPATH, Search_Locators.SWATCH_LINK_COLOR)
    SEARCH_CAPACITY = '130 ml'
    SAERCH_COLOR = 'czarny'
    EXPECTED_RESULT_OF_SEARCH_BY_CAPACITY_ARGUMENT = 1
    EXPECTED_RESULT_OF_SEARCH_BY_COLOR_ARGUMENT = 9

    @allure.testcase("SC_01_S_TC_01")
    @allure.title("Product search by capacity")
    @allure.description(
        "This test attempts to log into the website using a login and a password. Fails if any error happens.\n\nNote that this test does not test 2-Factor Authentication.")
    @allure.severity(allure.severity_level.NORMAL)
    @allure.label("owner", "Beti03")
    @pytest.mark.usefixtures("set_side_on_cups")
    def test_SC_01_S_TC_01_Product_Search_By_Capacity(self):
        # Znajdź wszystkie dostępnę pojemonści i zwróć listę
        list_of_available_capacities = self.driver.find_elements(*self.CAPACITY_LIST)
        # Utworzenie zmiennej do przechowanie tymczasowej listy zwróconej przez funkcje")# Utworzenie zmiennej do przechowanie tymczasowej listy zwróconej przez funkcje
        tmp_elements_list = convert_data_to_a_new_temporary_list(list_of_available_capacities)
        # Licznik
        counter_counting_the_position_of_the_search_query = 0
        for i in range(len(tmp_elements_list)):
            if tmp_elements_list[i] != self.SEARCH_CAPACITY:
                counter_counting_the_position_of_the_search_query += 1
            else:
                capacity_item_xpath = f"//dl[@id='narrow-by-list']/dd[@class='last even']/ol/li[{counter_counting_the_position_of_the_search_query}]"
                capacity_item_id_in_the_list = self.driver.find_element(By.XPATH, capacity_item_xpath)
                self.driver.implicitly_wait(10)
                capacity_item_id_in_the_list.click()
                allure.attach(self.driver.get_screenshot_as_png(), name='screenshot',
                              attachment_type=AttachmentType.PNG)
                WebDriverWait(self.driver, 150).until(
                    EC.visibility_of_element_located((By.XPATH, "//div[@class='category-products']/ul/li"))
                )
                self.driver.implicitly_wait(50)
                products_find = self.driver.find_elements(*self.CATEGORY_PRODUCTS_LIST)
                vissible_products = [item for item in products_find if item.is_displayed()]
                product_item_count = len(vissible_products)
                assert product_item_count == self.EXPECTED_RESULT_OF_SEARCH_BY_CAPACITY_ARGUMENT
                allure.attach(self.driver.get_screenshot_as_png(), name='Product Search By Capacity',
                              attachment_type=AttachmentType.PNG)

    @allure.description("TC-02")
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.usefixtures("set_side_on_mugs")
    def test_SC_01_S_TC_02_Product_Search_By_Black_Color(self):
        """
        :TODO do poprawy przypadek testowy
        CEL: Sprwadzenie czy zostanie zwrócony produkt/y do którego przypisany jest atrybut Kolor
            WARUNKI WSTĘPNE:
            1. Strona ustawiona na http://www.kubki-reklamowe.eu/polska-ceramika-reklamowa.html
            KROKI:
            1. Znajdź nagłówek o nazwie "czarny"
            2. Kliknij w pozycję "Pomarańczowy"
            3. Zlicz ilość wyświetlonych produktów na stronie
            REZULTAT:
            1. Oczekiwana liczba produktów zwróconych w zakresie cenowym 1 będzie równa 1
            2. Na karcie produktu będzie atrybut o nazwie "Kolor" z wartością "Czerwony"
        :return:
        """

        color_links = self.driver.find_elements(*self.SWATCH_LINK_COLOR)
        # Utwórz listę kolorów na podstawie atrybutu title
        color_titles = [link.get_attribute("title") for link in color_links]
        # # Kliknij każdy link i zweryfikuj wynik (np. załaduj stronę)
        for color in color_titles:
            if color == self.SAERCH_COLOR:
                link = WebDriverWait(self.driver, 10).until(
                    EC.presence_of_element_located((By.XPATH, f"//img[@title='{color}']/ancestor::a"))
                )
                # Kliknij link
                link.click()
                self.driver.implicitly_wait(50)
                products_find = self.driver.find_elements(*self.CATEGORY_PRODUCTS_LIST)
                vissible_products = [item for item in products_find if item.is_displayed()]
                product_item_count = len(vissible_products)
                assert product_item_count == self.EXPECTED_RESULT_OF_SEARCH_BY_COLOR_ARGUMENT
                allure.attach(self.driver.get_screenshot_as_png(), name='Product Search By Black Color',
                              attachment_type=AttachmentType.PNG)