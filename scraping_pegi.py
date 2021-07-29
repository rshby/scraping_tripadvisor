import requests
from bs4 import BeautifulSoup
import csv
from requests.api import request

data_pegi = []

for i in range(1, 39):
    url = "https://www.pegipegi.com/hotel/jogja/"+str(i)+".html"
    req = requests.get(url)
    soup = BeautifulSoup(req.text, "html.parser")
    link_hotel = soup.findAll("a", {"itemprop": "url"}, href=True)

    for hotel in link_hotel:
        url_hotel = hotel["href"]
        req_hotel = requests.get(url_hotel)
        soup1 = BeautifulSoup(req_hotel.text, "html.parser")
        nama_hotel = soup1.find(
            "h1", {"itemprop": "name"}).text.strip().replace("/n", "")
        try:
            alamat = soup1.find("span", {"itemprop": "address"})
        except:
            alamat = ""
        try:
            kamar = soup1.findAll(
                "img", {"class": "slideShowRoom gm-img-center"})
        except:
            kamar = "0"
        jumlh_kamar = 1
        for item in kamar:
            jumlh_kamar += 1
        data_pegi.append([nama_hotel, alamat, jumlh_kamar])


kolom = ["nama_hotel", "alamat_hotel", "jumlah_kamar"]
writer = csv.writer(open("hotel_pegi.csv", "w", newline=""))
writer.writerow(kolom)

for d in data_pegi:
    writer.writerow(d)
