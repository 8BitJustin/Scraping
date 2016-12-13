import urllib
import urllib.request
from bs4 import BeautifulSoup

"""
# This is when you set the variables, and print. It creates the page in HTML format

thepage = urllib.request.urlopen('http://www.arizona.edu/')
soupdata = BeautifulSoup(thepage, 'html.parser')

print(soupdata.prettify())
"""

# This is if you make it a function and run it

def make_soup(url):

    thepage = urllib.request.urlopen(url)
    soupdata = BeautifulSoup(thepage, "html.parser")
    return soupdata

soup = make_soup("http://jroassistanceform.x10host.com/")

print(soup.prettify())
