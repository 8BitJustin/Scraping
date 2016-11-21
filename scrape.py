from bs4 import BeautifulSoup
import urllib2

# Youtube video https://www.youtube.com/watch?v=BCJ4afDX4L4

f = open('C:\Users\Justin Olson\Documents\Scraped\scrapeTest.txt','w')
error = open('C:\Users\Justin Olson\Documents\Scraped\scrapeError.txt','w')

x = 0
while x < 500:
    soup = BeautifulSoup(urllib2.urlopen('http://games.espn.com/ffl/tools/projections' + str(x)).read(), 'html')
    tableStats = soup.find("table", ("class" : "playerTableTable tableBody"))
    for row in tableStats.findAll('tr') [2:]:
        col = row.findAll('td')

        try:
            name = col[0].a.string.strip()
            f.write(name+'\n')

        except Exception as e:
            errorFile.write (str(x) + '*************' + str(e) + '***************' + str(col) + '\n')
            pass

    x = X + 40

f.close
error.close