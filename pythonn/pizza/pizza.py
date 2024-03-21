import sys
from tabulate import tabulate
import csv

if len(sys.argv) < 2:
    sys.exit("Too few command-line arguments")
elif len(sys.argv) > 2:
    exit("Too many command-line arguments")
x = (sys.argv[1]).endswith(".csv")       #x = .csv
if x == False:                        #if x contains .csv
    exit("Not a CSV file")
table = []
try:
    with open(sys.argv[1],"r") as file:
        reader = csv.reader(file)
        for row in reader:
            table.append(row)
except FileNotFoundError:
    exit("File does not exist")

print(tabulate(table[1:],headers = table[0], tablefmt="grid"))

