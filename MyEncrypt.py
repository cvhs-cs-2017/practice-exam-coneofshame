def What_Is_This(plaintext):
    halfLength = int(len(plaintext) / 2)
    fronthalf = plaintext[:halfLength]
    backhalf = plaintext[halfLength:]
    if len(fronthalf) != len(backhalf):
        fronthalf = fronthalf + '='
        halfLength = halfLength + 1
    ciphertext = ''
    newBackHalf = ''
    cipher2 = ''
    for ch in backhalf:
        newBackHalf = ch + newBackHalf
    for i in range(halfLength):
        ciphertext = ciphertext + fronthalf[i]
        ciphertext = ciphertext + newBackHalf[i]
    if len(newBackHalf) < len(fronthalf):
        ciphertext = ciphertext + fronthalf[-1]
    for ch in ciphertext:
        if ch == '=':
            cipher2 = cipher2
        else:
            cipher2 = cipher2 + ch

    return cipher2
print(What_Is_This('Sorry i Haven\'t got any money on me today'))
#leo did it correctly
