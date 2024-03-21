import sys
import csv

if len(sys.argv) < 3:
    sys.exit("Too few command-line arguments")
elif len(sys.argv) > 3:
    exit("Too many command-line arguments")
data = []
try:
    with open(sys.argv[1],"r") as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            last,first = row["name"].split(",")
            data.append({'first': first.lstrip(),'last': last,'house' : row["house"]})
except FileNotFoundError:
    exit(f"Could not read {sys.argv[1]}")

with open(sys.argv[2],"w") as file:
    writer = csv.DictWriter(file,fieldnames =["first","last","house"])
    writer.writerow({"first" : "first", "last":"last","house":"house"})
    for row in data:
        writer.writerow({"first": row["first"],"last":row["last"],"house":row["house"]})

