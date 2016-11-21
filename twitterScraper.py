import urllib
import urllib.request
from bs4 import BeautifulSoup

# Twitter scraper example, https://www.youtube.com/watch?v=o0RasL5uxkg&t=39s

theurl = "https://twitter.com/Pac12Network"
thepage = urllib.request.urlopen(theurl)
soup = BeautifulSoup(thepage, "html.parser")

print(soup.title.text)
# print(soup.findAll('a')[0])
# print(soup.find('a'))
"""
for link in soup.findAll('a'):
    print(link.get('href'))
    print(link.text)
"""

"""
# Pulls up profile text of acct
print(soup.find('div',{"class":"ProfileHeaderCard"}).find('p').text)
"""

"""
# This will loop through all of the tweets via the class div of content
i = 1
for tweets in soup.findAll('div',{"class":"content"}):
    print(str(i) + '. ' + tweets.find('p').text)
    i += 1
"""