from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EX


driver = webdriver.Firefox()
driver.maximize_window()
driver.implicitly_wait(20)

driver.get("https://bonigarcia.dev/selenium-webdriver-java/loading-images.html")
wait = WebDriverWait(driver, 10).until(
    EX.visibility_of_element_located((By.CSS_SELECTOR, '[src="img/landscape.png"]'))
)
png = driver.find_element(By.ID, "award")
result = png.get_attribute("src")
print(result)

driver.quit()
