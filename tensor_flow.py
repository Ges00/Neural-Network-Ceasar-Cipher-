import tensorflow as tf
from tensorflow import keras

#hep libraries
import numpy as np
import matplotlib.pyplot as plt

#my libraries
import loading_data as ld
import frequency as freq

#caricmento dei dati per l'allenaento e per il testing
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
model.add(tf.keras.layers.Dense(26, activation=tf.nn.relu))
#hidden layer
model.add(tf.keras.layers.Dense(26, activation=tf.nn.relu))
#output layer
model.add(tf.keras.layers.Dense(26, activation=tf.nn.softmax))

#cercare la loss giusta
model.compile(optimizer='adam',
            loss='sparze_categorical_crossentropy',
            metrics=['accuracy'])
model.fit(x_train, y_train, epochs=3)
