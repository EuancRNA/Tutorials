import math
import sys




# @profile
def Leibniz(n_terms):
    pi = 0
    n = 4
    d = 1
    for i in range(1,n_terms):
        a = 2 * ( i % 2 ) - 1
        pi += a * n / d
        d += 2
    print(pi)

n_times = int(sys.argv[1])
Leibniz(n_times)




# @profile
def Acos():
    pi = round(2*math.acos(0.0), 3);
    print(pi)

Acos()
