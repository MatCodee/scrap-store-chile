from bs4 import BeautifulSoup

def scrap_falabella(html_doc):
    soup = BeautifulSoup(html_doc, 'html.parser')
    #print(soup.prettify())
    
    divs_products = soup.find_all('div',class_="jsx-4001457643")
    for div in divs_products:
        convert_element_div(div)
    
    
    #primer_element = soup.find(id=id_primer_elemento)
    #print(primer_element)
    
def convert_element_div(element):
    
    title_element = element.find('a',class_="jsx-1327784995").text
    #print(title_element.text)
    div_element = element.find('div',class_="jsx-1327784995")
    
    category_element = element.find('b',class_="jsx-1327784995").text
    #print(category_element.text)
    # Este es el enlace de la pagina
    div_price_element = div_element.find('div',["jsx-2797633547"])
    span_price_element = div_price_element.find('span').text
    #print(span_price_element)
    
    a_element = element.find('a',class_="jsx-3128226947")
    #print(a_element, end="\n\n")
    
    element = {
        "title": title_element,
        "category": category_element,
        "price": span_price_element,
        "link": a_element,
    }
    print(element,end="\n\n\n")