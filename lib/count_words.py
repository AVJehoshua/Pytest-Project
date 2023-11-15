

def count_words(string):
    num = "1234567890"
    special_chars = "!@£$%^&*()"
    if string == "":
        return "There are no words in this string"
    elif any(item in string for item in num):
        return "This is a string of numbers!"
    elif any(item in string for item in special_chars):
        return "This is a string of special chars!"
    else:
        return len(string.split())