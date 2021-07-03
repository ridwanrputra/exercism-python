
weight = {  1: "AEIOULNRST",
            2: "DG",
            3: "BCMP",
            4: "FHVMY",
            5: "K",
            8: "JX",
            10: "QZ",
          }


def score(word):
    return sum(k for k,v in weight.items() for char in word.upper() if char in v)
