from selenium.webdriver.common.by import By


class MainPageLocators:
    PAGE_TITLE = "//div[@class='page-title']"
class MessagePageLocators:
    NOTE_MSG = "//p[@class='note-msg']"
class Search_Locators:
    COLOR_LIST = "//dl[@id='narrow-by-list']/dd[@class='odd']/ol/li/a/span/img[@title='czarny']"
    CAPACITY_LIST = "//dl[@id='narrow-by-list']/dd[@class='odd']/ol/li"


class Products_Locators:
    CATEGORY_PRODUCTS_LIST = "//div[@class='products-list']/ul/li"
