def classify(number):
    
    if number <=0 :
        raise ValueError("error number cant zero or neg")

    factors = [i for i in range(1,number) if number%i ==0]
    
    if sum(factors) == number: return "perfect"
    if sum(factors) <= number: return "deficient"
    return "abundant"