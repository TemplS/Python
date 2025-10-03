from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


driver = webdriver.Chrome()
driver.maximize_window()

driver.get("http://uitestingplayground.com/classattr")

btn = driver.find_element(By.CSS_SELECTOR, ".btn-primary")
btn.send_keys(Keys.RETURN)
