from selenium.webdriver.common.by import By


class ShopOrder:

    def __init__(self, driver):
        self.browser = driver

    def input_data(self, user_data: dict):
        self.browser.find_element(By.ID, "first-name").send_keys(user_data["name"])
        self.browser.find_element(By.ID, "last-name").send_keys(user_data["last-name"])
        self.browser.find_element(By.ID, "postal-code").send_keys(user_data["postal-code"])

    def button(self):
        self.browser.find_element(By.ID, "continue").click()

    def price(self):
        x = self.browser.find_element(
            By.CSS_SELECTOR, "[data-test='total-label']").text
        return x
