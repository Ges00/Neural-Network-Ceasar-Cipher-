
#cifra il testo data una chiave
def encrypt(text, s):
    result = ""

# transverse the plain text
    for i in range(len(text)):
        char = text[i]
    # Encrypt uppercase characters in plain text
        if (char.isupper()):
            result += chr((ord(char) + s - 65) % 26 + 65)

    # Encrypt lowercase characters in plain text
        else:
            result += chr((ord(char) + s - 97) % 26 + 97)
    return result

#cifra tutte le parole in words
def get_keys(words):
    keys=[]
    for word in words:
        #ha senso aumentare gli interi su cui si generano le chiavi?
        key=random.randint(1, 26)
        #le lettere dovrebbero essere tutte lower
        cyphered_word = cc.encrypt(''.join(word), key)
        cyphered_words.append(cyphered_word)
        keys.append(key)
    return keys
