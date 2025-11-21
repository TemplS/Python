from selenium import webdriver
from shopauth import ShopAuth
from shopmainpage import ShopMainPage
from shopcart import ShopCart
from shoporder import ShopOrder
import allure


@allure.title("Проверка сайта магазина одежды")
@allure.description("Проверка основных функций сайта: авторизация, добавление товара в корзину, адрес получателя для отправки и оформление заказа")
@allure.feature("Быстрая проверка сайта")
@allure.severity("Blocker")
def test_shop():
    with allure.step("Заходим в браузер, настраиваем его и переходим на сайт"):
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.implicitly_wait(5)
        driver.get("https://www.saucedemo.com/")

    with allure.step("Авторизируемся"):
        auth = ShopAuth(driver)
        auth.input_data()
        auth.button()

    with allure.step("Добавляем товары в корзину и переходим в нее"):
        main = ShopMainPage(driver)
        locators = ["add-to-cart-sauce-labs-backpack",
                    "add-to-cart-sauce-labs-bolt-t-shirt",
                    "add-to-cart-sauce-labs-onesie"]
        main.add_product(locators)
        main.button()

    with allure.step("Сравниваем товары в корзине с теми, что добавили и нажимаем на кнопку"):
        cart = ShopCart(driver)
        waiting_list = ["Sauce Labs Backpack", "Sauce Labs Bolt T-Shirt", "Sauce Labs Onesie"]
        cart.check_cart(waiting_list)
        cart.button()

    with allure.step("Оформляем заказ"):
        order = ShopOrder(driver)
        with allure.step("Добавляем персональные данные"):
            user_data = {"name": "Daniil", "last-name": "Prokopev", "postal-code": "625046"}
            order.input_data(user_data)
        with allure.step("Нажимаем на кнопку"):
            order.button()
        with allure.step("Сравниваем итоговую цену с ожидаемой"):
            x = order.price()
            assert x == "Total: $58.29"

    driver.quit()
