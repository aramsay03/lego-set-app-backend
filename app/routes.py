from app import app, db
from app.models.sets import Set
from flask import render_template, request

@app.route('/')
def index():
    return "Lego app back-end"

@app.route('/sets', methods=['GET'])
def listsets():
    sets = Set.query.all()
    return render_template('index.html', title='Lego Sets', sets=sets)