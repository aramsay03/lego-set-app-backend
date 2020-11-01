from flask import url_for
from app import app, db
from app.models.sets import Set
from flask import render_template, request, redirect
import csv
from io import TextIOWrapper

@app.route('/')
def index():
    return "Lego app back-end"

@app.route('/sets', methods=['GET'])
def listsets():
    sets = Set.query.all()
    return render_template('index.html', title='Lego Sets', sets=sets)

@app.route('/update', methods=['GET', 'POST'])
def upload_csv():
    if request.method == 'POST':
        csv_file = request.files['file']
        csv_file = TextIOWrapper(csv_file, encoding='utf-8')
        csv_reader = csv.reader(csv_file, delimiter=',', skipinitialspace=True)
        for row in csv_reader:
            set = Set(set_num=row[0], name=row[1], year=row[2], theme_id=row[3], num_parts=row[4], image_url='')
            db.session.add(set)
            db.session.commit()
        return redirect(url_for('/sets'))
    return """
            <form method='post' action='/update' enctype='multipart/form-data'>
              Upload a csv file: <input type='file' name='file'>
              <input type='submit' value='Upload'>
            </form>
           """