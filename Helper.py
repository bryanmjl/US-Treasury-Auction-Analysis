# Import libraries
import time
import urllib.request
import xml.etree.ElementTree as ET
from selenium import webdriver
from selenium.webdriver.common.by import By


# Function to webscrape US treasury auction results for BILLS
def get_2022_bills_webscrape(url):
    '''
    :param URL: URL for US treasury auction results main page
    Returns an array of all URLs in XML format to be parsed (len of 232)
    '''

    # A. Select the dropdown box and change it to year 2022 -> Click Submit
    driver = webdriver.Chrome()
    driver.get(url)
    time.sleep(20)  # Let website render and grid table to appear

    driver.find_element(By.ID, "dropdownlistContentjqYearList").click()  # Click on our dropdown box
    time.sleep(20)  # Let website render and grid URL to appear subsequently

    driver.find_element(By.ID, "listitem1innerListBoxjqYearList").click()  # Click on 2nd index year 2022

    driver.find_element(By.ID, "jqButtonYear").click()  # Click submit in our combobox
    time.sleep(20)  # Let website render and 2022 year grid table to appear

    # B. For Bills, we want to expand on all terms and click on all the links, etc and save it to an array
    bill_URLs = []                                                                 # A list to store all URLs
    driver.find_element(By.XPATH, '//*[@id="row0jqxGrid"]/div[1]').click()         # Click onto Bill and expand everything out
    time.sleep(20)  # Let website render and jqxgrid to expand

    # Click onto 4 week Bill Term and expand -> download row2jqxgrid to row53jqxgrid
    driver.find_element(By.XPATH, '//*[@id="row1jqxGrid"]/div[2]').click()         # Click onto Bill Term: 4-week to expand
    for i in range(2, 53+1):
        targetID = "row" + str(i) + "jqxGrid"
        div_element = driver.find_element(By.ID, targetID)
        anchor_element = div_element.find_elements(By.TAG_NAME, "a")[4]
        href = anchor_element.get_attribute('href')
        bill_URLs.append(href)
    time.sleep(15)

    # Click onto 8 week Bill Term and expand -> download row55jqxgrid to row106jqxgrid
    driver.find_element(By.XPATH, '//*[@id="row54jqxGrid"]/div[2]').click()         # Click onto Bill Term: 8-week to expand
    for i in range(55, 106+1):
        targetID = "row" + str(i) + "jqxGrid"
        div_element = driver.find_element(By.ID, targetID)
        anchor_element = div_element.find_elements(By.TAG_NAME, "a")[4]
        href = anchor_element.get_attribute('href')
        bill_URLs.append(href)
    time.sleep(15)

    # Click onto 17 week Bill Term and expand -> download row108jqxgrid to row118jqxgrid
    driver.find_element(By.XPATH, '//*[@id="row107jqxGrid"]/div[2]').click()         # Click onto Bill Term: 17-week and expand everything out
    for i in range(108, 118+1):
        targetID = "row" + str(i) + "jqxGrid"
        div_element = driver.find_element(By.ID, targetID)
        anchor_element = div_element.find_elements(By.TAG_NAME, "a")[4]
        href = anchor_element.get_attribute('href')
        bill_URLs.append(href)
    time.sleep(15)

    # Click onto 13 week Bill Term and expand -> download row120jqxgrid to row171jqxgrid
    driver.find_element(By.XPATH, '//*[@id="row119jqxGrid"]/div[2]').click()         # Click onto Bill Term: 13-week to expand
    for i in range(120, 171+1):
        targetID = "row" + str(i) + "jqxGrid"
        div_element = driver.find_element(By.ID, targetID)
        anchor_element = div_element.find_elements(By.TAG_NAME, "a")[4]
        href = anchor_element.get_attribute('href')
        bill_URLs.append(href)
    time.sleep(15)

    # Click onto 26 week Bill Term and expand -> download row173jqxgrid to row224jqxgrid
    driver.find_element(By.XPATH, '//*[@id="row172jqxGrid"]/div[2]').click()         # Click onto Bill Term: 26-week to expand
    for i in range(173, 224+1):
        targetID = "row" + str(i) + "jqxGrid"
        div_element = driver.find_element(By.ID, targetID)
        anchor_element = div_element.find_elements(By.TAG_NAME, "a")[4]
        href = anchor_element.get_attribute('href')
        bill_URLs.append(href)
    time.sleep(15)

    # Click onto 52 week Bill Term and expand -> download row226jqxgrid to row238jqxgrid
    driver.find_element(By.XPATH, '//*[@id="row225jqxGrid"]/div[2]').click()         # Click onto Bill Term: 52-week to expand
    for i in range(226, 238+1):
        targetID = "row" + str(i) + "jqxGrid"
        div_element = driver.find_element(By.ID, targetID)
        anchor_element = div_element.find_elements(By.TAG_NAME, "a")[4]
        href = anchor_element.get_attribute('href')
        bill_URLs.append(href)

    # C. Return our output BILL_URLS
    return bill_URLs


