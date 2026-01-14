'''
You are given two lists, sentences and words, each comprising n strings, where n ranges from 
1
1 to 
100
100 inclusive. Each string in the sentences list has a length ranging from 
1
1 to 
500
500 inclusive. Each word in the words list is a single lowercase English alphabet word of length 
1
1 to 
10
10 inclusive.

Your task is to find all instances of each word in the corresponding sentence from the sentences list and replace them with the reverse of the word. The words and sentences at the same index in their respective lists are deemed to correspond to each other.

Return a new list comprising n strings, where each string is the sentence from the sentences list at the corresponding index, with all instances of the word from the words list at the same index replaced with its reverse.

If the word is not found in the respective sentence, keep the sentence as it is.

Remember, while replacing the instances of word in the sentence, you should preserve the case of the initial letter of the word. If a word starts with a capital letter in the sentence, its reversed form should also start with a capital letter.

Example

For sentences = ['this is a simple example.', 'the name is bond. james bond.', 'remove every single e'] and words = ['simple', 'bond', 'e'], the output should be ['this is a elpmis example.', 'the name is dnob. james dnob.', 'remove every single e'].

'''

def solution(sentences, words):
    # TODO: implement the solution
    
    reverse_words = []
    for word in words:
        reverse_word = (word[::-1])
        reverse_words.append(reverse_word)
        
    result = []
    for sentence, word, reverse_word in zip(sentences, words, reverse_words):
        sentence = sentence.replace(word, reverse_word)
        result.append(
            sentence.replace(word.capitalize(), reverse_word.capitalize())
        )
        
    return result