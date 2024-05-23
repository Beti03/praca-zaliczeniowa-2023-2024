from selenium.webdriver.common.by import By


class MainPageLocators:
    PAGE_TITLE = "//div[@class='page-title']"
    CATEGORY_PRODUCTS_LIST = "//div[@class='category-products']/ul/li"
    GLOBAL_SEARCH = "//input[@id='search']"
class MessagePageLocators:
    NOTE_MSG = "//p[@class='note-msg']"
class Search_Locators:
    SWATCH_LINK_COLOR = "//a[@class='swatch-link has-image']/span/img"
    CAPACITY_LIST = "//dl[@id='narrow-by-list']/dd[@class='odd']/ol/li"
class Products_Locators:

    TAB_DESCRIPTION = "//div[@id='product-tabs']/ul/li[@id='tab-description']"
    TAB_ADDITIONAL = "//div[@id='product-tabs']/ul/li[@id='tab-additional']"
    TAB_TABREVIEWS = "//div[@id='product-tabs']/ul/li[@id='tab-tabreviews']"
    TAB_TAGS = "//div[@id='product-tabs']/ul/li[@id='tab-tags']"
    TAB_PRODUCT_CMS_BLOCK1 = "//div[@id='product-tabs']/ul/li[@id='tab-product_cms_block1']"