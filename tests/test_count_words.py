from lib.count_words import *

"""
Purpose: To create a function called count_words which takes a string, 
as an argument and returns num of words in that string


Possible outcomes: Assuming that the definition of 'word' are words in the
dictionary - 

1 - If string is an empty string, return 'There are no words in this string'

2 - If string has words within it, return the number of words in string

3 - If string is a string of numbers, return 'There are no words,
in this string.

4 - If string is a string of special_chars, return There are no,
words in this string

5 - 
"""

# Test to check if string given is an empty string, 
# return There are no words in this string:

def test_if_string_is_an_empty_string():
    assert count_words("") == "There are no words in this string"

# Test to see if string is a string of numbers, return There are no words,
# in this string.

def test_if_string_is_a_string_of_num():
    assert count_words("15") == "This is a string of numbers!"

# Test if string is a string of numbers, return "This is a string of numbers!":

def test_if_string_is_a_string_of_special_chars():
    assert count_words("!?") == "This is a string of special chars!"

# Test if string is a string of words, if so, return count of words:

def test_if_string_contains_words_return_num_of_words():
    assert count_words("Life is absurd, embrace it.") == 5


