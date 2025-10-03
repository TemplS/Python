from selenium import webdriver
from selenium.webdriver.common.by import By


driver = webdriver.Firefox()
driver.maximize_window()

driver.get("http://the-internet.herokuapp.com/login")

login_input = driver.find_element(By.ID, 'username')
login_input.send_keys("tomsmith")
password_input = driver.find_element(By.ID, 'password')
password_input.send_keys("SuperSecretPassword!")
btn = driver.find_element(By.CSS_SELECTOR, "i")
btn.click()
text = driver.find_element(By.CSS_SELECTOR, '[class="flash success"]').text
print(text)
driver.quit()
