def addarg(arg1):
    def wrap(f):
        def wrapped_f(*args, **kw):
            return f(arg1, *args, **kw)
        return wrapped_f
    return wrap

@addarg(1)
def myfunc(*args, **kwarg):
    return args
    
if __name__ == "__main__":
    print(myfunc("One", "Two"))
    print(myfunc(1, 2, 3))
    print(myfunc(("one", 1), ("two", 2)))
