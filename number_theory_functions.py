import math

def primitive_root(n):
    primitive_roots = []
    coprime_to_n = []
    for i in range(1, n):
        if math.gcd(n, i) == 1:
            coprime_to_n.append(i)
    for i in range(1, n):
        powers_of_i = []
        for e in range(1, n):
            powers_of_i.append(i**e % n)
        if sorted(powers_of_i) == coprime_to_n:
            primitive_roots.append(i)
    return primitive_roots

def root_equivalents(modulus, root):
    root_equivalents = []
    for i in range(0, modulus):
        if i**2 % modulus == root:
            root_equivalents.append(i)
    return root_equivalents

def is_prime_Wilsons_Theorem(n):
    if math.factorial(n - 1) % n == n - 1:
        return True
    else:
        return False


def sumset_exploration(set_A, set_B): # a tool for exploring various sumsets
    set_A = set(set_A)
    set_B = set(set_B)
    sumset = []
    for a in set_A:
        for b in set_B:
            sumset.append(a + b)
    sumset = set(sumset)
    return sumset

import itertools
def partition(n):
    partitions = []
    l = ""
    for i in range(1, n + 1):
        l += str(i)
    for i in range(1, n + 1):
        comb = itertools.product(l, repeat=i)
        for element in comb:
            z = 0
            for character in element:
                z += int(character)
            if z == n:
                new_part = []
                for e in element:
                    new_part.append(int(e))
                if sorted(new_part) not in partitions:
                    partitions.append(new_part)
    return partitions

# Pigeonhole functions
def socks(colors, number_needed):
    return (number_needed - 1)*(colors)

print(socks(2, 2))