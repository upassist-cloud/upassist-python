import functools


def attribute_required(attribute: str):
    """Decorator that ensures a required attribute is present before executing a method.

    Args:
        attribute: Name of the required attribute

    Returns:
        Decorated function that checks for the required attribute

    Raises:
        ValueError: If the required attribute is not present
    """

    def wrapper(func):
        """Wrapper function that adds the attribute check.

        Args:
            func: Function to be decorated

        Returns:
            Function that checks for the required attribute before execution
        """

        @functools.wraps(func)
        def inner(self, *args, **kwargs):
            """Inner function that performs the attribute check.

            Args:
                self: Instance of the class
                *args: Positional arguments
                **kwargs: Keyword arguments

            Returns:
                Result of the decorated function

            Raises:
                ValueError: If the required attribute is not present
            """
            if not getattr(self, attribute):
                raise ValueError(f"`{attribute}` is required to perform object action")
            return func(self, *args, **kwargs)

        return inner

    return wrapper
