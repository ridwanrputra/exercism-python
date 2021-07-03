def distance(strand_a, strand_b):
    if len(strand_a)!=len(strand_b):
         raise ValueError("strand_a and strand_b should be equal in length")

    return sum(char_a != char_b for char_a, char_b in zip(strand_a, strand_b))
