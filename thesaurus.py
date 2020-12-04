import json

# Load an open data.json file read mode
data = json.load(open("data.json"))

# Function to return meaning of input word
def meaning(word):
    # check for existing word
    if word in data:
        return data[word]
    else:
        return "Word doesn't exist. Please double check it."

# Ask user to input word and store input in variable
word = input("Enter word: ")

print(meaning(word))

