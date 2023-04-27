"""
Name: Justin Ho
Brute Force Scraper for court cases given URL access 

Instructions on how to use this scraper in README.md
"""

from selenium import webdriver
from selenium.webdriver.common.by import By
from credentials import url
from selenium.common.exceptions import TimeoutException
import json
import sys

if __name__ == "__main__":

    county = sys.argv[1]
    year = sys.argv[2]
    start = sys.argv[3]
    end = sys.argv[4]

    file_name = str(year) + "_" + county + "_" + str(start) + "_" + str(end) + ".json"

    scraped_cases = {}

    county_code = 1
    if county == "Lancaster":
        county_code = 2

    browser = webdriver.Chrome("./chromedriver")

    for i in range(int(start), int(end) + 1):

        case_id = "CI 0" + str(county_code) + " " + str(year) + "-" + str(i)
        
        print(case_id)

        try:
            browser.get(url)

            browser.find_element(By.ID, "court_type").send_keys("C")
            browser.find_element(By.ID, "county_num").send_keys(county)
            browser.find_element(By.ID, "case_type").send_keys("CI")
            browser.find_element(By.ID, "case_year").send_keys(year)
            browser.find_element(By.ID, "case_id").send_keys(i)

            browser.find_element(By.ID, "search").click()

            content = str(browser.page_source)

            scraped_cases[case_id] = content           

        except TimeoutException as ex:
            print("Timeout! for " + case_id )

    with open("./bfscraped/" + file_name, "w") as outfile:
        json.dump(scraped_cases, outfile)
        
        