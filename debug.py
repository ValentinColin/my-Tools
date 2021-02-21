#!/usr/bin/env python3.9

"""Simple debugging and info console module"""

##################
### CONSTANTES ###
##################

DEBUGING = False
INFO     = True


#################################
### CONSOLE DISPLAY FUNCTIONS ###
#################################

def debug(*args, **kwars):
    """Debugging print.
    print only if DEBUGING is set to True.
    """
    if DEBUGING:
        print("[DEBUG]:", *args, **kwars)


def info(*args, **kwargs):
    """Info print.
    print only if INFO is set to True.
    You can set the `filename` manually, else __name__ is used.
    """
    if INFO and ("filename" in kwargs):
        print("[INFO][" + kwargs["filename"] + "]", *args, **kwargs)
    elif INFO:
        print("[INFO][" + __name__ + "]", *args, **kwargs)


###############################
### DECORATOR FOR DEBUGGING ###
###############################

def deco_debug(func):
    """Decorator for debugging.
    print: ~<func_name>(*args,**kwargs)
           ~  └> <return of func_name>
    """

    def new_fct(*args, **kwargs):
        debug("~ input of {}: args: {}, kwargs: {}".format(func.__name__, args, kwargs))
        output = func(*args, **kwargs)
        debug("~ output of {}:".format(func.__name__), output)
        return output

    return new_fct


if __name__ == "__main__":

    DEBUGING = True

    @deco_debug
    def my_pow(nbr, power=0):
        print("I'm in function my_pow")
        return nbr ** power

    my_pow(nbr=3, power=4)
