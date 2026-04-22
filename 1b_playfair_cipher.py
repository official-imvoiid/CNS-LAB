# ============================================================
# Program 1b: Playfair Cipher
# Required Packages: None (uses built-in Python only)
# ============================================================

def create_matrix(key):
    key = key.upper().replace("J", "I")
    alphabet = "ABCDEFGHIKLMNOPQRSTUVWXYZ"   # 'J' excluded
    matrix = []
    for char in key + alphabet:
        if char.isalpha() and char not in matrix:
            matrix.append(char)
    return [matrix[i:i+5] for i in range(0, 25, 5)]


def find_pos(matrix, char):
    for i in range(5):
        for j in range(5):
            if matrix[i][j] == char:
                return i, j


def process(text, matrix, shift):
    result = ""
    for i in range(0, len(text), 2):
        r1, c1 = find_pos(matrix, text[i])
        r2, c2 = find_pos(matrix, text[i+1])

        if r1 == r2:            # same row
            result += matrix[r1][(c1 + shift) % 5] + matrix[r2][(c2 + shift) % 5]
        elif c1 == c2:          # same column
            result += matrix[(r1 + shift) % 5][c1] + matrix[(r2 + shift) % 5][c2]
        else:                   # rectangle rule
            result += matrix[r1][c2] + matrix[r2][c1]
    return result


# ---------------- Main ----------------
print("--- Playfair Cipher ---")
text = input("Enter text: ").upper().replace("J", "I").replace(" ", "")
key = input("Enter key: ")

if len(text) % 2 != 0:
    text += "X"

matrix = create_matrix(key)
encrypted = process(text, matrix, 1)
decrypted = process(encrypted, matrix, -1)

print("Encrypted Text:", encrypted)
print("Decrypted Text:", decrypted)
