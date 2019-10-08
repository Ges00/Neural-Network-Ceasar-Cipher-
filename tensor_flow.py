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
#caricmento dei dati per l'allenaento e per il testing
#le x sono le frequenze delle lettere di ogni parola cifrata
#le y sono array di zeri con un uno nella posizione che identifica la chiave corretta
(x_train, y_train), (x_test, y_test) = ld.load_data()
#x_train = tf.keras.utils.normalize(x_train,axis=1)
#x_test = tf.keras.utils.normalize(x_train,axis=1)

#prima cosa da fare, creo un modello incui gli output di un layer sonoinput del seguente
#simile a tf.model ma quest'ultima è più generica. per una rete base uso sequential
model = tf.keras.models.Sequential()
#usato per appiattire multi dimentional array
#model.add(tf.keras.layers.Flatten())

#layer di input, posso usare anche la relu
#model.add(tf.keras.models.Flatten())
model.add(tf.keras.layers.Dense(26, input_dim=26, activation='relu'))
#first hidden layer
model.add(tf.keras.layers.Dense(30, activation='relu'))
#second hidden layer
model.add(tf.keras.layers.Dense(30, activation='relu'))
#la sigmoidea ritorna una probabilità
#la relu è preferibile in quanto riesco ad avvicinarmi di più all'output desiderato
#output layer
model.add(tf.keras.layers.Dense(26, activation='softmax'))

#cercare la loss giusta
model.compile(optimizer='adam',
            loss='mean_squared_error',
            metrics=['accuracy'])
#riempimento del modello keras, cercare le epochs e i batch corretti
model.fit(x_train[1], y_train, epochs=3, batch_size=10)


# evaluate the keras model
_, accuracy = model.evaluate(x_train[1], y_train)
print('Accuracy: %.2f \n' % (accuracy*100))

#making prediction for the test set
x_words=x_train[0]

predictions = model.predict(x_train[1])
for i in range(5):
    key=get_key(y_train[i])
    print('%s => %s (expected %d)' % (x_words[i], predictions[i], key))

# serialize model to JSON
model_json = model.to_json()
with open("model.json", "w") as json_file:
    json_file.write(model_json)
# serialize weights to HDF5
model.save_weights("model.h5")
print("Saved model to disk")
