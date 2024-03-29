import os
import time

from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

EMAIL = os.getenv("EMAIL")
PASSWORD = os.getenv("PASSWORD")
PHONE = os.getenv("PHONE")

def abort_application():
    # Click Close Button
    close_button = driver.find_element(by=By.CLASS_NAME, value="artdeco-modal__dismiss")
    close_button.click()

    time.sleep(2)
    # Click Discard Button
    discard_button = driver.find_elements(by=By.CLASS_NAME, value="artdeco-modal__confirm-dialog-btn")[1]
    discard_button.click()


# Optional - Keep the browser open if the script crashes.
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)

driver.get("https://www.linkedin.com/jobs/search/?currentJobId=3791953240&f_AL=true&f_TPR=r2592000&f_WT=3%2C2&geoId=101165590&keywords=application%20support&location=United%20Kingdom&origin=JOB_SEARCH_PAGE_LOCATION_AUTOCOMPLETE&refresh=true&sortBy=R")

# Click Reject Cookies Button
time.sleep(2)
reject_button = driver.find_element(by=By.CSS_SELECTOR, value='button[action-type="DENY"]')
reject_button.click()

# Click Sign in Button
time.sleep(5)
sign_in_button = driver.find_element(by=By.LINK_TEXT, value="Sign in")
sign_in_button.click()

# Sign in
time.sleep(5)
search_email = driver.find_element(By.NAME, value="session_key")
search_password = driver.find_element(By.NAME, value="session_password")
search_email.send_keys(EMAIL)
search_password.send_keys(PASSWORD, Keys.ENTER)

# CAPTCHA - Solve Puzzle Manually
input("Press Enter when you have solved the Captcha")

# Get Listings
time.sleep(5)
all_listings = driver.find_elements(by=By.CSS_SELECTOR, value=".scaffold-layout__list")
print(all_listings)

# Apply for Jobs
for listing in all_listings:
    print("Opening Listing")
    listing.click()
    time.sleep(2)
    try:
        # Click Apply Button
        apply_button = driver.find_element(by=By.CSS_SELECTOR, value=".jobs-s-apply button")
        apply_button.click()

        # Insert Phone Number
        # Find an <input> element where the id contains phoneNumber
        time.sleep(3)
        # phone = driver.find_element(by=By.CSS_SELECTOR, value="input[type=text]")
        phone = driver.find_element(by=By.ID, value="single-line-text-form-component-formElement-urn-li-jobs-applyformcommon-easyApplyFormElement-3799104966-108701171-phoneNumber-nationalNumber")
        print(phone.text)
        if phone.text == "":
            phone.send_keys(PHONE)

        # Click Next Button
        time.sleep(3)
        apply_button1 = driver.find_element(by=By.CSS_SELECTOR, value=".artdeco-button")
        apply_button1.click()

        # Click Next Button
        time.sleep(3)
        next_button = driver.find_element(by=By.LINK_TEXT, value="Next")
        next_button.click()

        # Click Review Button
        time.sleep(3)
        review_button = driver.find_element(by=By.LINK_TEXT, value="Review")
        review_button.click()


        # Check the Submit Button
        submit_button = driver.find_element(by=By.CSS_SELECTOR, value="footer button")
        if submit_button.get_attribute("data-control-name") == "continue_unify":
            abort_application()
            print("Complex application, skipped.")
            continue
        else:
            # Click Submit Button
            print("Submitting job application")
            submit_button.click()

        time.sleep(2)
        # Click Close Button
        close_button = driver.find_element(by=By.CLASS_NAME, value="artdeco-modal__dismiss")
        close_button.click()

    except NoSuchElementException:
        abort_application()
        print("No application button, skipped.")
        continue

time.sleep(5)
driver.quit()