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
        print(data[wordL])
    elif city in data:
        print(data[city])
    elif acronym in data:
        print(data[acronym])
    elif len(wGuessed) > 0:   
        wCorrected = input(f"did you mean {wGuessed[0]}?: Yes or No: ")
        check = wCorrected.lower()
        if check == "yes":
            print(data[wGuessed[0]])
        elif check == "no":
            print("Word doesn't exist. Please double check it")
        else:
            print("Command not Understood")              
    else:
        print("Word doesn't exist. Please double check it")

    more = input("Please enter another word or type any single letter to close the program: ")
    if len(more) > 1:
        print(meaning(more))
    else:
        return "Good Bye"
# Ask user to input word and store input in variable
word = input("Enter word: ")

print(meaning(word))

