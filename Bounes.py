"""
Define a string variable containing a sentence with at least 10 words.
Define a string variable containing a word that appears in the sentence.
Print the length of the sentence.
Print the index of the first occurrence of the word in the sentence.
Print the number of times the word appears in the sentence.
Print the sentence in all uppercase letters.
Print the sentence in all lowercase letters.
Replace the word in the sentence with a new word of your choice.
Print the last character of the sentence.
"""


stringVar = "Hello , my Name is Bakr Hawsawi I'm 23 years old"
stringVar2 = "Bakr"
print("Length of sentence:" , len(stringVar))
print("Index of first occurrence of word:" , stringVar.index(stringVar2))
print("Number of times word appears in sentence:", stringVar.count(stringVar2))
print("Sentence in all uppercase:", stringVar.upper())
print("Sentence in all lowercase:", stringVar.lower())
new_sentence = stringVar.replace(stringVar2, "Salem")
print("New sentence with replaced word:", new_sentence)
print("Last character of the sentence:", stringVar[-1])


