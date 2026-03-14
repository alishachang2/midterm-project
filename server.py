# import flask
from flask import Flask, url_for
import re

# import template engine
from flask import render_template
from flask import json
from flask import request, jsonify

import os

app = Flask(__name__)

# highlight filter for search
@app.template_filter('highlight')
def highlight_filter(text, query):
    if not query:
        return text
    pattern = re.compile(re.escape(query), re.IGNORECASE)
    return pattern.sub(lambda m: f'<mark class="bg-warning">{m.group()}</mark>', str(text))

# import data
filename = os.path.join(app.static_folder, 'data.json')
with open(filename) as shows_data:
    shows = json.load(shows_data)

def save_shows():
    with open(filename, 'w') as f:
        json.dump(shows, f, indent=2)

# home route
@app.route("/")
def home():
    return render_template('index.html', shows=shows)

# show page route
@app.route("/show/<int:id>")
def show_page(id):
    show = next((s for s in shows if s['id'] == id), None)
    return render_template('show_page.html', show=show)

# search route
@app.route("/search")
def search():
    query = request.args.get('q', '').strip().lower()
    if not query:
        return render_template('search.html', results=[], query='', count=0)
    results = [s for s in shows if any(
        query in str(s.get(f, '')).lower() for f in ['title', 'network', 'host', 'summary']
    ) or any(query in c['name'].lower() for c in s.get('notable_cast', []))]
    return render_template('search.html', results=results, query=query, count=len(results))

# add route - GET serves the page
@app.route("/add")
def add():
    return render_template('add.html')

# add route - POST saves data
@app.route("/add_show", methods=['POST'])
def add_show():
    request_data = request.get_json()

    # error handling
    errors = {}
    for field in ['title', 'network', 'host', 'summary']:
        if not request_data.get(field, '').strip():
            errors[field] = f'{field.capitalize()} is required'
    for field in ['season', 'year', 'rating']:
        try:
            int(request_data.get(field, ''))
        except (ValueError, TypeError):
            errors[field] = f'{field.capitalize()} must be a number'

    if errors:
        return jsonify({'success': False, 'errors': errors}), 400

    # create new show object
    new_id = max(s['id'] for s in shows) + 1
    new_show = {
        'id': new_id,
        'title': request_data['title'].strip(),
        'season': int(request_data['season']),
        'network': request_data['network'].strip(),
        'year': int(request_data['year']),
        'host': request_data['host'].strip(),
        'rating': int(request_data['rating']),
        'summary': request_data['summary'].strip(),
        'notable_cast': [],
        'genre': [g.strip() for g in request_data.get('genre', '').split(',') if g.strip()],
        'status': request_data.get('status', 'Unknown'),
        'similar_show_ids': [],
        'image': {'url': request_data.get('image_url', ''), 'alt': request_data['title'].strip()}
    }

    # add to array and save to file
    shows.append(new_show)
    save_shows()

    return jsonify({'success': True, 'id': new_id})

# edit route - GET serves the page
@app.route("/edit/<int:id>")
def edit(id):
    show = next((s for s in shows if s['id'] == id), None)
    return render_template('edit.html', show=show)

# edit route - POST saves data
@app.route("/edit_show/<int:id>", methods=['POST'])
def edit_show(id):
    show = next((s for s in shows if s['id'] == id), None)

    request_data = request.get_json()

    # error handling
    errors = {}
    for field in ['title', 'network', 'host', 'summary']:
        if not request_data.get(field, '').strip():
            errors[field] = f'{field.capitalize()} is required'
    for field in ['season', 'year', 'rating']:
        try:
            int(request_data.get(field, ''))
        except (ValueError, TypeError):
            errors[field] = f'{field.capitalize()} must be a number'

    if errors:
        return jsonify({'success': False, 'errors': errors}), 400

    # update the show
    show['title'] = request_data['title'].strip()
    show['season'] = int(request_data['season'])
    show['network'] = request_data['network'].strip()
    show['year'] = int(request_data['year'])
    show['host'] = request_data['host'].strip()
    show['rating'] = int(request_data['rating'])
    show['summary'] = request_data['summary'].strip()
    show['genre'] = [g.strip() for g in request_data.get('genre', '').split(',') if g.strip()]
    show['status'] = request_data.get('status', show.get('status', 'Unknown'))
    if request_data.get('image_url'):
        show['image']['url'] = request_data['image_url'].strip()

    save_shows()

    return jsonify({'success': True, 'id': id})

if __name__ == "__main__":
    app.run(debug=True)