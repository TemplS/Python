from selenium import webdriver
from shopauth import ShopAuth
from shopmainpage import ShopMainPage
from shopcart import ShopCart
from shoporder import ShopOrder


def test_shop():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.implicitly_wait(5)
    driver.get("https://www.saucedemo.com/")

    auth = ShopAuth(driver)
    auth.input_data()
    auth.button()

    main = ShopMainPage(driver)
    locators = ["add-to-cart-sauce-labs-backpack",
                "add-to-cart-sauce-labs-bolt-t-shirt",
                "add-to-cart-sauce-labs-onesie"]
    main.add_product(locators)
    main.button()

    cart = ShopCart(driver)
    cart.check_cart()
    cart.button()

    order = ShopOrder(driver)
    user_data = {"name": "Daniil", "last-name": "Prokopev", "postal-code": "625046"}
    order.input_data(user_data)
    order.button()
    x = order.price()

    driver.quit()

    assert x == "Total: $58.29"
