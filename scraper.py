import bs4
import re
import urllib2
import sys

link = 'http://www.flipkart.com/mobiles/pr?p[]=sort%3Dprice_asc&sid=tyy%2C4io&layout=grid'
response = urllib2.urlopen(link)
thePage = response.read()
soup = bs4.BeautifulSoup(thePage)
allMobiles = soup.find('div', attrs={'id': 'products'})
