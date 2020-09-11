import operator
def distance(strand_a, strand_b):
    if len(strand_a)!=len(strand_b):
         raise ValueError("strand_a and strand_b should be equal in length")

    #return len(list(filter(lambda match:match==True, map(lambda pair:pair[0]!=pair[1],zip(strand_a,strand_b)))))
    def iter(strand_a,strand_b,count):
        if len(strand_a)==0:
            return count
        if strand_a[0]!=strand_b[0]:
            count+=1
        return iter(strand_a[1:],strand_b[1:],count)
    return iter(strand_a,strand_b,0)

print(distance("GGACGGATTCTG", "AGGACGGATTCT"))
