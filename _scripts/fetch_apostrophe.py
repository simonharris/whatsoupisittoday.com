from lxml.html import parse
from pprint import pprint
import pickle
import json
import os


"""
Fetch today's soup from Apostrophe's website

Run: daily
"""

outfile = '/tmp/apostrophe.pkl'
soupurl = 'http://www.apostropheuk.com/php/showtodays.php?location='


def fix_text(astr):
	"""Remove undesirable characters and strings"""
	astr = astr.replace(' soup', '').strip()
	#astr = astr.replace('BROCCOLI PEA', 'BROCCOLI, PEA').strip()
	astr = astr.strip()
	return astr


souplist = {}


mypath = os.path.dirname(os.path.realpath(__file__))

shops = json.load(open(mypath + "/../_data/shops_apostrophe.json"))

pprint(shops)

for shop in shops:

	shopurl = soupurl + shop['key']
	print "Reading", shopurl
	doc = parse(shopurl)

	#<span class='special-title'>

	elements = doc.xpath("//li/a[@href='#']")
	pprint(elements)

	roughlist = [elem.text for elem in elements if ("soup" in elem.text)]
	roughlist = map(fix_text, roughlist)

	souplist[shop['key']] = roughlist


pprint(souplist)

output = open(outfile, 'wb')
pickle.dump(souplist, output, -1)
output.close()
