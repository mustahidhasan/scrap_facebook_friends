from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager


# set up the Chrome driver
driver = webdriver.Chrome(ChromeDriverManager().install())
# replace with the conversation link
driver.get('https://www.facebook.com/abulhasnat.shovan.5')

# find the message input box and type the message
message_input = driver.find_element(
    By.CSS_SELECTOR, 'div[data-blocked="true"] div[contenteditable="true"]')
message_input.send_keys('Hello, World!')

# get the data-lexical-text attribute of the message input box
data_lexical_text = message_input.get_attribute('data-lexical-text')
print(data_lexical_text)

# close the driver
driver.quit()
