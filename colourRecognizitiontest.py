import cv2
import numpy as np
from tensorflow.keras.models import load_model

def predict_color(ROI):
    
    colors = {0: "grey", 1: "yellow", 2: "green"}
    RGB = (np.asarray(ROI)[0][0])
    color_pred = co_model.predict(np.array([RGB]))
    color_pred = list(list(color_pred.astype(int))[0])
    color_index = color_pred.index(max(color_pred))
    
    return colors[color_index], RGB
  
# def __Website__Feedback__():
    #load image
file = 'data/screenshot/img2.png'
image = cv2.imread(file)
# image = cv2.resize(image, (412, 365))

#load models
co_model = load_model('Models/color.h5')

#preprocessing of imagex
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
    if area > 1000:
        x,y,w,h = cv2.boundingRect(c)
        ROI = image[y:y+h, x:x+w]
        ROI = cv2.resize(ROI, (68, 68))
        cv2.imwrite('Alphabets/ROI_{}.png'.format(image_number), ROI)
        final_color, RGB = predict_color(ROI)
        #print alphabet and color predicted and the RGB value associated
        colours.append(final_color)
        cv2.rectangle(image, (x, y), (x + w, y + h), (255,0,0), 2)
        image_number = image_number + 1
