from selenium.webdriver.common.by import By


class ShopAuth:

    def __init__(self, driver):
        self.browser = driver

    def input_data(self):
        self.browser.find_element(
            By.ID, "user-name").send_keys("standard_user")
        self.browser.find_element(
            By.ID, "password").send_keys("secret_sauce")

    def button(self):
        self.browser.find_element(By.ID, "login-button").click()
