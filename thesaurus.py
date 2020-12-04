import json

# Load an open data.json file read mode
data = json.load(open("data.json"))

# Function to return meaning of input word
def meaning(word):
    return data[word]

# Ask user to input word and store input in variable
word = input("Enter word: ")

print(meaning(word))

