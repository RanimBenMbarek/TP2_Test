# Generated by Selenium IDE
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

class TestCas():
  def setup_method(self, method):
    self.driver = webdriver.Chrome()
    self.vars = {}
  
  def teardown_method(self, method):
    self.driver.quit()
  
  def test_divisionzero(self):
    self.driver.get("https://safatelli.github.io/tp-test-logiciel/assets/calc.html")
    self.driver.set_window_size(858, 713)
    self.driver.find_element(By.CSS_SELECTOR, "html").click()
    self.driver.find_element(By.ID, "num1").click()
    self.driver.find_element(By.ID, "num1").click()
    self.driver.find_element(By.ID, "num1").send_keys("2")
    self.driver.find_element(By.ID, "calculatorForm").click()
    self.driver.find_element(By.ID, "operator").click()
    dropdown = self.driver.find_element(By.ID, "operator")
    dropdown.find_element(By.XPATH, "//option[. = '/']").click()
    self.driver.find_element(By.ID, "num2").click()
    self.driver.find_element(By.ID, "num2").send_keys("0")
    self.driver.find_element(By.CSS_SELECTOR, "button").click()
    self.driver.find_element(By.ID, "result").click()
    self.driver.find_element(By.ID, "result").click()
    element = self.driver.find_element(By.ID, "result")
    actions = ActionChains(self.driver)
    actions.double_click(element).perform()
    self.driver.find_element(By.ID, "result").click()
    assert self.driver.find_element(By.ID, "result").text == "Résultat : Infinity"
  
  def test_emptyrequiredfield(self):
    self.driver.get("https://safatelli.github.io/tp-test-logiciel/assets/calc.html")
    self.driver.set_window_size(858, 713)
    self.driver.find_element(By.ID, "operator").click()
    dropdown = self.driver.find_element(By.ID, "operator")
    dropdown.find_element(By.XPATH, "//option[. = '+']").click()
    self.driver.find_element(By.CSS_SELECTOR, "button").click()
    value = self.driver.find_element(By.ID, "result").get_attribute("value")
    assert value == None
  

inst = TestCas()
inst.setup_method('')
inst.test_divisionzero()
inst.test_emptyrequiredfield()
inst.teardown_method('')