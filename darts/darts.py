import math
def score(x, y):
    rad = math.sqrt(x*x+y*y)
    
    if rad <=1:
        return 10
    elif rad <=5:
        return 5
    elif rad <=10:
        return 1
    return 0
