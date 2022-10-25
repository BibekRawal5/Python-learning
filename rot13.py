def rot13(message):
    coded_message = ""
    for letter in message.strip():
        if letter.isalpha():
            ascii = ord(letter) + 13
            if letter.islower():
                if 97 <= ascii <= 122:
                    coded_message += chr(ascii)
                else:
                    ascii = ascii - 122
                    print("HELLO")
                    coded_message += chr(ascii + 96)
                    
            else:
                if 65 <= ascii <= 90:
                    coded_message += chr(ascii)
                else:
                    ascii = ascii - 90
                    print("RED")
                    coded_message += chr(ascii + 64)
                    
        else:
            coded_message += letter
    return coded_message