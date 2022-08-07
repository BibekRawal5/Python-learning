def main():
    fruit = input("Fruit: ")
    print(f"Calories: {calorie(fruit)}")

def calorie(fruit):
    fruits = {
        "apple": 130,
        "avocado": 50,
        "banana" : 110,
        "cantaloupe": 50,
        "grapefruit": 60,
        "Grapes": 90,
        "honeydew": 50,
        "kiwifruit": 90,
        "lemon": 15,
        "nectarine": 60,
        "lime": 20,
        "peach": 60,
        "orange": 80,
        "pear": 100,
        "pineapple": 50,
        "strawberries": 50,
        "plums": 70,
        "sweet cherries": 100,
        "tangerine" : 50,
        "watermelon": 80
        }
    return fruits[fruit.lower().strip()]

if __name__ == "__main__":
    main()