# -*- coding: utf-8 -*-

"""
@TODO: zde napiste svoje unit testy pro modul censor.py
"""
import subprocess
import pytest
import censor


def test_delete_tags():
    """
    Test odstraneni znacek z HTML
    """
    html = ["<a>", "<p>Text</p>", "<h1>Text", "Text</h1>", "<html><body>Text</body></html>"]
    output = ["Text", "Text", "Text", "Text"]
    result = censor.delete_tags(html)
    assert result == output


def test_censor_text():
    """
    Test censorovaciho systemu
    """
    words = ["lorem", "sit", "Elit", "etiam"]
    text = ["Lorem ipsum dolor sit amet, consectetur adipiscing elit.",
            "Etiam rhoncus imperdiet semper."]
    output = ["##### ipsum dolor ### amet, consectetur adipiscing ####.",
              "##### rhoncus imperdiet semper."]
    result = censor.censor_text(words, text)
    return result == output


def test_errors_argparse():
    """
    Test volani programu s chybnymi argumenty
    ocekavame chybu ve vysledku
    """
    with pytest.raises(subprocess.CalledProcessError):
        subprocess.check_output('python censor.py   ', shell=True, stderr=subprocess.STDOUT)
        subprocess.check_output('python censor.py -i', shell=True, stderr=subprocess.STDOUT)
        subprocess.check_output('python censor.py -i neco.txt', shell=True, stderr=subprocess.STDOUT)
        subprocess.check_output('python censor.py  -i neco.txt -l', shell=True, stderr=subprocess.STDOUT)


def test_censor_with_tags():
    """
    Test censoru bez odstraneni znacek ze souboru
    """
    output = ['<html>', '<body>', '<h1>Ahoj ###### cau</h1>', '<p>',
              'Zdeněk Štybar zakončil svůj krátký návrat k cyklokrosu druhým místem v '
              'Grand Prix Svena Nijse. Tradiční novoroční ###### v Baalu vyhrál už '
              'podvanácté nejslavnější místní'
              ' ########, jehož jméno závod ####.', '</p>', '', '</body>', '</html>']
    res = subprocess.check_output("python censor.py  -i data_test.html -l list_test.txt", shell=True)
    return output == res.splitlines()


def test_censor_clean():
    """
    Test cesnsoru s odstranenim HTML znacek
    :return:
    """
    output = ['Ahoj ###### cau',
              'Zdeněk Štybar zakončil svůj krátký návrat k cyklokrosu druhým místem v '
              'Grand Prix Svena Nijse. Tradiční novoroční ###### v Baalu vyhrál už '
              'podvanácté nejslavnější místní ########, jehož jméno závod ####.'
              ]
    res = subprocess.check_output("python censor.py  -i data_test.html -l list_test.txt -c", shell=True)
    return output == res.splitlines()


def test_censor_file_output():
    """
    Test vystupu do souboru
    :return:
    """
    output = ['Ahoj ###### cau',
              'Zdeněk Štybar zakončil svůj krátký návrat k cyklokrosu druhým místem v '
              'Grand Prix Svena Nijse. Tradiční novoroční ###### v Baalu vyhrál už '
              'podvanácté nejslavnější místní ########, jehož jméno závod ####.'
              ]
    subprocess.call("python censor.py  -i data_test.html -l list_test.txt -c -o output.txt", shell=True)
    with open('output.txt', "r") as file:
        content = file.read().splitlines()
    return output == content
