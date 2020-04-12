from math import *
from itertools import *

functions_in_this_package = {"is_prime": "a primality test Miller-Rabin",
                             "is_mersenne": "Lucas Lehmer mersenne prime test",
                             "prime_gen": "generates primes",
                             "mersenne_gen": "generates mersenne_gen primes",
                             "factor": "factors a number",
                             "partition": "partitions a number",
                             "primitive_root": "finds primitive roots modulo n",
                             "root_equivalents": "finds numbers modulo n equivalent to root given its square",
                             "sumset_exploration": "a tool for exploring various sumsets",
                             "pigeon_hole": "finds number of theoretical socks needed to be pulled blindly to ensure a certain number of socks of the same color"}


# import statistics
# import cmath


# Prime stuff


def is_prime_wilson_theorem(n):
    if factorial(n - 1) % n == n - 1:
        return True
    else:
        return False


def pythagorean_theorem(num):
    for i in range(1, num ** 2):
        pass


def is_prime(num):
    prime = True
    if (num % 2 != 0 or 2) and num != 1:
        for i in range(2, num):
            if num % i == 0:
                prime = False
    else:
        prime = False
    return prime


def prime_gen(start, stop):
    ans = []
    for i in range(start, stop + 1):
        if is_prime(i):
            ans.append(i)
    return ans


def lucas_lehmer(p):
    s = 4
    m = pow(2, p) - 1
    for i in range(1, p - 1):
        s = (pow(s, 2) - 2) % m
    if s == 0:
        return True, pow(2, p) - 1


def lucas_lehmer_gen(start, stop):
    answer = []
    for j in range(start, stop + 1):
        if lucas_lehmer(j):
            print(j, lucas_lehmer(j))
            answer.append(j ** 2 - 1)
        return answer


def prime_factor(number):
    ans = []
    for i in range(2, number):
        if is_prime(i):
            x = 0
            while x == 1:
                if number % i == 0:
                    ans.append(i)
                    number = int(number / i)
                else:
                    x = 2
            if number == 1:
                return ans


def factor(number):
    result = []
    for i in range(1, number + 1):
        if number % i == 0:
            result.append(i)
    return result


def find_lcm(m, n):
    result = m * n / gcd(m, n)
    print(result)


def totient_fuction(m, print_units):
    units = []
    for i in range(1, m + 1):
        if gcd(i, m) == 1:
            units.append(i)
    ans = len(units)
    if not print_units:
        return ans
    else:
        return ans, units


def nth_power(stop, power):
    ans = []
    for i in range(1, stop + 1):
        power = i ** power
        ans.append(power)
    return ans


def pascal_triangle(n, x):
    ans = 1
    for i in range(0, x + 1):
        number = n - i
        ans = number * ans
    ans = ans / factorial(x)
    return int(ans)


def pascals_triangle(stop):
    ans = []
    for n in range(1, stop + 1):
        l = [1]
        for k in range(1, n):
            l.append(pascal_triangle(n, k))
        l.append(1)
        print(l)
        ans.append(l)
    return ans


def d(n, m):
    if (m / n) % 1 == 0:
        return True


def partition(n):
    partitions = []
    l = ""
    for i in range(1, n + 1):
        l += str(i)
    for i in range(1, n + 1):
        comb = product(l, repeat=i)
        for element in comb:
            z = 0
            for character in element:
                z += int(character)
            if z == n:
                new_part = []
                for item in element:
                    new_part.append(int(item))
                if sorted(new_part) not in partitions:
                    partitions.append(new_part)
    return partitions


def primitive_root(n):
    primitive_roots = []
    coprime_to_n = []
    for i in range(1, n):
        if gcd(n, i) == 1:
            coprime_to_n.append(i)
    for i in range(1, n):
        powers_of_i = []
        for x in range(1, n):
            powers_of_i.append(i ** x % n)
        if sorted(powers_of_i) == coprime_to_n:
            primitive_roots.append(i)
    return primitive_roots


def root_equivalents(modulus, square_of_root):
    root_equivalent = []
    for i in range(0, modulus):
        if i ** 2 % modulus == square_of_root:
            root_equivalent.append(i)
    return root_equivalent


def sumset_exploration(set_a, set_b):
    sum_set = []
    for a in set_a:
        for b in set_b:
            sum_set.append(a + b)
    sum_set = set(sum_set)
    return sum_set


def pigeon_hole(colors, number_needed):
    return (number_needed - 1) * colors