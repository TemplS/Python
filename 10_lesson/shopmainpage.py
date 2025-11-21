from selenium.webdriver.common.by import By
import allure


class ShopMainPage:

    def __init__(self, driver):
        self.browser = driver

    @allure.step("Добавление товаров в корзину")
    def add_product(self, locators: list[str])-> None:
        """Добавляет продукты в корзину по локаторам"""
        for locator in locators:
            self.browser.find_element(
                By.ID, locator).click()

    @allure.step("Нажатие на кнопку")
    def button(self):
        """Нажимает на кнопку"""
        self.browser.find_element(
            By.CSS_SELECTOR, ".shopping_cart_link").click()
