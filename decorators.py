class ExceptionPrinter:
    """
    Tries to call a function; if there's an issue, run the example_method(),
    then print the exception.
    Can be used to decorate functions or methods.
    """

    def __init__(self, func):
        self.func = func
        self.name = None

    def __call__(self, *args, **kwargs):
        try:
            return self.func(*args, **kwargs)
        except Exception as exc:
            self.name = self.func.__qualname__
            self.example_function()
            print(str(exc))

    def __get__(self, instance, owner):
        from functools import partial
        return partial(self.__call__, instance)

    def example_function(self):
        print(f'hello {self.name}.')


class Example:

    def __init__(self, a, b):
        self.a = a
        self.b = b

    @ExceptionPrinter
    def example_method(self):
        return self.a / self.b


@ExceptionPrinter
def example_function(a, b):
    return a / b


if __name__ == '__main__':
    Example(1, 0).example_method()

    example_function(2, 0)
