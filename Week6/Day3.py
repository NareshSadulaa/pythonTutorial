# Web Scraping in Python

# import os
# import requests
# from bs4 import BeautifulSoup
#
# url = "https://www.fcbarcelona.com/en/"
# data = requests.get(url)
# d = BeautifulSoup(data.text, "html.parser")
# u = d.findAll('link')
# print(u)

# from os import makedirs
#
# import requests
# from bs4 import BeautifulSoup
#
# url = "https://www.fcbarcelona.com/en/"
# data = requests.get(url)
# soup = BeautifulSoup(data.content, 'html.parser')
# d = soup.findAll('img')
# c = 1
# for i in d:
#     makedirs('img_name')
#     img_name = i.get('src')
#     file = open(img_name,'wb')
#     file.write(requests.get('img').content)
#     c+=1
#     print(file)

# import os
# import requests
# from bs4 import BeautifulSoup
#
# url = "https://www.chess.com/"
# response = requests.get(url)
# soup = BeautifulSoup(response.content, "html.parser")
# c = 1
# for item in soup.find_all('img'):
#     os.makedirs('images', exist_ok=True)
#     file = open('images','wb')
#     file.write(item['src'])
#     c += 1
#     print(c)

import requests
from bs4 import BeautifulSoup
import os
from urllib.parse import urljoin

website_url = 'https://stock.adobe.com/in/search?k=mahadev'
web_response = requests.get(website_url)

soup = BeautifulSoup(web_response.text, "html.parser")

os.makedirs('img', exist_ok=True)
value01 = 1

for item in soup.find_all('img'):
    img_src = item.get('src')
    if not img_src:
        continue  # Skip if src is missing

    # Handle relative URLs
    img_url = urljoin(website_url, img_src)

    try:
        img_data = requests.get(img_url).content
        with open(f'img/{value01}.jpg', 'wb') as f:
            f.write(img_data)
        value01 += 1
    except Exception as e:
        print(f"Failed to download {img_url}: {e}")