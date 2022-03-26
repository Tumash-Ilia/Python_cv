"""
Implementujte program dle zadání úlohy 9. na elearning.tul.cz

Vytvořte program, který prohledá zadaný textový
soubor a nejde v něm řádky, na kterých se vyskytuje hledaný vzor. Případně více
vzorů. Tyto řádky pak vypíše na obrazovku a přidat k ním jejich čísla v původním
souboru.

Tak trochu se toto chování podobá unixovému příkazu grep, přesněji
řečeno grep -n.  Ten můžete případně použít pro kontrolu. Nicméně váš program
toho bude umět v mnoha ohledech méně a v jednom více (vyhledávání více vzorů
najednou). Nejde tedy o to vytvářet 100% kopii příkazu grep.

Program musí jít  ovládat z příkazové řádky. Základním parametrem zadávaným
vždy, je jméno souboru. Pokud jméno souboru není zadané program nemůže pracovat
a měl by v takovém případě zobrazit nápovědu.

Druhý parametr  parametr -s --search bude volitelný. Může být následován
libovolným počtem n slov. Samozřejmě, pokud je tam parametr -s musí tam být to
slovo alespoň jedno (tedy n >= 1).  Pokud není zadané hledané slovo, musí
program opět vypsat chybu nebo nápovědu.
 """
import argparse


def parse_args():
    '''
    zpracuje argumenty prikazove radky
    -f -filename: nazev vstupniho souboru
    -s -search: vzor pro vyhledani
    -h --help: navod
    '''
    parser = argparse.ArgumentParser("Searches for strings in files")
    parser.add_argument("-f", "--filename", help="Input file name.", nargs=1)
    parser.add_argument("-s", "--search",   help="Text to be searched for.", nargs='+')
    args = parser.parse_args()
    if args.filename is None:
        parser.error("The syntax of the command is incorrect.")
    else:
        content = read_file(args.filename[0])
        if args.search is None:
            print_result(enumerate_all(content))
        else:
            print_result(search_in_lines(content, args.search))


def read_file(name):
    """
    Nacitani dat ze souboru
    :param name: nazev|cesta ke souboru
    :return: data ze souboru
    """
    try:
        with open(name, "r") as file:
            content = file.read().splitlines()
    except FileNotFoundError:
        return print("File not found, check name:'{}'".format(name))
    return content


def search_in_lines(content, words):
    '''
    Metoda najde radky ve kterych vyskytuji zadana slova
    :param content: list radku
    :param words: vzor pro vyhledani
    :return: ocislovane radky
    '''
    text = []
    for line_num, line in enumerate(content, start=1):
        cnt = 0
        for word in words:
            if word in line:
                cnt += 1
            if cnt == len(words):
                text.append("".join([str(line_num), ":", line]))
    return text


def enumerate_all(content):
    '''
    Metoda ocisluje vsechny radky ve vstupnim textu
    :param content: vstupni text
    :return: ocislovane radky
    '''
    text = []
    for line_num, line in enumerate(content, start=1):
        text.append("".join([str(line_num), ":", line]))
    return text


def print_result(result):
    '''
    Metoda pro vypis vysledku
    :param result: vysledek pro vypis
    '''
    for res in result:
        print(res)


if __name__ == '__main__':
    parse_args()
