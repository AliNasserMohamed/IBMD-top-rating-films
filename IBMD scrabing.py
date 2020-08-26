import requests
from bs4 import BeautifulSoup
import csv

csv_file = open("films.csv", "w", encoding="UTF_8")
newcsv_file = open("newfilms.csv", "w", encoding="UTF_8")
fields = ["name", "release_year", "info", "rating"]
new_writer = csv.DictWriter(newcsv_file, fieldnames=fields, delimiter="*")
new_writer.writeheader()
writer = csv.writer(csv_file)
r = requests.get("https://www.imdb.com/chart/top")
soup = BeautifulSoup(r.content, "lxml")
films = soup.findAll("tr")
for film in films:
    info = film.findAll(["th", "td"])[1].find("a")
    release = film.find("span", class_="secondaryInfo")
    rating = film.findAll(["th", "td"])[2].find("strong")
    if info:
        row = []
        name = info.text
        title = info["title"]
        row.append(name)
        row.append(release.text[1:5])
        row.append(title)
        row.append(rating.text)
        writer.writerow(row)
        new_writer.writerow({"name": name, "release_year": release.text[1:5], "info": title, "rating": rating.text})
