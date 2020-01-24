#python3
# Program that loads json dictionary of items in

import os
import json

# Getting relative path to file
dirname = os.path.dirname(__file__)
filename = os.path.join(dirname, 'data.json')

# Load data 
data = json.load(open(filename,'r+'))
print(data)
