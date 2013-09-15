from lxml.html import parse
from pprint import pprint
import pickle
import re

"""
Fetch this week's soup from Leon's website

Run: daily, early morning
"""

outfile = '/tmp/leon.pkl';
soupurl = 'http://www.leonrestaurants.co.uk/';

def fix_text(astr) :
	#astr = astr.strip()
	#astr = astr.replace('has nuts in it', '')
	#astr = re.sub('/NEW /', '', astr)
	#astr = re.sub('/ - Back by popular demand!$/', '', astr);
	#astr = astr.strip()
	return astr

doc = parse(soupurl)
elements = doc.xpath('//div[@class="soup"]//h2')

roughlist = [elem.text_content() for elem in elements]
souplist = map(fix_text, roughlist)

output = open(outfile, 'wb')
pickle.dump(souplist, output, -1)
output.close()
