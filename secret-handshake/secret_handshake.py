def binToHandshake(bin_):
    #if bin_
    pass

def commands(number):
    bin_ = bin(number)[2:]
    temp = []
    if int(bin_)>= 10000:
        return int("".join(reversed(bin_)))
    return bin_

print(commands(16))