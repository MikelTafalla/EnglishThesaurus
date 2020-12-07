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
    display = f""
    counter = 0
    # check for existing word
    if wordL in data:
        for element in data[wordL]:
            counter += 1
            display += "\n" + str(counter) + " " + element + "\n"
        print(display)
    elif city in data:
        for element in data[city]:
            counter += 1
            display += "\n" + str(counter) + " " + element + "\n"
        print(display)
    elif acronym in data:
        for element in data[acronym]:
            counter += 1
            display += "\n" + str(counter) + " " + element + "\n"
        print(display)
    elif len(wGuessed) > 0:   
        wCorrected = input(f"did you mean {wGuessed[0]}?: Yes or No: ")
        check = wCorrected.lower()
        counter = 0
        if check == "yes":
            for element in data[wGuessed[0]]:
                counter += 1
                display += "\n" + str(counter) + " " + element + "\n"
            print(display)
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

