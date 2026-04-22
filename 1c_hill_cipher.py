# ============================================================
# Program 1c: Hill Cipher (2x2)
# Required Packages: numpy
# Install: pip install numpy
# ============================================================

import numpy as np


def mod_inverse(a, m):
    for x in range(1, m):
        if (a * x) % m == 1:
            return x
    return None


def encrypt(text, key):
    text = text.upper().replace(" ", "")
    if len(text) % 2 != 0:
        text += 'X'
    result = ""
    for i in range(0, len(text), 2):
        pair = np.array([[ord(text[i]) - 65], [ord(text[i+1]) - 65]])
        enc = np.dot(key, pair) % 26
        result += chr(enc[0][0] + 65) + chr(enc[1][0] + 65)
    return result


def decrypt(cipher, key):
    det = int(key[0][0] * key[1][1] - key[0][1] * key[1][0]) % 26
    det_inv = mod_inverse(det, 26)

    adj = np.array([[key[1][1], -key[0][1]],
                    [-key[1][0], key[0][0]]])
    inv_key = (det_inv * adj) % 26

    result = ""
    for i in range(0, len(cipher), 2):
        pair = np.array([[ord(cipher[i]) - 65], [ord(cipher[i+1]) - 65]])
        dec = np.dot(inv_key, pair) % 26
        result += chr(dec[0][0] + 65) + chr(dec[1][0] + 65)
    return result


# ---------------- Main ----------------
print("--- Hill Cipher (2x2) ---")
text = input("Enter text: ")

# Example invertible 2x2 key matrix (mod 26)
key = np.array([[3, 3],
                [2, 5]])
print("Key Matrix:\n", key)

encrypted = encrypt(text, key)
decrypted = decrypt(encrypted, key)

print("Encrypted Text:", encrypted)
print("Decrypted Text:", decrypted)
