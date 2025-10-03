from selenium import webdriver
from selenium.webdriver.common.by import By


driver = webdriver.Firefox()
driver.maximize_window()
driver.implicitly_wait(20)

driver.get("http://uitestingplayground.com/ajax")

btn = driver.find_element(By.ID, "ajaxButton").click()
txt = driver.find_element(By.CSS_SELECTOR, "p[class='bg-success']")
print(txt.text)

driver.quit()
