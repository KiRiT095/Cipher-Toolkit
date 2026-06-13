# Caesar Cipher Encryption

## Algorithm

1. Start the program.
2. Input the plaintext (password/message) to be encrypted.
3. Input the encryption key `k`.
4. Initialize an empty string `result`.
5. Loop through each character `char` in the plaintext.
6. If `char` is uppercase:
   - `x = ord(char) - ord('A')`
   - `x = (x + k) mod 26`
   - `x = x + ord('A')`
   - Convert using `chr(x)`
   - Append to `result`
7. Else if `char` is lowercase:
   - `x = ord(char) - ord('a')`
   - `x = (x + k) mod 26`
   - `x = x + ord('a')`
   - Convert using `chr(x)`
   - Append to `result`
8. Else:
   - Leave the character unchanged.
   - Append it to `result`
9. Repeat until all characters are processed.
10. Print `result`.
11. End the program.


## Flowchart

![Caesar Cipher Flowchart](Resources/Caesarcipher.png)