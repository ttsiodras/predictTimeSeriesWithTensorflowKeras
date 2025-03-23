#!/usr/bin/env python3
import numpy as np
import tensorflow as tf

latencies = np.loadtxt("data")
mean, std = latencies.mean(), latencies.std()
latencies_normalized = (latencies - mean) / std

sequence_length = 10

X, y = [], []

for i in range(len(latencies_normalized) - sequence_length):
    X.append(latencies_normalized[i:i + sequence_length])
    y.append(latencies_normalized[i + sequence_length])

X, y = np.array(X), np.array(y).reshape(-1, 1)

model = tf.keras.Sequential([
    tf.keras.layers.LSTM(64, input_shape=(sequence_length, 1)),
    tf.keras.layers.Dense(1)
])

model.compile(optimizer='adam', loss='mse')

model.fit(X, y, epochs=50, batch_size=32)

model.save("rnn_model.keras")
