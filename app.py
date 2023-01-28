#! /usr/bin/env python3

from flask import *
from htmlmin.minify import html_minify
from werkzeug.middleware.proxy_fix import ProxyFix

app = Flask(__name__)
app.wsgi_app = ProxyFix(app.wsgi_app, x_for=1, x_proto=1, x_host=1, x_prefix=1)


@app.get("/")
def index():
    return html_minify(render_template("index.html"))


@app.get("/profile/<userid>")
def profile(userid):
    return redirect(url_for("index"), code=301)


@app.get("/share/<userid>")
def harvest(userid):
    return redirect(url_for("index"), code=301)


@app.get("/privacy")
def privacy():
    return html_minify(render_template("privacy.html"))


def main():
    app.run(port=8000)


if __name__ == "__main__":
    main()
