def main():
    months =[
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
    ]

    time = input("Input: ")
    if '/' in time:
        m,d,y = time.split("/")
        m,d,y = int(m), int(d), int(y)
        print(f"{y}-{m:02}-{d:02}")
    
    elif ',' in time:
        m,y = time.split(",")
        m,d = m.split(" ")
        d,y = int(d), int(y)
        print(f"{y}-{months.index(m):02}-{d:02}")
            


if __name__ == "__main__":
    main()