# ============================================================
# Program 5b: SHA Hash Algorithm
# Required Packages: None (uses built-in hashlib)
# ============================================================

import hashlib


# ---------------- Main ----------------
print("--- SHA Hash ---")
text = input("Enter string to hash: ")

data = text.encode('utf-8')

sha1   = hashlib.sha1(data).hexdigest()
sha256 = hashlib.sha256(data).hexdigest()
sha512 = hashlib.sha512(data).hexdigest()

print("\nSHA-1   :", sha1)
print("SHA-256 :", sha256)
print("SHA-512 :", sha512)
