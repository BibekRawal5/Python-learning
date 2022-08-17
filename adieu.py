import inflect

def main():
    p = inflect.engine()
    names = []
    while True:
        try:
            name = input("Name: ")
        except EOFError:
            break
        else:
            names.append(name)
    print("Adieu,adieu to "+ p.join(names))


if __name__ == "__main__":
    main()