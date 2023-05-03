'''Bonus (Not required), create a new file in the last LAB repo and do the following:

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
sentance ="My name is shorog essa alessa . I love computer programming ,I am interested in the Python language.I also love sports."
appearWord  = "shorog"
print("length of the sentence is:",len(sentance))
print("the index of the first occurrence of the word in the sentence is:",sentance.index("M"))
print(" number of times the word appears in the sentence is:",sentance.count("love"))
print("sentance in upper case is:",sentance.upper())
print("sentance in lower case is:",sentance.lower())
new_string =sentance.replace("I","shorog")
print("the last character of the sentence is:"," ","s."))


