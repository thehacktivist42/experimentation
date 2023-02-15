from periodictable import elements

def key(dict, elem):
    return list(dict.keys())[list(dict.values()).index(elem)]

orbitals = {
    0 : 's',
    1 : 'p',
    2 : 'd',
    3 : 'f'
}

iupacNames = {
    0 : 'nil',
    1 : 'un',
    2 : 'bi',
    3 : 'tri',
    4 : 'quad',
    5 : 'pent',
    6 : 'hex',
    7 : 'hept',
    8 : 'oct',
    9 : 'enn'
}

subshells = []

for i in range(1,10):
    for j in ['s','p','d','f']:
        if key(orbitals, j) < i:
            subshells.append(str(i)+j)

subshells_dict = {}

for i in subshells:
    subshells_dict[i] = int(i[0])+ key(orbitals, i[1])
subshells = [i[0] for i in sorted(subshells_dict.items(), key = lambda x : x[1])]

electrons = {
    's' : 2,
    'p' : 6,
    'd' : 10,
    'f' : 14
}

def electronicConfiguration(n):
    if n == 24:
        return "1s2 2s2 2p6 3s2 3p6 4s1 3d5"
    elif n == 29:
        return "1s2 2s2 2p6 3d2 3p6 4s1 3d10"
    global subshells, electrons
    at = 0
    li = []
    for i in subshells:
        k = 0
        if at == n:
            break
        sub = electrons[i[1]]
        k = min(n-at, sub)
        li.append(i+str(k))
        at+=k
    return ' '.join(li)

def iupacName(n):
    global iupacNames
    li = list(str(n))
    st = ""
    for i in li:
        st += iupacNames[int(i)]
    st += 'ium'
    return st.capitalize()

def elemSearch(n):
    global elements
    for el in elements:
        if el.number == n:
            return el.name.capitalize()

n = int(input("Enter the atomic number of the element: "))
if n <= 118:
    elem = elemSearch(n)
else:
    elem = iupacName(n)
print(f"The electronic configuration of the element {elem} having atomic number {n} is:", electronicConfiguration(n))
