# -*- coding: utf-8 -*-
"""Stock-Prediction-Using-ML.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1Pde_BXakdRO3sUCT2JuG8nSww1udd15n
"""

#Code For Google Stock Analysis

#pip install yfinance

import pandas as pd
import math
#import pandas_datareader as web
import numpy as np
from sklearn.preprocessing import MinMaxScaler
from keras.models import Sequential
from keras.layers import Dense, LSTM
import matplotlib.pyplot as plt
plt.style.use("fivethirtyeight")
#from pandas_datareader import data as web
from datetime import datetime
import yfinance as yf
import streamlit as st

df = yf.download('goog', start = '2012-01-01', end='2020-01-01')
st.header("Google Stock Analysis")
df.head()

plt.figure(figsize=(16,8))
plt.title('Closing Price')
plt.plot(df['Close'])
plt.xlabel('Date')
plt.ylabel('Closing Price')
plt.show
st.altair_chart(plt.show)

data  = df.filter(['Close'])

dataset = data.values  

training_data_length = math.ceil(len(dataset)* .8)

training_data_length

scaler = MinMaxScaler(feature_range=(0,1))
scaled_data = scaler.fit_transform(dataset)


scaled_data

train_data = scaled_data[0:training_data_length, : ]
  
x_train = []
y_train = []

for i  in range (60, len(train_data)) :
  x_train.append(train_data[i-60:i , 0])
  y_train.append(train_data[i,0])

x_train, y_train = np.array(x_train), np.array(y_train)

x_train = np.reshape(x_train,(x_train.shape[0],x_train.shape[1], 1  ))
x_train.shape

model =Sequential()
model.add(LSTM(50, return_sequences=True, input_shape=(x_train.shape[1],1)))
model.add(LSTM(50, return_sequences=False))
model.add(Dense(25))
model.add(Dense(1))
model.compile(optimizer='adam', loss='mean_squared_error')

model.fit(x_train, y_train, batch_size=1,epochs=5 )

test_data= scaled_data[training_data_length - 60: , :]

x_test = []
y_test = dataset[training_data_length : , :]
for i in range (60,len(test_data)):
  x_test.append(test_data[i - 60 : i, 0])

x_test = np.array(x_test)

x_test = np.reshape(x_test, (x_test.shape[0],x_test.shape[1], 1))

predictions = model.predict(x_test)

predictions = scaler.inverse_transform(predictions)

rmse = np.sqrt(np.mean(predictions - y_test)**2)              #root mean square errori

rmse

train = data[:training_data_length]
valid = data[training_data_length:]
valid['Predictions'] = predictions

plt.figure(figsize=(16,8))
plt.title("Model")
plt.xlabel("Year")
plt.ylabel('Closing Price in USD') 
plt.plot(train['Close'])
plt.plot(valid[['Close' , 'Predictions']])
plt.legend(['Train','Valid', 'Predictions'], loc='lower right')
st.altair_chart(plt.legend(['Train','Valid', 'Predictions'], loc='lower right'))

valid
st.write(valid)
