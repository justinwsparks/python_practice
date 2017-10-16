from bs4 import BeautifulSoup as soup
from urllib.request import urlopen as uReq

my_url = 'https://www.google.com'

# open connection, download content
uClient = uReq(my_url)
pageHtml = uClient.read()
uClient.close()

# completes html parsing
pageSoup = soup(pageHtml, "html.parser")




# grab all style tags

styles = pageSoup.findAll("style")
print(str(styles))