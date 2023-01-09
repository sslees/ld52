#! /usr/bin/env python3

import sys
from uuid import uuid4

from flask import *

import data

app = Flask(__name__)


@app.get("/")
def index():
    return render_template("index.html", userid=str(uuid4()).replace("-", ""))


@app.post("/register")
def register():
    data.register(**request.json)
    return "", 201


@app.get("/profile/<userid>")
def profile(userid):
    return render_template(
        "profile.html",
        username=data.username(userid),
        userid=userid,
        score=data.score(userid),
        leaderboard=data.leaderboard,
        place=data.place(userid),
    )


@app.get("/harvest/<userid>")
def harvest(userid):
    return render_template(
        "harvest.html",
        unharvested=data.harvest(request.remote_addr, userid),
        username=data.username(userid),
    )


@app.get("/about")
def about():
    return render_template("about.html")


@app.get("/privacy")
def privacy():
    return render_template("privacy.html")


def main():
    data.init()
    app.run(debug=True)


if __name__ == "__main__":
    main()
