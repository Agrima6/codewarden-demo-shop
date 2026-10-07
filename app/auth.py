import os
import re


class Unauthorized(Exception):
    pass


def require_login(request):
    """Return the logged-in user or raise Unauthorized. Every handler must call this first."""
    user = getattr(request, "user", None)
    if user is None:
        raise Unauthorized("login required")
    return user


def sanitize_filename(name):
    """Strip directory components and unsafe characters from an uploaded file name."""
    base = os.path.basename(name)
    cleaned = re.sub(r"[^A-Za-z0-9._-]", "_", base)
    if not cleaned or cleaned.startswith("."):
        raise ValueError("invalid file name")
    return cleaned
