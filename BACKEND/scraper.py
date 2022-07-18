import bs4 as bs
import urllib.request
import re

def scraper(url):
    article_text = ""

    user_agent = 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9.0.7) Gecko/2009021910 Firefox/3.0.7'
    headers={'User-Agent':user_agent,} 

    request=urllib.request.Request(url,None,headers)
    response = urllib.request.urlopen(request)
    data = response.read()

    parsed_article = bs.BeautifulSoup(data, 'lxml')

    title = parsed_article.find('title').text

    paragraphs = parsed_article.find_all('p')

    if len(paragraphs) != 0:
        for p in paragraphs:
            article_text += p.text
    
    else:
        divs = parsed_article.find_all('div', id = 'container')

        for div in divs:
            article_text += div.text

    
    article_text = re.sub(r'[[0-9]*]', ' ', article_text)
    article_text = re.sub(r's+', ' ', article_text)

    return title, article_text 