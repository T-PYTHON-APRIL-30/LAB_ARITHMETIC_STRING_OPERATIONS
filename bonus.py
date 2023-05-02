from re import S


sentence ="high level programming language with dynamic semantics data structures combined with dynamic"
word="dynamic"

#Print the length of the sentence.
print("\nThe length of the sentence: {}".format(len(sentence)))


#Print the index of the first occurrence of the word in the sentence.
print("The index of the word first occurrence: {}".format(sentence.find(word)))

#Print the number of times the word appears in the sentence.
print("Number of times the word appears: {}".format(sentence.count(word)))

#Print the sentence in all uppercase letters.
print("The sentence in uppercase letters: {}".format(sentence.upper()))

#Print the sentence in all lowercase letters.
print("The sentence in lowercase letters: {}".format(sentence.lower()))

#Replace the word in the sentence with a new word of your choice.
print("Word replacement: {}".format(sentence.replace("dynamic", "replaced\n",2)))
