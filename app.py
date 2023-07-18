from flask import Flask, render_template, request
import feedparser
from markupsafe import Markup

data = feedparser.parse("./dummy.xml")
entries = data.entries

app = Flask(__name__)


def markup_entries(entries: dict) -> dict:
    for entry in entries:
        entry.summary = Markup(entry.summary)
    return entries


@app.route("/")
def index():
    return render_template("index.html", entries=markup_entries(entries=entries))


@app.route("/article")
def article():
    for entry in entries:
        guid = request.args.get("guid")
        if entry.guid == guid:
            entry.summary = Markup(entry.summary)
            return render_template("article.html", entry=entry)
    return "Article not found.", 404
