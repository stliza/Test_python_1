from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest


@pytest.fixture
def driver():
    driver = webdriver.Firefox()
    driver.fullscreen_window()
    yield driver
    driver.quit()


def test_form(driver):
    driver.get(
        "https://bonigarcia.dev/selenium-webdriver-java/data-types.html")
    driver.find_element(
        By.CSS_SELECTOR, "[name='first-name']").send_keys("Иван")
    driver.find_element(
        By.CSS_SELECTOR, "[name='last-name']").send_keys("Петров")
    driver.find_element(
        By.CSS_SELECTOR, "[name='address']").send_keys("Ленина, 55-3")
    driver.find_element(
        By.CSS_SELECTOR, "[name='e-mail']").send_keys("test@skypro.com")
    driver.find_element(
        By.CSS_SELECTOR, "[name='phone']").send_keys("+7985899998787")
    driver.find_element(
        By.CSS_SELECTOR, "[name='city']").send_keys("Москва")
    driver.find_element(
        By.CSS_SELECTOR, "[name='country']").send_keys("Россия")
    driver.find_element(
        By.CSS_SELECTOR, "[name='job-position']").send_keys("QA")
    driver.find_element(
        By.CSS_SELECTOR, "[name='company']").send_keys("SkyPro")
    driver.find_element(
        By.CSS_SELECTOR, "[type='submit']").click()

    assert driver.find_element(By.CSS_SELECTOR, ".alert-danger#zip-code")
    other_input = driver.find_elements(By.CSS_SELECTOR, ".alert")
    for input in other_input:
        if input.get_attribute("id") != "zip-code":
            assert driver.find_element(By.CSS_SELECTOR, ".alert-success")
