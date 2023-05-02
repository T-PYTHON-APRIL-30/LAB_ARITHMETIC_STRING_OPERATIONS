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

sentence = "Web application development camp using Python with Tuwaiq Academy Django"


word = "Python"

print("Length of the sentence:", len(sentence))

print("Index of the word in the sentence:", sentence.index(word))

print("Number of times the word appears in the sentence:", sentence.count(word))

print("Sentence in uppercase:", sentence.upper())

print("Sentence in lowercase:", sentence.lower())

new_word = "Java"
new_sentence = sentence.replace(word, new_word)
print("New sentence:", new_sentence)

print("Last character of the sentence:", sentence[-1])
