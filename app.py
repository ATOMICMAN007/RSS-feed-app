from flask import Flask, render_template
import feedparser
from markupsafe import Markup 

data = feedparser.parse("./dummy.xml")
entries = data.entries

app = Flask(__name__)


def markup_entries(entries):
    for entry in entries:
        entry.summary = Markup(entry.summary)
    return entries


@app.route("/")
def index():
    return render_template("index.html", entries=markup_entries(entries=entries))
