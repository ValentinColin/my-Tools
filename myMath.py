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
# --coding:utf-8--
"""
from copy import copy,deepcopy
from math import sqrt
import math
#import cmath






def facto(n):
    """renvoie la factorielle de n"""
    facto = 1
    for k in range(1,n+1):
        facto *= k
    return facto

def coefBino(k,n):
    """renvoie le coefficient binomiale: k parmi n"""
    return facto(n)//(facto(k)*facto(n-k))

def arrangement(k,n):
    """renvoie le nombre de k arrangement parmi n """
    return facto(n)//facto(n-k)

def isSquare(x):
    """renvoie un bouléen pour savoir si x est un carré """
    bool=True
    if type(x) is float:
        raise ValueError
    elif not type(x) is int:
        raise TypeError
    else:
        if not math.ceil(sqrt(x))==math.floor(sqrt(x)):
            bool=False
    return bool

def facteurFermat(N):
    """calcul deux facteurs (A,B) du nombre IMPAIR N tel que N=A*B
    et A et B ne sont pas les facteurs triviaux
    Si N est paire lève l'exception: ValueError

    """
    if N%2==0:
        raise ValueError
    else:
        A=math.ceil(sqrt(N))
        Bsq=A*A-N
        while not isSquare(Bsq):
            A=A+1
            Bsq=A*A-N
    if not (A-sqrt(Bsq))*(A+sqrt(Bsq))==N:
        raise facteurFermatERROR
    return (A-int(sqrt(Bsq)),A+int(sqrt(Bsq)))

def prod(list):
    result = 1
    for x in list:
        result *= x
    return result

def permutations(liste):
    """Prend en argument une _liste (pas de tuple)
    renvoie la _liste des permutation d'une _liste
    mais attention la taille de la _liste renvoyer
    est en !n ->factorielle "le nombre l'élément" """
    if len(liste)==2:
        return [(liste[0],liste[1]),(liste[1],liste[0])]
    else:
        result=[]
        for i in range(len(liste)):
            b=liste[:]
            del b[i]
            result+=[tuple([liste[i]])+a for a in permutations(b)]
        return result

def signature(permu):
    """La permutation est une liste des premiers entiers, mélanger dans un certain ordre"""
    return int(prod([prod([(permu[j]-permu[i])/(j-i) for i in range(j+1) if j!=i]) for j in range(len(permu))]))

def sgn(x):
    """Fonction signe"""
    if   x < 0:  return -1
    elif x > 0:  return  1
    else:        return  0

def intVersList(nbr):
    """découpe le nombre en chiffre dans une liste
    exemple: 123 deviendra [1,2,3]"""
    return [int(list(str(nbr))[i+1]) for i in range(len(list(str(nbr)))-2)]

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

def generator_syracuse(n):
    """type générateur
    génère la suite de syracuse de n jusqu'à atteindre 1"""
    yield n
    while n != 1:
        if n % 2 == 0:
            n//=2
        else:
            n = 3 * n + 1
        yield n

def compte_apparition(nombre):
    """retourne un dictionnaire qui en clé sont les carractère
    et en valeurs le nombre de fois qu'il apparaissent """
    liste = intVersList(nombre)
    occurence = {}.fromkeys(set(liste),0)
    for valeur in liste:
        occurence[valeur] += 1
    return occurence

def suite_Robinson(n):
    """renvoie la liste des premiers termes de la suite de robinson pour U(0)=0 jusqu'à U(n)"""
    resultat=[0]
    while len(resultat) <= n:
        liste_chiffre = transfo(resultat[-1])
        dict_occu = compte_apparition(liste_chiffre)
        ############ je me suis arrété là il faut écrire le terme suivant maintenant que j'ai les occurance
        liste_chiffre_suivante = []
