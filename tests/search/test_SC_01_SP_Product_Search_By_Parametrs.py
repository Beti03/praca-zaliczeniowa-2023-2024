import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.locators import Search_Locators, Products_Locators, MainPageLocators, MessagePageLocators
from conftest import convert_data_to_a_new_temporary_list

CUP_CAPACITY = '130 ml'
MUG_COLOR = 'czarny'


class Test_SC_01_S_Product_Search_By_Parametrs:
    CAPACITY_LIST = (By.XPATH, Search_Locators.CAPACITY_LIST)
    COLOR_LIST = (By.XPATH, Search_Locators.COLOR_LIST)
    CATEGORY_PRODUCTS_LIST = (By.XPATH, Products_Locators.CATEGORY_PRODUCTS_LIST)
    PAGE_TITLE = (By.XPATH, MainPageLocators.PAGE_TITLE)
    NOTE_MSG = (By.XPATH, MessagePageLocators.NOTE_MSG)

    @pytest.mark.usefixtures("set_side_on_cups")
    def test_SC_01_S_TC_01_Product_Search_By_Capacity(self):
        """
        SC_02_S_Product_Search_By_Color:
        Wyszukiwanie przez wybranie pojemności
        TODO: Uzupełnić
        :return:
        """
        # Znajdź wszystkie dostępnę pojemonści i zwróć listę
        list_of_available_capacities = self.driver.find_elements(*self.CAPACITY_LIST)
        # Utworzenie zmiennej do przechowanie tymczasowej listy zwróconej przez funkcje
        tmp_elements_list = convert_data_to_a_new_temporary_list(list_of_available_capacities)
        # Licznik
        counter_counting_the_position_of_the_search_query = 0
        for i in range(len(tmp_elements_list)):
            if tmp_elements_list[i] != CUP_CAPACITY:
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
                products_find = self.driver.find_elements(By.XPATH, "//div[@class='category-products']/ul/li")
                vissible_products = [item for item in products_find if item.is_displayed()]
                product_item_count = len(vissible_products)
                assert product_item_count == 1

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
        expected_color = 'czarny'
        # # Znajdź wszystkie dostępnę pojemonści i zwróć listę
        # # list_of_available_colors = self.driver.find_element(By.XPATH, "//dl[@id='narrow-by-list']/dd[@class='odd']/ol/li/a/span//img[@title='czarny']")
        # list_of_available_colors = self.driver.find_element(By.CSS_SELECTOR, f"//a[img(@title, '{color}')")
        # list_of_available_colors.click()
        # self.driver.implicitly_wait(1000)
        # # print(list_of_available_colors.text)
        color_links = self.driver.find_elements(By.XPATH, "//a[@class='swatch-link has-image']/span/img")

        # Utwórz listę kolorów na podstawie atrybutu title
        color_titles = [link.get_attribute("title") for link in color_links]
        # # Kliknij każdy link i zweryfikuj wynik (np. załaduj stronę)
        for color in color_titles:
            if color == expected_color:
                link = WebDriverWait(self.driver, 10).until(
                    EC.presence_of_element_located((By.XPATH, f"//img[@title='{color}']/ancestor::a"))
                )
                # Kliknij link
                link.click()
                self.driver.implicitly_wait(50)
                products_find = self.driver.find_elements(By.XPATH, "//div[@class='category-products']/ul/li")
                vissible_products = [item for item in products_find if item.is_displayed()]
                product_item_count = len(vissible_products)
                assert product_item_count == 9