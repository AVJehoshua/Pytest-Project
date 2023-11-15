
def time_manager(string):
    if string == "":
        return "0 minutes"
    elif type(string) == int:
        return "This is not a string, it's an integer!"
    elif string == "1":
        return string + " minute"
    else:
        return string + " minutes"