a = 'a'
b = 'b'
def fact(n):
    if n == 0:
        return 1
    else:
        return n * fact(n-1)
def comb(n, r):
    return fact(n)//(fact(n-r)*fact(r))
''' Binomial Expansion: Summation from r = 0 to r = n of [comb(n, r) * a^(n-r) * b^(n-r)]'''
def binomial(a, b, n):
    
