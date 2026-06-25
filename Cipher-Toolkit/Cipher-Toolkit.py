#functions defined-------------------------------------

def encoder(result):

    encr = input(
        "Enter the kind of Encoding "
        "(Binary, Octal, Hexadecimal):\n\t"
    ).lower()

    e = ""

    if encr == "hexadecimal":

        for enc in result:
            e += hex(ord(enc))[2:] + " "

        return "Hexadecimal: " + e.strip()

    elif encr == "binary":

        for enc in result:
            e += bin(ord(enc))[2:] + " "

        return "Binary: " + e.strip()

    elif encr == "octal":

        for enc in result:
            e += oct(ord(enc))[2:] + " "

        return "Octal: " + e.strip()

    else:

        return "Invalid conversion type"

#-------------------------------------------------------
#caesar cipher defined

def caesar_cipher_encryption(password, key):
    result = ""

    for pas in password:
        if pas.islower():
            x = ord(pas) - ord('a')
            c = chr(((x + key) % 26) + ord('a'))

        elif pas.isupper():
            x = ord(pas) - ord('A')
            c = chr(((x + key) % 26) + ord('A'))

        else:
            c = pas

        result += c
    return result

#Rail fence defined--------
def rail_fence_encrypt(password, key):

                        if key <= 1 or key >= len(password):
                            return password

                        rails = [""] * key

                        k = 0
                        direction = 1

                        for j in password:

                            rails[k] += j

                            if k == key - 1:
                                direction = -1

                            elif k == 0:
                                direction = 1

                            k += direction

                        result = ""

                        for rail in rails:
                            result += rail

                        return result

#decoder------------------------------------------------------------

def decoder(encoded) :

    decoded=bin(encoded)

    return decoded

#Caesar cipher decryption------------------------------------------

def caesar_cipher_decryption(password, key):
    result = ""

    key = key % 26

    for pas in password:
        if pas.islower():
            x = ord(pas) - ord('a')
            c = chr(((x - key) % 26) + ord('a'))

        elif pas.isupper():
            x = ord(pas) - ord('A')
            c = chr(((x - key) % 26) + ord('A'))

        else:
            c = pas

        result += c

    return result
    

#Code--------------------------------------------------------------

while True:

    Service = input(
        "Welcome to Cipher Toolkit!\n\n"
        "Please select the service you wish to use:\n"
        "1. Encryption\n"
        "2. Decryption\n"
        "3. Decimal Conversion\n"
        "4. Password Strength Checker\n--> "
    ).lower()

    if Service in [
        "encryption",
        "decryption",
        "decimal conversion",
        "password strength checker"
    ]:

# DECIMAL CONVERSION-----------------------------------------------------------------------------------------------
        if Service == "decimal conversion":

            while True:
                try:
                    password = int(
                        input(
                            "Enter your password\n"
                            "Allowed characters: 0-9\n\t"
                        )
                    )
                    break

                except ValueError:
                    print("Try again with only numeric values\n")

            while True:

                encryption = input(
                    "Enter the kind of conversion "
                    "(Binary, Octal, Hexadecimal):\n\t"
                ).lower()

                if encryption == "hexadecimal":
                    print("Hexadecimal:", hex(password)[2:])
                    exit()

                elif encryption == "binary":
                    print("Binary:", bin(password)[2:])
                    exit()

                elif encryption == "octal":
                    print("Octal:", oct(password)[2:])
                    exit()

                else:
                    print("Invalid conversion type")

#---------------------------------------------------------------------------------------------------

        # CIPHER ENCRYPTION
        elif Service == "encryption":
            
            kind = input(
                "\nEnter the kind of cipher encryption "
                "you wish to test:\n"
                "1. Caesar Cipher (Numeric Key)\n"
                "2. Vigenère Cipher (Alphabetic Key)\n"
                "3. Rail Fence Cipher (Numeric Key)\n"
                "4. Play Fair Cipher (Alphabetic Key)\n--> "
            ).lower()
#-----------------------------------------------------------------------------------------------------

# CAESAR CIPHER Encryption---------------------------------------------------------------------------
          
            if kind == "caesar cipher":

                encode=input(
                    "\nWould you like to encode your password after applying cipher? (Y/N) : "
                    ).lower()

                password = input(
                    "\nPlease enter the text you wish to encrypt: "
                )
 
                while True:
                    try:
                        key = int(
                            input(
                                "Please enter the key for encryption "
                                "(numeric value only): "
                            )
                        )
                        break

                    except ValueError:
                        print("Please enter a numeric key.")


# CIPHER 
                res=caesar_cipher_encryption(password, key)


# ENCODE

                if encode == "y":
                    print (encoder(res))

                else :
                  print("Encrypted text:", res)
                break

        
#--------------------------------------------------------------------------------



#rail fence cipher---------------------------------------------------------------

            if kind=="rail fence cipher":
                    enc=input("Would you like to encode the password after encryption? (y/n)\n--> ").lower()

                    password=input("Please enter the password to encrypt : ")

                    while True:
                        try:
                            key = int(
                                input(
                                    "Please enter the no. of rails for encryption "
                                    "(numeric value only): "
                                )
                            )
                            break

                        except ValueError:
                            print("Please enter a numeric key.")

                            
                    encrypted = rail_fence_encrypt(password, key)



                    if enc=="y":
                        encoded= encoder(encrypted)
                        print ("Encoded and encrypted rail fence cipher would be : ", encoded)

                    else :
                        print("Encrypted : ", encrypted)


    else:
        print("Invalid service. Please try again.")
