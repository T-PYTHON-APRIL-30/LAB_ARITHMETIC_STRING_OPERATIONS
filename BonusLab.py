'''

Replace the word in the sentence with a new word of your choice.
Print the last character of the sentence.
'''

sentence = "Hi, my name is Yousef ALsaadan I started coding before 5 years ago."
word = "Yousef"

print(f"sentence: \n {sentence} \n")

print(f"The length of the sentence is: \n {len(sentence)} \n")
print(f"The first index: \n {sentence[0]} \n")
print(f"The word {word} appears {sentence.count(word)} times \n")

print(f"The sentence in uppercase: \n {sentence.upper()} \n")
print(f"The sentence in lowercase: \n {sentence.lower()} \n")

new_word = "Yousef Mohammed"
print(f"The new sentence is: \n {sentence.replace(word, new_word)} \n")

print(f"The last character: {sentence[-1]}")