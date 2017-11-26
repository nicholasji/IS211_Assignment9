#!/usr/bin/env python
# -*- coding: utf-8 -*-
#Week 9
#https://finance.yahoo.com/quote/AAPL/history?p=AAPL

from bs4 import BeautifulSoup
import urllib2


url = urllib2.urlopen('https://finance.yahoo.com/quote/AAPL/history?p=AAPL')
soup = BeautifulSoup(url.read(),'html.parser')
trs = soup.find_all('tr')

for tr in trs:
    tds = tr.find_all("td")

    try:  
        date = str(tds[0].get_text())  
        close_price = str(tds[4].get_text())

    except:
      
        continue  
    print 'Apple closed at',close_price, 'on', date
