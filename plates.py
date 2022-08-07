def main():
    plate = input("Plate: ")

    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")

def is_valid(plate1):
    if 2 >= len(plate1) >= 6:
        return False
    if plate1.isalnum() != True:
        return False
    
    for i in range(len(plate1)):
        if i < 2:
            if plate1[i].isalpha() != True:
                return False 
        if plate1[i].isnumeric():
            if(numbers == False and plate1[i] == '0'):
                return False
            numbers = True
        else:
            numbers = False

    if numbers == True:
        return True
    else:
        return False

if __name__ == "__main__":
    main()