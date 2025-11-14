from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Calculator:

    def __init__(self, driver):
        self.browser = driver

    def input_delay(self, seconds=int):
        ddt = self.browser.find_element(By.ID, "delay")
        ddt.clear()
        ddt.send_keys(seconds)

    def buttons(self, num):
        self.browser.find_element(By.XPATH, f"//span[text()='{num}']").click()

    def result(self, waiting):
        wait = WebDriverWait(self.browser, waiting)
        wait.until(
            EC.text_to_be_present_in_element((
                By.CSS_SELECTOR, ".screen"), "15"))
