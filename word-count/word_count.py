from collections import Counter
import re


def count_words(sentence):
    sentence = re.sub("[^A-Za-z0-9 ',_\t]+","",sentence).lower().replace(","," ").replace("_"," ").split()
    sentence = [word.strip("'") for word in sentence]
    return Counter(sentence)
