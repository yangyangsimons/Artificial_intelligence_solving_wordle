#Imports libraries
from unittest import result
import cv2
import numpy as np
import tensorflow as tf
from tensorflow.keras.models import load_model
from PIL import ImageGrab
import tkinter as tk

#Read the screenshot of the image saved in the directory
image = cv2.imread('data/image.png')
image = cv2.resize(image, (412, 365))
#Convert image to grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

#Sharpen the edges of the image for better contour detection
sharpen_kernel = np.array([[-1,-1,-1], [-1,9,-1], [-1,-1,-1]])
sharpen = cv2.filter2D(gray, -1, sharpen_kernel)

#Thresholding the image
thresh = cv2.threshold(sharpen,225,255, cv2.THRESH_BINARY_INV)[1]

#FInd contours in the image
cnts = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
cnts = cnts[0] if len(cnts) == 2 else cnts[1]
#Variable cnts includes all the contours found in the image

#The below for loop goes through every contour found and basically crops the image
#to every letter in a square and saves it
cnts = cnts[::-1] #reverses the list containing contours
image_number = 0
for c in cnts:
    area = cv2.contourArea(c)#finds out area of each contour
    if area > 800:
        x,y,w,h = cv2.boundingRect(c)#produces coordinated (x, y) and height(h) and width(w) of each square-containing alphabet
        ROI = image[y:y+h, x:x+w] #crops the image to the square-containing alphabet
        ROI = cv2.resize(ROI, (68, 68))#Resizes the square-containing alphabet to 68x68 pixels
        cv2.imwrite('Alphabets/ROI_{}.png'.format(image_number), ROI) #saves the square-containing alphabet
        cv2.rectangle(image, (x, y), (x + w, y + h), (255,0,0), 2) #produces blue-coloured rectangles on each contour found
        image_number = image_number + 1 #counts number of contours and adds by 1 in the for loop
# cv2.imwrite("Contours detected in Image", image) #displays the blue rectangle-bounded image to display all contours

#0: grey, 1: yellow, 2: green.

#Training data consists of different RGB values
training_data = np.array([[164, 198, 203], [131, 132, 130], [130, 154, 133], [118, 156, 126], [196, 201, 199], [126, 125, 121], [132, 131, 127], [135, 160, 140], [123, 154, 126], [127, 178, 182], [123, 123, 123], [138, 176, 183], [118, 154, 127], [127, 156, 124], [124, 125, 121], [199, 198, 194], [140, 164, 147], [137, 165, 140], [134, 167, 138], [134, 163, 139], [133, 163, 134], [127, 124, 119], [118, 179, 191], [123, 124, 122], [89, 184, 194], [124, 123, 119], [112, 176, 192], [122, 119, 115], [134, 174, 179], [132, 130, 129], [132, 130, 130], [127, 124, 119], [121, 178, 186], [125, 126, 123], [94, 180, 189], [127, 124, 123], [109, 167, 110], [124, 123, 122], [122, 151, 123], [125, 125, 123], [114, 161, 118], [105, 170, 101], [129, 126, 122], [124, 163, 126], [131, 127, 126], [123, 179, 127], [104, 167, 111], [119, 158, 124], [126, 153, 129], [114, 159, 115], [113, 159, 116]])

#Validation data consists of numbers as keys to colors. 
valid_data = np.array([1, 0, 2, 2, 0, 0, 0, 2, 2, 1, 0, 1, 2, 2, 0, 0, 2, 2, 2, 2, 2, 0, 1, 0, 1, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 2, 0, 2, 0, 2, 2, 0, 2, 0, 2, 2, 2, 2, 2, 2])

#Create model
model = tf.keras.models.Sequential([
  tf.keras.layers.Dense(3, input_shape=[3], activation='softmax') #3 neurons layer linked to 1 neuron output layer. 
])
model.compile(optimizer='sgd', loss='sparse_categorical_crossentropy', metrics=['accuracy']) #Optimizer settings

#fit the model
history = model.fit(
        training_data, valid_data, epochs=100
        )

#save the model
model.save('Models/color.h5')
co_model = load_model('Models/color.h5')
def crop_center(img,cropx,cropy):
    y,x = img.shape
    startx = x//2-(cropx//2)
    starty = y//2-(cropy//2)    
    
    return img[starty:starty+cropy,startx:startx+cropx]

def predict_color(ROI):
    
    colors = {0: "grey", 1: "yellow", 2: "green"}
    RGB = (np.asarray(ROI)[0][0])
    color_pred = co_model.predict(np.array([RGB]))
    color_pred = list(list(color_pred.astype(int))[0])
    color_index = color_pred.index(max(color_pred))
    
    return colors[color_index], RGB
  
def __Website__Feedback__():
    #load image
    file = 'data/screenshot/img2.png'
    image = cv2.imread(file)
    image = cv2.resize(image, (412, 365))

    #load models
    co_model = load_model('Models/color.h5')

    #preprocessing of image
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    #blur = cv2.medianBlur(gray, 5)
    sharpen_kernel = np.array([[-1,-1,-1], [-1,9,-1], [-1,-1,-1]])
    sharpen = cv2.filter2D(gray, -1, sharpen_kernel)
    thresh = cv2.threshold(sharpen,225,255, cv2.THRESH_BINARY_INV)[1]

    #find all contours
    cnts = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    cnts = cnts[0] if len(cnts) == 2 else cnts[1]

    image_number = 0
    cnts = cnts[::-1]
    colours = []
    for c in cnts:
        area = cv2.contourArea(c)
        if area > 800:
            x,y,w,h = cv2.boundingRect(c)
            ROI = image[y:y+h, x:x+w]
            ROI = cv2.resize(ROI, (68, 68))
            cv2.imwrite('Alphabets/ROI_{}.png'.format(image_number), ROI)
            final_color, RGB = predict_color(ROI)
            print(image_number)
            #print alphabet and color predicted and the RGB value associated
            colours.append(final_color)
            cv2.rectangle(image, (x, y), (x + w, y + h), (255,0,0), 2)
            image_number = image_number + 1
    return colours