#Q13 Write a python function parse_csv to parse CSV files.
import csv

with open('newCSVFile.csv', 'r') as csv_file:
    reader = csv.reader(csv_file)

    for row in reader:
        print(row)