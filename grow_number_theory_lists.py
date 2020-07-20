import numbertheorylists
import number_theory_essentials
far = input("How much do you want to grow the primes list")
numbertheorylists.primes = []
numbertheorylists.primes = number_theory_essentials.prime_gen(1, int(far)+1, want_list=True)
