def main():
    text = input("Enter the text: ")
    vowels = ['a', 'e', 'i', 'o','u']

    for vow in text:
        if vow.lower() in vowels:
            text = text.replace(vow,'')
    
    print("Output: " + text)


if __name__ == "__main__":
    main()