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
	astr = astr.replace('(v)', '').replace('(ve)', '').replace('(med)', '').replace('(lrg)', '').strip()
	return astr


doc = parse(soupurl)
#elements = doc.xpath('//section[@class="post-content"]/p[position()>3]')
elements = doc.xpath('//div[@class="left"]/header/h1')

souplist = [elem.text for elem in elements]
souplist = map(fix_text, souplist)
souplist = set(souplist)

#pprint(souplist)

allweek = [souplist,souplist,souplist,souplist,souplist]

#pprint(allweek)

output = open(outfile, 'wb')
pickle.dump(allweek, output, -1)
output.close()
