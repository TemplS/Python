from selenium.webdriver.common.by import By
import allure


class ShopAuth:

    def __init__(self, driver):
        self.browser = driver

    @allure.step("Авторизация")
    def input_data(self):
        """Вводите данные в поля для входа в аккаунт"""
        self.browser.find_element(
            By.ID, "user-name").send_keys("standard_user")
        self.browser.find_element(
            By.ID, "password").send_keys("secret_sauce")

    @allure.step("Нажатие на кнопку")
    def button(self):
        """Нажимает на кнопку"""
        self.browser.find_element(By.ID, "login-button").click()
