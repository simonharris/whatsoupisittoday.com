from pprint import pprint
import pickle

"""
Store Tossed soup data in a list and pickle it

Run: by hand, as and when
"""

outfile = '/tmp/tossed.pkl';


# update 20120612
#souplist = [
#        ['Chickpea & Spinach Dhal', 'Malaysian Chicken', 'Tomato & Basil'],
#        ['Sweet Potato, Coconut & Coriander ', 'Summer Chicken', 'Tomato & Basil'],
#        ['Pea & Mint', 'Chilli Chicken', 'Tomato & Basil'],
#        ['Minestrone', 'Indonesian Chicken Noodle', 'Tomato & Basil'],
#        ['Pick of the Week', 'Tomato & Basil'],
#]


# update 20120924
souplist = [
        ['Malaysian Chicken', 'Tomato & Basil', 'Classic Chicken', 'Lentil Dhal'],
        ['Malaysian Chicken', 'Tomato & Basil', 'Classic Chicken', 'Lentil Dhal'],
        ['Malaysian Chicken', 'Tomato & Basil', 'Classic Chicken', 'Lentil Dhal'],
        ['Malaysian Chicken', 'Tomato & Basil', 'Classic Chicken', 'Lentil Dhal'],
        ['Malaysian Chicken', 'Tomato & Basil', 'Classic Chicken', 'Lentil Dhal'],
]

output = open(outfile, 'wb')
pickle.dump(souplist, output, -1)
output.close()
