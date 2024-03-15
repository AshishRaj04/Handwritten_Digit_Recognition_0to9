import numpy as np
def load_data():
    X = np.load("data/X.npy")  # input data 
    y = np.load("data/y.npy")  # target values
    
    return X, y