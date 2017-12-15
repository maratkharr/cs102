def encrypt_caesar(plaintext):
    """
    Encrypts plaintext using a Caesar cipher.

    >>> encrypt_caesar("PYTHON")
    'SBWKRQ'
    >>> encrypt_caesar("python")
    'sbwkrq'
    >>> encrypt_caesar("")
    ''
    """
    ciphertext = ""
    for i in plaintext:
        if 64 < ord(i) < 64 + 26:
            if ord(i) > 64 + 26 - shift:
                ciphertext += chr(ord(i) + shift - 26)
            else:
                ciphertext += chr(ord(i) + shift)
        elif 96 < ord(i) < 96 + 26:
            if ord(i) > 96 + 26 - shift:
                ciphertext += chr(ord(i) + shift - 26)
            else:
                ciphertext += chr(ord(i) + shift)
        else:
            ciphertext += i
    return ciphertext


def decrypt_caesar(ciphertext):
    """
    Decrypts a ciphertext using a Caesar cipher.

    >>> decrypt_caesar("SBWKRQ")
    'PYTHON'
    >>> decrypt_caesar("sbwkrq")
    'python'
    >>> decrypt_caesar("")
    ''
    """
    plaintext = ""
    for i in ciphertext:
        if 64 < ord(i) < 64 + 26:
            if ord(i) < 64 + shift:
                plaintext += chr(ord(i) - shift + 26)
            else:
                plaintext += chr(ord(i) - shift)
        elif 96 < ord(i) < 96 + 26:
            if ord(i) < 96 + shift:
                plaintext += chr(ord(i) - shift + 26)
            else:
                plaintext += chr(ord(i) - shift)
        else:
            ciphertext += i
    return plaintext
