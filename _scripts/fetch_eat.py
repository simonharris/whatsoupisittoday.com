from lxml.html import parse
from pprint import pprint
import pickle
import re

"""
Fetch this week's soup from EAT's website

Run: weekly, early Monday morning
"""

outfile = '/tmp/eat.pkl';
soupurl = 'http://www.eatserver.co.uk/editor/menuProvider.php';

def fix_text(astr) :
	astr = astr.strip()
	astr = astr.replace('has nuts in it', '')
	astr = astr.replace('(less than 5% fat)', '')
	astr = re.sub('/NEW /', '', astr)
	astr = re.sub('/ - Back by popular demand!$/', '', astr);
	astr = astr.strip()
	return astr

doc = parse(soupurl)
elements = doc.xpath('//strong')

roughlist = [elem.text_content() for elem in elements]
roughlist = map(fix_text, roughlist)

souplist = [
	[roughlist[6], roughlist[4]],   # mon
	[roughlist[10], roughlist[8]],  # tues
	[roughlist[14], roughlist[12]], # weds
	[roughlist[18], roughlist[16]], # thurs
	[roughlist[22], roughlist[20]], # fri
]

output = open(outfile, 'wb')
pickle.dump(souplist, output, -1)
output.close()
