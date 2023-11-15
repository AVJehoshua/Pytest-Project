"""
1 - describe the problem :

As a user,
So that I can manage my time,
I want to see an estimate of reading time for a text, 
assuming that I can read 200 words a minute.

2 - Design the function signature:

Purpose: create a function, called 'time_manager()'
which tracks the time it takes for a reader,
to read a small text - reader reads at 200 words a minute

E.g: each page has 200 words, 
reader reads 3 pages, 
total time is 3 minutes.

Parameters: 1 string, representing the total num of pages,
(refer to example above)

Side effects: No side effects.

3 - Create examples as tests:

-* Test if string is an empty string, if so, return
0 minutes.

-* Test if string is not actually a string, but an integer, if so return
a nice error message

-* Test if string representing 1 page, returns 1 minute

-* Test if string representing 3 pages, returns 3 minutes

-* If string representing 5 pages, returns 5 minutes


"""

from lib.time_management import *

# Testing if string represting pages is higher than num of words,
# return nice error message.

page = 1

words = 200

def test_if_string_is_an_empty_string_return_0():
    assert time_manager("") == "0 minutes"

# Testing if the inputed parameter is a integer, and not a string:

def test_if_input_is_integer_not_string():
    assert time_manager(5) == "This is not a string, it's an integer!"

# Testing if inputed string representing 1 page, returns 1 minute:

def test_if_1_page_returns_reading_time_of_one_minute():
    assert time_manager("1") == "1 minute"

# Testing if inputed string representing 3 pages, returns 3 minutes:

def test_if_3_pages_returns_reading_time_of_3_minutes():
    assert time_manager("3") == "3 minutes"

# Testing if inputed string represeting 5 pages, returns 5 minutes:

def test_if_5_pages_returns_reading_time_of_5_minutes():
    assert time_manager("5") == "5 minutes"




