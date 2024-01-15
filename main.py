import os

from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
import time
import os

EMAIL = os.getenv("EMAIL")
PASSWORD = os.getenv("PASSWORD")

# Optional - Keep the browser open (helps diagnose issues if the script crashes)
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)

driver.get("https://www.linkedin.com/jobs/search/?currentJobId=3792867485&f_AL=true&f_SB2=42&geoId=101165590&keywords=Application%20Support&location=United%20Kingdom&origin=JOB_SEARCH_PAGE_LOCATION_AUTOCOMPLETE&refresh=true")

# Click Reject Cookies Button
time.sleep(2)
reject_button = driver.find_element(by=By.CSS_SELECTOR, value='button[action-type="DENY"]')
reject_button.click()

# Click Sign in Button
time.sleep(2)
sign_in_button = driver.find_element(by=By.LINK_TEXT, value="Sign in")
sign_in_button.click()

# Sign in
time.sleep(5)
search_email = driver.find_element(By.NAME, value="session_key")
search_password = driver.find_element(By.NAME, value="session_password")
search_email.send_keys(EMAIL)
search_password.send_keys(PASSWORD, Keys.ENTER)

# You may be presented with a CAPTCHA - Solve the Puzzle Manually
input("Press Enter when you have solved the Captcha")

time.sleep(5)
easy_apply = driver.find_element(by=By.CSS_SELECTOR, value=".jobs-s-apply button")
easy_apply.click()

time.sleep(5)
next_button = driver.find_element(by=By.CSS_SELECTOR, value=".display-flex button")
next_button.click()

time.sleep(5)
next_button.click()

time.sleep(5)
review_button = driver.find_element(by=By.CSS_SELECTOR, value=".display-flex justify-flex-end ph5 pv4 button")
review_button.click()

time.sleep(5)
submit_button = driver.find_element(by=By.CSS_SELECTOR, value=".job-details-easy-apply-footer__section checkbox")
submit_button.click()

time.sleep(5)
submit_button = driver.find_element(by=By.CSS_SELECTOR, value=".display-flex justify-flex-end ph5 pv4 button")
submit_button.click()