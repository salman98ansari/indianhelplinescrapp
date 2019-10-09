#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct  9 18:00:58 2019

@author: salman
"""

from selenium import webdriver
from bs4 import BeautifulSoup
import requests
url= requests.get('https://indianhelpline.com/ARUNACHAL-PRADESH/').text

soup = BeautifulSoup(url, 'lxml')
table= soup.findAll('tr')
#print(table[42])
file =open('andhrapradesh.csv','w')
header=' Name , Number\n'
file.write(header)
for td in table[42: ]:
    try:
        tr = td.findAll('td')
        name = tr[0].text
        number = tr[1].text
        print(name, number)
    except:
        pass 
    file.write(name.replace(',','') + ',' + number.replace(',','|')+ '\n')
file.close()

