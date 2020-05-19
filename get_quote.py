#get_quote.py
import requests
import random
#import selenium
from bs4 import BeautifulSoup as bs 
page  = requests.get("https://www.goodreads.com/quotes?page={}".format(random.randrange(100)) )
content = bs(page.content,'html.parser')
num = random.randrange(25)

all_quotes = content.findAll('div',{"class":"quoteText"})
print(all_quotes[num].get_text())


