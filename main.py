#! /usr/bin/env python3

import time
import random
import pyautogui
from selenium import webdriver

def initialize_driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    return driver

def process_links(driver):
    with open('testlinks.txt') as links:
        for link in links:
            time.sleep(random.randint(0,2))
            driver.switch_to.new_window("tab")
            print(f"Loading: {link.rstrip()}...")
            try:
                driver.get(link)
                print(f"Loaded: {link.rstrip()}.")
                pyautogui.press('tab', presses=4)
            except Exception as e:
                print(f"Encountered error:\n{e}")
                pass
            time.sleep(1)

def wait_indefinitely(driver):
    while True:
        time.sleep(86400)

def main():

    driver = initialize_driver()
    process_links(driver)
    wait_indefinitely(driver)
    driver.quit()

if __name__ == "__main__":
    main()
