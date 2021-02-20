# -*- coding: utf-8 -*-
"""
Created on Wed Feb 17 14:21:37 2021

@author: Anna Grzyb
"""

# Problem 3 - Printing Out all Available Letters 


def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    import string
    
    alphabet = ''
        
    for i in string.ascii_lowercase:
        
        if i not in lettersGuessed:
            
            alphabet += i
        
    
    return alphabet
        
# Test:

lettersGuessed = ['e', 'i', 'k', 'p', 'r', 's']

print(getAvailableLetters(lettersGuessed))










# Problem 3 - Printing Out all Available Letters
# 0.0/10.0 points (graded)

# Next, implement the function getAvailableLetters that takes in one parameter - a list of letters, lettersGuessed. This function returns a string that is comprised of lowercase English letters - all lowercase English letters that are not in lettersGuessed.

# Example Usage:

# >>> lettersGuessed = ['e', 'i', 'k', 'p', 'r', 's']
# >>> print(getAvailableLetters(lettersGuessed))
# abcdfghjlmnoqtuvwxyz

# Note that this function should return the letters in alphabetical order, as in the example above.

# For this function, you may assume that all the letters in lettersGuessed are lowercase.

# Hint: You might consider using string.ascii_lowercase, which is a string comprised of all lowercase letters:

# import string
# print(string.ascii_lowercase)
# abcdefghijklmnopqrstuvwxyz

    