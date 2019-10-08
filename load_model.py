# MLP for Pima Indians Dataset Serialize to JSON and HDF5
import tensorflow as tf
from tensorflow import keras
#hep libraries
import numpy as np
import matplotlib.pyplot as plt

#my libraries
import loading_data as ld
import frequency as freq
import os

((x_train, y_train),(x_test, y_test))=ld.load_data()

def get_key(key_array):
    for i in range(0,len(key_array)):
        if key_array[i]==1:
            return i+1
# load json and create model
json_file = open('model.json', 'r')
loaded_model_json = json_file.read()
json_file.close()
loaded_model = tf.keras.models.model_from_json(loaded_model_json)
# load weights into new model
loaded_model.load_weights("model.h5")
print("Loaded model from disk")

# evaluate loaded model on test data
loaded_model.compile(loss='binary_crossentropy', optimizer='rmsprop', metrics=['accuracy'])
score = loaded_model.evaluate(x_train[1], y_train, verbose=0)
print("%s: %.2f%%" % (loaded_model.metrics_names[1], score[1]*100))

x_words=x_train[0]

predictions = loaded_model.predict(x_train[1])
for i in range(5):
    key=get_key(y_train[i])
    print('%s => %s (expected %d)' % (x_words[i], predictions[i], key))
    expected_key=get_key(y_train[i])
    m=max(predictions[i])
    print(m)
    generated_key=[k for k, j in enumerate(predictions[i]) if j == m]
    generated_key[0]=generated_key[0]+1
    print('%s => %s (expected %d)' % (x_words[i],generated_key ,expected_key))
