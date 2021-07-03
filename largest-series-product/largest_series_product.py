from functools import reduce
from operator import  mul

def largest_product(series, size):
    if size > len(series) or size<0:
        raise ValueError('size cannot more than length of series or smaller than zero')
    
    series = list(map(int,series))
    idx_fst, idx_lst =  0,size
    maxProd = 0

    while idx_fst+size <= len(series):
        prod  = reduce(mul, series[idx_fst:idx_lst],1)
        if prod> maxProd :
            maxProd = prod
        idx_fst+=1
        idx_lst+=1
    return maxProd

