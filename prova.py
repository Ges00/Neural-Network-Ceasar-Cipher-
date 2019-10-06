import random
import numpy as np

key_array=[0, 0, 0, 1, 0, 0]

def get_key(key_array):
    for i in range(0,len(key_array)):
        if key_array[i]==1:
            return i+1

print(get_key(key_array))
