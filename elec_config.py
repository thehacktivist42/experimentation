### Program to calculate the Electronic Configuration of an element using its atomic number
### Designed and programmed by Harivansh Mehta.
### Copyright © 2022
### All rights reserved.

elements = {
    1: ['Hydrogen',    'H',  [-1, 1],    []],
    2: ['Helium',      'He', [],         [1, 2]],
    3: ['Lithium',     'Li', [1],        []],
    4: ['Beryllium',   'Be', [2],        [1]],
    5: ['Boron',       'B',  [3],        [-5, -1, 1, 2]],
    6: ['Carbon',      'C',  [-4, -3, -2, -1, 1, 2, 3, 4], []],
    7: ['Nitrogen',    'N',  [-3, 3, 5], [-2, -1, 1, 2, 4]],
    8: ['Oxygen',      'O',  [-2],       [-1, 1, 2]],
    9: ['Fluorine',    'F',  [-1],       []],
    10: ['Neon',       'Ne', [],         []],
    11: ['Sodium',     'Na', [1],        [-1]],
    12: ['Magnesium',  'Mg', [2],        [1]],
    13: ['Aluminum',   'Al', [3],        [-2, -1, 1, 2]],
    14: ['Silicon',    'Si', [-4, 4],    [-3, -2, -1, 1, 2, 3]],
    15: ['Phosphorus', 'P',  [-3, 3, 5], [-2, -1, 1, 2, 4]],
    16: ['Sulfur',     'S',  [-2, 2, 4, 6],    [-1, 1, 3, 5]],
    17: ['Chlorine',   'Cl', [-1, 1, 3, 5, 7], [2, 4, 6]],
    18: ['Argon',      'Ar', [],         []],
    19: ['Potassium',  'K',  [1],        [-1]],
    20: ['Calcium',    'Ca', [2],        [1]],
    21: ['Scandium',   'Sc', [3],        [1, 2]],
    22: ['Titanium',   'Ti', [4],        [-2, -1, 1, 2, 3]],
    23: ['Vanadium',   'V',  [5],        [-3, -1, 1, 2, 3, 4]],
    24: ['Chromium',   'Cr', [3, 6],     [-4, -2, -1, 1, 2, 4, 5]],
    25: ['Manganese',  'Mn', [2, 4, 7],  [-3, -2, -1, 1, 3, 5, 6]],
    26: ['Iron',       'Fe', [2, 3, 6],  [-4, -2, -1, 1, 4, 5, 7]],
    27: ['Cobalt',     'Co', [2, 3],     [-3, -1, 1, 4, 5]],
    28: ['Nickel',     'Ni', [2],        [-2, -1, 1, 3, 4]],
    29: ['Copper',     'Cu', [2],        [-2, 1, 3, 4]],
    30: ['Zinc',       'Zn', [2],        [-2, 1]],
    31: ['Gallium',    'Ga', [3],        [-5, -4, -2, -1, 1, 2]],
    32: ['Germanium',  'Ge', [-4, 2, 4], [-3, -2, -1, 1, 3]],
    33: ['Arsenic',    'As', [-3, 3, 5], [-2, -1, 1, 2, 4]],
    34: ['Selenium',   'Se', [-2, 2, 4, 6], [-1, 1, 3, 5]],
    35: ['Bromine',    'Br', [-1, 1, 3, 5], [4, 7]],
    36: ['Krypton',    'Kr', [2],        []],
    37: ['Rubidium',   'Rb', [1],        [-1]],
    38: ['Strontium',  'Sr', [2],        [1]],
    39: ['Yttrium',    'Y',  [3],        [1, 2]],
    40: ['Zirconium',  'Zr', [4],        [-2, 1, 2, 3]],
    41: ['Niobium',    'Nb', [5],        [-3, -1, 1, 2, 3, 4]],
    42: ['Molybdenum', 'Mo', [4, 6],     [-4, -2, -1, 1, 2, 3, 5]],
    43: ['Technetium', 'Tc', [4, 7],     [-3, -1, 1, 2, 3, 5, 6]],
    44: ['Ruthenium',  'Ru', [3, 4],     [-4, -2, 1, 2, 5, 6, 7, 8]],
    45: ['Rhodium',    'Rh', [3],        [-3, -1, 1, 2, 4, 5, 6]],
    46: ['Palladium',  'Pd', [2, 4],     [1, 3, 5, 6]],
    47: ['Silver',     'Ag', [1],        [-2, -1, 2, 3, 4]],
    48: ['Cadmium',    'Cd', [2],        [-2, 1]],
    49: ['Indium',     'In', [3],        [-5, -2, -1, 1, 2]],
    50: ['Tin',        'Sn', [-4, 2, 4], [-3, -2, -1, 1, 3]],
    51: ['Antimony',   'Sb', [-3, 3, 5], [-2, -1, 1, 2, 4]],
    52: ['Tellurium',  'Te', [-2, 2, 4, 6], [-1, 1, 3, 5]],
    53: ['Iodine',     'I',  [-1, 1, 3, 5, 7], [4, 6]],
    54: ['Xenon',      'Xe', [2, 4, 6],  [8]],
    55: ['Cesium',     'Cs', [1],        [-1]],
    56: ['Barium',     'Ba', [2],        [1]],
    57: ['Lanthanum',  'La', [3],        [1, 2]],
    58: ['Cerium',     'Ce', [3, 4],     [2]],
    59: ['Praseodymium', 'Pr', [3],      [2, 4, 5]],
    60: ['Neodymium',  'Nd', [3],        [2, 4]],
    61: ['Promethium', 'Pm', [3],        [2]],
    62: ['Samarium',   'Sm', [3],        [2]],
    63: ['Europium',   'Eu', [2, 3],     []],
    64: ['Gadolinium', 'Gd', [3],        [1, 2]],
    65: ['Terbium',    'Tb', [3],        [1, 2, 4]],
    66: ['Dysprosium', 'Dy', [3],        [2, 4]],
    67: ['Holmium',    'Ho', [3],        [2]],
    68: ['Erbium',     'Er', [3],        [2]],
    69: ['Thulium',    'Tm', [3],        [2]],
    70: ['Ytterbium',  'Yb', [3],        [2]],
    71: ['Lutetium',   'Lu', [3],        [2]],
    72: ['Hafnium',    'Hf', [4],        [-2, 1, 2, 3]],
    73: ['Tantalum',   'Ta', [5],        [-3, -1, 1, 2, 3, 4]],
    74: ['Tungsten',   'W',  [4, 6],     [-4, -2, -1, 1, 2, 3, 5]],
    75: ['Rhenium',    'Re', [4],        [-3, -1, 1, 2, 3, 5, 6, 7]],
    76: ['Osmium',     'Os', [4],        [-4, -2, -1, 1, 2, 3, 5, 6, 7, 8]],
    77: ['Iridium',    'Ir', [3, 4],     [-3, -1, 1, 2, 5, 6, 7, 8, 9]],
    78: ['Platinum',   'Pt', [2, 4],     [-3, -2, -1, 1, 3, 5, 6]],
    79: ['Gold',       'Au', [3],        [-3, -2, -1, 1, 2, 5]],
    80: ['Mercury',    'Hg', [1, 2],     [-2, 4]],
    81: ['Thallium',   'Tl', [1, 3],     [-5, -2, -1, 2]],
    82: ['Lead',       'Pb', [2, 4],     [-4, -2, -1, 1, 3]],
    83: ['Bismuth',    'Bi', [3],        [-3, -2, -1, 1, 2, 4, 5]],
    84: ['Polonium',   'Po', [-2, 2, 4], [5, 6]],
    85: ['Astatine',   'At', [-1, 1],    [3, 5, 7]],
    86: ['Radon',      'Rn', [2],        [6]],
    87: ['Francium',   'Fr', [1],        []],
    88: ['Radium',     'Ra', [2],        []],
    89: ['Actinium',   'Ac', [3],        []],
    90: ['Thorium',        'Th', [4],    [1, 2, 3]],
    91: ['Protactinium',   'Pa', [5],    [3, 4]],
    92: ['Uranium',        'U',  [6],    [1, 2, 3, 4, 5]],
    93: ['Neptunium',      'Np', [5],    [2, 3, 4, 6, 7]],
    94: ['Plutonium',      'Pu', [4],    [2, 3, 5, 6, 7]],
    95: ['Americium',      'Am', [3],    [2, 4, 5, 6, 7]],
    96: ['Curium',         'Cm', [3],    [4, 6]],
    97: ['Berkelium',      'Bk', [3],    [4]],
    98: ['Californium',    'Cf', [3],    [2, 4]],
    99: ['Einsteinium',    'Es', [3],    [2, 4]],
    100: ['Fermium',       'Fm', [3],    [2]],
    101: ['Mendelevium',   'Md', [3],    [2]],
    102: ['Nobelium',      'No', [2],    [3]],
    103: ['Lawrencium',    'Lr', [3],    []],
    104: ['Rutherfordium', 'Rf', [4],    []],
    105: ['Dubnium',       'Db', [5],    []],
    106: ['Seaborgium',    'Sg', [6],    []],
    107: ['Bohrium',       'Bh', [7],    []],
    108: ['Hassium',       'Hs', [8],    []],
    109: ['Meitnerium',    'Mt', [],     []],
    110: ['Darmstadtium',  'Ds', [],     []],
    111: ['Roentgenium',   'Rg', [],     []],
    112: ['Copernicium',   'Cn', [2],    []],
    113: ['Nihonium',      'Nh', [],     []],
    114: ['Flerovium',     'Fl', [],     []],
    115: ['Moscovium',     'Mc', [],     []],
    116: ['Livermorium',   'Lv', [],     []],
    117: ['Tennessine',    'Ts', [],     []],
    118: ['Oganesson',     'Og', [],     []]
}

