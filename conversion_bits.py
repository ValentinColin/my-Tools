""" Le ET logique (&):
comparaison bit à bit en utilisant le ET logique
Exemple:
a = 92    # 01011100
b = 21    # 00010101
c = a & b # 00010100
ou
d = 92    # 01011100
e = 1     # 00000001
f = d & e # 00000000
"""


def udec2bin(d, nb=0):
    """dec2bin(d,nb=0): conversion nombre entier positif ou nul
    -> chaîne binaire (si nb>0, complète à gauche par des zéros)"""
    if d == 0:
        b = "0"
    else:
        b = ""
        while d != 0:
            b = "01"[d & 1] + b  # "01"[0] donne "0" ET "01"[1] donne "1"
            d = (
                d >> 1
            )  # Opérateur '>>' (décalage d'un bit à droite = multiplication par 2)
    return b.zfill(nb)


def dec2bin(d, nb=8):
    """Représentation d'un nombre entier quelconque en chaine binaire
    (nb: nombre de bits du mot)"""
    if d == 0:
        return "0".zfill(nb)
    if d < 0:
        d += 1 << nb
    b = ""
    while d != 0:
        d, r = divmod(d, 2)
        b = "01"[r] + b
    return b.zfill(nb)
