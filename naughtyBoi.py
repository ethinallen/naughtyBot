from selenium import webdriver
# from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import time
from sys import argv

file = open('naughtyList.txt','r')
wrongFormat = file.readlines()

# list of words
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
def createDriver():
        driver = webdriver.Firefox()
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

if __name__ == '__main__':

    if len(argv) > 1:
        baseURL = argv[1]
    else:
        print('-~-\\\\ NO URL PROVIDED //-~-')
        exit()
    #creates the naughtyList
    formatList(wrongFormat)

    # starts the driver
    driver = createDriver()

    #Christ, Marge, ya got to give it a rest every now and then so that it can catch up
    time.sleep(3)

    # loops through all of the strings in the list
    # left headed so that way we can watch it :)
    length = len(naughtyList)

    for index, naughtyString in enumerate(naughtyList):
        try:
            string = baseURL + naughtyString
            print('-~- TRYING STRING {} OF {} -~-'.format(index, length))
            driver.get(string)
            # time.sleep(5)
        except:
            driver.close()

    # close the driver out
    driver.close()
