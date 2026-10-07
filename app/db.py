import sqlite3

_conn = None


def connect(path="shop.db"):
    global _conn
    if _conn is None:
        _conn = sqlite3.connect(path)
        _conn.row_factory = sqlite3.Row
    return _conn


def run_query(sql, params=()):
    """The only sanctioned way to talk to the database: always pass values as params."""
    cur = connect().execute(sql, params)
    return [dict(row) for row in cur.fetchall()]
