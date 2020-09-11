def is_pangram(sentence):
    sentence = sentence.strip('"').lower()
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    for char in alphabet:
         if char not in sentence:
             return False
    return True
