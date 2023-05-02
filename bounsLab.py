'''
1-Define a string variable containing a sentence with at least 10 words.
2-Define a string variable containing a word that appears in the sentence.
3-Print the length of the sentence.
4-Print the index of the first occurrence of the word in the sentence.
5-Print the number of times the word appears in the sentence.
6-Print the sentence in all uppercase letters.
7-Print the sentence in all lowercase letters.
8-Replace the word in the sentence with a new word of your choice.
9-Print the last character of the sentence.

'''

str1 = 'I joined Twuaiq Acadimy in the 30th of April, and we started learning Python language'

str2 = 'Python'

print(f'The length of the sentence is: {len(str1)}')

print(f'The index of the firist occurrence of the word {str2} is : {str1.index(str2)}')

print(f'The number of times the word {str2} apears in the sentence is {str1.count(str2)}')

print(str1.upper())

print(str1.lower())

print(str1.replace(str2,'Java'))

print(str1[len(str1)-1])





