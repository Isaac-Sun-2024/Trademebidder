import time
from bs4 import BeautifulSoup
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By

option = input('option: ')

priceandjunk = []
auctiontime = []

# Setup chrome driver
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

# Navigate to the url
driver.get('https://www.trademe.co.nz/a/marketplace/computers/laptops/laptops/dell/listing/4509630019')

# Find element by Tag Name
if option == '1':
    while True:
        my_div = driver.find_elements(By.TAG_NAME, 'strong')
        for element in my_div:
            priceandjunk = []
            priceandjunk.append(element.text)

        for i in priceandjunk:
            if '$' not in i:
                priceandjunk.pop(i)
        print(priceandjunk)
        time.sleep(3)

elif option == '2':
    while True:
        my_div = driver.find_elements(By.TAG_NAME, 'main')
        for element in my_div:
            auctiontime = []
            yabadaba = element.get_attribute('innerHTML')
            if 'minutes' in yabadaba and 'Closes' in yabadaba:
                soup = BeautifulSoup(yabadaba, 'html.parser')
                text = soup.get_text()
                start_word = "Closes:"
                end_word = "minutes"

                start_index = text.find(start_word)
                end_index = text.find(end_word) + len(end_word)

                # Extract the desired portion of the text
                desired_text = text[start_index:end_index]

                print(desired_text)
            else:
                print('ruh roh raggy, something went wrong!!!!')
                break
        time.sleep(3)