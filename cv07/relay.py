# -*- coding: utf-8 -*-

"""
Cvičení 7. - práce s daty

Vaším dnešním úkolem je spojit dohromady data, uložená ve dvou různých
souborech. První soubor obsahuje výsledky závodu - jména a časy závodníků. Druhý
pak obsahuje databázi závodníků uloženou jako JSON - mimo jiné jejich id. Cílem
je vytvořit  program, který tyto data propojí, tedy ke každému závodníkovi ve
štafetě najde jeho id. Případně také nenajde, data nejsou ideální. I tuto
situaci ale musí program korektně ošetřit.  Výsledky programu bude potřeba
zapsat do dvou souborů.

Kompletní zadání je jako vždy na https://elearning.tul.cz/

"""
import re
import json
from bs4 import BeautifulSoup



def output_json(result_list):
    """
    Uloží list slovníků do souboru output.json tak jak je požadováno
    v zadání.
    """
    with open('output.json', 'w') as output:
        output.write(json.dumps(result_list, indent=4, sort_keys=True))


def read_html():
    """
    Read data from html file
    :return: lists with time and names data
    """
    with open('result.html', "r") as file:
        html = file.read()
    soup = BeautifulSoup(html, 'lxml')
    res = soup.find('strong', text=re.compile("Relay"))
    relay = res.find_all_next('p')
    women = relay[1].get_text()
    men = relay[3].get_text()
    time = re.findall(r"\d{1}:\d{2}:\d{2}", women)
    names = re.findall(r"\((.*?)\)", women)
    time += re.findall(r"\d{1}:\d{2}:\d{2}", men)
    names += re.findall(r"\((.*?)\)", men)
    return time, names


def read_json():
    """
    Read json file
    :return: data from json
    """
    with open('competitors.json', "r") as file:
        data = file.read()
    return data


def find_id(data, first_name, last_name):
    """
    Search for an id in the list
    :param data: data from json
    :param first_name: first name
    :param last_name:  last name
    :return: id if exists, or False
    """
    for competitor in json.loads(data):
        if (competitor['lastname'] == last_name) & (competitor['firstname'] == first_name):
            return competitor['id']
    return False


def output_compare(compare_data):
    """
    Output to compare.txt
    :param compare_data: output data
    """
    with open('compare.txt', "w") as file:
        compare_data.sort(key=lambda tup: tup[0])
        for data in compare_data:
            file.write(' '.join(str(_) for _ in data) + "\n")


def output_errors(err_data):
    """
    Output to errors.txt
    :param err_data: output data
    """
    with open('errors.txt', "w") as file:
        for data in err_data:
            file.write(data + "\n")


def create_output():
    """
    Method processes the data
    """
    time, names = read_html()
    data = read_json()
    result_json = []
    result_compare = []
    result_errors = []
    for i, name in enumerate(names):
        for initials in name.split(", "):
            first_name = initials.split(" ")[0]
            last_name = initials.split(" ")[1]
            id_ = find_id(data, first_name, last_name)
            if i > 8:
                result = i - 8
            else:
                result = i + 1
            if id_:
                comp = {
                    "id_": id_,
                    "result": result,
                    "time": str(time[i])
                }
                result_json.append(comp)
                result_compare.append((id_, result))
            else:
                comp = {
                    "id_": "False",
                    "result": result,
                    "time": str(time[i]),
                    "no_match": initials
                }
                result_json.append(comp)
                result_errors.append(initials)
    output_json(result_json)
    output_compare(result_compare)
    output_errors(result_errors)


if __name__ == '__main__':
    create_output()
