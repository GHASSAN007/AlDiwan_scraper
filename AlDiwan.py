import requests , csv
from bs4 import BeautifulSoup as bs 
from itertools import zip_longest


urls = ["https://www.aldiwan.net/Poems-Topics-%D8%A7%D8%B9%D8%AA%D8%B0%D8%A7%D8%B1.html",]
links = []
poetry_titles = []
poetries = []
writers = []
lines = []

for url in urls:

    result = requests.get(url)

    scr = result.content

    soup = bs(scr , "lxml")

    poetry_title = soup.find_all("div" ,{"class":"record col-12"})

for i in range(len(poetry_title)):
    poetry_titles.append(poetry_title[i].text)
    links.append(poetry_title[i].find("a").attrs["href"])

for link in links :
    
    result = requests.get("https://www.aldiwan.net/"+link)
    scr = result.content
    soup = bs(scr , "lxml")

    poetry = soup.find("div" , {"class":"bet-1 row pt-0 px-5 pb-4 justify-content-center"})
    writer = soup.find("h2" , {"class":"text-center h3 mt-3"})
    line = soup.find("p" , {"class" , "d-inline-block px-2 mt-0 mb-1 poem-control main-color"})
    poetries.append(poetry.text)
    writers.append(writer.text)
    try :
        lines.append(line.text)
    except AttributeError: 
        print("TypeError: Check list of indices")
        


data = [urls , poetry_titles , poetries , writers , lines]
exported_data = zip_longest(*data)

with open("poetry.csv" , 'w') as data_file :
    write = csv.writer(data_file)
    write.writerow(["url" , "poetry title" , "poetries" ,"writer" , "number of lines"])
    write.writerows(exported_data)
