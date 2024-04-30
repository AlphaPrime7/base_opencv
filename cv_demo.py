from PIL import Image 
import numpy as np
import cv2 as cv 
import os
from enum import Enum

def convert_pil_arr(pil_obj):
    img_arr = np.array(pil_obj)
    return img_arr

def cv_draw_rectangle(img, face_rectangle, show = False, color=None, thickness=None):
    
    class colorcode(Enum): #BGR scale
        blue = (255, 0, 0)
        green = (0, 255, 0)
        red = (0, 0, 255)

    if thickness is None:
        thickness = 4 #-1 for black fill
    else:
        thickness = int(thickness)

    if color is None or color == 'red' or color == 'red'.upper() or color == (255, 0, 0):
        color = colorcode.red.value
    elif color == 'green' or color == 'green'.upper() or color == (0, 255, 0):
        color = colorcode.green.value
    elif color == 'blue' or color == 'blue'.upper() or color == (0, 0, 255):
        color = colorcode.blue.value

    if show is False:
        for (x,y,w,h) in face_rectangle:
            start_pt = (x,y) #x and y = top left corner of the image
            end_pt = (x+w,y+h) #x+w and y+h = bottom right corner
            cv.rectangle(img, start_pt, end_pt, color, thickness=thickness)
    else:
        for (x,y,w,h) in face_rectangle:
            start_pt = (x,y) #x and y = top left corner of the image
            end_pt = (x+w,y+h) #x+w and y+h = bottom right corner
            cv.rectangle(convert_pil_arr(pil_obj), start_pt, end_pt, color, thickness=thickness)
        cv.imshow('detected faces',img)
        cv.waitKey()
        cv.destroyAllWindows()  

#choose classifier
def use_builtin_face_classifier():
    opencv_base_dir = os.path.dirname(os.path.abspath(cv.__file__))
    haar_algo = os.path.join(opencv_base_dir, 'data/haarcascade_frontalface_alt.xml') #haar_classifier = cv.data.haarcascades + 'haarcascade_frontalface_alt.xml'; used alone and notice the alt there
    return haar_algo

def use_builtin_eye_classifier():
    opencv_base_dir = os.path.dirname(os.path.abspath(cv.__file__))
    haar_algo = os.path.join(opencv_base_dir, 'data/haarcascade_eye.xml') #haar_classifier = cv.data.haarcascades + 'haarcascade_frontalface_alt.xml'; used alone and notice the alt there
    return haar_algo

#CV
img=cv.imread("imaging.seesaw11.jpg")
#pil_obj = Image.fromarray(img)
#pil_obj = pil_obj.resize((810,1080))
#img = np.array(pil_obj)
grayimg=cv.cvtColor(img, cv.COLOR_BGR2GRAY)

haar_classifier = use_builtin_face_classifier()
eye_classifier = use_builtin_eye_classifier()
haar_cascade = cv.CascadeClassifier(haar_classifier) 
eye_cascade = cv.CascadeClassifier(eye_classifier)

faces_rect = haar_cascade.detectMultiScale(grayimg, scaleFactor=1.3, minNeighbors=3) 

for (x, y, w, h) in faces_rect: 
    cv.rectangle(img, (x, y), (x+w, y+h), (0, 0, 255), thickness=4) 
    pil_obj = Image.fromarray(img)
    face = pil_obj.crop((x,y,x+w,y+h))
    face = np.array(face)
   
    roi_gray = grayimg[y:y+h, x:x+w]
    roi_color = img[y:y+h, x:x+w]
    eyes = eye_cascade.detectMultiScale(roi_gray)
    for (ex,ey,ew,eh) in eyes:
        cv.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,255,0),2)


cv.imshow('Detected faces', img) 
cv.imshow('Cropped faces', face) 
cv.waitKey(0) 
cv.destroyAllWindows()

