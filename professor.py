import random

def main():
    level = get_level()
    score = 0
    for _ in range(10):
        x = generate_integer(level)
        y = generate_integer(level)
        tries = 0
        while True:
            try:
                answer = int(input(f"{x} + {y} = "))
            except ValueError:
                print("EEE")
                if tries == 2:
                    print(f"{x} + {y} = {x+y}")
                    break
                else:
                    tries += 1
            else:
                if answer == x + y:
                    score += 1
                    break
                elif tries == 2:
                    print(f"{x} + {y} = {x+y}")
                    break
                else:
                    print("EEE")
                    tries += 1
    print(f"Your score = {score}")
   

def get_level():
     while True:
        try:
            level = int(input("Level: "))
        except ValueError:
            pass
        else:
            if 1 <= level <= 3:
                return level

def generate_integer(level):
    if level == 1:
        return random.randint(0, 9)
    elif level == 2:
        return random.randint(10, 99)
    elif level == 3:
        return random.randint(100, 999)

if __name__ == "__main__":
    main()