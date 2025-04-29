import functools


def attribute_required(attribute: str):
    def wrapper(func):
        @functools.wraps(func)
        def inner(self, *args, **kwargs):
            if not getattr(self, attribute):
                raise ValueError(f"`{attribute}` is required to perform object action")
            return func(self, *args, **kwargs)

        return inner

    return wrapper
