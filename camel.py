def main():
    camel = input("Enter name of variable in camelCase: ")
    ret = convert(camel)
    print("Variable in snake_case : " + ret)

def convert(cam):
    for i in cam:
        if i.isupper():
            cam = cam.replace(i, f"_{i.lower()}")
    return cam
        
if __name__ == "__main__":
    main()