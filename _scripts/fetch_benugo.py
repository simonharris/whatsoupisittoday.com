from lxml.html import parse
from pprint import pprint
import pickle
import json
import os


"""
Fetch this today's soup from Benugo's website

Run: daily
"""

outfile = '/tmp/benugo.pkl';
soupurl = 'http://www.benugo.com/shops/'


def fix_text(astr):
	"""Remove undesirable characters and strings"""
	astr = astr.replace(' SOUP', '').strip()
	astr = astr.replace('BROCCOLI PEA', 'BROCCOLI, PEA').strip()
	astr = astr.strip()
	return astr


souplist = {}


mypath = os.path.dirname(os.path.realpath(__file__))

shops = json.load(open(mypath + "/../_data/shops_benugo.json"))

#pprint(shops)

for shop in shops:

	shopurl = soupurl + shop['key']
	print "Reading", shopurl

	try:
		doc = parse(shopurl)

		#<span class='special-title'>

		elements = doc.xpath("//span[@class='special-title']")
		pprint(elements)

		roughlist = [elem.text for elem in elements if ("SOUP" in elem.text)]
		roughlist = map(fix_text, roughlist)

	# e.g. 404
	except IOError:
		roughlist = ['Currently Unavailable']

	souplist[shop['key']] = roughlist


pprint(souplist)

output = open(outfile, 'wb')
pickle.dump(souplist, output, -1)
output.close()
