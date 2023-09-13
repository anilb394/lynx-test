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
    time.sleep(5)
    accept_dialogue(driver)

    # Selecting and Filling fields in Ihre Kontaktdaten section
    select_radio_button(driver, ElementLocators.gender_radio_button)
    fill_form_field(driver, ElementLocators.first_name_input, 'test')
    fill_form_field(driver, ElementLocators.last_name_input, 'test')
    fill_form_field(driver, ElementLocators.email_input, 'test@example.com')
    fill_form_field(driver, ElementLocators.mobile_input, '15210000000')

    # Selecting and Filling fields in Meldeanschrift section
    fill_form_field(driver, ElementLocators.street_input, 'Alexanderstrasse')
    fill_form_field(driver, ElementLocators.house_number_input, '11')
    fill_form_field(driver, ElementLocators.zip_input, '10997')
    fill_form_field(driver, ElementLocators.city_input, 'Berlin')
    select_dropdown_option(driver, ElementLocators.country_dropdown, "Deutschland")
    select_dropdown_option(driver, ElementLocators.province_dropdown, "Berlin")
    select_radio_button(driver, ElementLocators.radio_button1)

    # Selecting and Filling fields in Persönliche Angaben section
    select_dropdown_option(driver, ElementLocators.birth_day_dropdown, "10")
    select_dropdown_option(driver, ElementLocators.birth_month_dropdown, "November")
    select_dropdown_option(driver, ElementLocators.birth_year_dropdown, "1980")
    select_dropdown_option(driver, ElementLocators.born_country_dropdown, "Deutschland")
    fill_form_field(driver, ElementLocators.born_place_input, 'Munich')
    select_dropdown_option(driver, ElementLocators.nationality_dropdown, "Deutschland")
    select_radio_button(driver, ElementLocators.radio_button2)
    select_radio_button(driver, ElementLocators.radio_button3)
    select_dropdown_option(driver, ElementLocators.dependants_dropdown, "1")

    # Selecting and Filling fields in Sicherheitsfragen section
    fill_form_field(driver, ElementLocators.first_question_input, 'TestName')
    fill_form_field(driver, ElementLocators.second_question_input, 'Beruf')
    fill_form_field(driver, ElementLocators.third_question_input, 'School')

    time.sleep(3)
    # Proceed to next screen
    select_radio_button(driver, ElementLocators.radio_button4)

    # Defining a condition to wait for asserting next screen
    condition = EC.presence_of_element_located((By.NAME, "iban_reference"))

    try:
        WebDriverWait(driver, 5).until(condition)
        assert driver.find_element(By.NAME, "iban_reference").is_displayed()
        print("Test passed: \n"
              "Mandatory fields checks successful for Section Persönliche Angaben")

    except Exception as e:
        print(f"Error: {e}")

    # Closing the browser
    driver.quit()


if __name__ == "__main__":
    main()