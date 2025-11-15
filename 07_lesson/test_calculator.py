from selenium import webdriver
from selenium.webdriver.common.by import By
from calculator import Calculator


def test_calculator_page():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.implicitly_wait(5)
    driver.get(
        "https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")

    calc = Calculator(driver)
    calc.input_delay(5)
    calc.buttons("7")
    calc.buttons("+")
    calc.buttons("8")
    calc.buttons("=")
    calc.result(46)

    driver.quit()
