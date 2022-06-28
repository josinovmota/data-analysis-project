#Download the content
import requests
#Parse 
from bs4 import BeautifulSoup
#Catch the content
from lxml import etree
#Extrair números e símbolos
import re


url = "http://www.planalto.gov.br/ccivil_03/constituicao/ConstituicaoCompilado.htm"
REQUEST_HEADER = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}

def download_html(url):
    r = requests.get(url, headers=REQUEST_HEADER)
    return r.text

def parse_soup(html):
    soup = BeautifulSoup(html, 'html.parser')
    return soup

def extrair_preambulo(parse):
    dom = etree.HTML(str(parse))
    print(dom.xpath('/html/body/p[3]/font/small')[0].text)

if __name__ == "__main__":
    html = download_html(url)
    parse = parse_soup(html)



    
    