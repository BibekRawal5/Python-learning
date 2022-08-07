def main():
    format1 = int(input("Enter the time format 12/24: "))
    if format1 == 12:
        time = input("Enter time: ")
        ret = convert_12hr(time)
    else:
        time = input("Enter time: ")
        ret = convert_24hr(time)

    if 7 <= ret <= 8:
        print("Breakfast time")
    elif 12 <= ret <= 13:
        print("Launch time")
    elif 18 <= ret <=  19:
        print("Dinner time") 

def convert_12hr(t):
    hr, min = (t.split(":"))
    min, apm = min.split(" ")
    if apm.lower().strip() == "am":
        apm = float(0)
    else:
        apm = float(12)
    hr = float(hr)
    min = float(min)
    return hr + min/60 + apm

def convert_24hr(t):
    hr, min = (t.split(":"))
    hr = float(hr)
    min = float(min)
    return hr + min/60


if __name__ == "__main__":
    main()