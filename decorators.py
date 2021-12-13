#!/usr/bin/env python3.9

"""
A decorator simply does this:

callable = decorator(callable)
___________________

Using functools.wraps() allows you to keep information
on the wrapper function
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
Without the use of wraps(), the name of the example function would have been 'new_fct',
and the documentation string of the original example() function would have been lost.
"""


def debug(func):
    """Decorator for debugging.
    Displays inputs and output in the terminal."""

    def decorated(*args, **kwargs):
        if args and not kwargs:
            print("~ input of {}: args: {}".format(func.__name__, args))
        elif not args and kwargs:
            print("~ input of {}: kwargs: {}".format(func.__name__, kwargs))
        elif args and kwargs:
            print("~ input of {}: args: {}, kwargs: {}".format(func.__name__, args, kwargs))
        else:
            print("~ input of {}: NO_ARGS".format(func.__name__))
        output = func(*args, **kwargs) # stores the result of the function
        print("~ output of {}:".format(func.__name__), output)
        return output

    return decorated


def print_step_SF(msg: str, success_msg: str = "Success", error_msg: str = "Failed", error_case = Exception):
    """Affiche un log début/fin.
    msg:         message de base
    msg_success: fin du message en cas d'exécution sans erreur
    msg_error:   fin du message en cas d'erreur lors de l'exécution
    error_case:  cas d'echec (class héritant de Exception)
    
    note: Si la fonction wrapper doit print des infos, 
          il est préférable que le premier caractère soit un saut de ligne: \n
          pour des raison esthétique
    """

    def decorator(func):
 
        def decorated(*args, **kwargs):
            print(msg, end='', flush=True)
            output = None
            try:
                output = func(*args, **kwargs)
            except error_case:
                print("\r\033[K" + msg, "-", error_msg)
            else:
                print("\r\033[K" + msg, "-", success_msg)
            return output

        return decorated

    return decorator


def print_step_done(msg: str, msg_end: str = "done"):
    """Affiche un log début/fin.
    :msg:     string afficher AVANT ET APRÈS l'exécution de la fonction
    :msg_end: string ajouter à :msg: APRÈS l'exécution de la fonction
    
    exemple:
        msg     = "Creation of the target folder"
        msg_end = "done"
        >>> Creation of the target folder
        >>> # exécution de la fonction
        >>> Creation of the target folder - done
    """

    def decorator(func):
 
        def decorated(*args, **kwargs):
            print(msg)
            output = func(*args, **kwargs)
            print(msg, "-", end_msg)
            return output

        return decorated

    return decorator

def execution_time(func):
    """Measures the performance of the function.
    Decorator returning the time in seconds
    it takes for a function to execute."""
    import time

    def decorated(*args, **kwargs):
        start = time.time()
        output = func(*args, **kwargs)
        end = time.time()
        print("Took {} secondes.".format(end - start))
        return output

    return decorated

def singleton(defined_class):
    """Decorator for singleton classes (only one instance)."""
    instances_of_classes = {} # Dictionary of our singletons instances

    def get_instance():
        if defined_class not in instances_of_classes:
            # We create our first class object
            instances_of_classes[defined_class] = defined_class()
        return instances_of_classes[defined_class]

    return get_instance

def execution_limited(limit, overrun_func = None, *overrun_args, **overrun_kwargs):
    """Limits the number of times the function can be executed."""

    class ExecutionLimited(Exception):
        pass

    def decorator(func):
        fonction_executed = {}

        def decorated(*args, **kwargs):
            if func in fonction_executed:
                if fonction_executed[func] >= limit:
                    if overrun_func is not None:
                        overrun_func(*overrun_args, **overrun_kwargs)
                    else
                        raise ExecutionLimited(
                            f"Error, the function {func.__name__} "
                            f"can only be executed {limit} times.")
                else:
                    fonction_executed[func] += 1
            else:
                fonction_executed[func] = 1
            return func(*args, **kwargs)

        return decorated

    return decorator

def speed_reducer(seconds):
    """Apply a sleeper 'time.sleep(secs)' before the execution of the function."""
    import time

    def decorator(func):

        def decorated(*args, **kwargs):
            time.sleep(seconds)
            return func(*args, **kwargs)

        return decorated

    return decorator

def limited_frequency_execution(seconds, output = None):
    """Limits the execution of the function to once every 'seconds' seconds.
    Calculates from the end of the last run to the beginning of the next one.
    If this duration is too short the func decorated return None."""
    import time

    def decorator(func):
        last_used = float('-inf')

        def decorated(*args, **kwargs):
            nonlocal last_used
            now = time.time()
            if (now - last_used) >= seconds:
                output = func(*args, **kwargs)
                last_used = time.time()
            return output

        return decorated

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
