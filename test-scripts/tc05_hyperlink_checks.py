from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
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

    # Find hyerlinked text for click operation
    link_element = driver.find_element(By.XPATH, "//*[@id='wizard-content']/div/div/form/div[5]/div[2]/div/div[2]/p/a[1]")
    action_chains = ActionChains(driver)
    action_chains.click(link_element).perform()

    # Switch focus on new tab
    driver.switch_to.window(driver.window_handles[-1])
    time.sleep(5)
    try:
        assert driver.find_element(By.XPATH, "// *[ @ id = 'main']/div[2]/p[40]/strong[5]/a").is_displayed()
        print("Test Passed: \n"
              "Datenschutzerklärung Hyperlink Navigation is Successful")

    except Exception as e:
        print(f"Error: {e}")
    driver.close()

    # Switch focus on back on original tab
    driver.switch_to.window(driver.window_handles[0])
    time.sleep(2)

     # Closing the browser
    driver.quit()


if __name__ == "__main__":
    main()
