from selenium.webdriver.common.by import By


class Page_Locators:
    PAGE_TITLE = "//div[@class='page-title']"
    CATEGORY_PRODUCTS_LIST = "//div[@class='category-products']/ul/li"
    GLOBAL_SEARCH = "//input[@id='search']"
    PRODUCT_NAME_H2 = "//li[@class='item']/h2"
class Message_Page_Locators:
    NOTE_MSG = "//p[@class='note-msg']"
class Search_Locators:
    SWATCH_LINK_COLOR = "//a[@class='swatch-link has-image']/span/img"
    CAPACITY_LIST = "//dl[@id='narrow-by-list']/dd[@class='odd']/ol/li"
class Product_Page_Locators:
    PRODUCT_TITLE = "//div[@class='product-name']"
    PRICE_BOX_PRICE = "//div[@class='price-box']/span/span[@class='price']"
    PRODUCT_STATUS = "//div[@itemprop='offers']/div[@class='product-type-data']/p/span"
    TAB_DESCRIPTION = "//div[@id='product-tabs']/ul/li[@id='tab-description']"
    TAB_ADDITIONAL = "//div[@id='product-tabs']/ul/li[@id='tab-additional']"
    TAB_TABREVIEWS = "//div[@id='product-tabs']/ul/li[@id='tab-tabreviews']"
    TAB_TAGS = "//div[@id='product-tabs']/ul/li[@id='tab-tags']"
    TAB_PRODUCT_CMS_BLOCK1 = "//div[@id='product-tabs']/ul/li[@id='tab-product_cms_block1']"