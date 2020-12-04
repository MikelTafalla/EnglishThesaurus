import json

# Load an open data.json file read mode
data = json.load(open("data.json"))

# Function to return meaning of input word
def meaning(word):
    # change input word to lower case so there's no errors
    word = word.lower()
    city = word.capitalize()
    acronym = word.upper()
    
    # check for existing word
    if word in data:
        return data[word]
    elif city in data:
        return data[city]
    elif acronym in data:
        return data[acronym]
    else:
        return "Word doesn't exist. Please double check it."

# Ask user to input word and store input in variable
word = input("Enter word: ")

print(meaning(word))

