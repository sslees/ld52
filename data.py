import sqlite3

DB_FILE = "harvest.db"


def init():
    with sqlite3.connect(DB_FILE) as con:
        con.cursor().execute("CREATE TABLE IF NOT EXISTS users(id, name)")
        con.cursor().execute("CREATE TABLE IF NOT EXISTS souls(soulid, userid)")
        con.commit()


def register(id, name):
    with sqlite3.connect(DB_FILE) as con:
        con.cursor().execute("INSERT INTO users VALUES(?, ?)", (id, name))
        con.commit()


def username(userid):
    with sqlite3.connect(DB_FILE) as con:
        res = (
            con.cursor()
            .execute("SELECT name FROM users WHERE id=?", (userid,))
            .fetchone()
        )
        return res[0] if res else "error"


def harvest(soulid, userid):
    with sqlite3.connect(DB_FILE) as con:
        if not (
            con.cursor()
            .execute("SELECT 1 FROM souls WHERE soulid=?", (soulid,))
            .fetchone()
        ):
            con.cursor().execute("INSERT INTO souls VALUES(?, ?)", (soulid, userid))
            con.commit()
            return True
        return False
