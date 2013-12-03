from pprint import pprint
import pickle
from datetime import date

"""
Store Pure soup data in a list and pickle it

Run: weekly
"""

outfile = '/tmp/pure.pkl';

#
# Pure have a two-week rotation, so just define the whole menu here and decide
# which week it currently is later on.
#
souplist = {
	'even':[
		['Spiced Carrot', 'Tomato & Charred Red Onion', 'Siam Chicken'],
		['Leek & Potato', 'Thai Green Lentil, Spinach & Coconut', 'Chicken Sambar Dahl'],
		['Winter Chicken Noodle', 'Portobello Mushroom with Thyme', 'Lakeland Beef with Potato'],
		['Tomato & Basil', 'Moroccan Sweet Potato & Chickpea', 'Bean & Bacon Broth'],
		['Winter Vegetable & Barley', 'Tomato & Sweet Red Pepper', 'Tuscan Sausage Broth']
	],
	'odd':[
		['Tomato & Basil', 'Moroccan Sweet Potato & Chickpea', 'Lamb & Barley'],
		['Spiced Carrot', 'Tomato & Sweet Red Pepper', 'Chicken Laksa'],
		['Leek & Potato', 'Portobello Mushroom with Thyme', 'Chipotle Beef'],
		['Winter Chicken Noodle	', 'Tomato & Charred Red Onion', 'Boston Chicken Chowder'],
		['Winter Vegetable & Barley', 'Thai Green Lentil, Spinach & Coconut', 'Chorizo Puchero']
	]
}

# We'll run this over the weekend so we actually want next week
weeknum = date.today().isocalendar()[1] + 1

if (weeknum % 2) :
	whichweek = 'odd'
else :
	whichweek = 'even'

thisweek = souplist[whichweek]

output = open(outfile, 'wb')
pickle.dump(thisweek, output, -1)
output.close()
