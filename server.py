#import os module
import os

#import flask
from flask import Flask, url_for

#import template engine
from flask import render_template
from flask import json

app = Flask(__name__)

#import data
filename = os.path.join(app.static_folder, 'data.json')
with open(filename) as shows_data:
    shows = json.load(shows_data)

#show all shows route
# @app.route("/shows")
# def show_all_shows():
#     global shows
#     return render_template('shows.html', shows=shows)

@app.route("/")
def home():
    return render_template('index.html', shows=shows)

@app.route("/show/<int:id>")
def show_page(id):
    show = next((s for s in shows if s['id'] == id), None)
    if show is None:
        return "Show not found", 404
    return render_template('show_page.html', show=show)


if __name__ == "__main__":
    app.run(debug=True)