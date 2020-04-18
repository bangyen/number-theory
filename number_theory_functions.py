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
    root_equivalent = []
    for i in range(0, modulus):
        if i**2 % modulus == root:
            root_equivalent.append(i)
    return root_equivalent

def is_prime_wilsons_theorem(n):
    if math.factorial(n - 1) % n == n - 1:
        return True
    else:
        return False


def sum_set_exploration(set_a, set_b): # a tool for exploring various sum-sets
    set_a = set(set_a)
    set_b = set(set_b)
    sum_set = []
    for a in set_a:
        for b in set_b:
            sum_set.append(a + b)
    sum_set = set(sum_set)
    return sum_set


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
    return (number_needed - 1)*colors

print(socks(2, 2))
