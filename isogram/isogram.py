def is_isogram(string):
    string = [char for char in string.lower() if char.isalnum()]
    return len(set(string)) == len(string)
