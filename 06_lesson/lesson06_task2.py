from selenium import webdriver
from selenium.webdriver.common.by import By


driver = webdriver.Firefox()
driver.maximize_window()
driver.implicitly_wait(20)

driver.get("http://uitestingplayground.com/textinput")
input_field = driver.find_element(By.ID, "newButtonName")
btn = driver.find_element(By.ID, "updatingButton")
input_field.send_keys("SkyPro")
btn.click()
name = btn.text
print(name)

driver.quit()
