from unicodedata import name
from selenium import webdriver
from selenium.webdriver.common.by import By
import webbrowser
import time

driver = webdriver.Chrome("./chromedriver")
driver.get("https://www.nytimes.com/games/wordle/index.html")

def __openAndResizeTheWebsite__():
    driver.maximize_window()
    time.sleep(3)
    button = driver.find_element(by = By.ID, value = "pz-gdpr-btn-accept")
    button.click()
    time.sleep(1)
    button = driver.find_element(by = By.CLASS_NAME,value="Modal-module_closeIcon__b4z74")
    button.click()

# click the selected word.
def __autoClickLetters__(letter):
    time.sleep(1)
    button = driver.find_element(by = By.CSS_SELECTOR,value="button[data-key=" +letter + "]")
    button.click()

