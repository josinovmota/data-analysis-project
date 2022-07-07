#Download the content
import requests
#Parse 
from bs4 import BeautifulSoup
#Catch the content
from lxml import etree
#Extrair números e símbolos
import re
#Biblioteca spacy
import spacy

#find any white spaces
RE_NORMALIZE_BLANKS = re.compile(r'[\s]+')
RE_CATCH_TITLES = re.compile('TÍTULO')

url = "http://www.planalto.gov.br/ccivil_03/constituicao/ConstituicaoCompilado.htm"
REQUEST_HEADER = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}

#Clean the text
def replace_all_problems(text):
    fim = text.replace("\r\n", " ")
    return fim

#Normalize the text
def normalize_text(s):

    return RE_NORMALIZE_BLANKS.sub(' ', s).strip()

#Request the html
def download_html(url):
    r = requests.get(url, headers=REQUEST_HEADER)

    return r.text

#Split the html in the end of art 250
def remove_pos_normas_centrais(html):

    return html.split("Brasília, 5 de outubro de 1988.")[0]

#Parse the soup
def parse_soup(html):
    soup = BeautifulSoup(html, 'html.parser')
    
    return soup

#Extract the preambulo
def extract_preambulo(parse):
    dom = etree.HTML(str(parse))
    content = replace_all_problems((dom.xpath('/html/body/p[3]/font/small')[0].text))
    dictionary = {"preambulo": str(content)}
    return dictionary

def create_title(soup):
    find = soup.find_all("p", face="Arial")
    return find

    
#Limit of PS
N_PS = 100

#Main function
if __name__ == "__main__":
    html = download_html(url)
    html_preambulo_e_normas_centrais = remove_pos_normas_centrais(html)
    soup = parse_soup(html_preambulo_e_normas_centrais)
    retorno = ""


    for p,i in zip(soup.find_all('p'), range(N_PS)):
        print(normalize_text(p.text))
        print(i)
