import json
from difflib import get_close_matches

# Load an open data.json file read mode
data = json.load(open("data.json"))

# Function to return meaning of input word
def meaning(word):
    # change input word to lower case so there's no errors
    wordL = word.lower()
    city = word.capitalize()
    acronym = word.upper()
    wGuessed = get_close_matches(word, data.keys(), cutoff=0.8)

    # check for existing word
    if wordL in data:
        return data[wordL]
    elif city in data:
        return data[city]
    elif acronym in data:
        return data[acronym]
    elif len(wGuessed) > 0:   
        wCorrected = input(f"did you mean {wGuessed[0]}?: Yes or No: ")
        check = wCorrected.lower()
        if check == "yes":
            print(meaning(wGuessed[0]))
        elif check == "no":
            word = input("Word doesn't exist. Please reenter your word:")
            print(meaning(word))
        return "thanks for using our dictionay"
    else:
        return "Word daesn't exist. Please double check it"
# Ask user to input word and store input in variable
word = input("Enter word: ")

print(meaning(word))

