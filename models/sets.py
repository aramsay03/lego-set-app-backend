import csv

class Set:
    def __init__(self, index, set_num, name, year, theme_id, num_parts, image_url):
        self.index = int(index)
        self.set_num = set_num
        self.name = name
        self.year = int(year)
        self.theme_id = int(theme_id)
        self.num_parts = int(num_parts)
        self.image_url = image_url
    
    def read_sets_csv():
        sets = []

        with open("../csv_files/sets.csv", "r") as csvfile:
            reader = csv.reader(csvfile, skipinitialspace=True)

            for row in reader:
                print(row)