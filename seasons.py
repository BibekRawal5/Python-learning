import datetime
import sys
import inflect

def main():
    p = inflect.engine()
    date = input("Enter date(YYYY-MM-DD): ").strip()
    try:
        year, month, day = date.split("-")
        year, month, day = int(year), int(month) ,int(day)
        if not(0 < month <= 12):
            sys.exit("Given month is invalid")
    except ValueError:
        sys.exit("Invalid date format")

    date = datetime.date(year, month, day)
    days = compare(date)
    minutes = convert_to_minutes(days)
    print(f"{p.number_to_words(minutes, andword='')} minutes.")

def convert_to_minutes(days):
    return days * 1440

def compare(date):
    today = datetime.date.today()
    timedelta = today - date
    return timedelta.days


if __name__ == "__main__":
    main()