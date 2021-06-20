import urllib
import requests
from bs4 import BeautifulSoup
import csv

from requests.api import get

url_imdb = get("https://www.imdb.com/chart/moviemeter/?ref_=nv_mv_mpm")

req = url_imdb.text
soup = BeautifulSoup(req, "html.parser")
data_film = []

movies = soup.findAll("div", {"class": "col-xs-12 col-md-6"})
print(movies)


"""for film in soup.findAll("div", {"class": "col-xs-12 col-md-6"}):
    image = film.find(
        "span", "pull-left poster-wrap ribbonize")  # .find("a").find("img")["src"]
    judul = film.find(
        "span", "media-body media-vertical-align").find("h4").text
    print(judul)
"""
