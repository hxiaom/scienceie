import csv
import os

filename = './data/3.csv'

with open(filename, 'r', errors='ignore') as f:
    reader = csv.reader(f)
    for row in reader:
        patentnumber = row[0]
        title = row[1]
        abstract = row[2]
        file = open("./data/3/" + patentnumber + '.txt', 'w')
        file.write(title + '. ' + abstract)
        file.close()
        file = open("./data/3/" + patentnumber + '.ann', 'w')
        file.close()