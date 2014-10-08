from lxml.html import parse
from pprint import pprint
import pickle
import re
import datetime

"""
Fetch this week's soup from EAT's website

Run: weekly, early Monday morning
"""

outfile = '/tmp/eat.pkl';
soupurl = 'http://eat.co.uk/';

def fix_text(astr) :
	#astr = astr.strip()
	#astr = astr.replace('has nuts in it', '')
	#astr = astr.replace('(less than 5% fat)', '')
	#astr = re.sub('/NEW /', '', astr)
	astr = astr.replace('\n', ' ')
	#astr = re.sub('/\t/', '', astr)
	#astr = re.sub('/ - Back by popular demand!$/', '', astr);
	astr = astr.strip()
	return astr

doc = parse(soupurl)
elements = doc.xpath('//h4')

roughlist = [elem.text_content() for elem in elements]
roughlist = map(fix_text, roughlist)

#pprint(roughlist)

#fragile
today1    = roughlist[3]
today2    = roughlist[4]
tomorrow1 = roughlist[5]
tomorrow2 = roughlist[6]

today = datetime.datetime.today().weekday()

souplist = [
	[], # mon
	[], # tues
	[], # weds
	[], # thurs
	[], # fri
]

souplist[today]   = [today1, today2]
souplist[today+1] = [tomorrow1, tomorrow2]

#pprint(souplist)

output = open(outfile, 'wb')
pickle.dump(souplist, output, -1)
output.close()
