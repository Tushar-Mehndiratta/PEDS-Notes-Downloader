import os
import time
from selenium import webdriver


def download_notes_from_PEDS(user_id, pass_id, download_location):
    chrome_options = webdriver.ChromeOptions()
    prefs = {'download.default_directory': download_location}
    chrome_options.add_experimental_option('prefs', prefs)

    driver = webdriver.Chrome(chrome_options=chrome_options)

    URL = "http://peds.pdm.ac.in/"
    driver.get(URL)

    username = driver.find_element_by_id("username")
    username.clear()
    username.send_keys(user_id)

    password = driver.find_element_by_id("password")
    password.clear()
    password.send_keys(pass_id)

    driver.find_element_by_class_name("link1").click() # Login to PEDS
    driver.find_element_by_link_text("Notes").click()

    for i in range(2, 159):
        if i > 2 and (i-2) % 10 == 0:
            driver.find_element_by_xpath('//*[@id="pageNavPosition1"]/tbody/tr/td/span[18]').click()
        else:
            pass
        driver.find_element_by_xpath(f'//*[@id="results1"]/tbody/tr[{i}]/td[5]/a').click()

    # Wait until download is complete.
    while any([filename.endswith(".crdownload") for filename in os.listdir(download_location)]):
        time.sleep(5)


USER_ID = str(input("What is your PEDS Login ID? "))
PASS_ID = str(input("What is your PEDS Login Password"))
Location = str(input("Where do you want to Save your files? Please Enter FULL PATH..."))

download_notes_from_PEDS(USER_ID, PASS_ID, Location)
