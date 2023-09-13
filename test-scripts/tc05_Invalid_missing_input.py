from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from config import ElementLocators
from selenium_utils import *
import time


def initialize_driver():
    # Initialize the Chrome WebDriver
    return webdriver.Chrome()


def open_webpage(driver, url):
    driver.get(url)


def main():
    # Create and initialize the WebDriver
    driver = initialize_driver()

    # URL of the webpage
    url = 'https://www.lynxbroker.de/wertpapierdepot/depoteroeffnung/antrag/'

    # Open the webpage
    open_webpage(driver, url)

    # Wait for dialogue to display and accept it
    time.sleep(4)
    accept_dialogue(driver)

    fill_form_field(driver, ElementLocators.first_name_input, 'test')
    fill_form_field(driver, ElementLocators.last_name_input, 'test')
    fill_form_field(driver, ElementLocators.email_input, 'test.com')

    # Proceed to next screen
    select_radio_button(driver, ElementLocators.radio_button4)

    time.sleep(3)
    # Asserting element
    assert driver.find_element(By.NAME, "iban_reference").is_displayed()," Invalid/Missing data in Red fields"
    # Closing the browser
    driver.quit()


if __name__ == "__main__":
    main()