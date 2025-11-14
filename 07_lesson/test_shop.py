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
    main.add_product()
    main.button()

    cart = ShopCart(driver)
    cart.check_cart()
    cart.button()

    order = ShopOrder(driver)
    order.input_data()
    order.button()
    x = order.price()

    driver.quit()

    assert x == "Total: $58.29"
