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
data_hotel = []

for item in soup.findAll("div", "ui_column is-8 main_col allowEllipsis"):
    nama = item.find("a", "property_title prominent").text.replace(
        "@", "").strip()
    harga = item.find(
        "div", {"data-sizegroup": "mini-meta-price"}).text.replace("IDR", "").replace(",", "")
    jumlah_review = item.find("a", "review_count").text.replace(
        "reviews", "").replace("review", "")
    data_hotel.append([nama, harga, jumlah_review])
    print(f"Harga: {harga}\n")

# save to csv
kolom = ["Nama", "Alamat", "Review"]
writer = csv.writer(open("tripAd.csv", "w", newline=""))
writer.writerow(kolom)

for d in data_hotel:
    writer.writerow(d)

print(data_hotel)
