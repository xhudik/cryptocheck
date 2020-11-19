#!/usr/bin/env python 

from selenium import webdriver
# from selenium.webdriver.common.keys import Keys
from dominate import document
from dominate.tags import *
# import pandas as pd
# import numpy as np
# import re
from time import strftime
import time


# download gecko driver (from here: https://github.com/mozilla/geckodriver/releases/tag/v0.28.0)


def highlight(element):
    """Highlights (blinks) a Selenium Webdriver element"""
    drivera = element._parent

    def apply_style(s):
        drivera.execute_script("arguments[0].setAttribute('style', arguments[1]);",
                               element, s)

    original_style = element.get_attribute('style')
    apply_style("background: yellow; border: 2px solid red;")
    time.sleep(.3)
    apply_style(original_style)


options = webdriver.FirefoxOptions()
# options.add_argument('--ignore-certificate-errors')
# options.add_argument("--test-type")
options.headless = True
driver = webdriver.Firefox(executable_path='./geckodriver', options=options)

# accept cookies
driver.get("https://www.tradingview.com/symbols/BTCEUR/?exchange=BINANCE")
try:
    driver.find_element_by_xpath("//div/div/article/div[2]/div/button").click()
except Exception as e:
    print(f"No cookies info. {e}")


def getGraph(TVurl):
    driver.get(TVurl)
    print(TVurl)
    time.sleep(2)
    try:
        button3m = driver.find_element_by_xpath("//div[1]/div/div[2]/div[2]/div[1]/div/div[2]/div/div/div[4]")
        button3m.click()
    except Exception as e:
        print(e)

    graph = driver.find_element_by_xpath("//div[5]/div/div/div/div/div/div[1]/div")
    return graph


# btceur
btceur = getGraph("https://www.tradingview.com/symbols/BTCEUR/?exchange=BINANCE")
btceur.screenshot("screenshotBTCEUR.png")

# bnbeur
bnbeur = getGraph("https://www.tradingview.com/symbols/BNBEUR/?exchange=BINANCE")
bnbeur.screenshot("screenshotBNBEUR.png")

# bnbbtcdriver.get(
bnbbtc = getGraph("https://www.tradingview.com/symbols/BNBBTC/?exchange=BINANCE")
bnbbtc.screenshot("screenshotBNBBTC.png")

driver.quit()

doc = document(title='BTC-TrView')
with doc:
    h1(f"TradingView Prices, {strftime('%Y-%m-%d %H:%M')}")
    a(img(src='screenshotBTCEUR.png'), target="_blank",
      href="https://www.tradingview.com/symbols/BTCEUR/?exchange=BINANCE")
    hr()
    a(img(src='screenshotBNBEUR.png'), target="_blank",
      href="https://www.tradingview.com/symbols/BNBEUR/?exchange=BINANCE")
    hr()
    a(img(src='screenshotBNBBTC.png'), target="_blank",
      href="https://www.tradingview.com/symbols/BNBBTC/?exchange=BINANCE")

page = open('stocks.html', 'w')
page.write(doc.render(xhtml=True))
page.close()
