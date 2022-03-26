# -*- coding: utf-8 -*-

"""
@TODO - vyřešit úkol 12.

Podrobné zadání jako obvykle na https://elearning.tul.cz

"""
import collections
import time

from math import sqrt


def atkin_sieve(nmin, nmax):
    """
    Hledani mnoziny prvocisel pomoci 'Sieve of Atkin' algoritmu
    https://en.wikipedia.org/wiki/Sieve_of_Atkin
    """
    is_prime = dict([(i, False) for i in range(5, nmax + 1)])
    for var_x in range(1, int(sqrt(nmax)) + 1):
        for var_y in range(1, int(sqrt(nmax)) + 1):
            number = 4 * var_x ** 2 + var_y ** 2
            if (number <= nmax) and ((number % 12 == 1) or (number % 12 == 5)):
                is_prime[number] = not is_prime[number]
            number = 3 * var_x ** 2 + var_y ** 2
            if (number <= nmax) and (number % 12 == 7):
                is_prime[number] = not is_prime[number]
            number = 3 * var_x ** 2 - var_y ** 2
            if (var_x > var_y) and (number <= nmax) and (number % 12 == 11):
                is_prime[number] = not is_prime[number]
    for number in range(5, int(sqrt(nmax)) + 1):
        if is_prime[number]:
            i_k = 1
            while i_k * number ** 2 <= nmax:
                is_prime[i_k * number ** 2] = False
                i_k += 1
    primes = []
    for i in range(nmin, nmax + 1):
        if i in [0, 1, 4]:
            pass
        elif i in [2, 3] or is_prime[i]:
            primes.append(i)
        else:
            pass
    return primes


def find_codes(prime_array, y_cnt):
    """
    Hledani mnoziny prvocisel podle pozadavek
    :param prime_array: pole prvocisel
    :param y_cnt: pocet cislic ktere se bodou menit
    :return:
    """
    for i in prime_array:
        codes = []
        number_str = str(i)
        numbers_cnt = collections.Counter(number_str)
        for key, value in numbers_cnt.items():
            if value == y_cnt:
                numeral = key
                counter = 0
                for substitute in range(10):
                    number = int(number_str.replace(numeral, str(substitute)))
                    if number in prime_array:
                        counter = counter + 1
                        codes.append(number)
                        if counter == len(number_str) + 2:
                            return codes
    return None


def save_to_file(content):
    """
    Vypis do souboru
    :param content: data k ukladani
    """
    with open("new_codes.txt", 'w') as file:
        for num in content:
            file.write(str(num) + "\n")


if __name__ == '__main__':
    tic = time.perf_counter()
    at = atkin_sieve(10 ** 5, 10 ** 6 - 1)
    a = find_codes(at, 3)
    print(a)
    save_to_file(a)
    toc = time.perf_counter()
    print(f"Finished in  {toc - tic:0.4f} seconds")
