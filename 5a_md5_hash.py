# ============================================================
# Program 5a: MD5 Hash Algorithm
# Required Packages: None (uses built-in hashlib)
# ============================================================

import hashlib


# ---------------- Main ----------------
print("--- MD5 Hash ---")
text = input("Enter string to hash: ")

md5_hash = hashlib.md5(text.encode('utf-8')).hexdigest()

print("MD5 Hash:", md5_hash)
