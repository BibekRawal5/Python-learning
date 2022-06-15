def loop():
    for i in range (1, 4, 1):
        print("#" * i)


def main():
    user = input("Enter username: ")
    print("hello, " + user)

    x = int(input("X: "))
    y = int(input("Y: "))

    if x > y :
        print(str(x) + " is greater")
    elif x == y :
        print("They are equals")
    else:
        print(str(y) + " is greater")

    for i in range(3, 0, -2):
        print(f"{i} HEllo, {user.lower()}", end = "\t")
        print("NUmber " + str(i))

    i = 8
    while i <= 10:
        print("Hello, " + user)
        i += 1


def list():
    scores = []

    for i in range (4):
        scores.append(int(input("Enter the score: ")))
    
    print("Average: " + str(sum(scores) / len(scores)))


def uppercase():
    before = input("Enter the string: ")
    
    ##print("Uppercsae: " + before.upper())
    vib = []
    for c in before:
        vib.append(c.upper())
    print(vib[1])

uppercase()