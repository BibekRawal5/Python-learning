def convert(str):
    return str.replace(":)","🙂").replace(":(", "🙁")


def main():
    text = input("Enter your text: ")
    ret = convert(text)
    print(ret)

main()