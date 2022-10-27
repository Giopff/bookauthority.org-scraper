from selenium import webdriver
import requests
from bs4 import BeautifulSoup
import time
import shutil
import os


def download(image_url):
    filename = item.find('h2', class_='main').text  # image_url.split("/")[-1]

    r = requests.get(image_url, stream=True)

    if r.status_code == 200:
        r.raw.decode_content = True

        with open("data\\"+filename+".jpg", 'wb') as f:
            shutil.copyfileobj(r.raw, f)

        print('Image sucessfully Downloaded: ', filename)
    else:
        print('Image Couldn\'t be retreived')


browser = webdriver.Chrome()
url = 'https://bookauthority.org/books/best-business-books'  # enter url here
sada = browser.get(url)
time.sleep(10)

os.mkdir("data")
source = browser.page_source
soup = BeautifulSoup(source, 'html.parser')
with open("data\\Data.txt", 'w') as f:
    for item in soup.findAll('div', attrs={'class': 'book'}):
        img = item.find('img', class_='book-cover')
        download(img['src'])
        author = item.find('h3', class_='authors').text
        title = item.find('h2', class_='main').text
        f.write(f"{author}\n{title}\n\n")
        print("\n \n")
