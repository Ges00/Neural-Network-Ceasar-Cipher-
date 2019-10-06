import tensorflow as tf
from tensorflow import keras
#hep libraries
import numpy as np
import matplotlib.pyplot as plt

#my libraries
import loading_data as ld
import frequency as freq
import os

def get_key(key_array):
    for i in range(0,len(key_array)):
        if key_array[i]==1:
            return i+1
# load json and create model
json_file = open('model.json', 'r')
loaded_model_json = json_file.read()
json_file.close()
loaded_model = model_from_json(loaded_model_json)
# load weights into new model
loaded_model.load_weights("model.h5")
print("Loaded model from disk")

# evaluate loaded model on test data
loaded_model.compile(loss='binary_crossentropy', optimizer='rmsprop', metrics=['accuracy'])
score = loaded_model.evaluate(X, Y, verbose=0)
print("%s: %.2f%%" % (loaded_model.metrics_names[1], score[1]*100))

predictions = loaded_model.predict(x_train[1])
for i in range(5):
    key=get_key(y_train[i])
	print('%s => %s (expected %d)' % (x_words[i].tolist(), predictions[i], key))
