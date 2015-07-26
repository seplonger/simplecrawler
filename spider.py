__author__ = 'zean m'
__date__ ="2015-7-25 22:21:43"
__e-mail__="i@zean.xyz"
import requests
import BeautifulSoup

def cxg_spider(max_page):
    page = 1
    while page <= max_page:
        url="http://plough-man.com/?paged=" + str(page)
        source_code = requests.get(url)
        plain_text = source_code.text
        soup = BeautifulSoup.BeautifulSoup(plain_text)
        abc="abc"
        for link in soup.findAll('a',{'rel':'bookmark'}):
            href=link.get('href')
            title=link.string
            if href!=abc:
                #print(title)
                #print(href)
                get_single_essay_date(href)
                print("\n")
            abc=href
        page+=1

def get_single_essay_date(item_url):
    source_code = requests.get(item_url)
    plain_text = source_code.text
    soup=BeautifulSoup.BeautifulSoup(plain_text)
    #for essay_date in soup.findAll('span',{'class':'entry-date'}):
        #print(essay_date.string)
    for link in soup.findAll('a'):
        href=link.get('href')
        print(href)

cxg_spider(3)
