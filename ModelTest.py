import os
import numpy as np
import tensorflow as tf
import tensorflow.keras as keras
from keras.preprocessing.image import array_to_img, img_to_array, load_img
from PIL import Image

def convert_image_to_array(files):
    images_as_array=[]
    for file in files:
        # Convert to Numpy Array
        images_as_array.append(img_to_array(load_img(file)))
    return images_as_array

#Retrieve the model
model = keras.models.load_model("model90acc.h5")
##model.summary()

#Retrieve the test Image
image = Image.open("Sc_1.bmp")
#arryBMP = np.array(image)

image = np.array(convert_image_to_array(image))
#print('Test set shape : ',testImg.shape)

#Display the prediction
prediction = model.predict(testImg)

def method(): #temporarily creating a method so I can call that method into backend 
     print(prediction)