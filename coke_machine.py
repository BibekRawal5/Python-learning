def main():
    total = 50
    while total > 0:
        print(f"Amount due: {total}")
        coin = int(input("Insert Coin: "))
        if coin == 25 or coin == 10 or coin == 5:
            total = total - coin
    
    print(f"You are owed {total * - 1} cents")

if __name__ == "__main__":
    main()