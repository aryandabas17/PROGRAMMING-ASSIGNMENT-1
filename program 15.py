import csv
try:
    with open("output.csv") as csvfile:
        csvreader = csv.reader(csvfile)
        for row in csvreader:
            print(', '.join(row))
except FileNotFoundError:
    print(f"File not found.")
except Exception as e:
    print("An error occurred.")