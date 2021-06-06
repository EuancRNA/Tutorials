import math

@profile
def CalcPi(A,r):
    pi = A / math.pow(r,2)
    return(pi)

print( CalcPi(10,3) )
