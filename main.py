#! /usr/bin/env python3

from selenium import webdriver

import time

def initialize_driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    return driver

def wait_indefinitely(driver):
    while True:
        time.sleep(86400)

def main():

    driver = initialize_driver()
    wait_indefinitely(driver)
    driver.quit()

if __name__ == "__main__":
    main()
