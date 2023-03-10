from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from openpyxl import Workbook
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd
from selenium.webdriver.support import expected_conditions as EC
from openpyxl import load_workbook
import time
from selenium.webdriver.common.by import By

driver = None


def get_driver():
    global driver

    # check if driver is already created
    if not driver:
        # create a new driver
        driver = webdriver.Chrome(ChromeDriverManager().install())

    return driver


def get_the_user_info(my_value):
    # Create an instance of ChromeOptions and add the path to the Chrome driver
    chrome_options = Options()
    chrome_options.add_argument("--headless")  # To run Chrome in headless mode

    # Create an instance of WebDriver
    driver = get_driver()

    # Navigate to the Facebook profile
    profile_link = my_value
    driver.get(profile_link)

    time.sleep(10)
    name_element = driver.find_element_by_xpath(
        '/html/body/div[1]/div/div[1]/div/div[3]/div/div/div/div[1]/div[1]/div/div/div[1]/div[2]/div/div/div/div[3]/div/div/div/div/div/span')
    # nickname_element = driver.find_element_by_xpath(
    #     '/html/body/div[1]/div/div[1]/div/div[3]/div/div/div/div[1]/div[1]/div/div/div[1]/div[2]/div/div/div/div[3]/div/div/div/div/div/span/h1/span')

    # Extract the first name, last name, and nickname from the elements
    full_name = name_element.text
    print("full name", full_name)
    first_name = full_name.split()[0]
    last_name = full_name.split()[-1]
    # nickname = nickname_element.text
    print("first name:", first_name)
    print("last name:", last_name)
    # print("nick name:", nickname)
    time.sleep(10)
    # send sms
    send_message = driver.find_element_by_xpath(
        "/html/body/div[1]/div/div[1]/div/div[3]/div/div/div/div[1]/div[1]/div/div/div[1]/div[2]/div/div/div/div[4]/div/div/div[2]/div/div")
    send_message.click()
    # Load the Excel file

    time.sleep(20)
    message_text = "Hello " + first_name + " How r you??"
    # print("message: ", message_text)
    set_message = driver.find_element_by_xpath(
        "/html/body/div[1]/div/div[1]/div/div[5]/div/div[1]/div[1]/div/div/div/div/div[2]/div[2]/div/div/div[4]/div[2]/div/div/div/p")

    print("line 64", set_message)
    time.sleep(10)
    set_message.click()

    time.sleep(10)
    message_input = driver.find_element(
        By.XPATH, '/html/body/div[1]/div/div[1]/div/div[5]/div/div[1]/div[1]/div/div/div/div/div[2]/div[2]/div/div/div[4]/div[2]/div/div/div[1]/p/br')

    message_input.send_keys(message_text)

    time.sleep(10)

    # set_text = driver.find_element_by_xpath(
    #     '/html/body/div[1]/div/div[1]/div/div[5]/div/div[1]/div[1]/div/div/div/div/div[2]/div[2]/div/div/div[4]/div[2]/div/div/div/p/span')
    # set_text.send_keys(message_text)

    click_send_button = driver.find_element_by_xpath(
        "/html/body/div[1]/div/div[1]/div/div[5]/div/div[1]/div[1]/div/div/div/div/div[2]/div[2]/div/span[2]/div")
    click_send_button.click()
    print("clicked the msg field")


def get_the_sheet_file():

    df = pd.read_excel('FB_AGENCY_MESSAGE_INTRO.xlsx')

    # Iterate through each row in the DataFrame
    for index, row in df.iterrows():
        # Extract the value of the desired column for the current row
        my_value = row['URL']

        # Pass the value to another function
        get_the_user_info(my_value)


def login_to_facebook():

    # Instantiate a webdriver object and navigate to the Facebook login page
    driver = get_driver()
    driver.get('https://www.facebook.com/')

    # Locate the email and password input fields, enter your login credentials, and submit the form
    email_input = driver.find_element_by_name('email')
    password_input = driver.find_element_by_name('pass')

    email_input.send_keys('phone_number')
    password_input.send_keys('password')
    password_input.send_keys(Keys.RETURN)
    time.sleep(10)
    get_the_sheet_file()


if __name__ == "__main__":
    login_to_facebook()
