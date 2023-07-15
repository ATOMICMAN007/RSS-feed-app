from flask import Flask, render_template
import feedparser

data = feedparser.parse("./dummy.xml")
entries = data.entries

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html", lentries = len(entries), entries=entries)
