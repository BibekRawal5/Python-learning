greating = input("Greeting: ")
great = greating.strip().lower()

if great == "hello":
    print("$0")
elif great[0] == "h":
    print("$20")
else:
    print("$100")