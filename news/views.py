from django.shortcuts import render
import requests
from bs4 import BeautifulSoup


n_html = requests.get('https://90tv.ir/news')
n_soup = BeautifulSoup(n_html.content, 'html.parser')
n_heading = n_soup.find_all('h2')
n_news = []
for n_header in n_heading:
    n_news.append(n_header.get_text())


v_html = requests.get('https://www.varzesh3.com/')
v_soup = BeautifulSoup(v_html.content, 'html.parser')
v_heading = v_soup.find_all('li', {'data-filter':{'1', '3'}})
v_news = []
for v_header in v_heading[0:10]:
    v_news.append(v_header.get_text())

def index(request):
    return render(request, 'news/index.html', {'n_news':n_news, 'v_news':v_news})