# Function to webscrape US treasury auction results for BILLS
def get_2022_notes_webscrape(url):
    '''
    :param URL: URL for US treasury auction results main page
    Returns an array of all URLs in XML format to be parsed (len of 49)
    '''

    # A. Select the dropdown box and change it to year 2022 -> Click Submit:
    driver = webdriver.Chrome()
    driver.get(url)
    time.sleep(20)  # Let website render and grid table to appear

    driver.find_element(By.ID, "dropdownlistContentjqYearList").click()  # Click on our dropdown box
    time.sleep(20)  # Let website render and grid URL to appear subsequently

    driver.find_element(By.ID, "listitem1innerListBoxjqYearList").click()  # Click on 2nd index year 2022

    driver.find_element(By.ID, "jqButtonYear").click()  # Click submit in our combobox
    time.sleep(20)  # Let website render and 2022 year grid table to appear

    # B. For Notes, we want to expand on all terms and click on all the links, etc and save it to an array
    note_URLs = []                                                                 # A list to store all URLs
    driver.find_element(By.XPATH, '//*[@id="row1jqxGrid"]/div[1]').click()         # Click onto Note and expand everything out
    time.sleep(20)  # Let website render and jqxgrid to fully expand

    # Click onto 7 year Note and expand -> download row3jqxgrid to row14jqxgrid
    driver.find_element(By.XPATH, '//*[@id="row2jqxGrid"]/div[2]').click()         # Click onto Note Term: 7-year to expand
    for i in range(3, 14+1):
        targetID = "row" + str(i) + "jqxGrid"
        div_element = driver.find_element(By.ID, targetID)
        anchor_element = div_element.find_elements(By.TAG_NAME, "a")[4]
        href = anchor_element.get_attribute('href')
        note_URLs.append(href)
    time.sleep(15)

    # Click onto 5 year Note and expand -> download row16jqxgrid to row27jqxgrid
    driver.find_element(By.XPATH, '//*[@id="row15jqxGrid"]/div[2]').click()         # Click onto Note Term: 5-year to expand
    for i in range(16, 27+1):
        targetID = "row" + str(i) + "jqxGrid"
        div_element = driver.find_element(By.ID, targetID)
        anchor_element = div_element.find_elements(By.TAG_NAME, "a")[4]
        href = anchor_element.get_attribute('href')
        note_URLs.append(href)
    time.sleep(15)

    # Click onto 2 year Note and expand -> download row29jqxgrid to row40jqxgrid
    driver.find_element(By.XPATH, '//*[@id="row28jqxGrid"]/div[2]').click()         # Click onto Note Term: 5-year to expand'
    for i in range(29, 40+1):
        targetID = "row" + str(i) + "jqxGrid"
        div_element = driver.find_element(By.ID, targetID)
        anchor_element = div_element.find_elements(By.TAG_NAME, "a")[4]
        href = anchor_element.get_attribute('href')
        note_URLs.append(href)
    time.sleep(15)

    # Click onto 3 year Note and expand -> download row42jqxgrid to row53jqxgrid
    driver.find_element(By.XPATH, '//*[@id="row41jqxGrid"]/div[2]').click()         # Click onto Note Term: 5-year to expand
    for i in range(42, 53+1):
        targetID = "row" + str(i) + "jqxGrid"
        div_element = driver.find_element(By.ID, targetID)
        anchor_element = div_element.find_elements(By.TAG_NAME, "a")[4]
        href = anchor_element.get_attribute('href')
        note_URLs.append(href)
    time.sleep(15)

    # Click onto 10 year Note and expand -> download row55jqxgrid to row66jqxgrid
    driver.find_element(By.XPATH, '//*[@id="row54jqxGrid"]/div[2]').click()         # Click onto Note Term: 5-year to expand
    for i in range(55, 66+1):
        targetID = "row" + str(i) + "jqxGrid"
        div_element = driver.find_element(By.ID, targetID)
        anchor_element = div_element.find_elements(By.TAG_NAME, "a")[4]
        href = anchor_element.get_attribute('href')
        note_URLs.append(href)

    # C. Return our output NOTE_URLs
    return note_URLs


# Create function to parse all bills and notes of various maturities
def parse_xml(url):
    '''
    :param URL: URL for US treasury auction results XML data
    Returns a dictionary of auctionresults and auctionannouncements
    '''

    # Download the XML data URL link
    response = urllib.request.urlopen(url, timeout=10)
    xml_data = response.read()

    # Parse the XML data as tree structures - 2 child tags auction announcement and auction results
    root = ET.fromstring(xml_data)

    # Get auction announcement first
    auction_announcement = {}
    for i in root.find(root[0].tag):
        auction_announcement[i.tag] = i.text

    # Get auction_results next
    auction_results = {}
    for i in root.find(root[1].tag):
        auction_results[i.tag] = i.text
    
    # Return a union of auction announcement and auction results dictionaries
    return dict(auction_announcement.items() | auction_results.items())
