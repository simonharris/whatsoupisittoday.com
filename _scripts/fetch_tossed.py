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
#souplist = [
#        ['Malaysian Chicken', 'Tomato & Basil', 'Classic Chicken', 'Lentil Dhal'],
#        ['Malaysian Chicken', 'Tomato & Basil', 'Classic Chicken', 'Lentil Dhal'],
#        ['Malaysian Chicken', 'Tomato & Basil', 'Classic Chicken', 'Lentil Dhal'],
#        ['Malaysian Chicken', 'Tomato & Basil', 'Classic Chicken', 'Lentil Dhal'],
#        ['Malaysian Chicken', 'Tomato & Basil', 'Classic Chicken', 'Lentil Dhal'],
#]

# update 20130401
souplist = [
	['100 Calorie Tomato and Basil','100 Calorie Malaysian Chicken','150 Calorie Pea and Mint','150 Calorie Summer Chicken','Super Skinny Miso'],
	['100 Calorie Tomato and Basil','100 Calorie Malaysian Chicken','150 Calorie Pea and Mint','150 Calorie Summer Chicken','Super Skinny Miso'],
	['100 Calorie Tomato and Basil','100 Calorie Malaysian Chicken','150 Calorie Pea and Mint','150 Calorie Summer Chicken','Super Skinny Miso'],
	['100 Calorie Tomato and Basil','100 Calorie Malaysian Chicken','150 Calorie Pea and Mint','150 Calorie Summer Chicken','Super Skinny Miso'],
	['100 Calorie Tomato and Basil','100 Calorie Malaysian Chicken','150 Calorie Pea and Mint','150 Calorie Summer Chicken','Super Skinny Miso']
]

output = open(outfile, 'wb')
pickle.dump(souplist, output, -1)
output.close()
