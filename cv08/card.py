"""
@TODO implementujte dle zadání cvičení 8
"""


class Card:
    """
    Třída pro reprezentaci hracích karet
    """

    def __init__(self, given_rank, given_suit):

        if given_rank not in range(2, 15):
            raise TypeError
        if given_suit not in ["s", "k", "p", "t"]:
            raise TypeError

        self._rank = given_rank
        self._suit = given_suit

    @property
    def rank(self):
        '''getter pomoci dekoratoru'''
        return self._rank

    @rank.setter
    def rank(self, given_rank):
        '''setter pomoci dekoratoru'''
        if given_rank not in range(2, 15):
            raise TypeError
        self._rank = given_rank

    @property
    def suit(self):
        '''getter pomoci dekoratoru'''
        return self._suit

    @suit.setter
    def suit(self, given_suit):
        '''setter pomoci dekoratoru'''
        if given_suit not in ["s", "k", "p", "t"]:
            raise TypeError
        self._rank = given_suit

    def black_jack_rank(self):
        """
        Metoda vrací hodnotu karty dle pravidel pro Black Jack
        :return:
        """
        if self._rank == 14:
            return 11
        if self._rank > 10:
            return 10
        return self._rank

    def __str__(self):
        suit = {'s': 'srdcov', 'k': 'károv', 'p': 'pikov', 't': 'trefov'}
        cards = ["dvojka", "trojka", "čtyřka", "pětka", "šestka", "sedma",
                 "osma", "devítka", "desítka", "spodek",
                 "královna", "král", "eso"]
        if self._rank == 14:
            return "{}é {}".format(suit[self._suit], cards[self._rank - 2])
        if self._rank == 13 or self._rank == 11:
            return "{}ý {}".format(suit[self._suit], cards[self._rank - 2])
        return "{}á {}".format(suit[self._suit], cards[self._rank - 2])

    def __lt__(self, other):
        return self._rank < other.rank

    def __le__(self, other):
        return self._rank <= other.rank

    def __eq__(self, other):
        return self._rank == other.rank

    def __ne__(self, other):
        return self._rank != other.rank

    def __gt__(self, other):
        return self._rank > other.rank

    def __ge__(self, other):
        return self._rank >= other.rank


if __name__ == '__main__':
    pass
