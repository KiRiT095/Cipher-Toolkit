# Cipher Toolkit (Pre-Alpha 0.2)

A Python-based project exploring classical cryptography concepts, encoding techniques, and cybersecurity fundamentals as part of my cybersecurity learning journey.

## Current Features

### Encoding Utilities

* Convert decimal numbers to:

  * Binary
  * Octal
  * Hexadecimal

### Cipher Encryption

* Caesar Cipher Encryption
* Support for uppercase letters, lowercase letters, digits, and special characters

### Program Features

* Interactive command-line interface
* Input validation using exception handling (`try-except`)
* Menu-driven toolkit architecture

## Current Status

🚧 This project is currently in **Pre-Alpha 0.2** and is actively being developed. New cryptographic algorithms, decryption tools, and security-related utilities will be added as I continue learning Python and cybersecurity concepts.

## Planned Features

### Encryption

* Vigenère Cipher
* Rail Fence Cipher
* Playfair Cipher

### Decryption

* Caesar Cipher Decryption
* Decryption support for all implemented ciphers
* Automatic multi-cipher decryption mode (experimental)

### Security Utilities

* Password Strength Analyzer
* SHA-256 Password Hashing
* Improved User Interface

## Project Workflow

The toolkit is designed to allow users to optionally apply an **encoding layer** before encryption.

Example:

```
Plaintext
    ↓
Binary / Octal / Hexadecimal Encoding (Optional)
    ↓
Cipher Encryption
    ↓
Encrypted Output
```

This layered approach helps demonstrate the differences between **encoding** and **encryption** while exploring classical cryptographic techniques.

## Technologies Used

* Python 3

## Learning Objectives

This project serves as a hands-on approach to:

* Strengthening Python programming skills
* Understanding classical cryptographic techniques
* Exploring secure coding practices
* Learning fundamental cybersecurity concepts
* Building practical cybersecurity-related tools

## Disclaimer

This project is intended **for educational purposes only**.

Binary, octal, and hexadecimal conversions are **encoding methods**, not encryption techniques, and should not be considered secure methods of protecting sensitive information.

The cryptographic implementations in this project focus on learning classical cryptography concepts and are **not suitable for real-world security applications**.

## Documentation

Algorithms and flowcharts used in the development process are available in the `Algorithms/` directory.

## Author

**Aarsh Dubey**

Cyber Security Engineering Student | Python Enthusiast | Aspiring Security Professional
