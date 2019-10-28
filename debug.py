"""
Module de débuguage, et d'info console
"""

# CONSTANTES

DEBUGING  = False
INFO      = True

#  FONCTIONS D'AFFICHAGE CONSOLE

def debug(*txt):
    """fonction de debug,
    cet fonction est équivalente à un print"""
    if DEBUGING:
        print("[DEBUG]:",*txt)

def info(*txt,nom_fichier=None):
    """Fonction donnant des information en direct sur l'état du programme,
    cet fonction est équivalente à un print.
    Ne pas oublier de donner le nom du fichier dans le quelle la fonction est appeler"""
    if INFO and nom_fichier:
        print("[INFO]["+nom_fichier+"]",*txt)
    elif INFO:
        print("[INFO]",*txt)

# DÉCORATEUR DE FONCTION POUR DÉBUGUER

def deco_debug(fonction):
    """décorateur de fonction pour le débuguage"""
    def new_fct(*args, **kwargs) :
        """ajout des décoration de débuguage"""
        debug("~{}({},{})".format(fonction.__name__, args, kwargs))
        result=fonction(*args, **kwargs) # stock ce que fonction peut renvoyer
        debug("~$~", result)
        return result
    return new_fct

def print_args(fonction):
    """décorateur de fonction pour le débuguage"""
    #def new_fct(*args, **kwargs): # afin d'accepter les dictionnaire en arguments
    def new_fct(*args):
        #debug("~{}({},{})".format(fonction.__name__, args, kwargs))
        debug("~{}({})~".format(fonction.__name__, args))
        #result=fonction(*args, **kwargs) # stock ce que fonction peut renvoyer
        result=fonction(*args) # stock ce que fonction peut renvoyer
        debug("~$~", result)
        return result
    return new_fct



if __name__=="__main__":
    @print_args
    def fnt(nbr,p=0):
        print("je suis dans la fonction fnt")
        return nbr**p

    fnt(3,4)
