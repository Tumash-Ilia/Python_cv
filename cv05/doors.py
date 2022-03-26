# -*- coding: utf-8 -*-
"""
Úkol 5.
Napište program, který načte soubor large.txt a pro každé dveře vyhodnotí,
zda je možné je otevřít nebo ne. Tedy vyhodnotí, zda lze danou množinu uspořádat
požadovaným způsobem. Výstup z programu uložte do souboru vysledky.txt ve
formátu 1 výsledek =  1 řádek. Na řádek napište vždy počet slov v množině a True
nebo False, podle toho, zda řešení existuje nebo neexistuje.

Podrobnější zadání včetně příkladu je jako obvykle na elearning.tul.cz
"""

import collections


def read_input(name):
    """
    Nacitani dat ze souboru
    :param name: nazev|cesta ke souboru
    :return: data ze souboru
    """
    try:
        with open(name, "r") as file:
            content = file.read().splitlines()
    except FileNotFoundError:
        print("File not found, check name:'{}'".format(name))
    return content


def write_output(output):
    """
    Ulozeni output do souboru vysledky.txt
    :param output: data k ukladani
    """
    with open("vysledky.txt", "w") as file:
        for out in output:
            file.write(out)


def open_doors(content):
    """
    Metoda kontroluje, zda je mozne otevrit dvere, nebo ne.
    Podle poctu vyskytu pismen urcime True nebo False
    :param content: text, ktery chceme overit
    """
    doors_num = int(content.pop(0))
    answer = ""
    for _ in range(doors_num):
        words_num = int(content.pop(0))
        first = []
        last = []
        for _ in range(words_num):
            word = content.pop(0)
            first.append(word[0])
            last.append(word[-1])
        first_dic = collections.Counter(first)
        last_dic = collections.Counter(last)
        door_open = True
        cnt = 0
        for k in first_dic:
            if k in last_dic:
                if (first_dic[k] - last_dic[k]) > 1:
                    door_open = False
                    break
                if (first_dic[k] - last_dic[k]) == 1:
                    cnt += 1
            else:
                if (first_dic[k]) > 1:
                    door_open = False
                    break
                if (first_dic[k]) == 1:
                    cnt += 1
            if cnt >= 2:
                door_open = False
                break
        answer += str(words_num) + " " + str(door_open) + "\n"
    write_output(answer)


if __name__ == '__main__':
    open_doors(read_input("large.txt"))
