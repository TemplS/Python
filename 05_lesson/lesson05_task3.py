from selenium import webdriver
from selenium.webdriver.common.by import By


driver = webdriver.Firefox()
driver.maximize_window()

driver.get("http://the-internet.herokuapp.com/inputs")

text_input = driver.find_element(By.CSS_SELECTOR, 'input')
text_input.send_keys("Sky")
text_input.clear()
text_input.send_keys("Pro")
driver.quit()
