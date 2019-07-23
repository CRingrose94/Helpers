from importlib import import_module


def missing_import(name, fail_msg=''):
    """
    Generates a class which raises an import error when initialised.
    e.g. SomeClass = missing_import('SomeClass') will make SomeClass() raise ImportError
    """
    def init(self, *args, **kwargs):
        raise ImportError(
            f'The class {name} you tried to call is not importable; '
            f'this is likely due to it not doing installed.\n\n'
            f'{f"Fail Message: {fail_msg}" if fail_msg else ""}'
        )
    return type(name, (), {'__init__': init})


def try_load(engine, module):
    """
    Try to load a particular engine from a module.
    If this fails, a dummy class is imported in its place with an import error raised on initialisation.

    :param engine: Name of the engine (some class being imported)
    :param module: Name of the QUBEKit module (.example)
    :return: Either the engine is imported as normal, or it is replaced with dummy class which
    just raises an import error with a message
    """
    try:
        module = import_module(module, __name__)
        return getattr(module, engine)
    except (ModuleNotFoundError, AttributeError) as exc:
        print(f'Failed to load: {engine}; continuing for now.\nError:\n{exc}\n')
        return missing_import(engine, fail_msg=str(exc))
