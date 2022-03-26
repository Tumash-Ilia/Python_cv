# -*- coding: utf-8 -*-

"""
@TODO: zde napiste svoje unit testy pro program codes.py
"""
import codes


def test_prime_generator():
    """
    Test generatoru prvocisel
    """
    out = [11, 13, 17, 19, 23, 29]
    result = codes.atkin_sieve(10, 30)
    assert out == result


def test_find_codes():
    """
    Test z elearningu
    """
    out = [56003, 56113, 56333, 56443, 56663, 56773, 56993]
    prime_num = codes.atkin_sieve(10 ** 4, 10 ** 5 - 1)
    assert out == codes.find_codes(prime_num, 2)
