import random
from math import *
from numbertheorylists import *

functions_in_this_package = {"is_prime": "a primality test Miller-Rabin",
                             "is_merrsenne": "Lucas Lehmer merssene prime test",
                             "prime_gen": "genorates primes",
                             "merrsenne_gen": "genorates merssene primes",
                             "factor": "factors a number"}


# import statistics
# import cmath


# Prime stuff
def is_prime_2(num):
    for i in range(2, ceil((sqrt(num))) + 1):
        if (num / i) % 1 != 0:
            return False
    return True


# def is_prime(num):
#     # Returns True if num is a prime number.
#
#     s = num - 1
#     t = 0
#     while s % 2 == 0:
#         # keep halving s while it is even (and use t
#         # to count how many times we halve s)
#         s = s // 2
#         t += 1
#
#     for trials in range(5):  # try to falsify number's primality 5 times
#         a = random.randrange(2, num - 1)
#         v = pow(a, s, num)
#         if v != 1:  # this test does not apply if v is 1.
#             i = 0
#             while v != (num - 1):
#                 if i == t - 1:
#                     return False
#                 else:
#                     i = i + 1
#                     v = (v ** 2) % num
#     return True


def pi_function(x):
    rx = int(sqrt(x))
    sieve = [0 for _ in range(rx + 1)]
    n = x
    for p in range(2, rx + 1):
        if sieve[p] == 0:
            n = n - n // p + 1
            for q in range(p * p, rx + 1, p):
                sieve[q] = 1
    n = n - 1
    return n


def is_merrsenne(p):
    s = 4
    m = pow(2, p) - 1
    for i in range(1, p - 1):
        s = (pow(s, 2) - 2) % m
    if s == 0:
        return pow(2, p) - 1


def merrsenne_gen(n):
    answer = []
    for j in range(1, n):
        if is_merrsenne(j):
            print(is_merrsenne(j))
            n = input("Continue?")
            answer.append(j)
            if "continue" not in n.lower():
                return answer


def prime_gen(m, n):
    ans = []
    m = m - (m % 6) + 1
    for i in range(m, n, 2):
        if is_prime_2(i):
            print(i)
        i = i + 4
        ans.append(i)
    return ans


def prime_factor(number):
    ans = []
    for i in range(2, number):
        if is_prime_2(i):
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


def totient_fuction(mod):
    m = mod
    units = []
    for i in range(1, m):
        if gcd(i, m) == 1:
            units.append(i)
    ans = len(units)
    return ans


def nth_power(stop, power):
    ans = []
    for i in range(1, stop + 1):
        power = i ** power
        ans.append(power)
    return ans


def pascal_triangle(n, x):
    ans = 1
    for i in range(0, x):
        number = n - i
        ans = number * ans
    ans = ans / factorial(x)
    return int(ans)


# def pascal_triangle_gen(stop):
#     for i in range(1, stop + 1):
#         for x in range(1, i + 1):
#             print(pascal_triangle(i, x))


def d(n, m):
    if (m / n) % 1 == 0:
        return True


def choose(n, k):
    num = factorial(n)
    den = factorial(n - k) * factorial(k)
    return num / den


def partition(n):
    ans = []
    current_partition = []
    function_done = False
    partition_over = False
    number_of_partitions = bell_numbers[n + 1]
    last_one = 1

    while not function_done:
        to_go = n
        unit = 0
        while not partition_over:
            unit = random.randint(1, to_go)
            to_go = to_go - unit
            current_partition.append(unit)
            if to_go == 0:
                partition_over = True
        partition_over = False
        if current_partition not in ans:
            ans.append(current_partition)
            print(current_partition)
        current_partition = []
        if len(ans) == number_of_partitions:
            function_done = True
    return ans
