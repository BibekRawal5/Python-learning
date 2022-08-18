import sys

if len(sys.argv) <= 1:
    print("Too few command line arguments")
    sys.exit()
elif len(sys.argv) > 2:
    print("Too many command line arguments")
    sys.exit()


count = 0
if sys.argv[1].endswith(".py"):
    try:
        with open(sys.argv[1]) as file:
            for line in file:
                if line.strip().startswith("#"):
                    continue
                if line.isspace():
                    continue
                else:
                    count += 1
    except FileNotFoundError:
        print("File not found")
        sys.exit()

else:
    print("Enter a python file")
    sys.exit()

print(f"number of lines: {count}")