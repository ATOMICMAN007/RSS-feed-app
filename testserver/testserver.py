import pathlib

from flask import Flask, Response

app = Flask(__name__)


def fetch_data(feed: str = "devto"):
    with open(str(pathlib.Path.cwd().parent) + f"/{feed}.xml", "r", encoding="utf-8") as file:
        data = file.read()
        return data


@app.route("/devto/rss")
def devtorss():
    return Response(fetch_data(), mimetype="application/rss+xml")


@app.route("/wired/rss")
def wiredrss():
    return Response(fetch_data("wired"), mimetype="application/rss+xml")
