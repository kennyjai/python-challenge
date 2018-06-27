import os
import csv

pybankCSV = os.path.join('..','Resources','budget_data.csv')

with open(pybankCSV, 'r') as csvfile:

    csvreader = csv.reader(csvfile, delimiter=",")

    totalnet = 0

    for row in csvreader:

        totalnet += row[1]

print(totalnet)