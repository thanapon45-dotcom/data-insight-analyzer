import csv

def load_sales(filepath):
    sales = []
    with open(filepath, newline="") as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            sales.append(int(row["sales"]))
    return sales
