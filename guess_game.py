import random

def main():
    while True:
        try:
            level = int(input("Level: "))
        except ValueError:
            pass
        else:
            if level <= 0:
                continue
            break

    rint = random.randint(1, level)
    while True:
        try:
            guess = int(input("Guess: "))
        except ValueError:
            pass
        else:
            if guess <= 0:
                continue
            elif guess < rint:
                print("Too small!")
            elif guess > rint:
                print("Too large!")
            else:
                print("Just right!")
                break

if __name__ == "__main__":
    main()