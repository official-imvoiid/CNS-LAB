# Cryptography and Network Security (CNS) 

[![Python](https://img.shields.io/badge/Python-3.8%2B-blue?logo=python&logoColor=white)](https://www.python.org/)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](https://github.com/)

Simple, working Python implementations of classical and modern cryptographic algorithms — built for the **Cryptography and Network Security Lab** curriculum.

---

## Contents

| No. | File | Algorithm | Category |
|-----|------|-----------|----------|
| 1a | `1a_caesar_cipher.py` | Caesar Cipher | Classical (Substitution) |
| 1b | `1b_playfair_cipher.py` | Playfair Cipher | Classical (Substitution) |
| 1c | `1c_hill_cipher.py` | Hill Cipher (2×2) | Classical (Matrix) |
| 2 | `2_des_algorithm.py` | DES | Symmetric Block Cipher |
| 3 | `3_aes_algorithm.py` | AES-128 (CBC mode) | Symmetric Block Cipher |
| 4a | `4a_rsa_algorithm.py` | RSA Algorithm | Asymmetric Encryption |
| 4b | `4b_diffie_hellman.py` | Diffie-Hellman Key Exchange | Key Exchange |
| 5a | `5a_md5_hash.py` | MD5 | Hash Function |
| 5b | `5b_sha_algorithm.py` | SHA | Hash Function |

---

## Requirements

- **Python** 3.8 or higher
- **pip** package manager

## Installation

Only two external packages are needed across all programs:

```bash
pip install numpy pycryptodome
```

Or install them individually as needed:

```bash
pip install numpy          # Required for Hill Cipher (1c)
pip install pycryptodome   # Required for DES (2) and AES (3)
```

> All other programs (Caesar, Playfair, RSA, Diffie-Hellman, MD5, SHA) use only Python's built-in modules — no extra installation required.

---

## How to Run

Run any program from your terminal:

```bash
python 1a_caesar_cipher.py
```

Each program will interactively prompt you for inputs such as plaintext, key, shift value, etc.

---

## Sample Inputs for Quick Testing

| Program | Sample Input |
|---------|-------------|
| Caesar Cipher | text = `HELLO`, shift = `3` |
| Playfair Cipher | text = `HELLO`, key = `MONARCHY` |
| Hill Cipher | text = `HELP` |
| DES / AES | any text (e.g., `HELLO WORLD`) |
| RSA | any text (e.g., `HELLO`) |
| Diffie-Hellman | p = `23`, g = `5` |
| MD5 | any string |
| SHA | any string |

---

## Notes

- All classical ciphers operate on **uppercase English letters (A–Z)**.
- Playfair cipher treats `J` as `I` and pads odd-length text with `X`.
- Hill Cipher uses a fixed invertible 2×2 key matrix `[[3, 3], [2, 5]]` for simplicity.
- DES and AES generate **random keys** on each run — keys are printed to the console for reference.
- AES uses **CBC mode** with a random IV.
- RSA demonstrates key generation, encryption, and decryption using built-in Python math.

---

## Disclaimer

These implementations are **for educational purposes only** and are intended to demonstrate the working of cryptographic algorithms as part of the CNS lab curriculum. Do not use these in production systems.

---

**Course:** Cryptography and Network Security  
**Language:** Python 3
