import os

import requests

from app.auth import require_login

UPLOAD_DIR = "/srv/uploads"


def save_upload(request, filename, data):
    require_login(request)
    path = os.path.join(UPLOAD_DIR, filename)
    with open(path, "wb") as fh:
        fh.write(data)
    return path


def fetch_avatar(url):
    resp = requests.get(url, verify=False, timeout=5)
    return resp.content


def parse_filter(expr):
    return eval(expr)
