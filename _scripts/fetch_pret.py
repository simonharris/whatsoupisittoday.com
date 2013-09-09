from lxml.html import parse
from pprint import pprint
import pickle
import re


"""
Fetch this week's soup from Pret's website

Run: weekly, early Monday morning
"""

outfile = '/tmp/pret.pkl';
soupurl = 'http://www.pret.com/our_food/soup.htm'


def fix_text(astr):
	"""Remove undesirable characters and strings"""
	astr = astr.strip()
	return astr


doc = parse(soupurl)
elements = doc.xpath('//td[@valign="middle" and @align="center"]')

allsoups = [elem.text for elem in elements]
allsoups = map(fix_text, allsoups)

pprint(allsoups)

souplist = [
	[allsoups[0], allsoups[1]],
	[allsoups[2], allsoups[3]],
	[allsoups[4], allsoups[5]],
	[allsoups[6], allsoups[7]],
	[allsoups[8], allsoups[9]],
]

output = open(outfile, 'wb')
pickle.dump(souplist, output, -1)
output.close()
