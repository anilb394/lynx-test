from selenium import webdriver
from selenium_utils import *
import time

# Initialize the Chrome WebDriver
driver = webdriver.Chrome()

# Navigate to the webpage
driver.get('https://www.lynxbroker.de/wertpapierdepot/depoteroeffnung/antrag/')

time.sleep(3)
accept_dialogue(driver)

try:
    # Check if the first section is displayed
    section1 = driver.find_element(By.XPATH, '//*[@id="masthead"]/nav[2]/div/div[2]/ul/li[1]/a')
    assert section1.is_displayed(), "Persönliche Angaben is not displayed"

    # Check if the second section is displayed
    section2 = driver.find_element(By.XPATH, '//*[@id="masthead"]/nav[2]/div/div[2]/ul/li[2]/a')
    assert section2.is_displayed(), "Regulatorische Informationen is not displayed"

    # Check if the third section is displayed
    section3 = driver.find_element(By.XPATH, '//*[@id="masthead"]/nav[2]/div/div[2]/ul/li[3]/a')
    assert section3.is_displayed(), "Handel is not displayed"

    # Check if the forth section is displayed
    section4 = driver.find_element(By.XPATH, '//*[@id="masthead"]/nav[2]/div/div[2]/ul/li[4]/a')
    assert section4.is_displayed(), "Handel is not displayed"

    # Check if the fifth section is displayed
    section5 = driver.find_element(By.XPATH, '//*[@id="masthead"]/nav[2]/div/div[2]/ul/li[5]/a')
    assert section5.is_displayed(), "Abschluss is not displayed"


    print("DOF start page is loaded and All sections are displayed successfully!")

except Exception as e:
    print(f"Error: {e}")


    # Close the browser when you're done
    driver.quit()
