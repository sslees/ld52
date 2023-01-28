#! /usr/bin/env python3

from uuid import uuid4

from flask import *
from werkzeug.middleware.proxy_fix import ProxyFix

import data

app = Flask(__name__)
app.wsgi_app = ProxyFix(app.wsgi_app, x_for=1, x_proto=1, x_host=1, x_prefix=1)


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


@app.get("/share/<userid>")
def harvest(userid):
    return render_template(
        "harvest.html",
        unharvested=data.harvest(request.remote_addr, userid),
        username=data.username(userid),
    )


@app.get("/privacy")
def privacy():
    return render_template("privacy.html")


def main():
    data.init()
    app.run(port=8000)


if __name__ == "__main__":
    main()
