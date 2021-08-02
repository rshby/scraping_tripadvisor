import requests  # import library request untuk melakukan get url
from bs4 import BeautifulSoup  # import library BeautifulSoup untuk scraping website
import csv  # import library csv untuk menyimpan data scrpaing ke file csv

# url yang akan discraping
url = "https://www.tripadvisor.com/Attractions-g294230-Activities-a_allAttractions.true-Yogyakarta_Region_Java.html"

req = requests.get(url)  # untuk request atau load url yang akan discraping
# buat variabel soup untuk scraping dan meminta html.parser pada url yang akan discraping
soup = BeautifulSoup(req.content, "html.parser")
# buat list kosong dengan nama data_things_to_do untuk menampung hasil scraping
data_things_to_do = []

print(req)  # untuk cek apakan request telah berhasil

# buat perulangan untuk mengambil semua elemen yang menampung data kegiatan
for item in soup.findAll("section", {"class": "_3Y-YU9SE _2gl5HHyP"}):
    # ambil atau scrap elemen yang menampung informasi nama kegiatan
    nama = item.find("div", {"class": "_1gpq3zsA _1zP41Z7X"}).text
    review = item.find(
        "span", {"class": "DrjyGw-P _26S7gyB4 _14_buatE _1dimhEoy"}).text.replace(",", "")  # ambil elemen yang berisi informasi tentang review kegiatan
    try:
        deskripsi = item.find(
            "div", {"class": "DrjyGw-P _26S7gyB4 _3SccQt-T"}).text  # ambil elemen yang berisi tentang deskripsi kegiatan
    except:
        deskripsi = ""  # jika deskripsi tidak ada, maka diisi NaN value
    try:
        single_review = item.find("div", {"class": "_2AdNKb-q"}).find(
            "div", {"class": "DrjyGw-P _26S7gyB4 _3SccQt-T"}).text.replace("\n", " ")  # ambil elemen yang berisi informasi tentang review kegitatan
    except:
        single_review = ""  # jika tidak ada review maka diisi dengan NaN value

    # masukkan data yang sudah discraping ke dalam list kosong yang dibuat tadi
    data_things_to_do.append([nama, deskripsi, single_review, review])

    # save to csv
# buat nama untuk header kolom
kolom = ["Nama", "Deskripsi", "Review", "Jumlah_Review"]
# buat file csv yang akan digunakan untuk menyimpan data hasil scraping
writer = csv.writer(open("tripAd_things_to_do.csv", "w", newline=""))
writer.writerow(kolom)  # tuliskan header kolom ke dalam file csv tersebut

for data in data_things_to_do:  # buat perulangan untuk mengambil semua data yang ada di list data_things_to_do
    writer.writerow(data)  # masukkan data ke dalam file csv yang telah dibuat

print(data_things_to_do)  # tampilkan data yang sudah kita scraping
