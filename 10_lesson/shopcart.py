from selenium.webdriver.common.by import By
import allure


class ShopCart:

    def __init__(self, driver):
        self.browser = driver

    @allure.step("Сравнение товаров в корзине с добавленными по названию")
    def check_cart(self, waiting_list = list[str]):
        """Сравнивает названия товаров в корзине с заданными"""
        names = self.browser.find_elements(
            By.CSS_SELECTOR, ".inventory_item_name")
        shopping_list = []
        for name in names:
            shopping_list.append(name.text)
        assert shopping_list == waiting_list

    @allure.step("Нажатие на кнопку")
    def button(self):
        """Нажимает на кнопку Checkout"""
        self.browser.find_element(By.ID, "checkout").click()
