from selenium.webdriver.common.by import By


class ShopMainPage:

    def __init__(self, driver):
        self.browser = driver

    def add_product(self):
        self.browser.find_element(
            By.ID, "add-to-cart-sauce-labs-backpack").click()
        self.browser.find_element(
            By.ID, "add-to-cart-sauce-labs-bolt-t-shirt").click()
        self.browser.find_element(
            By.ID, "add-to-cart-sauce-labs-onesie").click()

    def button(self):
        self.browser.find_element(
            By.CSS_SELECTOR, ".shopping_cart_link").click()
