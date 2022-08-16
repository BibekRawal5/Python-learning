def main():
    items = {}
    while True:
        try:
            item = input("Item: ")
            if item.upper() in items:
                items[item.upper().strip()] += 1
            else:
                items[item.upper().strip()] = 1
        except EOFError:
            for item in sorted(items):
                print(f"{items[item]}, {item}")
            break
            

if __name__ == "__main__":
    main()
