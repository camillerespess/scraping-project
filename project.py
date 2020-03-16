from selenium import webdriver
from bs4 import BeautifulSoup
import time
import csv

csvfile = open("report_card.csv", 'w', newline='', encoding='utf-8')
c = csv.writer(csvfile)
c.writerow(['jurisdiction', '2019 average score', '2019 basic achievement percantage', '2019 proficiency percentage'])

# load your driver
driver = webdriver.Chrome('/Users/camillerespess/Documents/python/chromedriver')

# get the web page
driver.get('https://www.nationsreportcard.gov/profiles/stateprofile?chort=1&sub=RED&sj=&sfj=NP&st=MN&year=2019R3');

# wait for all the things to load
time.sleep(8)

page = driver.page_source
soup = BeautifulSoup(page, "html.parser")

table = soup.find('tbody')
rows = table.find_all('tr')

for row in rows:
    cells = row.find_all('td')
    try:
        print(cells[0].text)
        print(cells[1].text)
        print(cells[3].text)
        print(cells[4].text)
    except:
        pass

driver.quit()
csvfile.close()
