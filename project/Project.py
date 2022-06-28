
#Download the content
import requests
#Parse 
from bs4 import BeautifulSoup
#Catch the content
from lxml import etree
#Extrair números e símbolos
import re
#Biblioteca spacy


RE_NORMALIZE_BLANKS = re.compile(r'[\s]+')

url = "http://www.planalto.gov.br/ccivil_03/constituicao/ConstituicaoCompilado.htm"
REQUEST_HEADER = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}

def replace_all_problems(text):
    fim = text.replace("\r\n", " ")
    return fim


def normalize_text(s):

    return RE_NORMALIZE_BLANKS.sub(' ', s).strip()


def download_html(url):
    r = requests.get(url, headers=REQUEST_HEADER)

    return r.text

def remove_pos_normas_centrais(html):

    return html.split("Brasília, 5 de outubro de 1988.")[0]

def parse_soup(html):
    soup = BeautifulSoup(html, 'html.parser')
    
    return soup

def extract_preambulo(parse):
    dom = etree.HTML(str(parse))
    content = replace_all_problems((dom.xpath('/html/body/p[3]/font/small')[0].text))
    dictionary = {"preambulo": str(content)}
    return dictionary

N_PS = 20

if __name__ == "__main__":
    html = download_html(url)
    html_preambulo_e_normas_centrais = remove_pos_normas_centrais(html)
    parsed = parse_soup(html_preambulo_e_normas_centrais)