from selenium.webdriver.common.by import By
import allure


class ShopOrder:

    def __init__(self, driver):
        self.browser = driver

    @allure.step("Добавление данных пользователя")
    def input_data(self, user_data: dict):
        """Подставляет данные пользователя в поля"""
        self.browser.find_element(By.ID, "first-name").send_keys(user_data["name"])
        self.browser.find_element(By.ID, "last-name").send_keys(user_data["last-name"])
        self.browser.find_element(By.ID, "postal-code").send_keys(user_data["postal-code"])

    @allure.step("Нажатие на кнопку")
    def button(self):
        """Нажимает на кнопку Продолжить"""
        self.browser.find_element(By.ID, "continue").click()

    @allure.step("Получение итоговой стоимости товаров")
    def price(self) -> str:
        """Возвращает конечную стоимость"""
        x = self.browser.find_element(
            By.CSS_SELECTOR, "[data-test='total-label']").text
        return x
