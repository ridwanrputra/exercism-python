
def primes(limit):
    passNumber = []
    primeList = []

    for i in range(2,limit+1):
        if i not in passNumber:
            primeList.append(i)
            for j in range(i*i, limit+1,i):
                passNumber.append(j)

    return primeList

