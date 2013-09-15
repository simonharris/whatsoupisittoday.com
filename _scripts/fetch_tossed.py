from pprint import pprint
import pickle

"""
Store Tossed soup data in a list and pickle it

Run: by hand, when updates supplied by Tossed
"""

outfile = '/tmp/tossed.pkl';

# update 20130915
souplist = [
	['Low GI Minestrone', 'Big Protein Chicken', '100 Calorie Tomato and Basil','100 Calorie Malaysian Chicken'],
	['Low GI Minestrone', 'Big Protein Chicken', '100 Calorie Tomato and Basil','100 Calorie Malaysian Chicken'],
	['Low GI Minestrone', 'Big Protein Chicken', '100 Calorie Tomato and Basil','100 Calorie Malaysian Chicken'],
	['Low GI Minestrone', 'Big Protein Chicken', '100 Calorie Tomato and Basil','100 Calorie Malaysian Chicken'],
	['Low GI Minestrone', 'Big Protein Chicken', '100 Calorie Tomato and Basil','100 Calorie Malaysian Chicken']
]

output = open(outfile, 'wb')
pickle.dump(souplist, output, -1)
output.close()
