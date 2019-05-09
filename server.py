from bs4 import BeautifulSoup as bs
import pandas as pd
import re
import urllib
import requests

url="http://dataquestio.github.io/web-scraping-pages/simple.html"
obj=requests.get(url)
# print(obj.status_code)
# print(obj.content)
soup = bs(obj.content,'lxml')
# print(soup.prettify())

# list the children of the BeautifulSoup doc
print('Children of the doc')
# print(list(soup.children)[1])
html =list(soup.children)[1]
print(list(html.children))
