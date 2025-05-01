import secrets
import string


def generate_bearer_token(length=32):
    """Generate a secure random bearer token.

    Args:
        length: Length of the token in characters (default: 32)

    Returns:
        A random string token suitable for use as a bearer token
    """
    characters = string.ascii_letters + string.digits
    return "".join(secrets.choice(characters) for _ in range(length))
