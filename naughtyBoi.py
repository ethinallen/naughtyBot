from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import time

#specify the path to the driver
pathToDriver = '/home/drew/geckodriver'

url = 'http://cgi.resourceindex.com/'
fieldPathList = [
'/html/body/div/div[2]/div[1]/div[1]/div/form/input'
]

submitPath = '/html/body/div/div[2]/div[1]/div[1]/div/form/span/input'

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
        driver = webdriver.Firefox(executable_path=pathToDriver)
        driver.get(url)
        return driver

# submits a given naughtyString
def sendString(url, driver, fieldPathList, naughtyString):
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
    sendString(url, driver, fieldPathList, naughtyString)
    time.sleep(.5)
