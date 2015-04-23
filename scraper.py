import bs4
import re
import urllib2
import sys

item_count = 600
for i in range(0, item_count, 40):
    link = "http://www.flipkart.com/mobiles/pr?p%5B%5D=sort%3Dprice_asc&sid=tyy%2C4io&layout=grid&ajax=true&start=%d" % (i+1)
    
    print link
response = urllib2.urlopen(link)
thePage = response.read()
soup = bs4.BeautifulSoup(thePage)
allMobiles = soup.find('div', attrs={'id': 'products'})
