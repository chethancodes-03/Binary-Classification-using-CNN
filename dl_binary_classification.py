# -*- coding: utf-8 -*-
"""DL BINARY CLASSIFICATION

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1dk70soFd5s9AlmA7k2kMR0CDFJyjIq_9
"""

import tensorflow as tf

print(tf.__version__)

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

dataset = pd.read_csv("C:/Users/91944/OneDrive/Documents/ASSIGNMENTS/DL PROJECT/Churn_Modelling.csv")

x = dataset.drop(labels=["RowNumber","CustomerId","Surname","Exited"],axis=1)
y = dataset['Exited']

x.head(10)

y.head()

from sklearn.preprocessing import LabelEncoder

label_1 = LabelEncoder()
x['Geography'] = label_1.fit_transform(x['Geography'])
label_2 = LabelEncoder()
x['Gender'] = label_2.fit_transform(x['Gender'])
x.head()

if 'Geography' in x.columns:
    x = pd.get_dummies(x, drop_first=True, columns=['Geography'])
else:
    print("Column 'Geography' not found in DataFrame.")
x.head(8)

#split into train and test
from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size = 0.2, random_state = 0)

#features normalization
from sklearn.preprocessing import StandardScaler
sc = StandardScaler()
x_train = sc.fit_transform(x_train)
x_test = sc.transform(x_test)

x_train

x_test

#build model
model = tf.keras.models.Sequential()

#input lyr and 1 hiddent laye
# 1) nodes = 6(avg of inputs dim and output dim)     2)activation fun = ReLU     3)input = 11
model.add(tf.keras.layers.Dense(units=6, activation='relu', input_dim = 11))

#2 hidden layer
model.add(tf.keras.layers.Dense(units=6, activation='relu'))

#output
model.add(tf.keras.layers.Dense(units=1, activation='sigmoid'))

#compiling the model
model.compile(optimizer='adam',loss='binary_crossentropy', metrics=['accuracy'])

model.summary()

model.fit(x_train, y_train.to_numpy(), batch_size=10, epochs=20)

#evalute
test_loss, test_acc = model.evaluate(x_test,y_test.to_numpy())

print('test acccuracy{}'.format(test_acc))

y_pred = (model.predict(x_test) > 0.5).astype("int32")
print(y_pred)

print(y_test)

y_test = y_test.to_numpy()

print(y_pred[33]), print(y_test[33])

#confusion ,atrix
from sklearn.metrics import confusion_matrix, accuracy_score
cm = confusion_matrix(y_test, y_pred)
print(cm)

acc_cm = accuracy_score(y_test, y_pred)
print(acc_cm)

