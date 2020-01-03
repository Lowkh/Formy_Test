import os
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options  
import pytest
import time

@pytest.fixture()
def driver():
    chrome_options = Options()  
    chrome_options.add_argument("--headless") 
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument("--disable-gpu")
    driver = webdriver.Chrome(options =chrome_options)      
    yield driver
    driver.quit()
    # create a object for the chrome driver and pass around

def test_formy_buttons(driver):
    driver.get("https://formy-project.herokuapp.com/buttons")

    assert "Form" in driver.title
    elem = driver.find_element_by_css_selector('.btn-primary')
    elem.click()
    time.sleep(1)
    elem = driver.find_element_by_css_selector('.btn-success')
    elem.click()
    time.sleep(1)
    elem = driver.find_element_by_css_selector('.btn-info')
    elem.click()
    time.sleep(1)
    elem = driver.find_element_by_css_selector('.btn-warning')
    elem.click()
    time.sleep(1)
    elem = driver.find_element_by_css_selector('.btn-danger')
    elem.click()
    time.sleep(1)
    elem = driver.find_element_by_css_selector('.btn-link')
    elem.click()
    time.sleep(1)
    elem = driver.find_element_by_xpath('//button[text()="Left"]')
    elem.click()
    time.sleep(1)
    elem = driver.find_element_by_xpath('//button[text()="Middle"]')
    elem.click()
    time.sleep(1)
    elem = driver.find_element_by_xpath('//button[text()="Right"]')
    elem.click()
    time.sleep(1)
    elem = driver.find_element_by_xpath('//button[text()="1"]')
    elem.click()
    time.sleep(1)
    elem = driver.find_element_by_xpath('//button[text()="2"]')
    elem.click()
    time.sleep(1)
    elem = driver.find_element_by_id('btnGroupDrop1')
    elem.click()
    time.sleep(1)
    

