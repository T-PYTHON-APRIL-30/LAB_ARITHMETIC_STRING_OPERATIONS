'''
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

aboutMe ="My name is Noura Aldayhani, I graduated from IMSIU majoring in Information Sysytems"
containingWord ="Aldayhani"
print(f"Length of the sentence: {aboutMe.__len__()}")
print(f"The index of the word: {aboutMe.index(containingWord)}")
print(f"Number of times appeared: {aboutMe.count(containingWord)}")
print(f"Uppercase: {aboutMe.upper()}")
print(f"Lowercase: {aboutMe.lower()}")
print(f"Replace the word to \'Sultan\': {aboutMe.replace(containingWord,'Sultan')}")
print(f"The last char: {aboutMe[-1]}")