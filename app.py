from flask import Flask, render_template, request
import feedparser
from markupsafe import Markup

app = Flask(__name__)

wired = "http://127.0.0.1:8989/wired/rss"
devto = "http://127.0.0.1:8989/devto/rss"


def fetch_data(link: str):
    # data = feedparser.parse(f"./{feed}.xml")
    data = feedparser.parse(link)
    return data.entries


def markup_entries(entries: dict) -> dict:
    for entry in entries:
        entry.summary = Markup(entry.summary)
    return entries


@app.route("/")
def index():
    entries = fetch_data("devto")
    return render_template("index.html", entries=markup_entries(entries=entries))


@app.route("/feed/<path:link>")
def feed(link):
    entries = fetch_data(link)
    return render_template("feed.html", entries=markup_entries(entries=entries))


@app.route("/article")
def article():
    feedname = request.args.get("feedname")
    entries = fetch_data(feedname)
    for entry in entries:
        guid = request.args.get("guid")
        if entry.guid == guid:
            entry.summary = Markup(entry.summary)
            return render_template("article.html", entry=entry)
    return "Article not found.", 404


@app.route("/addfeed")
def addfeed():
    return render_template("addfeed.html")
