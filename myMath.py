#!/usr/bin/env python3.9

"""
###############################################################################
#
#                                   My Math
#
#    Créateur(s) : Valentin COLIN
#
#    Version : 27 octobre 2019
#
#
###############################################################################
#
#                              Fonctions Libres
#
#    1.  facto  .................................................... ligne   42
#    2.  coefBino  ................................................. ligne   49
#    3.  arrangement  .............................................. ligne   53
#    4.  isSquare  ................................................. ligne   57
#    5.  facteurFermat  ............................................ ligne   69
#    6.  prod  ..................................................... ligne   87
#    7.  permutations  ............................................. ligne   93
#    8.  signature  ................................................ ligne  108
#    9.  sgn  ...................................................... ligne  112
#   10.  intVersList  .............................................. ligne  118
#   11.  generator_syracuse  ....................................... ligne  140
#   12.  compte_apparition  ........................................ ligne  151
#   13.  suite_Robinson  ........................................... ligne  160
#
###############################################################################
"""

import math
from typing import Union
from math import sqrt
from copy import copy, deepcopy



def facto(n: int) -> int:
    """Returns the factorial of n."""
    if n < 0:
        raise ArithmeticError("Can't calculate the factorial of a negative integer.")
    facto = 1
    for k in range(1, n + 1):
        facto *= k
    return facto


def coefBino(k: int, n: int) -> int:
    """Returns the binomial coefficient: k among n."""
    return facto(n) // (facto(k) * facto(n - k))


def arrangement(k: int, n: int) -> int:
    """Returns the number of k arrangements among n."""
    return facto(n) // facto(n - k)


def isSquare(x: int) -> bool:
    """Verify is x is a square."""
    bool = True
    if type(x) is float:
        raise ValueError
    elif not type(x) is int:
        raise TypeError
    else:
        if not math.ceil(sqrt(x)) == math.floor(sqrt(x)):
            bool = False
    return bool


def facteurFermat(N: int) -> tuple[int, int]:
    """Calculate the 2 factors of Fermat.
    Calculating two factors (A,B) of the number N (odd) such that N=A*B
    and A and B are not the trivial factors.
    If N is even, the exception is raised: ValueError.
    """
    if N % 2 == 0:
        raise ValueError
    else:
        A = math.ceil(sqrt(N))
        Bsq = A * A - N
        while not isSquare(Bsq):
            A = A + 1
            Bsq = A * A - N
    if not (A - sqrt(Bsq)) * (A + sqrt(Bsq)) == N:
        raise facteurFermatERROR
    return (A - int(sqrt(Bsq)), A + int(sqrt(Bsq)))


def prod(list: list):
    """Return the product of the items in the list."""
    result = 1
    for x in list:
        result *= x
    return result


def permutations(list_) -> list[tuple]:
    """Returns the list of permutations of list_.
    Be aware of the size of the list_ to be sent back
    is in !n -> factorial "the number the element of list_".
    """
    list_ = list(list_)
    if len(list_) == 2:
        return [(list_[0], list_[1]), (list_[1], list_[0])]
    else:
        result = []
        for i in range(len(list_)):
            b = list_[:]
            del b[i]
            result += [tuple([list_[i]]) + a for a in permutations(b)]
        return result


def signature(permu: list[tuple]) -> int:
    """Return the signature of the permutation.
    A permutation is said to be even if it has an even number of inversions,
    otherwise it is odd. 
    The signature of a permutation is 1 if it is even, -1 if it is odd.
    """
    return int(
        prod(
            [
                prod([(permu[j] - permu[i]) / (j - i) for i in range(j + 1) if j != i])
                for j in range(len(permu))
            ]
        )
    )


def sgn(x: Union[int, float]) -> int:
    """Sign function."""
    if x < 0:
        return -1
    elif x > 0:
        return 1
    else:
        return 0


def intVersList(nbr: int) -> list[int]:
    """Cuts out the number in digits from a list.
    example: 123 will become [1,2,3].
    """
    return [int(list(str(nbr))[i + 1]) for i in range(len(list(str(nbr))) - 2)]


"""
algo: PERMUTATIONS
données: un ensemble E

    SI Card E = 2 FAIRE
        RENVOYER les 2 permutations (sous forme de couple) de E dans une paire ie. {(e1,e2),(e2,e1)}
    SINON FAIRE
        resultat <-- ensemble vide
        POUR i DANS le segment d'entier [1,Card E] FAIRE
            B <-- E
            supprimer le i-èmes élément de B
            concaténer { (i-èmes élément de E) + a / a ∈ PERMUTATIONS (B) } à resultat
            # attention le + correspond à la concaténation des n-uplets
        RENVOYER resultat

"""


def generator_syracuse(n: int):
    """Generator of Synracuse.
    Generates the syracuse sequence from n up to 1"""
    yield n
    while n != 1:
        if n % 2 == 0:
            n //= 2
        else:
            n = 3 * n + 1
        yield n


def compte_apparition(number: int) -> dict:
    """Returns a dictionary which in key are the carracteries
    and in values the number of times it appears.
    """
    liste = intVersList(number)
    occurence = {}.fromkeys(set(liste), 0)
    for valeur in liste:
        occurence[valeur] += 1
    return occurence


def suite_Robinson(n: int) -> list:
    """Returns the list of the first terms of the robinson sequence. 
    U(0)=0 to U(n)
    """
    resultat = [0]
    while len(resultat) <= n:
        liste_chiffre = transfo(resultat[-1])
        dict_occu = compte_apparition(liste_chiffre)
        ############ je me suis arrété là il faut écrire le terme suivant maintenant que j'ai les occurance
        liste_chiffre_suivante = []
