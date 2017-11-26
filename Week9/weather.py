#!/usr/bin/env python
# -*- coding: utf-8 -*-
#Week 9
#https://www.wunderground.com/history/airport/KNYC/2017/11/11/MonthlyHistory.html

from bs4 import BeautifulSoup
import urllib2


url = urllib2.urlopen('https://www.wunderground.com/history/airport/KNYC/2017/11/11/MonthlyHistory.html')
soup = BeautifulSoup(url.read(),'html.parser')
trs = soup.find_all('tr')

for tr in trs:
    tds = tr.find_all("td")
    span = tr.find_all('span')

    try:  
        date = str(tds[0].get_text())
        high = int(span[0].get_text())
        avg = int(span[1].get_text())
        low = int(span[2].get_text())

    except:
 
        continue 

    print 'date: Nov.',date,'2017 high:',high,'avg:',avg,'low:',low
    
