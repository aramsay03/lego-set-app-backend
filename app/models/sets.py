from app import db
import csv
from pathlib import Path
from io import TextIOWrapper

class Set(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    set_num = db.Column(db.String(64), index=True)
    name = db.Column(db.String(64))
    year = db.Column(db.Integer)
    theme_id = db.Column(db.Integer)
    num_parts = db.Column(db.Integer)
    image_url = db.Column(db.String(64))

    # def __init__(self, index, set_num, name, year, theme_id, num_parts, image_url):
    #     self.index = int(index)
    #     self.set_num = set_num
    #     self.name = name
    #     self.year = int(year)
    #     self.theme_id = int(theme_id)
    #     self.num_parts = int(num_parts)
    #     self.image_url = image_url
    
    def __repr__(self):
        return '<Set {}>'.format(self.set_num)
    
    # def update_sets_db():
    #     # sets = []
    #     csv_file_path = Path("/Users/alan/projects/python/lego_app/app/csv_files")
    #     csv_to_open = csv_file_path / "sets.csv"
    #     # csv_file = TextIOWrapper(csv_to_open, "r", encoding='utf-8')

    #     with open(csv_to_open, "r") as csvfile:
    #         csv_reader = csv.reader(csv_to_open, delimiter=',', skipinitialspace=True)
    #         for row in csv_reader:
    #             set = Set(set_num=row[0], name=row[1], year=row[2], theme_id=row[3], num_parts=row[4], image_url='')
    #             db.session.add()
    #             db.session.commit()