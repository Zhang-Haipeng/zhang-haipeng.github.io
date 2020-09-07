---
layout: post
title: Web scraping for making reservations
tags: [Coding Practice]
excerpt_separator: <!--more-->
---

Making a reservation for the driving license knowledge test can be difficult during summer times due to large demands. So I made this python script to monitor and catch available appointments and make automatic reservations. <br>

<!--more-->

The script is far from complete. But while I was still testing its functionalities and debugging some issues, it grabbed me a very nice appointment. LOL <br/>
<br/>

<u> Improvements needed: </u>
* Add docstrings to the functions.
* Break the long workflow into functions. 
* Figure out the bugs that could possibly mess up the workflow. 
* Wonder if it's possible to get it done without using Selenium, which is not efficient. 

```python
# Python3

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
from selenium.webdriver.common.action_chains import ActionChains
import time
import datetime

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# define config dicts and functions
loc_id_dict = {
    'point_grey': "542161df66423009309050c01dcc17f7d1db1ef8e7cea3012331509b79ea6959",
    'east_van': "0ab916058f4b572eae9dfbdf0693fa9f2f97a34a19bee6c68d09cb28b78ac3c3",
    'guildford_surrey': "050a91560b08e8aedfef609cb69e0c41469b56e575f325681f98196495169661",
    'metrotown_burnaby': "e879cd70e75ba8db2fb03b3d2060bf7c1c74e5d879ebea3cc585fd2d707a278d",
    'north_van': "80a96ca1218413463f6601d41d2e97391e2b9da1aadaf033220be663264db0f3",
    'richmond': "b1d4daefba2458c80d880e3931798ef508477d19f6cf1652327459a4a1a27ee3",
    'royal_centre': "ea01f5e5ba07af767a739c1d66730bef9663a1a307b84e4674cffcd93caad1b5",
    'surrey': "d8225a23dd9830e9684fb00f8aea2fff279c892cb1065244aaa0ae05396a0fe2",
}


def change_month(driver, direction="next"):
    if direction=='next':
        button = driver.find_elements_by_xpath("//*[contains(text(), 'chevron_right')]")[0]
    else:
        button = driver.find_elements_by_xpath("//*[contains(text(), 'chevron_left')]")[0]
    
    button.click()
    return

def check_av(driver):
    pg = BeautifulSoup(driver.page_source)
    available_button = "v-btn v-btn--flat v-btn--floating theme--light"
    av_bt_list = pg.findAll("button", {"class": available_button})
    return av_bt_list

def fill_info(driver):
    driver.find_element_by_id('LastName').send_keys('Zhang')
    driver.find_element_by_id('FirstName').send_keys('Haipeng')
    driver.find_element_by_id('DOB').send_keys('my_birthday')
    driver.find_element_by_id('Email').send_keys('my_email')
    driver.find_element_by_id('ConfirmEmail').send_keys('my_email')
    driver.find_element_by_id('Phone').send_keys('my_phone')
    driver.find_element_by_xpath("//input[@type='checkbox']").click()
    driver.find_element_by_id('contactStepCreateAppointmentButton').click()
    return

def month_calendar(driver, month_range={'august':8, 'september':9, 'october':10}):
    pg = BeautifulSoup(driver.page_source)
    
    for x in month_range.keys():
        if x in str.lower(pg.text):
            return month_range[x]

# main function for the workflow
def search_and_book(loc_id_dict, current_month, current_day, current_loc):
    driver = webdriver.Chrome(executable_path=r'/Users/roc/Documents/04-software_dev/02_icbc_reservation/chromedriver')
    url = "https://onlinebusiness.icbc.com/qmaticwebbooking/#/"
    driver.get(url)
    t = 300 # max wait time
    
    WebDriverWait(driver, t).until(
        EC.element_to_be_clickable((By.CLASS_NAME, "v-input--selection-controls__ripple"))
    ).click()
    
    time.sleep(0.5)

    # work-around to select `Single knowledge test`
    actions = ActionChains(driver) 
    actions.send_keys(Keys.TAB)
    actions.send_keys(Keys.ARROW_DOWN)
    actions.perform()
    time.sleep(0.5)

    earliest_day = 1000
    new_finding = 0
    month = 8
    while new_finding == 0:
        for location in loc_id_dict.keys():
            # slecte a location
            driver.find_element_by_id('step2').click()
            WebDriverWait(driver, t).until(
        EC.element_to_be_clickable((By.ID, loc_id_dict[location]))
    ).click()
            
        
            av_bt_list = check_av(driver)
            while (len(av_bt_list) == 0) & (month_calendar(driver) < 11):
                time.sleep(0.5)
                WebDriverWait(driver, t).until(
                    EC.element_to_be_clickable((By.XPATH, "//button[normalize-space()='chevron_right']"))
                ).click()

                av_bt_list = check_av(driver)
                
            
            if len(av_bt_list)>0:
                earliest_day = str(str(av_bt_list[0]).split(">")[2]).split("<")[0]
            
            if ((month_calendar(driver)+1)*100 + int(earliest_day)) > 813:
                if ((month_calendar(driver)+1)*100 + int(earliest_day)) < (current_month*100 + current_day):
                    new_finding = 1
                    current_loc = location
                    current_month = (month_calendar(driver)+1)
                    current_day = int(earliest_day)
                    now = datetime.datetime.now()
                    print (now.strftime("%Y-%m-%d %H:%M:%S"))
                    print("Earlier date found! {}: {}.{}".format(current_loc, current_month, current_day))
            
            n = 1
            while n < 10:
                while month_calendar(driver) > 8:
                    WebDriverWait(driver, t).until(
                            EC.element_to_be_clickable((By.XPATH, "//button[normalize-space()='chevron_left']"))
                        ).click()
                n+=1
            assert month_calendar(driver) == 8


    # if catching ealier choice: make a new reservation
    if new_finding == 1:
        new_finding = 0
        print()
        print("Making a new reservation...")
        driver2 = webdriver.Chrome(executable_path=r'/Users/roc/Documents/04-software_dev/02_icbc_reservation/chromedriver')
        url = "https://onlinebusiness.icbc.com/qmaticwebbooking/#/"
        driver2.get(url)
        t = 300 # max wait time

        WebDriverWait(driver2, t).until(
            EC.element_to_be_clickable((By.CLASS_NAME, "v-input--selection-controls__ripple"))
        ).click()

        time.sleep(0.5)

        # work-around to select `Single knowledge test`
        actions = ActionChains(driver2) 
        actions.send_keys(Keys.TAB)
        actions.send_keys(Keys.ARROW_DOWN)
        actions.perform()
        time.sleep(0.5)

        WebDriverWait(driver2, t).until(
        EC.element_to_be_clickable((By.ID, 'step2'))
    ).click()
        
        WebDriverWait(driver2, t).until(
        EC.element_to_be_clickable((By.ID, loc_id_dict[current_loc]))
    ).click()

        av_bt_list = check_av(driver2)
        while len(av_bt_list) == 0:
            WebDriverWait(driver2, t).until(
        EC.element_to_be_clickable((By.XPATH, "//button[normalize-space()='chevron_right']"))
    ).click()

            av_bt_list = check_av(driver2)

        # click the earliest date
        earliest_day = str(str(av_bt_list[0]).split(">")[2]).split("<")[0]
        xpath = "//button[normalize-space()={}]".format(earliest_day)
        WebDriverWait(driver2, t).until(
        EC.element_to_be_clickable((By.XPATH, xpath))
    ).click()

        # click the earliest time
        WebDriverWait(driver2, t).until(
        EC.element_to_be_clickable((By.ID, "timeButton1"))
    ).click()


        # fill in required information
        time.sleep(2)
        fill_info(driver2)

        WebDriverWait(driver2, t).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "[aria-label='Cancel appointment.']"))
            ).click()

        WebDriverWait(driver2, t).until(
            EC.element_to_be_clickable((By.XPATH, "//button[normalize-space()='Yes']"))
            ).click()

        # confirm new booking
        time.sleep(1)
        WebDriverWait(driver2, t).until(
            EC.element_to_be_clickable((By.XPATH, "//button[normalize-space()='Book your appointment']"))
            ).click()
        time.sleep(10)
        print("New reservation made!!\n{}: {}.{}".format(current_loc, current_month, current_day))
        driver2.quit()
        driver.quit()
        
    return [current_loc, current_month, current_day]



current_month = 8
current_day = 17
# earliest_month = 100
earliest_day = 1000
month = 8
earliest_location = "None"
current_loc = 'surrey'
new_finding = 0

try:
    [current_loc, current_month, current_day] = search_and_book(loc_id_dict, current_month, current_day, current_loc)
except Exception as e:
    print(e)


```
