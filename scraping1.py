# -*- coding: utf-8 -*-
"""
Created on Wed Jun 16 18:34:15 2021

@author: ROG
"""


import requests
from bs4 import BeautifulSoup
import csv

url = "https://www.tripadvisor.com/Hotels-g294230-Yogyakarta_Region_Java-Hotels.html"

req = requests.get(url)
soup = BeautifulSoup(req.text, "html.parser")

for item in soup.findAll("div", "ui_column is-8 main_col allowEllipsis"):
    nama = item.find("a", "property_title prominent").text.replace("@", "")
    harga = item.find(
        "div", {"data-sizegroup": "mini-meta-price"}).text.replace("IDR", "Rp").replace(",", ".")
    print(f"{nama}, {harga}\n")
