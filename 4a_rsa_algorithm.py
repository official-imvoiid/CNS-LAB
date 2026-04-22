# ============================================================
# Program 4a: RSA Algorithm
# Required Packages: None (uses built-in Python only)
# ============================================================

from math import gcd


def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


def mod_inverse(e, phi):
    for d in range(2, phi):
        if (e * d) % phi == 1:
            return d
    return None


# ---------------- Main ----------------
print("--- RSA Algorithm ---")
p = int(input("Enter first prime  (p): "))
q = int(input("Enter second prime (q): "))

if not (is_prime(p) and is_prime(q)):
    print("Both numbers must be prime!")
    exit()

n = p * q
phi = (p - 1) * (q - 1)

# Choose e such that 1 < e < phi and gcd(e, phi) = 1
e = 2
while e < phi:
    if gcd(e, phi) == 1:
        break
    e += 1

# Compute d (modular inverse of e mod phi)
d = mod_inverse(e, phi)

print(f"\nPublic Key  : (e={e}, n={n})")
print(f"Private Key : (d={d}, n={n})")

text = input("\nEnter text to encrypt: ")

# Encrypt each character
encrypted = [pow(ord(ch), e, n) for ch in text]
decrypted = "".join(chr(pow(ch, d, n)) for ch in encrypted)

print("Encrypted   :", encrypted)
print("Decrypted   :", decrypted)
