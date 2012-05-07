from pprint import pprint
import pickle

"""
Store Tossed soup data in a list and pickle it

Run: by hand, as and when
"""

outfile = '/tmp/tossed.pkl';


# update 20111013
souplist = [
        ['Skinny Minestrone', 'Malaysian Chicken', 'Tomato & Basil'],
        ['Pumpkin & Lentil Hotpot', 'Chilli Chicken', 'Tomato & Basil'],
        ['Mamma\'s Chicken', 'Sweet Potato, Coconut & Coriander', 'Tomato & Basil'],
        ['Smokey Bacon & Lentil', 'Leek & Potato', 'Tomato & Basil'],
        ['Pick of the Week', 'Tomato & Basil'],
]


output = open(outfile, 'wb')
pickle.dump(souplist, output, -1)
output.close()
