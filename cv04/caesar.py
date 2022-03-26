"""
Vytvorte funkce encrypt a decrypt pro Caesarovu sifru.
Kompletni zadani v elearningu.
"""


def encrypt(word, offset):
    """
    :param word - slovo k zasifrovani
    :param offset - znakovy posun
    :return: zasifrovane slovo
    """
    letters = "abcdefghijklmnopqrstuvwxyz"
    encrypted = ""
    for sym in word:
        if sym.isalpha():
            if sym.isupper():
                encrypted += (letters[(letters.index(sym.lower()) + offset) % len(letters)]).upper()
            else:
                encrypted += letters[(letters.index(sym) + offset) % len(letters)]
        else:
            encrypted += sym

    return encrypted


def decrypt(word, offset):
    """
    :param word - zasifrovane slovo
    :param offset - znakovy posun
    :return: desifrovane slovo
    """
    decrypted = encrypt(word, -offset)
    return decrypted
