#python3
# Program that loads json dictionary of items in and adjusts for mispelled words

import difflib
from difflib import get_close_matches
import os
import json

# Getting relative path to file
dirname = os.path.dirname(__file__)
filename = os.path.join(dirname, 'data.json')

# Load data 
data = json.load(open(filename,'r+'))

# Function that inputs key and returns a value 
def translate(word):
    word = word.lower()
    if word in data:
        return data[word]
    elif len(get_close_matches(word, data.keys())) > 0:
        yn = input("Did you mean %s instead? Enter Y if yes, or N if no." % get_close_matches(word, data.keys())[0])
        if yn == "Y":
            return data[get_close_matches(word, data.keys())[0]]
        elif yn == "N":
            return "The word doesn't exist. Please double check it."
        else:
            return "We didn't understand your entry."

    else:
        return "The word does not exist please double check it." 


word = input("Enter word: ")

print(translate(word))

