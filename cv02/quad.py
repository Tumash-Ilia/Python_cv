#!/bin/env python
# -*- coding: utf-8 -*-
"""
PJP - cvičení číslo 2
"""


# funkce pro skalarni soucin
def soucin(a, b):
    ab = a[0] * b[1] - a[1] * b[0]
    return ab


def is_convex(a, b, c, d):
    """
    Druhým úkolem je vytvořit funkci, která ze čtyř zadaných bodů určí,
    zda tvoří konvexní čtyřúhelník.
    
    Body na vstupu jsou zadávány jako tuple (x, y) kde x a y mohou být
    libovolná reálná čísla, tedy i záporná. Body mohou vytvořit čtyřúhelník,
    ale není to pravidlem.

    Je potřeba aby funkce hlídala i extrémní situace, jako například,
    že body čtyřúhelník vůbec nevytváří. 
    """
    """
    1. zkontroluju zda 4 body vytvari ctyruhelnik
    """
    tup = (a, b, c, d)
    for i in range(len(tup)):
        for j in range(i + 1, len(tup)):
            if tup[i] == tup[j]:
                return False
    """
    2. najdu souradnice vektoru, ktere tvori hrany
    """
    ab = (b[0] - a[0], b[1] - a[1])
    bc = (c[0] - b[0], c[1] - b[1])
    cd = (d[0] - c[0], d[1] - c[1])
    da = (a[0] - d[0], a[1] - d[1])
    """
    3. najdu skalarni soucin vsech dvojic hran
    """
    abbc = soucin(ab, bc)
    bccd = soucin(bc, cd)
    cdda = soucin(cd, da)
    daab = soucin(da, ab)
    """
    4. Pokud ctyruhelnik je konvexni vsechny skalarni souceny musi mit stejne znamenko.
       Jestli jeden soucin se lisi znamenkem od ostatnich, tam bude konkavni vrchol   
    """
    if abbc >= 0:
        if bccd < 0 or cdda < 0 or daab < 0:
            return False
    else:
        if bccd > 0 or cdda > 0 or daab > 0:
            return False
    return True


if __name__ == '__main__':
    is_convex((0.0, 0.0), (1.0, 0.0), (1.0, 1.0), (0.0, 1.0))
