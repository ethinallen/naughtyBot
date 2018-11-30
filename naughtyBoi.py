from selenium import webdriver
# from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import time

#url of the site that you want to test
url = 'https://www.surveyfactory.com/account?'

#list of the xpaths that need to have strings entered into them
fieldPathList = [
'/html/body/table/tbody/tr/td/table[2]/tbody/tr/td/table[2]/tbody/tr[2]/td/table/tbody/tr[5]/td/table/tbody/tr/td/form/table/tbody/tr[1]/td[2]/input',
'/html/body/table/tbody/tr/td/table[2]/tbody/tr/td/table[2]/tbody/tr[2]/td/table/tbody/tr[5]/td/table/tbody/tr/td/form/table/tbody/tr[2]/td[2]/table/tbody/tr/td[1]/input'
]

#the xpath of the button that submits the fields
submitPath = '//*[@id="buttonlogin"]'

file = open('naughtyList.txt','r')
wrongFormat = file.readlines()

naughtyList = []

# formats
def formatList(wrongFormat):
    for wordLine in wrongFormat:
        length = len(wordLine)
        if length > 4:
            fword = wordLine[1:length-3]
        else:
            fword = ''
        naughtyList.append(fword)
    return naughtyList

# starts the driver
def createDriver(url):
        driver = webdriver.Firefox(executable_path='/home/drew/geckodriver')
        driver.get(url)
        return driver

# submits a given naughtyString
def chaos(url, driver, fieldPathList, naughtyString):
    time.sleep(.5)
    for fieldPath in fieldPathList:
        driver.find_element_by_xpath(fieldPath).clear()
        submitField = driver.find_element_by_xpath(fieldPath)
        submitField.send_keys(naughtyString)
    submitButton = driver.find_element_by_xpath(submitPath)
    submitButton.click()

#creates the naughtyList
formatList(wrongFormat)

# starts the driver
driver = createDriver(url)

#Christ, Marge, ya got to give it a rest every now and then so that it can catch up
time.sleep(3)

# loops through all of the strings in the list
# left headed so that way we can watch it :)
for naughtyString in naughtyList:
    print('Entering string: ' + naughtyString)
    chaos(url, driver, fieldPathList, naughtyString)
    time.sleep(.5)
