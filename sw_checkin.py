#!/usr/bin/env python

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

def check(num,fname,lname):
    browser = webdriver.Firefox()
    browser.get("https://www.southwest.com/")

    checkIn = browser.find_element_by_xpath('//*[@id="booking-form--check-in-tab"]')
    checkIn.click()

    inputElement = browser.find_element_by_id("confirmationNumber")
    inputElement.send_keys(num)

    inputElement = browser.find_element_by_id("firstName")
    inputElement.send_keys(fname)

    inputElement = browser.find_element_by_id("lastName")
    inputElement.send_keys(lname)

    checkIn = browser.find_element_by_xpath('//*[@id="jb-button-check-in"]')
    checkIn.click()

    checkIn = browser.find_element_by_xpath('//*[@id="printDocumentsButton"]')
    checkIn.click()

check('RLMQOS','Colin','Socha')
