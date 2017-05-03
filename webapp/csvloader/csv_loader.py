import csv

class CsvLoader:

    def __init__(self):


    def load(self, file_path):
        with open(file_path, 'r') as file:
            reader = csv.reader(file)
            header = next(reader)

            for row in reader:
                print(row)
