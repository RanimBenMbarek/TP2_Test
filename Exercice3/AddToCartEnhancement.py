import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By


class TestAddToCart:
    def setup_method(self, method):
        self.driver = webdriver.Chrome()
        self.vars = {}
    def teardown_method(self, method):
        self.driver.quit()
    def test_AddToCart(self):
        self.driver.get("https://www.demoblaze.com/")
        self.driver.set_window_size(1722, 1034)
        # Define variables
        product_name = "Samsung galaxy s6"
        expected_message = "Product added"
        # Click on the product
        self.driver.find_element(By.LINK_TEXT, product_name).click()
        # Click on "Add to cart"
        self.driver.find_element(By.LINK_TEXT, "Add to cart").click()
        # Wait for the alert
        alert = self.driver.switch_to.alert
        # Assertion to verify product added message
        assert alert.text == expected_message, f"Expected message '{expected_message}' not found. Actual message: {alert.text}"
        # Dismiss the alert
        alert.accept()
