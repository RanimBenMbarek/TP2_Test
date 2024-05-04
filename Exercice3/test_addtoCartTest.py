# Generated by Selenium IDE
import pytest
import time
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

class TestAddtoCartTest():
  def setup_method(self, method):
    self.driver = webdriver.Chrome()
    self.vars = {}
  
  def teardown_method(self, method):
    self.driver.quit()
  
  def test_addtoCartTest(self):
    self.driver.get("https://www.demoblaze.com/")
    self.driver.set_window_size(1296, 688)
    self.driver.find_element(By.LINK_TEXT, "Samsung galaxy s6").click()
    self.driver.find_element(By.LINK_TEXT, "Add to cart").click()
    assert self.driver.switch_to.alert.text == "Product added"
    self.driver.close()
  