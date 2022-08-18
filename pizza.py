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
        reader = csv.DictReader(file)
        for row in reader:
            menu.append({"Pizza": row["Pizza"], "Small": row["Small"], "Large": row["Large"]})

else:
    print("Enter a valid csv file")
    sys.exit()

print(tabulate(menu, headers = "keys", tablefmt = "grid"))
# print(menu)