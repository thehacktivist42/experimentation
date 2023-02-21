def get_super(x):
    normal = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+-=()"
    super_s = "ᴬᴮᶜᴰᴱᶠᴳᴴᴵᴶᴷᴸᴹᴺᴼᴾQᴿˢᵀᵁⱽᵂˣʸᶻᵃᵇᶜᵈᵉᶠᵍʰᶦʲᵏˡᵐⁿᵒᵖ۹ʳˢᵗᵘᵛʷˣʸᶻ⁰¹²³⁴⁵⁶⁷⁸⁹⁺⁻⁼⁽⁾"
    res = x.maketrans(''.join(normal), ''.join(super_s))
    return x.translate(res)
a = input("Enter the first variable: ")
b = input("Enter the second variable: ")
n = int(input("Enter the power: "))
def fact(n):
    if n == 0:
        return 1
    else:
        return n * fact(n-1)
def comb(n, r):
    return fact(n)//(fact(n-r)*fact(r))
''' Binomial Expansion: Summation from r = 0 to r = n of [comb(n, r) * a^(n-r) * b^r]'''
def binomial(a, b, n):
    ac, bc = 1, 1
    try:
        ac = int(''.join([i for i in list(a) if i.isdigit()]))
        ast = ''.join([i for i in list(a) if not i.isdigit()])
    except ValueError:
        pass 
    try:
        bc = int(''.join([i for i in list(b) if i.isdigit()]))
        bst = ''.join([i for i in list(b) if not i.isdigit()])
    except ValueError:
        pass
    ans = []
    for r in range(n+1):
        if r == 0:
            if ac != 1:
                ans.append(str(ac**n)+ast+get_super(str(n)))
            else:
                ans.append(a+get_super(str(n)))
        elif r == n:
            if bc != 1:
                ans.append(str(bc**n)+bst+get_super(str(n)))
            else:
                ans.append(b+get_super(str(n)))
        elif r == 1:
            if ac != 1 and bc != 1:
                ans.append(str(comb(n, r)*(ac**(n-r))*(bc**r))+ast+get_super(str(n-r))+bst)
            elif ac != 1 and bc == 1:
                ans.append(str(comb(n, r)*(ac**(n-r)))+ast+get_super(str(n-r))+b)
            elif ac == 1 and bc != 1:
                ans.append(str(comb(n, r)*(bc**r))+a+get_super(str(n-r))+bst)
            else:
                ans.append(str(comb(n, r))+a+get_super(str(n-r))+b)
        elif r == n-1:
            if ac != 1 and bc != 1:
                ans.append(str(comb(n, r)*(ac**(n-r))*(bc**r))+ast+bst+get_super(str(r)))
            elif ac != 1 and bc == 1:
                ans.append(str(comb(n, r)*(ac**(n-r)))+ast+b+get_super(str(r)))
            elif ac == 1 and bc != 1:
                ans.append(str(comb(n, r)*(bc**r))+a+bst+get_super(str(r)))
            else:
                ans.append(str(comb(n, r))+a+b+get_super(str(r)))
        else:
            if ac != 1 and bc != 1:
                ans.append(str(comb(n, r)*(ac**(n-r))*(bc**r))+ast+get_super(str(n-r))+bst+get_super(str(r)))
            elif ac != 1 and bc == 1:
                ans.append(str(comb(n, r)*(ac**(n-r)))+ast+get_super(str(n-r))+b+get_super(str(r)))
            elif ac == 1 and bc != 1:
                ans.append(str(comb(n, r)*(bc**r))+a+get_super(str(n-r))+bst+get_super(str(r)))
            else:
                ans.append(str(comb(n, r))+a+get_super(str(n-r))+b+get_super(str(r)))
    return '  +  '.join(ans)
print(f"The Binomial Expansion for ({a}+{b}){get_super(str(n))} is: {binomial(a, b, n)}")