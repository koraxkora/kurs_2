def bold(f):
    def wrapper(arg):
        # x = f(arg)
        return f"<b>{f(arg)}</b>"
    return wrapper

def italic(f):
    return lambda *args, **kwargs: f"<i>{f(*args, **kwargs)}</i>"

@italic
@bold
def foo(arg):
    return f'To jest {arg}'

print(foo('ala'))



