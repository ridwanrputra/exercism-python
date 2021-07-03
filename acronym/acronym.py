def abbreviate(words):
    words = words.replace("-",' ').replace("_","").upper().split()
    return "".join(word[0] for word in words)