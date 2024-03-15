import numpy as np
from PIL import Image
def load_data():
    X = np.load("data/X.npy")  # input data 
    y = np.load("data/y.npy")  # target values
    
    return X, y

def convert_to_grayscale():
    image = Image.open('assects/0.jpg')

    grayscale_image = image.convert('L')
    resized_image = grayscale_image.resize((20 , 20))
    matrix = np.array(resized_image)

    return matrix


    
 

