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

# I (varun31415) created a primes class to put all the prime functions in I will leave the other functions there in case you want to leave it as is
# I also tried to rename the functions to make up for the class name 
class primes:
  class pi: # this class is for the prime pi function. I will put my sieve function in there and a bunch of others
    def sieve(num):
      pass# still working on it, I lost the previous code somewhere in my computer
    def regular(num): # please find a better name for this function
      pi = 0
      for i in range(2,num+1):
        if factorial(i- 1) % i = i- 1:
          pi = pi + 1
      return pi
  class primality_test:
    def wilsons_theorem(n):
      return factorial(n - 1) % n == n - 1
    def regular(num): # please try to find a better name for this function
      prime = True
      if (num % 2 != 0 or 2) and num != 1:
          for i in range(2, num):
              if num % i == 0:
                  prime = False
      else:
          prime = False
      return prime
    def merrsenne(p):
      s = 4
      m = pow(2, p) - 1
      for i in range(1, p - 1):
          s = (pow(s, 2) - 2) % m
      if s == 0:
          return pow(2, p) - 1
    
def is_prime_wilsons_theorem(n):
  return factorial(n - 1) % n == n - 1 # shortened it to one line, no need of if statements 
 
# pythagorean was originally spelled wrong. please rename all other cases of this function spelled wrong to prevent errors
def pythagorean_theorem(num):
    for i in range (1,num**2):
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

def is_prime(num):
    isprime = True
    if (num % 2 != 0 or 2) and num != 1:
        for i in range(2, num):
            if num % i == 0:
                isprime = False
    else:
        isprime = False
    return isprime


def prime_gen(start, stop):
    ans = []
    for i in range(start, stop + 1):
        if is_prime(i):
            ans.append(i)
    return ans


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


def totient_fuction(modulus, print_units):
    m = modulus
    units = []
    for i in range(1, m):
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
    for i in range(0, x):
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
        l = []
    return ans


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



