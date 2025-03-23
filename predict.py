#!/usr/bin/env python3
import math
import random
import numpy as np
import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'
from tensorflow.keras.models import load_model
from tensorflow.keras.losses import MeanSquaredError

from generator import blackbox

SEQUENCE_LENGTH = 10
model = load_model(
    "rnn_model.keras", custom_objects={"mse": MeanSquaredError()})


def predict_latency(latency_sequence):
    mean, std = np.mean(latency_sequence), np.std(latency_sequence)
    normalized = (np.array(latency_sequence) - mean) / std
    current_sequence = normalized.reshape(1, SEQUENCE_LENGTH, 1)
    return model.predict(current_sequence, verbose=0)[0][0] * std + mean


def main():
    latency_sequence = []
    for i in range(500, 900):
        sample = blackbox(i)
        if len(latency_sequence) == SEQUENCE_LENGTH:
            print(f"0:{sample}")
            print(f"1:{predict_latency(latency_sequence)}")
            print(f"2:{100*abs((sample - predict_latency(latency_sequence))/sample)}")
            latency_sequence.pop(0)
        latency_sequence.append(sample)

if __name__ == "__main__":
    main()
