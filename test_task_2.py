from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pytest


@pytest.fixture
def driver():
    driver = webdriver.Firefox()
    yield driver
    driver.quit()


def test_calculator(driver):
    driver.get(
       "https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")
    driver.find_element(
       By.CSS_SELECTOR, "#delay").clear()
    driver.find_element(
       By.CSS_SELECTOR, "#delay").send_keys("45")
    driver.find_element(
        By.CSS_SELECTOR, ".btn-outline-primary:first-child").click()
    driver.find_element(
        By.CSS_SELECTOR, ".operator").click()
    driver.find_element(
        By.CSS_SELECTOR, ".btn-outline-primary:nth-child(2)").click()
    driver.find_element(
        By.CSS_SELECTOR, ".btn-outline-warning").click()

    waiter = WebDriverWait(driver, 45)
    waiter.until(
        EC.text_to_be_present_in_element((By.CSS_SELECTOR, ".screen"), "15"))
    assert driver.find_element(By.CSS_SELECTOR, ".screen").text == "15"
    print(driver.find_element(By.CSS_SELECTOR, ".screen").text)
