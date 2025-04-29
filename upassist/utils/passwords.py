import secrets
import string


def generate_bearer_token(length=32):
    characters = string.ascii_letters + string.digits
    return "".join(secrets.choice(characters) for _ in range(length))
