"""

implementujte testy pro program hledac.py
pokrytí kódu musí být minimálně 75%

"""
import subprocess
import pytest
import hledac


@pytest.fixture()
def enum_all_res():
    """Return result for enumerate test."""
    return ["1:Lorem", "2:ipsum", "3:", "4:dolor", "5:sit"]


@pytest.fixture()
def search_res_one():
    """Return result for search test."""
    res = ['1:Lorem ipsum dolor sit amet, consectetur adipiscing elit.Nunc felis eros, tempus',
           '2:at vehicula vel, imperdiet sit amet urna.Quisque a ante lorem, sit amet ornare']
    return res


@pytest.fixture()
def search_res_two():
    """Return answer to search question."""
    res = ["1:Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nunc felis eros, tempus",
           "3:Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aliquam erat volutpat."]
    return res


def test_enumerate_all(enum_all_res):
    """
    Test ocislovani radku
    :param enum_all_res: vysledek pro porovnani
    """
    content = ["Lorem", "ipsum", "", "dolor", "sit"]
    result = hledac.enumerate_all(content)
    assert result == enum_all_res


def test_search_lines_one(search_res_one):
    """
    Test vyhledani rakdu ktere obshuji 1 slovo
    :param search_res_one: vysledek pro porovnani
    """
    text = [
        "Lorem ipsum dolor sit amet, consectetur adipiscing elit.Nunc felis eros, tempus",
        "at vehicula vel, imperdiet sit amet urna.Quisque a ante lorem, sit amet ornare",
        "tellus. Suspendisse potenti.Nullam pretium imperdiet purus in imperdiet.Fusce"
    ]
    words = ["orem"]
    result = hledac.search_in_lines(text, words)
    assert result == search_res_one


def test_search_lines_two(search_res_two):
    """
    Test vyhledani rakdu ktere obshuji 2 slova
    :param search_res_two: vysledek pro porovnani
    """
    text = [
        "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nunc felis eros, tempus",
        "at vehicula vel, imperdiet sit amet urna.Quisque a ante lorem, sit amet ornare",
        "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aliquam erat volutpat."
    ]
    words = ["dolor", "amet"]
    result = hledac.search_in_lines(text, words)
    assert result == search_res_two


def test_run_with_file_name():
    """
    Test cislo 1 z elearningu, chybi parametr -s
    Pro porovnani vysledku byl vyuzit standartni Win cmd prikaz - findstr
    """
    win_command = subprocess.check_output('findstr /n /r ^.*$ lipsum.txt', shell=True)
    my_command = subprocess.check_output('python hledac.py -f lipsum.txt', shell=True)
    assert win_command == my_command


def test_run_with_one_word():
    """
    Test cislo 2 z elearningu, bylo zadano jedno slovo
    Pro porovnani vysledku byl vyuzit standartni Win cmd prikaz - findstr
    """
    win_command = subprocess.check_output('findstr /n orem lipsum.txt', shell=True)
    my_command = subprocess.check_output('python hledac.py -f lipsum.txt -s orem', shell=True)
    assert win_command == my_command


def test_run_with_two_words():
    """
    Test cislo 3 z elearningu, byly zadany dve slova
    Pro porovnani vysledku byl vyuzit standartni Win cmd prikaz - findstr
    """
    win_command = subprocess.check_output('findstr /n "dolor" lipsum.txt | findstr "amet"', shell=True)
    my_command = subprocess.check_output('python hledac.py -f lipsum.txt -s dolor amet', shell=True)
    assert win_command == my_command


def test_error_no_search_args():
    """
    Test cislo 5 z elearningu, parametr -s bez zadaneho vzoru
    ocekavame chybu ve vysledku
    """
    with pytest.raises(subprocess.CalledProcessError):
        subprocess.check_output('python hledac.py -f lipsum.txt -s ', shell=True, stderr=subprocess.STDOUT)


def test_error_no_file_args():
    """
    Test volani s parametrem -f bez jmena souboru
    ocekavame chybu ve vysledku
    """
    with pytest.raises(subprocess.CalledProcessError):
        subprocess.check_output('python hledac.py -f ', shell=True, stderr=subprocess.STDOUT)


def test_error_no_args():
    """
    Test cislo 4 z elearningu, volani bez paramtru
    ocekavame chybu ve vysledku
    """
    with pytest.raises(subprocess.CalledProcessError):
        subprocess.check_output('python hledac.py ', shell=True, stderr=subprocess.STDOUT)
