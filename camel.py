def main():
    camel = input("Enter name of variable in camelCase: ")
    ret = convert(camel)
    print("Variable in snake_case : " + ret)

def convert(cam):
    for i in cam:
        if i.isupper():
            print(i)
            cam = cam.replace(i, f"_{i.lower()}")
            print(cam)
    return cam
        
if __name__ == "__main__":
    main()