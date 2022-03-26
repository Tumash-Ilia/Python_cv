# -*- coding: utf-8 -*-

"""
@TODO - vyřešit úkol 11. - filtrování textu

Podrobné zadání jako obvykle na https://elearning.tul.cz

"""
import argparse
import re


def read_file(file_name):
    '''
    Cteni dat ze souboru
    :param file_name: nazev souboru
    :return: text
    '''
    try:
        with open(file_name, "r") as file:
            content = file.read().splitlines()
    except FileNotFoundError:
        print("File not found, check name:'{}'".format(file_name))
    return content


def save_to_file(file_name, text):
    """
    Vypis do souboru
    :param text: output text
    """
    with open(file_name, "w") as file:
        file.write(text)


def censor_text(forbidden_words, input_text):
    '''
    Nahradi zakazana slova sekvenci znaku #
    :param forbidden_words: zakazana slova
    :param input_text:vsuptni text
    :return: censorovany text
    '''
    text = "\n".join(input_text)
    for word in forbidden_words:
        words_pattern = r'\w+'
        for _ in re.findall(words_pattern, text, flags=re.IGNORECASE):
            if word.lower() == _.lower():
                text = re.sub(r"\b({})\b".format(word), "#" * len(word), text, flags=re.IGNORECASE)

    return text


def delete_tags(html_file):
    '''
    Metoda odstrani HTML znacky z textu
    :param html_file: html soubor
    :return: pouze text bez znacek
    '''
    cleanr = re.compile('<.*?>')
    new_html = []
    for element in html_file:
        clean_txt = re.sub(cleanr, '', element)
        if clean_txt != '':
            new_html.append(clean_txt)
    return new_html


def parse_args():
    """
    -i, --input : soubor který má být upraven (běžný text)
    -l, --list : soubor se seznamem zakázaných slov
    -c, --clean : přepínač vyčištění souboru od html
    -o, --output: výstupní soubor, pokud není volba použita, tak vypsat data na obrazovku
    -h, --help : nápověda - o čem program je a jak se ovládá
    """
    parser = argparse.ArgumentParser("Program pro odfiltrovani zadanych slov z textu")
    parser.add_argument("-i", "--input", help="Input file name.")
    parser.add_argument("-l", "--list", help="File with list of forbidden words.")
    parser.add_argument("-c", "--clean", action='store_true', help="Clean file from HTML tags.")
    parser.add_argument("-o", "--output", help="Output file name.")

    args = parser.parse_args()
    input_file = []
    forb_words = []
    if args.input is None:
        parser.error("No file to read from.")
    else:
        input_file = read_file(args.input)
    if args.list is None:
        parser.error("No file with list of forbidden words.")
    else:
        forb_words = read_file(args.list)
    if args.clean:
        text = censor_text(forb_words, delete_tags(input_file))
    else:
        text = censor_text(forb_words, input_file)
    if args.output is None:
        print(text)
    else:
        save_to_file(args.output, text)


if __name__ == '__main__':
    parse_args()
