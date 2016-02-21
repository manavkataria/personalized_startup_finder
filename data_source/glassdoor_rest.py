import urllib2, sys
from BeautifulSoup import BeautifulSoup

def getGlassdoor(company):
	url = "http://api.glassdoor.com/api/api.htm?t.p=55690&t.k=em66CFmfXYu&userip=172.23.227.50&useragent=Mozilla&format=json&v=1&action=employers&q="+company
	hdr = {'User-Agent': 'Mozilla/5.0'}
	req = urllib2.Request(url,headers=hdr)
	response = urllib2.urlopen(req)
	soup = BeautifulSoup(response)
	print soup
	return soup

getGlassdoor('apple')
