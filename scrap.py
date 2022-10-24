from bs4 import BeautifulSoup
import re


def scrap_falabella(html_doc):
    soup = BeautifulSoup(html_doc, 'html.parser')
    #print(soup.prettify())
    
    divs_products = soup.find_all('div',class_="jsx-4001457643")
    info_products = []
    for div in divs_products:
        info_products.append(convert_element_div(div))
    
    #primer_element = soup.find(id=id_primer_elemento)
    #print(primer_element)
    return info_products
    
    

def convert_element_div(element):
    title_element = element.find('a',class_="jsx-1327784995")

    #print(title_element.text)
    div_element = element.find('div',class_="jsx-1327784995")

    
    category_element = element.find('b',class_="jsx-1327784995")
    #print(category_element.text)
    # Este es el enlace de la pagina
    div_price_element = div_element.find('div',["jsx-2797633547"])
    span_price_element = div_price_element.find('span')
    #print(span_price_element)
    
    a_element = element.find('a',class_="jsx-3128226947")
    img_element = a_element.find('img',class_="jsx-3128226947")
    print(img_element)
    select_src_from_img(img_element)

    #print(a_element, end="\n\n")

    element = {
        "title": title_element.text,
        "category": category_element.text,
        "price": span_price_element.text,
        "link": a_element['href'],
        "image":img_element,
    }
    print(element,end="\n\n\n")
    return element


def select_src_from_img(content):
    patron = re.compile(r'\bsrc\b$\n') 
    text = re.findall(r'\bsrc\b$\n', content.string())
    #text = patron.match(content)
    print(text)
    return text