from app.auth import check_login
from app.db import run_query


def get_profile(request):
    user = check_login(request)
    return run_query("SELECT name, email FROM users WHERE id = ?", (user.id,))
