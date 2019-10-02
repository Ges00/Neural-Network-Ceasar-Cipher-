from collections import Counter

alphabet=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
        'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

#trova la frequenza intera di ogni lettera
def find_frequency(phrase):
    all_freq = {}
    for i in phrase:
        if i in all_freq:
            all_freq[i] += 1
        else:
            all_freq[i] = 1
    for letter in alphabet:
        if letter not in all_freq:
            all_freq[letter]=0
    return all_freq

#elimina gli spazi dal dict delle frequenze
def delete_special_chars(all_freq):
    all_freq_not_space = dict(all_freq)
    #da aggiungere nel caso di frasi
    #del all_freq_not_space[' ']
    return all_freq_not_space

#frequenza percentuale delle lettere nella frase
def percentage_freq(phrase):
    all_freq_dict=find_frequency(phrase)
    for letter in all_freq_dict:
        all_freq_dict[letter]=round(all_freq_dict[letter]/len(phrase), 4)
    all_freq=[]
    for key, value in sorted(all_freq_dict.items()): # Note the () after items!
        all_freq.append(value)
    return all_freq
