from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from openpyxl import Workbook
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd
from selenium.webdriver.support import expected_conditions as EC
from openpyxl import load_workbook
import time
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
    nickname_element = driver.find_element_by_xpath(
        '/html/body/div[1]/div/div[1]/div/div[3]/div/div/div/div[1]/div[1]/div/div/div[1]/div[2]/div/div/div/div[3]/div/div/div/div/div/span/h1/span')

    # Extract the first name, last name, and nickname from the elements
    full_name = name_element.text
    print("full name", full_name)
    first_name = full_name.split()[0]
    last_name = full_name.split()[-1]
    nickname = nickname_element.text
    print("first name:", first_name)
    print("last name:", last_name)
    print("nick name:", nickname)

    # Load the Excel file
    workbook = load_workbook('facebook_user_info.xlsx')

    # Select the active worksheet
    worksheet = workbook.active
    # Add the data to the Excel file
    row = [first_name, last_name, nickname]
    worksheet.append(row)

    # Set the column names
    worksheet.cell(row=1, column=1, value='first_name')
    worksheet.cell(row=1, column=2, value='last_name')
    worksheet.cell(row=1, column=3, value='nickname')

    # Save the changes to the Excel file
    workbook.save('facebook_user_info.xlsx')


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

    email_input.send_keys('01754627430')
    password_input.send_keys('19171518-Sagor19')
    password_input.send_keys(Keys.RETURN)
    time.sleep(50)
    # # Wait for the login to complete
    # element_present = EC.presence_of_element_located(
    #     (By.ID, 'userNavigationLabel'))
    # WebDriverWait(driver, 10).until(element_present)

    # # Verify that you are logged in
    # assert 'Facebook' in driver.title
    get_the_sheet_file()


if __name__ == "__main__":
    login_to_facebook()
