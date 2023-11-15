# Write tests for a function called 'make snippet' which takes a string as
# an argument, and returns the first 5 words and then '...' if there are
# more than 5 words

"""
Possible outcomes: 

1 - if string given is empty string, return empty string

2 - if string given has exactly 3  words, return string as is

3 - if string given has exactly 4 words, return string as is

4 - if string given has exactly 5 words, return string as is 

5 - if string given has more than 5 words, stop at 5 and add ... to the end

6 - if string given is a very long string, stop at 5 and add ... to the end


"""
from lib.make_snippet import *

# Writing a test to check if string is empty, if so, return empty string:

def test_if_string_given_is_empty_string():
    assert make_snippet("") == ""

# Writing a test to check if string has 3 words, return string:

def test_if_string_given_has_3_words():
    assert make_snippet("Embrace the absurd") == "Embrace the absurd"


# Writing a test to check if string has 4 words, return string:

def test_if_string_given_has_4_words():
    assert make_snippet("Embrace the absurd bitch") == "Embrace the absurd bitch"


# Writing a test to check if string has 5 words, return string:

def test_if_string_given_has_5_words():
    assert make_snippet("My name is Jehoshua Lawal") == "My name is Jehoshua Lawal"


# Writing a test to check if string has more than 5 words, then truncate:

def test_if_str_has_more_than_5_words_and_truncate():
    assert make_snippet("Tomorrow the weather will be sunny") == "Tomorrow the weather will be..."


# Writing a test to check truncate a very long string:

def test_if_very_long_string_can_be_shortened():
    assert make_snippet("Tomorrow the weather will be sunny, the day after that it will be rainy, the year after that it will be absurd. life is absurd. embrace it") == "Tomorrow the weather will be..."