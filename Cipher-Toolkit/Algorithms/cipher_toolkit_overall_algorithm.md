# Cipher Toolkit Project - Overall Algorithm

## Aim
To design a menu-driven Python project that performs cipher encryption, cipher decryption, decimal conversion, and password strength checking.

---

## Overall Algorithm

1. Start the program.

2. Display the main menu:
   - Cipher Encryption
   - Cipher Decryption
   - Decimal Conversion
   - Password Strength Checker

3. Input the user's service choice.

4. If the choice is **Cipher Encryption**:
   1. Display the encryption cipher menu.
   2. Input the cipher type.
   3. Input the plaintext and the required key/value.
   4. If the selected cipher is Caesar Cipher, encrypt the text using the Caesar formula.
   5. If the selected cipher is Vigenère Cipher, encrypt the text using the keyword.
   6. If the selected cipher is Rail Fence Cipher, encrypt the text using the rail pattern.
   7. If the selected cipher is Play Fair Cipher, encrypt the text using the Play Fair rules.
   8. Display the encrypted result.

5. If the choice is **Cipher Decryption**:
   1. Display the decryption cipher menu.
   2. Input the cipher type.
   3. Input the ciphertext and the required key/value.
   4. If the selected cipher is Caesar Cipher, decrypt the text by reversing the Caesar shift.
   5. If the selected cipher is Vigenère Cipher, decrypt the text using the keyword.
   6. If the selected cipher is Rail Fence Cipher, decrypt the text using the rail pattern reconstruction.
   7. If the selected cipher is Play Fair Cipher, decrypt the text using the Play Fair rules.
   8. Display the decrypted result.

6. If the choice is **Decimal Conversion**:
   1. Input the decimal number.
   2. Ask the user which conversion is required:
      - Binary
      - Octal
      - Hexadecimal
   3. Convert the number into the selected base.
   4. Display the converted result.

7. If the choice is **Password Strength Checker**:
   1. Input the password.
   2. Check whether the password contains:
      - Uppercase letters
      - Lowercase letters
      - Digits
      - Special characters
      - Minimum length
   3. Assign a strength level based on the conditions.
   4. Display the password strength.

8. Ask the user whether they want to use another service.
   - If yes, repeat from Step 3.
   - If no, stop the program.

9. End the program.

---

## Caesar Cipher Encryption Algorithm

1. Input the plaintext.
2. Input the key.
3. Loop through each character.
4. If the character is uppercase:
   - Convert it to a 0-25 index using `ord(char) - ord('A')`
   - Add the key
   - Apply modulo 26
   - Convert back to ASCII using `+ ord('A')`
   - Convert to character using `chr()`
5. If the character is lowercase:
   - Convert it to a 0-25 index using `ord(char) - ord('a')`
   - Add the key
   - Apply modulo 26
   - Convert back to ASCII using `+ ord('a')`
   - Convert to character using `chr()`
6. If the character is special or numeric, leave it unchanged.
7. Append each processed character to the result string.
8. Display the encrypted text.

---

## Caesar Cipher Decryption Algorithm

1. Input the ciphertext.
2. Input the key.
3. Loop through each character.
4. If the character is uppercase:
   - Convert it to a 0-25 index using `ord(char) - ord('A')`
   - Subtract the key
   - Apply modulo 26
   - Convert back to ASCII using `+ ord('A')`
   - Convert to character using `chr()`
5. If the character is lowercase:
   - Convert it to a 0-25 index using `ord(char) - ord('a')`
   - Subtract the key
   - Apply modulo 26
   - Convert back to ASCII using `+ ord('a')`
   - Convert to character using `chr()`
6. If the character is special or numeric, leave it unchanged.
7. Append each processed character to the result string.
8. Display the decrypted text.

---

## Decimal Conversion Algorithm

1. Input a decimal number.
2. Ask the user for the required base conversion.
3. If the choice is Binary, convert using `bin()`.
4. If the choice is Octal, convert using `oct()`.
5. If the choice is Hexadecimal, convert using `hex()`.
6. Remove the prefix (`0b`, `0o`, `0x`) if needed.
7. Display the result.

---

## Password Strength Checker Algorithm

1. Input the password.
2. Initialize the strength counter to 0.
3. Check if the password length is at least 8 characters.
4. Check if it contains at least one uppercase letter.
5. Check if it contains at least one lowercase letter.
6. Check if it contains at least one digit.
7. Check if it contains at least one special character.
8. Increase the strength counter for each condition satisfied.
9. Based on the final score, display:
   - Weak Password
   - Moderate Password
   - Strong Password

#Flowchart
![Cipher Toolkit Flowchart](Resources/Flowchart.png)
---

## Notes
- Special characters and digits are left unchanged in Caesar Cipher.
- The same menu structure can be reused for encryption and decryption.
- The project can later be expanded with more ciphers and better error handling.
