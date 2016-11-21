import urllib
import urllib.request
from bs4 import BeautifulSoup

def make_soup(url):
    thepage = urllib.request.urlopen(url)
    soupdata = BeautifulSoup(thepage, "html.parser")
    return soupdata

i = 1

soup = make_soup("http://www.arizona.edu/")
for img in soup.findAll('img'):
    temp = (img.get('src'))
    if temp[:1] == '/':
        image = "http://www.arizona.edu/" + temp
    else:
        image = temp

    """
    Prints out all image links
    print(image)
    """

    nametemp = img.get('alt')

    if len(nametemp) == 0:
        filename = str(i)
        i += 1
    else:
        filename = nametemp

    imagefile = open(filename + ".jpeg",'wb')
    imagefile.write(urllib.request.urlopen(image).read())
    imagefile.close()