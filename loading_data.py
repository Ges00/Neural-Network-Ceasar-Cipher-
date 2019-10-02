import random
import cifrario_cesare as cc
import frequency as freq

#dizionario lettera: frequenza lingua INGLESE
letters_frequency=dict({
    "A" : "0.855", "K" : "0.081", "U" : "0.268",
    "B" : "0.160", "L" : "0.421", "V" : "0.106",
    "C" : "0.316", "M" : "0.253", "W" : "0.183",
    "D" : "0.387", "N" : "0.717", "X" : "0.019",
    "E" : "0.121", "O" : "0.747", "Y" : "0.172",
    "F" : "0.218", "P" : "0.207", "Z" : "0.011",
    "G" : "0.209", "Q" : "0.010",
    "H" : "0.496", "R" : "0.633",
    "I" : "0.733", "S" : "0.673",
    "J" : "0.022", "T" : "0.894"
})

alphabet=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
        'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

#caricamento delle parole dal fil words.txt
def load_words():
    words = []
    f = open(r'D:\file_txt\words.txt', 'r')
    for line in f:
        # tolgo il \n per ogni riga
        words.append(line.rstrip() + ' ')
    #cancello i simboli dalle parole
    for word in words:
        for char in word:
            if char.lower() not in alphabet:
                word=word.replace(char,'')
    random.shuffle(words)
    f.close()

    return words


#genera le frasi dalle parole singole
def generate_phrases():
    words=load_words()
    phrases = [words [i:i + 10] for i in range(0, len(words), 10)]
    return phrases


#cifra tutte le frasi nell'array passato
def phrase_encryption(phrases):
    cyphered_phrases=[]
    for phrase in phrases:
        #ha senso aumentare gli interi su cui si generano le chiavi?
        key=random.randint(1, 26)
        cyphered_phrase = cc.encrypt(''.join(phrase), key)
        cyphered_phrases.append(cyphered_phrase)

#cifra tutte le parole in words
def words_encryption(words):
    cyphered_words=[]
    keys=[]
    for word in words:
        #ha senso aumentare gli interi su cui si generano le chiavi?
        key=random.randint(1, 26)
        #le lettere dovrebbero essere tutte lower
        cyphered_word = cc.encrypt(''.join(word)
        keys.append(key)
        cyphered_words.append(cyphered_word)
    return (cyphered_words,keys)

#carico le parole in vettori e genero i la tupla di vettori in uscita pronti per l'allenamento
#X sta per PLAINTEXT, Y per testo CIPHERTEXT
def load_data():
    #466467 parole
    words=load_words()
    #le parole per il test sono l'80% del dataset globale
    training_words_length=int(len(words)*0.8)

    training_w_e_keys=words_encryption(words[:training_words_length])
    test_w_e_keys=words_encryption(words[training_words_length:len(words)]))

    #373173 parole cifrate
    x_train=get_frequencies(training_w_e_keys(0))

    #93294 parole cifrate
    x_test=get_frequencies(words_encryption(test_w_e_keys(1))


    return ((x_train, y_train), (x_test, y_test))

#prende in ingresso delle parole e ritorna un vettore 2dimensinale con le
#frequenze delle lettere di ogni parola
def get_frequencies(words):
    frequencies=[]
    for i in range(0, len(words)):
        frequency=freq.percentage_freq(words[i])
        frequencies.append(frequency)
    return frequencies


load_data
