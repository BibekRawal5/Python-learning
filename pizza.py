from tabulate import tabulate
import sys
import csv

if len(sys.argv) <= 1:
    print("Too few command line arguments")
    sys.exit()
elif len(sys.argv) > 2:
    print("Too many command line arguments")
    sys.exit()

menu = []
if sys.argv[1].endswith(".csv"):
    with open(sys.argv[1]) as file:
        reader = csv.reader(file)
        for row in reader:
            menu.append([row[0], row[1], row[2]])

else:
    print("Enter a valid csv file")
    sys.exit()

print(tabulate(menu,tablefmt = "grid"))
# print(menu)