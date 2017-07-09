import requests
import time
import bs4
import urllib

start_url = "https://en.wikipedia.org/wiki/Special:Random"
target_url = 'https://en.wikipedia.org/wiki/Philosophy'

def continue_crawl(search_history, target_url, max_steps=25):
    if target_url == search_history[-1]:
        print('Encontramos o artigo final (target)!)')
        return False
    elif len(search_history) > max_steps:
        print('A busca se tornou muito longa. Abortando a busca!')
        return False
    elif search_history[-1] in search_history[:-1]:
        print('Nós estamos em um artigo que já vimos. Abortando a busca!')
        return False
    else:
        return True

def find_first_link(url):
    print('Crawl: ' + url)
    response = requests.get(url)
    html = response.text
    soup = bs4.BeautifulSoup(html, "html.parser")

    # Esta div contém o corpo principal do artigo
    content_div = soup.find(id="mw-content-text")

    # armazena o primeiro link encontrado no artigo, se o artigo não contém
    # nenhum link, este artigo será None
    article_link = None

    # Para cada descendente direto de content_div existem parágrafos
    for element in content_div.find_all("p"): #, recursive=False):
        # Encontra a primeira marcação de âncora que seja um filho direto de um parágrafo.
        # É importante olhar apenas para os descendentes diretos, pois outros tipos de
        # links, como rodapés e guias de pronunciação, podem ser apresentados antes
        # do primeiro link para um artigo. Estes outros tipos de links, contudo, não
        # são descendentes diretos, pois estão em divs de outras classes.
        if element.find("a", recursive=False):
            article_link = element.find("a", recursive=False).get('href')
            break

    if not article_link:
        return 

    # Constrói uma URL completa dada uma URL relativa article_link
    first_link = urllib.parse.urljoin('https://en.wikipedia.org/', article_link)

    return first_link

article_chain = [start_url]

while continue_crawl(article_chain, target_url): 
    # download html of last article in article_chain
    # find the first link in that html
    first_link = find_first_link(article_chain[-1])
    if not first_link:
        print("Nós chegamos a um artigo sem links. Abortando a busca!")
        break
    # add the first link to article chain
    article_chain.append(first_link)
    # delay for about two seconds
    time.sleep(2)
    
print(article_chain)