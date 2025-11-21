from selenium import webdriver
from calculator import Calculator
import allure


@allure.title("Проверка калькулятора")
@allure.description("Проверка работы окна ожидания, кнопок калькулятора и конечного результата")
@allure.feature("Полная проверка калькулятора с ожиданием")
@allure.severity("Blocker")
def test_calculator_page():
    with allure.step("Заходим в браузер, настраиваем его и переходим на сайт"):
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.implicitly_wait(5)
        driver.get(
            "https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")

    calc = Calculator(driver)
    calc.input_delay(45)
    calc.buttons("7")
    calc.buttons("+")
    calc.buttons("8")
    calc.buttons("=")
    calc.result(46, "15")

    driver.quit()
