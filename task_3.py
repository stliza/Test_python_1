from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver = webdriver.Firefox()
driver.get("https://www.saucedemo.com/")
driver.find_element(By.CSS_SELECTOR, "#user-name").send_keys("standard_user")
driver.find_element(By.CSS_SELECTOR, "#password").send_keys("secret_sauce")
driver.find_element(By.CSS_SELECTOR, "#login-button").send_keys(Keys.RETURN)
driver.find_element(
    By.CSS_SELECTOR, "#add-to-cart-sauce-labs-backpack").click()
driver.find_element(
    By.CSS_SELECTOR, "#add-to-cart-sauce-labs-bolt-t-shirt").click()
driver.find_element(By.CSS_SELECTOR, "#add-to-cart-sauce-labs-onesie").click()
driver.find_element(By.CSS_SELECTOR, ".shopping_cart_link").click()
driver.find_element(By.CSS_SELECTOR, "#checkout").click()
driver.find_element(By.CSS_SELECTOR, "#first-name").send_keys("Liza")
driver.find_element(By.CSS_SELECTOR, "#last-name").send_keys("Brown")
driver.find_element(By.CSS_SELECTOR, "#postal-code").send_keys("200123")
driver.find_element(By.CSS_SELECTOR, "#continue").click()
txt = driver.find_element(By.CSS_SELECTOR, ".summary_total_label").text

total = "Total: $58.29"

if (txt == total):
    print(txt)
else:
    print("Стоимость не соответствует")
