import sys, os

from flask import Flask, render_template
from flask_flatpages import FlatPages
from flask_frozen import Freezer # Added
#from flaskext.markdown import Markdown

DEBUG = True
FLATPAGES_AUTO_RELOAD = DEBUG
FLATPAGES_EXTENSION = '.json'

app = Flask(__name__)
app.config.from_object(__name__)
pages = FlatPages(app)
freezer = Freezer(app)

@app.route("/")
def index():
    infos = pages.get_or_404("info")
    return render_template('index.html', infos=infos)

@app.route("/experiences/")
def experience():
    infos = pages.get_or_404("experiences")
    return render_template('experiences.html', infos=infos)

@app.route("/projects/")
def project():
    infos = pages.get_or_404("projects")
    return render_template('projects.html', infos=infos)

if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "build":
        
        app.debug = False
        app.testing = True
        freezer.freeze()
    else:
        app.run(port=10001)
