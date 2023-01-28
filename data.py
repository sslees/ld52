import sqlite3

DB_FILE = "harvest.db"


def init():
    with sqlite3.connect(DB_FILE) as con:
        con.cursor().execute("create table if not exists users(id, name)")
        con.cursor().execute("create table if not exists souls(soulid, userid)")
        con.commit()


def register(id, name):
    with sqlite3.connect(DB_FILE) as con:
        if not (
            con.cursor().execute("select 1 from users where id=?", [id]).fetchone()
        ):
            con.cursor().execute("insert into users values(?, ?)", [id, name])
            con.commit()


def username(userid):
    with sqlite3.connect(DB_FILE) as con:
        res = (
            con.cursor()
            .execute("select name from users where id=?", [userid])
            .fetchone()
        )
        return res[0] if res else ""


def harvest(soulid, userid):
    with sqlite3.connect(DB_FILE) as con:
        if not (
            con.cursor()
            .execute("select 1 from souls where soulid=?", [soulid])
            .fetchone()
        ):
            con.cursor().execute("insert into souls values(?, ?)", [soulid, userid])
            con.commit()
            return True
        return False


def score(userid):
    with sqlite3.connect(DB_FILE) as con:
        res_score = (
            con.cursor()
            .execute("select count(*) from souls where userid=?", [userid])
            .fetchone()
        )
        res_total = (
            con.cursor().execute("select count(distinct soulid) from souls").fetchone()
        )
        return (
            f"👻 {res_score[0] if res_score else 0}"
            + f" of {res_total[0] if res_total else 0}"
        )


def leaderboard(places):
    with sqlite3.connect(DB_FILE) as con:
        return (
            con.cursor()
            .execute(
                """
SELECT COALESCE(place, -1),
    name,
    COALESCE(score, 0)
FROM users
    LEFT JOIN (
        SELECT userid,
            COUNT(*) AS score,
            RANK() OVER(
                ORDER BY COUNT(*) DESC
            ) place
        FROM souls
        GROUP BY userid
    ) AS scores ON users.id = scores.userid
ORDER BY score DESC,
    name
LIMIT ?
""",
                [places],
            )
            .fetchall()
        )


def place(userid):
    with sqlite3.connect(DB_FILE) as con:
        res = (
            con.cursor()
            .execute(
                """
SELECT place,
    (
        SELECT COUNT(*)
        FROM users
    )
FROM (
        SELECT userid,
            COUNT(*) AS score,
            RANK() OVER(
                ORDER BY COUNT(*) DESC
            ) place
        FROM souls
        GROUP BY userid
    ) AS scores
    JOIN users ON scores.userid = users.id
WHERE userid = ?
""",
                [userid],
            )
            .fetchone()
        )
        return f"🏆 {res[0]} of {res[1]}" if res else "none"
