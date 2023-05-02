#Define a string variable containing a sentence with at least 10 words.
sentence = "Hello frind, I hope you doing great today, keep it going."

#Define a string variable containing a word that appears in the sentence.
word = "World"

#Print the length of the sentence.
print(len(sentence))

#Print the index of the first occurrence of the word in the sentence.
print(sentence[0])

#Print the number of times the word appears in the sentence.
print(sentence.count(word))

#Print the sentence in all uppercase letters.
print(sentence.upper())

#Print the sentence in all lowercase letters.
print(sentence.lower())

#Replace the word in the sentence with a new word of your choice.
print(sentence.replace("frind",word))

#Print the last character of the sentence.
print(sentence[-1])