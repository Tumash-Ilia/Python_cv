# -*- coding: utf-8 -*-

"""
Úkol 6.
Vaším dnešním úkolem je vytvořit program, který o zadaném textu zjistí některé
údaje a vypíše je na standardní výstup. Hlavním smyslem cvičení je procvičit
si práci s regulárními výrazy, takže pro plný bodový zisk je nutné použít k
řešení právě tento nástroj.

Program musí pracovat s obecným textem, který bude zadaný v souboru. Jméno
souboru bude zadáno jako vstupní parametr funkce main, která by měla být
vstupním bodem programu. Samozřejmě, že funkce main by neměla řešit problém
kompletně a měli byste si vytvořit další pomocné funkce. Můžete předpokládat,
že soubor bude mít vždy kódování utf-8 a že bude psaný anglicky, tedy jen
pomocí ASCII písmen, bez české (či jiné) diakritiky.

Konkrétně musí program zjistit a vypsat:

1. Počet slov, která obsahují nejméně dvě samohlásky (aeiou) za sebou. Například
slovo bear.

2. Počet slov, která obsahují alespoň tři samohlásky - například slovo atomic.

3. Počet slov, která mají šest a více znaků - například slovo terrible.

4. Počet řádků, které obsahují nějaké slovo dvakrát.

Podrobnější zadání včetně příkladu je jako obvykle na elearning.tul.cz
"""

import re


def main(file_name):
    """
    zpracujte soubor
    """

    content = read_file(file_name)
    two_vowels(content)
    three_vowels(content)
    long_words(content)
    line_count(content)


def read_file(file_name):
    """
    Read from file
    :param file_name: file name
    :return: content from file
    """
    try:
        with open(file_name, "r") as file:
            content = file.read()
    except FileNotFoundError:
        print("File not found, check path:'{}'".format(file_name))
    return content


def two_vowels(content):
    """
    Count of words with closely 2 vowels
    :param content: text to work with
    """
    reg = re.findall(r"(?i)\b\w*[aeiyou]{2}\w*\b", content)
    dic = {}
    # prevod vsech slov na lower_case, abych dostal spravny pocet slov
    # slo by to udelat i content.lower(), ale jste chtel videt vyuziti regexu
    reg = ' '.join(reg).lower().split(" ")
    for word in reg:
        dic[word] = reg.count(word)
    print("1.", len(dic))


def three_vowels(content):
    """
    Count of words with 3 vowels in word
    :param content: text to work with
    """
    reg = re.findall(r"(?i)(?:\w*[aeiyou]){3}\w*", content)
    dic = {}
    reg = ' '.join(reg).lower().split(" ")
    for word in reg:
        dic[word] = reg.count(word)
    print("2.", len(dic))


def long_words(content):
    """
    Count of words with 6+ letters
    :param content: text to work with
    """
    reg = re.findall(r"(?i)\w*\w{6}\w*", content)
    dic = {}
    reg = ' '.join(reg).lower().split(" ")
    for word in reg:
        dic[word] = reg.count(word)
    print("3.", len(dic))


def line_count(content):
    """
    Number of identical words in line
    :param content: text to work with
    """
    lines = content.split("\n")
    cnt = 0
    for line in lines:
        reg = re.findall(r"(?i)\w+", line)
        dic = {}
        reg = ' '.join(reg).lower().split(" ")
        for word in reg:
            dic[word] = reg.count(word)
        if 2 in dic.values():
            cnt += 1
    print("4.", cnt)


if __name__ == '__main__':
    main('simple.txt')
