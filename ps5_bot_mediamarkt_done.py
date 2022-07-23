from random import randrange
import undetected_chromedriver as uc
from selenium import webdriver as wd
import time
import random
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC 
from selenium.common.exceptions import NoSuchElementException


if __name__ == '__main__':
    options = wd.ChromeOptions()
    options.add_argument(r'--user-data-dir=C:\Users\ataka\AppData\Local\Google\Chrome\User Data\Default')

    wd = uc.Chrome(
        options=options
    )
    while True:
        try:
            wd.get('https://www.mediamarkt.de/de/product/_sony-playstationr5-horizon-forbidden-west-gran-turismo-7-2802982.html')
            wd.implicitly_wait(3)
            add_to_cart = wd.find_element(By.XPATH, ' //*[@id="pdp-add-to-cart-button"]').click()
            break
        except NoSuchElementException:
            print('not available')
            print('waiting for 12 sec...')
            time.sleep(12)

  

    # nein danke
    wd.find_element(
        By.XPATH, '//*[@id="mms-app-root"]/div[6]/div[2]/div[2]/div[1]/button'
    ).click()

    random_wait = random.randrange(1, 2)
    time.sleep(random_wait)

    # zum einkaufswagen
    wd.find_element(
        By.XPATH, '//*[@id="mms-app-root"]/div[6]/div[2]/div[3]/div[2]/button'
    ).click()

    random_wait = random.randrange(1, 2)
    time.sleep(random_wait)

    # Lieferung auswählen
    lieferung = wd.find_element(
        By.XPATH, '//*[@id="mms-app-root"]/div[3]/div[1]/div/div/div/div/div[5]/div/div/div[2]/div/div[2]'
    ).click()

    wd.find_element(
        By.XPATH, '//*[@id="mms-styled-modal-header"]/button'
    ).click()
  
    wd.implicitly_wait(1)

    # zur Kasse gehen
    while True:
        try:
            wd.find_element(
                By.XPATH, '//*[@id="continueButtonWrapper"]/div/button'
            ).click()
            break
        except NoSuchElementException:
             wd.implicitly_wait(11)
             print('trying to go to the register...')

    random_wait = random.randrange(1, 2)
    time.sleep(random_wait)

    # Zahlungsmethode Vorkasse
    wd.find_element(
        By.XPATH, '//*[@id="mms-app-root"]/div[3]/div[1]/div/div[2]/div/div[5]/div/div[1]/div[4]/div/div/div/div/div[1]/div/span'
    ).click()
    wd.implicitly_wait(2)
    # Weiter
    while True:
        try:
            wd.find_element(
            By.XPATH, '//*[@id="mms-app-root"]/div[3]/div[1]/div/div[2]/div/div[8]/div/div/div/div/div[4]/div/button'
            ).click()
        except NoSuchElementException:
            wd.implicitly_wait(11)
            print('trying to go weiter...')

    # jetzt kaufen
    while True:
        try:
            wd.find_element(
            By.XPATH, '//*[@id="continueButtonWrapper"]/div/button'
            ).click()
            pass
        except NoSuchElementException:
            wd.implicitly_wait(11)
            print('trying to buy...')
    
   