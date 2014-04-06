from lxml.html import parse
from pprint import pprint
import pickle
import re

"""
Fetch this week's soup from Leon's website

Run: daily, early morning
"""

outfile = '/tmp/leon.pkl'
soupurl = 'http://leonrestaurants.co.uk/menu/all-day/'

def fix_text(astr) :
	astr = astr.replace(' Soup', '').strip()
	return astr


def is_soup(item):
	if ("Soup" in item):
		return True
	return False


doc = parse(soupurl)
elements = doc.xpath('//div[@class="more-info-wrapper"]/h1[@class="menu-item-title"]')

roughlist = [elem.text for elem in elements if (is_soup(elem.text))]
souplist = map(fix_text, roughlist)

#pprint(souplist)

output = open(outfile, 'wb')
pickle.dump(souplist, output, -1)
output.close()
