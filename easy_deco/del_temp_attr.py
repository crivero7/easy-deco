import inspect

class DelTempAttr(object):

    def __init__(self):
        """

        """
        pass
        
    def __call__(self, fn):
        """
        Decorator to delete all temporary attributes generated in each pipeline component

        **Parameters**

        * **:param f:** (Function) function to be decorated
        """
        def wrapper(*args, **kwargs):

            result = fn(*args, **kwargs)

            attrs = inspect.getmembers(self, lambda attr:not(inspect.isroutine(attr)))

            for attr, _ in attrs:

                if attr.startswith('_') and attr.endswith('_'):
                    
                    if not(attr.startswith('__')) and not(attr.endswith('__')):

                        delattr(self, attr)

            self.data = result

            return result

        return wrapper

def all_methods(decorator):
    
    def decorate(cls):
        
        for name, fn in inspect.getmembers(cls, inspect.ismethod):
            
            if not name.startswith('__'):
                        
                setattr(cls, name, decorator(fn))
        
        return cls
    
    return decorate
