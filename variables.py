name = input("Name: ")
age = int(input("Age: "))
ismale = bool(input("True or False: "))

# print(f"Your name is {name}\nYour age is {age}")


print(f"Your name is \"{name.upper()}\"", end = "\t")
print(f"Your age is {age}", end = "\n")

if ismale == "True":
    print(f"You are male")
else:
    print(f"You are female")

if bool(name.upper().islower()) is True:
    print(f"It is in lowercase")
else:
    print(f"It is in uppercase")


comp1 = input("First String: ")
comp2 = input("Seconf String: ")

if comp1.strip().upper() == comp2.strip().upper():
    print(f"Both string are same")
else:
    print(f"They are different strings")