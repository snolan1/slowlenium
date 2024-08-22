#! /usr/bin/env python3

import time
import random
import pyautogui
from selenium import webdriver

def initialize_driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    return driver

def install_vimium(driver):
    driver.get("https://chromewebstore.google.com/detail/vimium/dbepggeogbaibhgnhhndojpepiihcmeb?hl=en")

    time.sleep(1)
    pyautogui.press('tab', presses=10)
    time.sleep(1)
    pyautogui.press('enter', presses=1)
    time.sleep(1)
    pyautogui.press('tab', presses=1)
    time.sleep(1)
    pyautogui.press('enter', presses=1)
    time.sleep(5)
    pyautogui.press('tab', presses=1)
    time.sleep(1)
    pyautogui.press('enter', presses=1)
    time.sleep(1)

def install_ublock_origin(driver):
    driver.get(" https://chromewebstore.google.com/detail/ublock-origin/cjpalhdlnbpafiamejdnhcphjbkeiagm?hl=en")

    time.sleep(5)
    pyautogui.press('tab', presses=9)
    time.sleep(1)
    pyautogui.press('enter', presses=1)
    time.sleep(1)
    pyautogui.press('tab', presses=1)
    time.sleep(1)
    pyautogui.press('enter', presses=1)
    time.sleep(5)
    pyautogui.press('tab', presses=1)
    time.sleep(1)
    pyautogui.press('enter', presses=1)
    time.sleep(1)

def process_links(driver, link_set='testlinks.txt'):
    # TODO factor out magic file here
    with open(link_set) as links:
        for link in links:
            # TODO factor out magic numbers here
            time.sleep(random.randint(0,2))
            driver.switch_to.new_window("tab")
            print(f"Loading: {link.rstrip()}...")
            try:
                driver.get(link)
                print(f"Loaded: {link.rstrip()}.")
                pyautogui.press('tab', presses=4)
            # Connection refused, etc
            except Exception as e:
                print(f"Encountered error:\n{e}")
                pass
            time.sleep(1)

def wait_indefinitely(driver):
    while True:
        time.sleep(86400)

def main():

    driver = initialize_driver()
    install_vimium(driver)
    install_ublock_origin(driver)
    #process_links(driver, './link_sets/group2.html')
    process_links(driver)
    wait_indefinitely(driver)
    driver.quit()

if __name__ == "__main__":
    main()
