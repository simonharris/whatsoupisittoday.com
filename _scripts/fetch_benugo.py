from lxml.html import parse
from pprint import pprint
import pickle
import json
#import re


"""
Fetch this today's soup from Benugo's website

Run: daily
"""

outfile = '/tmp/benugo.pkl';
soupurl = 'http://www.benugo.com/shops/'


def fix_text(astr):
	"""Remove undesirable characters and strings"""
	astr = astr.strip()
	return astr


souplist = {}

shops = json.load(open("../_data/shops_benugo.json"))

pprint(shops)


for shop in shops:

	shopurl = soupurl + shop['key']
	print "Reading", shopurl
	#doc = parse(shopurl)
	#elements = doc.xpath('//strong')
	#pprint(elements)

	#roughlist = [elem.text_content() for elem in elements]
	#roughlist = map(fix_text, roughlist)

	souplist[shop['key']] = ['Chicken & Mushroom', 'Vegetarian Gruel']


pprint(souplist)

output = open(outfile, 'wb')
pickle.dump(souplist, output, -1)
output.close()

