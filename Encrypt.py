"""Write a code that will take (AnyString) and substitute all vowels with
character's like $#%^&* etc..... but DO NOT USE ' or " as any of your characters."""
def encrypt(plaintext):
    plaintext= plaintext.lower()
    ciphertext = ""
    for ch in plaintext:
        if ch == "a":
            ciphertext = ciphertext + "$"
        elif ch == 'e':
            ciphertext = ciphertext + '#'
        elif ch == 'i':
            ciphertext = ciphertext + '%'
        elif ch == 'o':
            ciphertext = ciphertext + '^'
        elif ch == 'u':
            ciphertext = ciphertext + '&'
        else:
            ciphertext = ciphertext + ch
    return ciphertext
print(encrypt('HEllo how are you'))
