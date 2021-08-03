import requests  # import library untuk scraping
from bs4 import BeautifulSoup  # import library untuk scraping
import csv  # import library untuk menyimpan data ke csv
from requests.api import request  # import library yang diperlukan

data_pegi = []  # buat variabel untuk menampung data hasil scraping

# karena hotel di jogja pada halaman pegi-pegi ada 39 pages
# maka buat perulangan untuk scraping pages 1 sampai pages 39
for i in range(1, 39):
    url = "https://www.pegipegi.com/hotel/jogja/" + \
        str(i)+".html"  # url masing-masing pages
    req = requests.get(url)
    soup = BeautifulSoup(req.text, "html.parser")
    # ambil link masing-masing hotel
    link_hotel = soup.findAll("a", {"itemprop": "url"}, href=True)

    for hotel in link_hotel:  # scrap data masing-masing hotel
        # url hotel adalah href dari hasil scraping elemen link_hotel
        tersedia_kamar = 0
        url_hotel = hotel["href"]
        req_hotel = requests.get(url_hotel)
        soup1 = BeautifulSoup(req_hotel.text, "html.parser")
        nama_hotel = soup1.find("h1", {"itemprop": "name"}).text.strip().replace(
            "/n", "")  # ambil nama hotel
        try:
            # ambil alamat hotel
            alamat = soup1.find("span", {"itemprop": "address"})
        except:
            alamat = ""  # apabila alamat hotel tidak ditemukan
        try:
            # ambil elemen penanda kamar yang tersedia
            kamar = soup1.findAll(
                "img", {"class": "slideShowRoom gm-img-center"})
        except:
            kamar = "0"  # apabila kamar hotel tidak ditemukan
        jumlh_kamar = 0
        for item in kamar:
            jumlh_kamar += 1  # hitung semua jumlah kamar yang ada

        for ktersedia in soup1.findAll("div", {"class": "listContentRoom"}):
            kmr_tsd = soup1.find("div", {"class": "note"}).text.replace(
                "Tersedia", "").replace("kamar lagi !", "").strip()
            kmr_tsd = 0 if kmr_tsd == "Kamar terbatas !" else kmr_tsd
            tersedia_kamar += int(kmr_tsd)
        # masukkan data hasil scraping ke variabel data_pegi
        total_kamar = jumlh_kamar+tersedia_kamar
        data_pegi.append([nama_hotel, alamat, jumlh_kamar, total_kamar])

# siapkan nama kolom untuk data csv
kolom = ["nama_hotel", "alamat_hotel", "jenis_kamar", "total_kamar_tersedia"]
writer = csv.writer(open("hotel_pegi_2.csv", "w", newline="")
                    )  # buat file csv dan nama file
writer.writerow(kolom)

for d in data_pegi:
    writer.writerow(d)  # masukkan data ke file csv yang sudah dibuat
