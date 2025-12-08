'''
Given a string consisting of words separated by whitespace, your task is to write a Python function that accepts this string. 
It then replaces each character in the words with the corresponding character opposite in the English alphabet and stitches 
them all together to form a new string.

Here's what you need to consider:

The input string will include between 1 and 100 words.
Each word consists of characters separated by white space.
A word is composed of characters ranging from a to z or A to Z. So, if a word contains a lowercase 'a', for instance, it 
should be replaced with 'z', 'b' with 'y', 'c' with 'x', and so on, maintaining the same case. For words with an uppercase 
'A', it should be replaced with 'Z', 'B' with 'Y', 'C' with 'X', and so forth, while preserving the uppercase.
The given string will not start or end with a space, and there will be no occurrence of double spaces.
After transforming the characters of the words, form a new string by taking the last word first and appending the remaining 
words in their original order, each separated by spaces.
Note: The opposite letter mappings are as follows: a ↔ z, b ↔ y, c ↔ x, ..., m ↔ n, n ↔ m, ..., x ↔ c, y ↔ b, z ↔ a. The 
mapping is case-sensitive.

Example

For the input string "CapitaL letters", the output should be "ovggvih XzkrgzO".
'''

def solution(input_str):
    # TODO: implement the string transformation function
    
    new_words = []
    
    words = input_str.split(' ')
    for word in words:
        new_word = ""
        
        letters = list(word)
        for letter in letters:
            if letter.isupper():
                new_word += chr(ord('A') + ord('Z') - ord(letter))
            else:
                new_word += chr(ord('a') + ord('z') - ord(letter))
        
        new_words.append(new_word)
    
    new_words = new_words[-1:] + new_words[:-1]
    
    return " ".join(new_words)
    