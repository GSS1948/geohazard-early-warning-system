import numpy as np
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import LSTM, RepeatVector, TimeDistributed, Dense

def build_lstm_autoencoder(timesteps, n_features):
    """Builds an unsupervised LSTM Autoencoder for temporal reconstruction loss profiling."""
    model = Sequential([
        tf.keras.layers.Input(shape=(timesteps, n_features)),
        LSTM(32, activation='relu', return_sequences=False),
        RepeatVector(timesteps),
        LSTM(32, activation='relu', return_sequences=True),
        TimeDistributed(Dense(n_features))
    ])
    model.compile(optimizer='adam', loss='mse')
    return model

def create_windows(data, window_size):
    """Transforms continuous multi-channel arrays into overlapping sliding temporal windows."""
    return np.array([data[i:i + window_size] for i in range(len(data) - window_size)])
