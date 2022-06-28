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

def replace_all_problems(text):
    fim = text.replace("\r\n", " ")
    return fim

def download_html(url):
    r = requests.get(url, headers=REQUEST_HEADER)
    return r.text

def parse_soup(html):
    soup = BeautifulSoup(html, 'html.parser')
    endelement = soup.find_all("p", string="Brasília, 5 de outubro de 1988. ")
    soup = str(soup)
    uau = soup.split('<p align="justify" style="text-indent: 38px"><font face="Arial" size="2">Brasília, 5 de outubro de 1988. </font></p>')
    soup = BeautifulSoup(uau, 'html.parser')
    print(soup.text)
    return soup

def extract_preambulo(parse):
    dom = etree.HTML(str(parse))
    content = replace_all_problems((dom.xpath('/html/body/p[3]/font/small')[0].text))
    dictionary = {"preambulo": str(content)}
    return dictionary

if __name__ == "__main__":
    html = download_html(url)
    parse = parse_soup(html)

