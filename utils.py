import csv
from tabulate import tabulate

def read_csv_file(filepath):
    data = []
    with open(filepath, encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            data.append(row)
    return data


def print_table(data):
    if not data:
        print("Нет данных для отображения")
        return

    headers = data[0].keys()
    rows = [row.values() for row in data]

    print(tabulate(rows, headers=headers, tablefmt="github"))