import random
import pyfiglet
import sys

def main():
    if len(sys.argv) == 1:
        string = input("Input: ")
        figlet = pyfiglet.Figlet()
        ran = random.choice(figlet.getFonts())
        print(ran)
        figlet.setFont(font = ran)
        print(figlet.renderText(string))
    elif len(sys.argv) == 3:
        figlet = pyfiglet.Figlet()
        if (sys.argv[1] != "-f" and sys.argv[1] != "--font") or sys.argv[2] not in figlet.getFonts():
            print("Invalid command line arguments")
            sys.exit()
        else:
            string = input("Input: ")
            figlet.setFont(font = sys.argv[2])
            print(figlet.renderText(string))
    else:
        print("Invalid command line arguments")
        sys.exit()


if __name__ == "__main__":
    main()

