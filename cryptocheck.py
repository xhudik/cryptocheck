from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import pandas as pd
import numpy as np
import re
import time


options = webdriver.FirefoxOptions()
#options.add_argument('--ignore-certificate-errors')
#options.add_argument("--test-type")
driver = webdriver.Firefox(executable_path='/home/tomas/now/cryptocheck/geckodriver', options=options)

#accept cookies
driver.get("https://www.tradingview.com/symbols/BTCEUR/?exchange=BINANCE")
driver.find_element_by_xpath("//div/div/article/div[2]/div/button").click()

def getGraph(TVurl):
	driver.get(TVurl)
	button3m  = driver.find_element_by_xpath("//div[1]/div/div[2]/div[2]/div[1]/div/div[2]/div/div/div[4]")
	button3m.click()
	graph  = driver.find_element_by_xpath("//div[5]/div/div/div/div/div/div[1]/div")
	return graph


#btceur
btceur = getGraph("https://www.tradingview.com/symbols/BTCEUR/?exchange=BINANCE")
btceur.screenshot("screenshotBTCEUR.png")

#bnbeur
bnbeur = getGraph("https://www.tradingview.com/symbols/BNBEUR/?exchange=BINANCE")
bnbeur.screenshot("screenshotBNBEUR.png")

#bnbbtcdriver.get(
bnbbtc = getGraph("https://www.tradingview.com/symbols/BNBBTC/?exchange=BINANCE")
bnbbtc.screenshot("screenshotBNBBTC.png")




