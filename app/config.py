import os


def get_secret(name):
    """Read a secret from the environment. Raises if it is missing."""
    value = os.environ.get(name)
    if not value:
        raise RuntimeError(f"missing required secret: {name}")
    return value
