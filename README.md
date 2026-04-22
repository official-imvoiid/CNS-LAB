# Cryptography and Network Security (CNS) Lab

This repository contains simple, working Python implementations of classical and modern cryptographic algorithms written for the **Cryptography and Network Security Lab**.

## Contents

| No.  | File                         | Algorithm                    | Type                 |
|------|------------------------------|------------------------------|----------------------|
| 1a   | `1a_caesar_cipher.py`        | Caesar Cipher                | Classical (Substitution) |
| 1b   | `1b_playfair_cipher.py`      | Playfair Cipher              | Classical (Substitution) |
| 1c   | `1c_hill_cipher.py`          | Hill Cipher (2x2)            | Classical (Matrix)   |
| 2    | `2_des_algorithm.py`         | DES                          | Symmetric Block Cipher |
| 3    | `3_aes_algorithm.py`         | AES-128 (CBC mode)           | Symmetric Block Cipher |
| 4b   | `4b_diffie_hellman.py`       | Diffie-Hellman Key Exchange  | Key Exchange         |
| 5a   | `5a_md5_hash.py`             | MD5                          | Hash Function        |

## Requirements

- Python 3.8 or higher
- `pip` package manager

## Packages to Install

Only two external packages are needed across all programs:

```bash
pip install numpy pycryptodome
```

Or install them individually as needed:

```bash
pip install numpy          # for Hill Cipher (1c)
pip install pycryptodome   # for DES (2) and AES (3)
```

The remaining programs (Caesar, Playfair, Diffie-Hellman, MD5) use only Python's **built-in** modules, so no extra installation is required for them.

## How to Run

Run any program from your terminal:

```bash
python 1a_caesar_cipher.py
```

Each program will prompt you for inputs such as text, key, shift value, etc.

## Sample Inputs for Quick Testing

| Program        | Sample Input               |
|----------------|----------------------------|
| Caesar         | text = `HELLO`, shift = `3`  |
| Playfair       | text = `HELLO`, key = `MONARCHY` |
| Hill Cipher    | text = `HELP`              |
| DES / AES      | any text (e.g., `HELLO WORLD`) |
| Diffie-Hellman | p = `23`, g = `5`          |
| MD5            | any string                 |

## Notes

- All classical ciphers operate on **uppercase English letters (A-Z)**.
- Playfair cipher treats `J` as `I` and pads odd-length text with `X`.
- Hill Cipher uses a fixed invertible 2x2 key matrix `[[3, 3], [2, 5]]` for simplicity.
- DES and AES generate **random keys** on each run - keys are printed to the screen for reference.
- AES uses **CBC mode** with a random IV (prepended behavior is not needed here since encryption and decryption share the same session).

## Disclaimer

These implementations are **for educational purposes only** and are intended to demonstrate the working of cryptographic algorithms as part of the CNS lab curriculum. Do not use these in production systems.

---

**Course:** Cryptography and Network Security  
**Language:** Python 3
