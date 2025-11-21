from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import allure


class Calculator:

    def __init__(self, driver):
        self.browser = driver

    @allure.step("Добавляем время задержки")
    def input_delay(self, seconds=int):
        """Устанавливает время задержки калькулятора"""
        ddt = self.browser.find_element(By.ID, "delay")
        ddt.clear()
        ddt.send_keys(seconds)

    @allure.step("Вводим значение на калькуляторе")
    def buttons(self, num):
        """Нажимает на кнопки"""
        self.browser.find_element(By.XPATH, f"//span[text()='{num}']").click()

    @allure.step("Ожидаем получение результата и сравниваем")
    def result(self, waiting = type[float], result = type[str]):
        """Ожидает время ответа калькулятора и сравнивает значение с ожидаемым"""
        wait = WebDriverWait(self.browser, waiting)
        wait.until(
            EC.text_to_be_present_in_element((
                By.CSS_SELECTOR, ".screen"), result))
