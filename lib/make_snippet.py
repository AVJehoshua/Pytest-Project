
def make_snippet(string):
    if len(string.split()) <= 5:
        return string
    else:
        return " ".join(string.split()[:5]) + "..."