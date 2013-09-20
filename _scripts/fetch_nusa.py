from lxml.html import parse
from pprint import pprint
import pickle
import re

"""
Fetch today's soup from Nusa's website

Run: daily, early morning
"""

outfile = '/tmp/nusa.pkl';
soupurl = 'http://www.nusakitchen.co.uk/index.php?go=our-food,soups';

def fix_text(astr) :
	#astr = astr.strip()
	#astr = astr.replace('has nuts in it', '')
	#astr = re.sub('/NEW /', '', astr)
	#astr = re.sub('/ - Back by popular demand!$/', '', astr);
	astr = astr.strip()
	return astr

doc = parse(soupurl)
elements = doc.xpath('//div[@id="ourfoodpageleft"]//th')

roughlist = [elem.text_content() for elem in elements]
souplist = map(fix_text, roughlist)

#pprint(souplist)

output = open(outfile, 'wb')
pickle.dump(souplist, output, -1)
output.close()
