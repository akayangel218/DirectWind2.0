# Data Collector
from selenium import webdriver
from BeautifulSoup import BeautifulSoup
import pandas as pd


# Path to the chromedriver
driver = webdriver.Chrome("/usr/lib/chromium-browser/chromedriver")

# VIA Rail
d = [] # Date
p = [] # Price
driver.get(<a href="https://reservia.viarail.ca/search/">"https://reservia.viarail.ca/search/tripresult.aspx?t=D&from=bc")

