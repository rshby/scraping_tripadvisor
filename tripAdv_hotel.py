import requests  # import library yang digunakan
from bs4 import BeautifulSoup  # import library yang digunakan
import csv  # import library yang digunakan untuk menyimpan file ke csv

# url yang akan discraping
url = "https://www.tripadvisor.com/Hotels-g294230-Yogyakarta_Region_Java-Hotels.html"

req = requests.get(url)  # buat variabel req untuk load url
# buat variabel soup untuk menggunakan BeautifulSoup pada url yang akan discraping
soup = BeautifulSoup(req.text, "html.parser")
data_hotel = []  # buat list kosong untuk menampung data hotel

# buat perulangan untuk mengambil elemen yang akan discraping
for item in soup.findAll("div", "ui_column is-8 main_col allowEllipsis"):
    nama = item.find("a", "property_title prominent").text.replace(
        "@", "").strip()  # scrap/ambil elemen yang berisi informasi nama hotel
    harga = item.find("div", {"data-sizegroup": "mini-meta-price"}).text.replace(
        "IDR", "").replace(",", "")  # ambil elemen yang berisi informasi harga hotel
    jumlah_review = item.find("a", "review_count").text.replace("reviews", "").replace(
        "review", "")  # ambil elemen yang berisi informasi jumlah review

    # masukkan data yang discrap ke list variabel data_hotel
    data_hotel.append([nama, harga, jumlah_review])

# save to csv
kolom = ["Nama", "Harga", "Review"]  # buat nama kolom
# buat file csv (nama: tripAd.csv)
writer = csv.writer(open("tripAd.csv", "w", newline=""))
writer.writerow(kolom)  # untuk membuat kolom dan nama kolom dalam file csv

for d in data_hotel:  # buat perulangan untuk mengambil data di dalam list data_hotel
    # masukkan data yang ada di dalam data_hotel ke dalam file csv yang sudah dibuat
    writer.writerow(d)

print(data_hotel)  # tampilkan data yang sudah discraping
