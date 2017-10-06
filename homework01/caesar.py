D1 = dict(zip("ABCDEFGHIJKLMNOPQRSTUVWXYZ",range(26)))
D2 = dict(zip(range(26),"ABCDEFGHIJKLMNOPQRSTUVWXYZ"))

plaintext = input()

# encrypt
ciphertext = ""
for c in plaintext.upper():
    if c.isalpha(): ciphertext += D2[ (D1[c] + 3) % 26]
    else: ciphertext += c

# decrypt
plaintext2 = ""
for c in ciphertext.upper():
    if c.isalpha(): plaintext2 += D2[ (D1[c] - 3) % 26]
    else: plaintext2 += c

print(plaintext)
print(ciphertext)
print(plaintext2)