from lxml.html import parse
from pprint import pprint
import pickle
import re

"""
Fetch this week's soup from Abokado's website

Run: weekly, early Monday morning
"""

outfile = '/tmp/abokado.pkl';
soupurl = 'http://abokado.com/menu/soups-and-abowlagos/'

def fix_text(astr):
	"""Remove undesirable characters and strings"""
	astr = astr.replace('(v)', '').replace('(ve)', '').strip()
	return astr


doc = parse(soupurl)
elements = doc.xpath('//section[@class="post-content"]/p[position()>3]')

souplist = [elem.text for elem in elements]
souplist = map(fix_text, souplist)

pprint(souplist)

output = open(outfile, 'wb')
pickle.dump(souplist, output, -1)
output.close()
