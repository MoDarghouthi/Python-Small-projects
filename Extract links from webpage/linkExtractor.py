import requests as rq
from bs4 import BeautifulSoup 

url = input("Enter web page link:")
if ("https" or "http") in url:
    data = rq.get(url)
else:
    data = rq.get("https://" + url)

soup = BeautifulSoup(data.text, "html.parser")

links = []

for link in soup.find_all("a"):
    links.append(link.get("href"))


with open("ExtractedLinks.txt", "a") as saved:
    print(links[:10], file=saved)