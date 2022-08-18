import csv
import sys

if len(sys.argv) != 3:
    print("Wrong amount of command line arguments")
    sys.exit()
    
if not sys.argv[1].endswith(".csv") or not sys.argv[2].endswith(".csv"):
    print("Enter the csv file in command line arguments")
    sys.exit()

try:
    file_read = open(sys.argv[1])
    file_write = open(sys.argv[2], "w")
except FileNotFoundError:
    print("File not found for taking data")
    sys.exit()
else:
    reader = csv.DictReader(file_read)
    writer = csv.DictWriter(file_write, fieldnames = ["First", "Last", "House"])
    writer.writerow({"First": "first", "Last": "last", "House": "house"})
    for row in reader:
        last, first = row["name"].split(", ")
        writer.writerow({"First": first, "Last": last, "House": row["house"]})
    file_read.close()
    file_write.close()
    

