from flask import Flask, render_template, request
import feedparser
from markupsafe import Markup

app = Flask(__name__)


def fetch_data():
    data = feedparser.parse("./dummy.xml")
    return data.entries


def markup_entries(entries: dict) -> dict:
    for entry in entries:
        entry.summary = Markup(entry.summary)
    return entries


@app.route("/")
def index():
    entries = fetch_data()
    return render_template("index.html", entries=markup_entries(entries=entries))


@app.route("/article")
def article():
    entries = fetch_data()
    for entry in entries:
        guid = request.args.get("guid")
        if entry.guid == guid:
            entry.summary = Markup(entry.summary)
            return render_template("article.html", entry=entry)
    return "Article not found.", 404
