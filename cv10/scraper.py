# -*- coding: utf-8 -*-

"""
@TODO - vyřešit úkol 10. - zpracování HTML
"""
import re
import sys

from bs4 import BeautifulSoup
import requests


def find_links(start_link):
    """
    Metoda hleda vsechny odkazy v dokumentu
    :param start_link: odkaz ze ktereho zaciname hlidat
    :return: list odkazu
    """
    result = {}
    if ".html" in start_link:
        index = start_link.split("/")[-1]
        server = start_link.replace(index, "")
    else:
        index = "index.html"
        server = start_link

    # program zpracuje odkazy i bez http/https
    if "http://" not in server and "https://" not in server:
        server = "http://" + server

    result.setdefault(index, set())
    i = 0
    while True:
        if i < len(result):
            for key, value in list(result.items()):
                response = requests.get(server + key)
                soup = BeautifulSoup(response.content, 'html.parser')
                for link in soup.find_all('a', href=True):
                    if ".html" in link['href'] and "http://" not in link['href']:
                        result[key].add(link['href'])
                for link in value:
                    if link not in result:
                        result.setdefault(link, set())
            i += 1
        else:
            break
    return server, result


def find_mails(server, links):
    """
    Hledani vsech mailu
    :param server: server link
    :param links: odkaz na stranku
    :return: mails
    """
    mails = []
    for link in links.keys():
        response = requests.get(server + link)
        soup = BeautifulSoup(response.content, 'html.parser')
        match = re.findall(r'\b[\w\.-]+[@#][\w\.-]+\b', str(soup))
        mails += match
    return mails


def edit_mails(mails):
    """
    Formatovani mailu
    :param mails: mails
    :return: formatovane adresy
    """
    result = []
    for mail in mails:
        new_mail = ""
        for sym in mail:
            if sym.islower() or sym.isdigit() or sym == ".":
                new_mail += sym
            if sym in ('#', '@'):
                new_mail += "@"
        result.append(new_mail)
    return result


def edit_links(links):
    """
    Formatovani odkazu
    :param links: odkazy na stranky
    :return: formatovane odkazu
    """
    for key, value in links.items():
        links[key] = list(value)
    return links


def save_to_file(links, mails):
    """
    Vypis do souboru
    :param links: odkazy
    :param mails: adresy
    """
    with open("scrap_result.txt", "w") as file:
        file.write(str(links)+"\n\n")
        for mail in mails:
            file.write(mail+"\n")


def scarp(arg):
    """
    Spousteni programu
    :param arg: argument z CMD
    """
    server, links = find_links(arg)
    links = edit_links(links)
    mails = edit_mails(find_mails(server, links))
    save_to_file(links, mails)


if __name__ == '__main__':
    scarp(sys.argv[1])
