'''
Bonus (Not required), create a new file in the last LAB repo and do the following:

Define a string variable containing a sentence with at least 10 words.
Define a string variable containing a word that appears in the sentence.
Print the length of the sentence.
Print the index of the first occurrence of the word in the sentence.
Print the number of times the word appears in the sentence.
Print the sentence in all uppercase letters.
Print the sentence in all lowercase letters.
Replace the word in the sentence with a new word of your choice.
Print the last character of the sentence.
'''
#Define a string variable containing a sentence with at least 10 words.
mySentence="Sometimes I stare at a door or a wall and I wonder what is this reality, why am I alive, and what is this all about?"

#Define a string variable containing a word that appears in the sentence.
secondString="I"

#Print the length of the sentence.
print(len(mySentence))

#Print the index of the first occurrence of the word in the sentence.
print(mySentence.index(secondString))

#Print the number of times the word appears in the sentence.
print(mySentence.count(secondString))

#Print the sentence in all uppercase letters.
print(mySentence.upper())

#Print the sentence in all lowercase letters.
print(mySentence.lower())

#Replace the word in the sentence with a new word of your choice.
print(mySentence.replace("I","You"))

#Print the last character of the sentence.
print(mySentence[-1])