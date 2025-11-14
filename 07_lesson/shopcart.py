from selenium.webdriver.common.by import By


class ShopCart:

    def __init__(self, driver):
        self.browser = driver

    def check_cart(self):
        names = self.browser.find_elements(
            By.CSS_SELECTOR, ".inventory_item_name")
        name1 = names[0]
        name2 = names[1]
        name3 = names[2]
        print(name1.text, " ", name2.text, " ", name3.text)

    def button(self):
        self.browser.find_element(By.ID, "checkout").click()
