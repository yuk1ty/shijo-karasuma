import csv

def load(file_path):
  with open(file_path, 'r') as file:
    reader = csv.reader(file)
    header = next(reader)

    for row in reader:
      print(row)
