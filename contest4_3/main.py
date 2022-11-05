import sys
def takes(*argType):
    def check(f):
        def new_f(*args):
            for (a, t) in zip(args, argType):
                if not isinstance(a, t):
                    raise TypeError
            return f(*args)
        new_f.__name__ = f.__name__
        new_f.__doc__ = f.__doc__
        new_f.__module__ = f.__module__
        return new_f
    return check
exec(sys.stdin.read())