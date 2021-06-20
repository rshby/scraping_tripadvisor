import requests
import urllib
import requests
from bs4 import BeautifulSoup
import csv

url = "https://www.tripadvisor.com/Attractions-g294230-Activities-a_allAttractions.true-Yogyakarta_Region_Java.html"

req = requests.get(url)
soup = BeautifulSoup(req.content, "html.parser")
data_things_to_do = []

print(req)

for item in soup.findAll("section", {"class": "_3Y-YU9SE _2gl5HHyP"}):
    nama = item.find("div", {"class": "_1gpq3zsA _1zP41Z7X"}).text
    review = item.find(
        "span", {"class": "DrjyGw-P _26S7gyB4 _14_buatE _1dimhEoy"}).text.replace(",", "")
    try:
        deskripsi = item.find(
            "div", {"class": "DrjyGw-P _26S7gyB4 _3SccQt-T"}).text
    except:
        deskripsi = ""
    try:
        single_review = item.find("div", {"class": "_2AdNKb-q"}).find(
            "div", {"class": "DrjyGw-P _26S7gyB4 _3SccQt-T"}).text.replace("\n", " ")
    except:
        single_review = ""

    data_things_to_do.append([nama, deskripsi, single_review, review])

    # save to csv
kolom = ["Nama", "Deskripsi", "Review", "Jumlah_Review"]
writer = csv.writer(open("tripAd_things_to_do.csv", "w", newline=""))
writer.writerow(kolom)

for data in data_things_to_do:
    writer.writerow(data)

print(data_things_to_do)
