#!user/bin/env python
# -*- coding: utf-8 -*-
#Week 9 
#https://www.cbssports.com/nfl/stats/playersort/nfl/year-2017-season-regular-category-touchdowns

from bs4 import BeautifulSoup
import urllib2

url = urllib2.urlopen('https://www.cbssports.com/nfl/stats/playersort/nfl/year-2017-season-regular-category-touchdowns')
soup = BeautifulSoup(url.read(),'html.parser')
trs = soup.find_all('tr')
name = []
pos = []
team = []
td = []
for tr in trs:

    try:
        if tr.td.has_attr('align'):
            name.append(tr.td.a.get_text())
            pos.append(tr.td.find_next_siblings()\
                       [0].get_text())
            team.append(tr.td.find_next_siblings()\
                       [1].get_text())
            td.append(tr.td.find_next_siblings()\
                       [5].get_text())
    except AttributeError:
        
	continue

for i in range(20):
    print name[i],pos[i],team[i],td[i]

