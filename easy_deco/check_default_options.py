from .core import decorator

@decorator
def check_default_options(func=None,  *args, **options):
    """
    This decorator help you to check
    """
    if not func:

        default_options = func(*args, **options)

        options = {key: options[key] if key in options.keys() else default_options[key] for key in default_options.keys()}

    else:

        options = {key: options[key] if key in options.keys() else options[key] for key in options.keys()}

    return options