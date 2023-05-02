'''
Define a string variable containing a sentence with at least 10 words.
Define a string variable containing a word that appears in the sentence.
Print the length of the sentence.
Print the index of the first occurrence of the word in the sentence.
Print the number of times the word appears in the sentence.
Print the sentence in all uppercase letters.
Print the sentence in all lowercase letters.
Replace the word in the sentence with a new word of your choice.
Print the last character of the sentence.'''

hopes= "i enjoy watching football and i hope Al-itthad win the leauge after waiting 13 years"
football_team="enjoy"

#Print the length of the sentence.
print(len(hopes))

#Print the index of the first occurrence of the word in the sentence
print (hopes.index("enjoy"))

#Print the number of times the word appears in the sentence.
print(hopes.count("win"))

#Print the sentence in all uppercase letters.
print(hopes.upper())

#Print the sentence in all lowercase letters.
print(hopes.lower())

#Replace the word in the sentence with a new word of your choice.
print(hopes.replace("win","lose"))

#Print the last character of the sentence.
print(hopes[-1:])





