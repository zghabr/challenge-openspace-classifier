import csv


def get_colleagues_list(filepath):
    with open(filepath, mode='r') as file:
        csvFile = csv.reader(file)
        colleagues = []
        for lines in csvFile:
            colleagues.append(lines[0])
        return colleagues
