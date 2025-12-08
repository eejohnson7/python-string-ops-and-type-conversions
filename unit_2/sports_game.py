'''
You are given a string s of length n, with n ranging from 1 to 500 inclusive. This string represents the complex and 
jumbled record of a sports game. It combines player names and scores but lacks a uniform structure. The player names 
consist of words made up of lowercase English alphabets (a-z), while the scores are integers ranging from 1 to 100 inclusive.

Your mission involves writing a Python function solution(). This function should parse the given string, isolate the 
integers representing player scores, and return the sum of these scores.

For instance, for the input string, "joe scored 5 points, while adam scored 10 points and bob scored 2, with an extra 1 
point scored by joe", your function should return the sum 5 + 10 + 2 + 1, which totals 18.
'''

def solution(s):
    # TODO: implement
    words = s.split(" ")
    sum = 0
    
    for word in words:
        if word.isdigit():
            sum += int(word)
        else:
            chars = list(word)
            previous_char = None
            num = ""

            for char in chars:
                if char.isdigit():
                    num += char
                    
                if previous_char is not None and not char.isdigit() and num != "":
                    sum += int(num)
                    num = ""
                    
                previous_char = char
            
    return sum