def key(dict, elem): # Another QoL function for accessing the key of a dictionary element from its value.
    return list(dict.keys())[list(dict.values()).index(elem)]

orbitals = { # Key-value pairs of orbitals and their azimuthal quantum number values
    0 : 's',
    1 : 'p',
    2 : 'd',
    3 : 'f'
}

iupacNames = { # Key-value pairs of numbers and their IUPAC nomenclature for elements with atomic number > 119
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
            subshells.append(str(i)+j) # Creates a list of all possible subshells for principal quantum numbers 1 to 9 (i.e, from 1s to 9f). This range can be modified as per need.

subshells_dict = {}

for i in subshells:
    subshells_dict[i] = int(i[0])+ key(orbitals, i[1])
subshells = [i[0] for i in sorted(subshells_dict.items(), key = lambda x : x[1])] # Sorts the list according to their ascending n+l value as per Aufbau principle.

electrons = { # Key-value pairs of orbitals and their maximum electron capacity
    's' : 2,
    'p' : 6,
    'd' : 10,
    'f' : 14
}

def electronicConfiguration(n): # MAIN FUNCTION
    if n == 24: # Exceptional electronic configuration of Chromium
        return "1s2 2s2 2p6 3s2 3p6 4s1 3d5"
    elif n == 29: # Exceptional electronic configuration of Copper
        return "1s2 2s2 2p6 3d2 3p6 4s1 3d10"
    global subshells, electrons
    at = 0
    li = []
    for i in subshells:
        k = 0
        if at == n:
            break
        sub = electrons[i[1]]
        k = min(n-at, sub) # If subshell is fully filled, adds the max number of electrons, else, adds the number of electrons left
        li.append(i+str(k))
        at+=k
    return ' '.join(li)

def iupacName(n): # Function to define the names of elements with atomic number more than 119 (not present in periodic table).
    global iupacNames
    li = list(str(n))
    st = ""
    sym = ""
    for i in li:
        st += iupacNames[int(i)]
        sym += iupacNames[int(i)][0]
    st += 'ium'
    return st.capitalize() + " (" + sym.capitalize() + ")"

def elemSearch(n): # Searches the elements by atomic number in the elements dictionary and returns the names of the element.
    global elements
    return elements[n][0] + " (" + elements[n][1] + ")"

n = int(input("Enter the atomic number of the element: "))
if n <= 118: # For elements present in periodic table, their proper name is used.
    elem = elemSearch(n)
else:
    elem = iupacName(n) # For elements not present in periodic table, their IUPAC name is used.
print(f"The electronic configuration of the element {elem} having atomic number {n} is:", electronicConfiguration(n))
end = input("Press Enter to quit.")