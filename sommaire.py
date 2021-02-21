#!/usr/bin/env python3.9

"""
Convertie le fichier FILE_PATH en fichier .txt pour le manipuler et
garder une sauvgarde en cas d'accident.
Puis crée un fichier de la même extension initiale que le fichier
dans lequel on aura rajouter un sommaire.
"""

import os
from datetime import date

today = date.today()

#################  CONSTANTE À FOURNIR À CHAQUE UTILISATION  ##################
# FILE_PATH = "/Users/valentin/Desktop/script/python/ClassMatrice.py" # localisation du fichier
FILE_PATH = "/Users/valentin/Github/class/ClassMatrice.py"          # localisation du fichier
TITLE     = "Matrice"               # titre d'en tête du sommaire
CREATOR   = "Valentin COLIN"        # créateur du fichier
VERSION   = today.strftime("%d %B %Y") # jour mois année (ex: 27 september 2019)
# VERSION   = "27 octobre 2019"       # année de production du fichier
###############################################################################

# On retire l'extension .txt .py ou n'importe quoi qu'elle extension
FILE_PATH_R = FILE_PATH[::-1]
p = FILE_PATH_R.index('.')+1
FILE_PATH_TXT = FILE_PATH[:-p]+".txt"
# On renomme le fichier pour pouvoir traiter des fichier .txt (juste temporaire)
os.rename(FILE_PATH, FILE_PATH_TXT)

# On fait une copie de,tous le texte du fichier pour le réécrire après
fileR = open(FILE_PATH_TXT, "r")
text = fileR.read()
class_number = text.count('class ')
fileR.close()

# On recopie le texte encore une fois mais ligne par ligne afin de travailler dessus
fileR = open(FILE_PATH_TXT, "r")
lines = fileR.readlines()
fileR.close()


# Début de la construction des éléments qui serviront à construire le sommaire
# Dictionnaire qui contiendra toutes les fonctions/classes définie dans le fichier
dict_class = {}           # sous la forme { "NAME_CLASS"                   : [line_in_script, index_in_summary] }
dict_fonctions = {}       # sous la forme { ("NAME_FONCTION","NAME_CLASS") : [line_in_script, index_in_summary] }
dict_fonctions_libre = {} # sous la forme { "NAME_CLASS"                   : [line_in_script, index_in_summary] }

# On récupère tous les noms de classes/fonctions et leurs numéro de ligne
index_fonction_libre = 0 # on leurs donnera des valeurs négative pour les identifier
index_fonction = 0
index_class    = 0
liste_ligne_utile = []
last_class = None
for i,line in enumerate(lines): # pour chaque ligne du script..
    if 'def ' in line:
        name_fonction = line[line.index('def ')+4 : line.index('(')]
        if '    def ' in line: # pour savoir si la fonction est défini dans une classe
            index_fonction += 1
            dict_fonctions[(name_fonction,last_class)] = [i+1,index_fonction]
            liste_ligne_utile.append(i+1)
        else:
            index_fonction_libre += 1
            dict_fonctions_libre[name_fonction] = [i+1,index_fonction_libre] # i+1 est le numéro de ligne réel de la ligne: 'line'
            liste_ligne_utile.append(i+1)
    elif 'class ' in line:
        index_fonction = 0
        index_class += 1
        name_class = line[line.index('class ')+6 : line.index(':')]
        dict_class[name_class] = [i+1,index_class] # i+1 est le numéro de ligne réel de la ligne: 'line'
        liste_ligne_utile.append(i+1)
        last_class = name_class

####################  Fonctions de construction de lignes  ####################

def create_class_line(index,name,line): # prend 2 lignes par classe
    index,line = str(index), str(line)
    index = "#\n# "+(4-len(index))*" "+index+"."   # 7  caract
    name  = "    "+name+":  "+(54-len(name))*"." # 61 caract
    line  = " ligne "+(4-len(line))*" "+line     # 11 caract
    return index+name+line+"\n"

def create_fonct_line(name_class,index_in_class,name,line): # prend 1 ligne par fonction
    index_class = dict_class[name_class][1]
    index_class,index_in_class = str(index_class), str(index_in_class)
    name,line = str(name), str(line)
    index = "# "+(4-len(index_class))*" "+index_class+"."+index_in_class+" "*(2-len(index_in_class)) # 9 caract
    name  = "  ------> "+name+"  "+(47-len(name))*"." # 59 caract
    line  = " ligne "+(4-len(line))*" "+line          # 11 caract
    return index+name+line+"\n"

def create_fonct_line_lib(index,name,line):
    index,line = str(index), str(line)
    index = "# "+(4-len(index))*" "+index+"."   # 7  caract
    name  = "  "+name+"  "+(57-len(name))*"." # 61 caract
    line  = " ligne "+(4-len(line))*" "+line     # 11 caract
    return index+name+line+"\n"

######################  Calcul de la taille du sommaire  ######################

# facteur pour prendre compte le nombre de fonctions libres
fnct_lib = 0
if dict_fonctions_libre:
    fnct_lib = 1
# taille du sommaire (en lignes)
summary_size = 13 + len(dict_fonctions) + 2*class_number + fnct_lib*(5+len(dict_fonctions_libre))
if dict_class:
    summary_size += 3

#############################  DEBUT DU SOMMAIRE  #############################

textInsert = "\"\"\"\n\
###############################################################################\n\
#\n\
# {space}{title}\n\
#\n\
#    Créateur(s) : {crea}\n\
#\n\
#    Version : {vers}\n\
#\n\
".format(space=((76-len(TITLE))//2)*" ", \
         title=TITLE,crea=CREATOR,vers=VERSION)

if dict_class:
    textInsert += "###############################################################################\n"
    textInsert += "#\n"
    textInsert += "#                                  CLASSE(S)\n"


######### ÉCRITURE DES LIGNES UNE À UNE #########
for ligne_utile in liste_ligne_utile:
    for class_name, class_value in dict_class.items():
        if ligne_utile == class_value[0]:
            textInsert += create_class_line(class_value[1],class_name,class_value[0]+summary_size)
            break
    for key_tuple_fnct, value_list_fnct in dict_fonctions.items():
        if ligne_utile == value_list_fnct[0]:
            textInsert += create_fonct_line(key_tuple_fnct[1],value_list_fnct[1],key_tuple_fnct[0],value_list_fnct[0]+summary_size)
            break

if dict_fonctions_libre: # ..s'il y a des fonctions libres
    textInsert += "#\n########################################################"
    textInsert += "#######################\n#\n"
    textInsert += "#                              Fonctions Libres\n#\n"
    for ligne_utile in liste_ligne_utile:
        for name_fnct, value_list_fnct in dict_fonctions_libre.items():
            if ligne_utile == value_list_fnct[0]:
                textInsert += create_fonct_line_lib(value_list_fnct[1],name_fnct,value_list_fnct[0]+summary_size)
###############################################################################

textInsert += "#\n\
###############################################################################\n\
\"\"\"\n"

##############################  FIN DU SOMMAIRE  ##############################
###############################################################################
###########################  Réécriture du script  ############################

# On réécrit le fichier final avec le sommaire et son contenue initiale
fileW = open(FILE_PATH, "w")
fileW.write(textInsert + text)
fileW.close()
