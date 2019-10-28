def deco_debug(fct):
    """Décorateur de fonction pour le débuguage,
    affiche arguments et resultat obtenu dans le terminal."""
    def new_fct(*args, **kwargs):
        if args and not kwargs:
            print("~{}({})".format(fct.__name__,args))
        elif not args and kwargs:
            print("~{}({})".format(fct.__name__,kwargs))
        elif args and kwargs:
            print("~{}({},{})".format(fct.__name__, args, kwargs))
        result = fct(*args, **kwargs) # stock ce que fct peut renvoyer
        print("~$~", result)
        return result
    return new_fct

def execution_time(fct):
    """Décorateur retournant le temps en secondes
    qu'une fonction à mis pour s'éxécuter."""
    def new_fct(*args,**kwargs):
        start = time.time()
        result = fct(*args,**kwargs)
        end = time.time()
        print("Took {} secondes.".format(end-start))
        return result
    return new_fct

def singleton(classe_definie):
    """Décorateur permettant d'avoir des classes singletons (unique instance)"""
    instances = {} # Dictionnaire de nos instances singletons
    def get_instance():
        if classe_definie not in instances:
            # On crée notre premier objet de classe_definie
            instances[classe_definie] = classe_definie()
        return instances[classe_definie]
    return get_instance

def deco_execution_limited(limit):
    class ExecutionLimited(Exception):
        pass
    def deco(fct):
        fonction_executed = {}
        def new_fct(*args,**kwargs):
            if fct in fonction_executed:
                fonction_executed[fct] += 1
                if fonction_executed[fct] > limit:
                    raise ExecutionLimited("Error, the function {} can only be executed {} times.".format(fct.__name__,limit))
            else:
                fonction_executed[fct] = 1
            return fct(*args,**kwargs)
        return new_fct
    return deco

def speed_reducer(secs):
    """Apply a sleeper 'time.sleep(secs)' before the execution of the function."""
    import time
    def deco(fct):
        def new_fct(*args,**kwargs):
            time.sleep(secs)
            return fct(*args,**kwargs)
        return new_fct
    return deco
