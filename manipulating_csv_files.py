# manipulating CSV files in python

import csv

try:
    with open("worksheet_01.csv", "w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(["name", "profession"])
        writer.writerow(["fulano da silva", "developer full-back-"])
        writer.writerow(["ciclano ferreira", "DevOps"])
        writer.writerow(["beutrano de souza", "QA"])
except IOError as exc:
    print("error opening the file.")
    print(exc)

try:
    with open("worksheet_01.csv", "r", newline="", encoding="utf-8") as file:
        reader = csv.reader(file)
        for row in reader:
            print(row)
except FileNotFoundError as exc:
    print("file not found for reading.")
    print(exc)