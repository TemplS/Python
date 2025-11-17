from selenium.webdriver.common.by import By


class ShopMainPage:

    def __init__(self, driver):
        self.browser = driver

    def add_product(self, locators: list[str])-> None:
        for locator in locators:
            self.browser.find_element(
                By.ID, locator).click()

    def button(self):
        self.browser.find_element(
            By.CSS_SELECTOR, ".shopping_cart_link").click()
