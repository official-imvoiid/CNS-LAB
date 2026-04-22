# ============================================================
# Program 4b: Diffie-Hellman Key Exchange
# Required Packages: None (uses built-in Python only)
# ============================================================

import random


# ---------------- Main ----------------
print("--- Diffie-Hellman Key Exchange ---")
p = int(input("Enter a prime number (p): "))
g = int(input("Enter a base (g): "))

# Step 1: Private keys
a = random.randint(2, p - 2)
b = random.randint(2, p - 2)

# Step 2: Public keys
A = pow(g, a, p)
B = pow(g, b, p)

# Step 3: Shared secrets
secret_a = pow(B, a, p)
secret_b = pow(A, b, p)

print(f"\nPublic values : p = {p}, g = {g}")
print(f"Alice's private key (a): {a}")
print(f"Bob's   private key (b): {b}")
print(f"Alice's public key  (A): {A}")
print(f"Bob's   public key  (B): {B}")
print(f"Alice's shared secret : {secret_a}")
print(f"Bob's   shared secret : {secret_b}")

if secret_a == secret_b:
    print("\nKey exchange successful! Shared secret established.")
else:
    print("\nKey exchange failed.")
