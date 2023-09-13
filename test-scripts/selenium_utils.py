from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select




def accept_dialogue(driver):
    try:
        driver.find_element(By.XPATH, "/html/body/div[1]/div/div[4]/div[1]/div[2]/button[4]").click()
    except Exception as e:
        print(f"Error accepting dialogue: {e}")


def select_radio_button(driver, locator):
    radio_button = driver.find_element(*locator)
    radio_button.click()

def select_dropdown_option(driver, element_locator, option_text):
    try:
        select_element = Select(driver.find_element(*element_locator))
        select_element.select_by_visible_text(option_text)
    except Exception as e:
        print(f"Error selecting dropdown option: {e}")


def fill_form_field(driver, element_locator, input_text):
    try:
        driver.find_element(*element_locator).send_keys(input_text)
    except Exception as e:
        print(f"Error filling form field: {e}")
