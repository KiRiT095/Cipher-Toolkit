while True:

    Service = input(
        "Welcome to Cipher Toolkit!\n\n"
        "Please select the service you wish to use:\n"
        "1. Cipher Encryption\n"
        "2. Decimal Conversion\n"
        "3. Password Strength Checker\n--> "
    ).lower()

    if Service in [
        "cipher encryption",
        "decimal conversion",
        "password strength checker"
    ]:

        # DECIMAL CONVERSION
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
                    break

                elif encryption == "binary":
                    print("Binary:", bin(password)[2:])
                    break

                elif encryption == "octal":
                    print("Octal:", oct(password)[2:])
                    break

                else:
                    print("Invalid conversion type")

        # CIPHER ENCRYPTION
        elif Service == "cipher encryption":

            kind = input(
                "\nEnter the kind of cipher encryption "
                "you wish to test:\n"
                "1. Caesar Cipher\n"
                "2. Vigenère Cipher\n"
                "3. Rail Fence Cipher\n"
                "4. Play Fair Cipher\n--> "
            ).lower()

            # CAESAR CIPHER
            if kind == "caesar cipher":

                result = ""

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

                for pas in password:

                    if pas.islower():

                        x = ord(pas) - ord('a')

                        c = chr(
                            ((x + key) % 26)
                            + ord('a')
                        )

                    elif pas.isupper():

                        x = ord(pas) - ord('A')

                        c = chr(
                            ((x + key) % 26)
                            + ord('A')
                        )

                    else:

                        c = pas

                    result += c

                print("\nEncrypted text:", result)
                break

            else:
                print("This cipher has not been implemented yet.")

    else:
        print("Invalid service. Please try again.")
