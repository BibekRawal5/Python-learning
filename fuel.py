import sys

def main():
    fraction = input("Entet the fraction(X/Y): ")
    gauge = indicator(fraction)
    print(gauge)

def indicator(f):
    try:
        x,y = f.split("/")
        x = int(x)
        y = int(y)
        per = x/y * 100
        per = round(per)
    except ValueError:
        print("The fraction you enter is invalid")
        sys.exit()
    except ZeroDivisionError:
        print("The fraction has zero as a denominator")
        sys.exit()
    else:
        if per <= 1:
            return "E"
        elif per >= 99:
            return "F"
        return per


if __name__ == "__main__":
    main()