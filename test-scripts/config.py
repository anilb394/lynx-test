from selenium.webdriver.common.by import By


class ElementLocators:
    # Common locators
    accept_dialogue_button = (By.XPATH, "/html/body/div[1]/div/div[4]/div[1]/div[2]/button[4]")

    # Form element locators
    title_dropdown = (By.NAME, "title")
    first_name_input = (By.ID, "firstname")
    last_name_input = (By.ID, "lastname")
    email_input = (By.ID, "email")
    mobile_input = (By.NAME, "mobile")
    street_input = (By.ID, "street")
    house_number_input = (By.ID, "streetnumber")
    co_input = (By.ID, "co")
    zip_input = (By.ID, "zip")
    city_input = (By.ID, "city")
    country_dropdown = (By.ID, "country")
    province_dropdown = (By.XPATH, "//*[@id='state']/div[1]/select")
    birth_day_dropdown = (By.XPATH, "//*[@id='wizard-content']/div/div/form/div[3]/div[2]/div/div[2]/div[1]/div/div/div/div[1]/select")
    birth_month_dropdown = (By.XPATH, "//*[@id='wizard-content']/div/div/form/div[3]/div[2]/div/div[2]/div[1]/div/div/div/div[2]/select")
    birth_year_dropdown = (By.XPATH, "//*[@id='wizard-content']/div/div/form/div[3]/div[2]/div/div[2]/div[1]/div/div/div/div[4]/select")
    born_country_dropdown = (By.ID, "bornin")
    born_place_input = (By.ID, "place_of_birth")
    nationality_dropdown = (By.ID, "nationality")
    dependants_dropdown = (By.ID, "dependants")
    first_question_input = (By.NAME, "first_question")
    second_question_input = (By.NAME, "second_question_answer")
    third_question_input = (By.NAME, "third_question_answer")

    # Radio buttons
    gender_radio_button = (By.XPATH, "//*[@id='gender']/button[1]/span")
    radio_button1 = (By.XPATH, "//*[@id='wizard-content']/div/div/form/div[2]/div[2]/div/div[2]/div[7]/div/button[1]/span")
    radio_button2 = (By.XPATH, "//*[@id='wizard-content']/div/div/form/div[3]/div[2]/div/div[2]/div[6]/div/button[2]/span")
    radio_button3 = (By.XPATH, "//*[@id='wizard-content']/div/div/form/div[3]/div[2]/div/div[2]/div[8]/div/button[2]/span")
    radio_button4 = (By.XPATH, "//*[@id='wizard-content']/div/div/form/div[6]/div[2]/div/div[1]/button")

