from pprint import pprint
import pickle
import re
import urllib2
import json 


"""
Fetch this week's soup from Leon's website

Run: daily, early morning
"""

outfile = '/tmp/leon.pkl'
soupurl = 'http://www.leonrestaurants.co.uk/_js/menu.php' 


def fix_text(astr) :
	#astr = astr.strip()
	#astr = astr.replace('has nuts in it', '')
	#astr = re.sub('/NEW /', '', astr)
	#astr = re.sub('/ - Back by popular demand!$/', '', astr);
	astr = astr.strip()
	return astr


js = urllib2.urlopen(soupurl).read()

# strip out non-JSON guff
js = js.replace('window.InitData=', '')
js = js.replace(';', '')

data = json.loads(js)

souplist = [a['dish'] for a in data if a['sub_cat'] == 'SOUPS']

output = open(outfile, 'wb')
pickle.dump(souplist, output, -1)
output.close()
