from selenium.webdriver.common.by import By


class ShopCart:

    def __init__(self, driver):
        self.browser = driver

    def check_cart(self):
        names = self.browser.find_elements(
            By.CSS_SELECTOR, ".inventory_item_name")
        shopping_list = []
        for name in names:
            shopping_list.append(name.text)
        assert shopping_list == ["Sauce Labs Backpack", "Sauce Labs Bolt T-Shirt", "Sauce Labs Onesie"]

    def button(self):
        self.browser.find_element(By.ID, "checkout").click()
