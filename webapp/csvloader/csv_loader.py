import csv

def load(file_path):
    result = []

    with open(file_path, 'r') as file:
        reader = csv.reader(file)
        header = next(reader)

        for row in reader:
            result.append(row)

    return result
