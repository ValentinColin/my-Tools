"""
A decorator simply does this:

callable = decorator(callable)
___________________

Utiliser functools.wraps() permet de conserver des informations
sur la fonction wrapper
ex:
******************
import functools
def my_decorator(fct):
    @functools.wraps(fct)
    def new_fct(*args,**kwargs):
        print("Calling decorated function")
        return fct(*args,**kwargs)

@my_decorator
def example():
    "Docstring"
    print("Called example function")

>>> example()
Calling decorated function
Called example function
>>> example.__name__
'example'
>>> example.__doc__
'Docstring'
*****************
Sans l'utilisation de wraps(), le nom de la fonction d'example aurait été 'new_fct',
et la chaine de documentation de la fonction example() originale aurait été perdue
"""
# --coding:utf-8--


def debug(function):
    """Function decorator for debugging, displays arguments
    and result obtained in the terminal."""
    def decorated_function(*args, **kwargs):
        if args and not kwargs:
            print("~ {} (args = {})".format(function.__name__,args))
        elif not args and kwargs:
            print("~ {} (kwargs = {})".format(function.__name__,kwargs))
        elif args and kwargs:
            print("~ {} (args = {}, kwargs = {})".format(function.__name__, args, kwargs))
        else:
            print("~ {} (NO ARGS)".format(function.__name__))
        result = function(*args, **kwargs) # stores the result of the function
        print("~$~ {}'s result --> ".format(function.__name__), result)
        return result
    return decorated_function

def execution_time(function):
    """Decorator returning the time in seconds
    it takes for a function to execute."""
    import time
    def decorated_function(*args,**kwargs):
        start = time.time()
        result = function(*args,**kwargs)
        end = time.time()
        print("Took {} secondes.".format(end-start))
        return result
    return decorated_function

def singleton(class):
    """Decorator allowing to have singletons classes (single instance)."""
    instances = {} # Dictionary of our singletons instances (if decorator used on multiple class)
    def get_instance():
        if class not in instances:
            # We create our first class object
            instances[class] = classe_definie()
        return instances[class]
    return get_instance

def execution_limited(limit):
    """Limits the number of times the function can be executed."""
    class ExecutionLimited(Exception):
        pass
    def decorator(function):
        fonction_executed = {}
        def decorated_function(*args,**kwargs):
            if function in fonction_executed:
                fonction_executed[function] += 1
                if fonction_executed[function] > limit:
                    raise ExecutionLimited("Error, the function {} can only be executed {} times.".format(function.__name__,limit))
            else:
                fonction_executed[function] = 1
            return function(*args,**kwargs)
        return decorated_function
    return decorator

def speed_reducer(secs):
    """Apply a sleeper 'time.sleep(secs)' before the execution of the function."""
    import time
    def decorator(function):
        def decorated_function(*args,**kwargs):
            time.sleep(secs)
            return function(*args,**kwargs)
        return decorated_function
    return decorator

def limited_frequency_execution(secs):
    """Limits the execution of the function to once every 'secs' seconds.
    Calculates from the end of the last run to the beginning of the next one."""
    import time
    def decorator(function):
        last_used = float('-inf')
        def decorated_function(*args,**kwargs):
            nonlocal last_used
            now = time.time()
            if now - last_used >= secs:
                result = function(*args,**kwargs)
                last_used = time.time()
                return result
        return decorated_function
    return decorator



if __name__ == '__main__':
    import time

    @limited_frequency_execution(4) # forbid the function from being executed more than once every 4 seconds
    def foo(arg1,arg2,arg3):
        time.sleep(2)
        return "result..."

    start = time.time()
    for _ in range(10):
        time.sleep(1)
        print(foo("param1","param2","param3")," ~$~ time : {:.{prec}f}".format(time.time()-start,prec=2),"secondes")
