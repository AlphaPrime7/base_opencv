#SCALE
from PIL import Image 
import numpy as np
import cv2 as cv 
import os
from enum import Enum
from collections import OrderedDict
import math

def convert_pil_arr(pil_obj):
    img_arr = np.array(pil_obj)

    return img_arr

def convert_arr_pil(cv_obj):
    pil_image = Image.fromarray(cv_obj)
    
    return pil_image

def cv_draw_rectangle(img, face_rectangle, show = False, color=None, thickness=None):
    
    class colorcode(Enum): #BGR scale
        blue = (255, 0, 0)
        green = (0, 255, 0)
        red = (0, 0, 255)

    if thickness is None:
        thickness = 2 #-1 for black fill
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
            cv.rectangle(img, start_pt, end_pt, color, thickness=thickness) #best results with cv array
    else:
        for (x,y,w,h) in face_rectangle:
            start_pt = (x,y) 
            end_pt = (x+w,y+h) 
            cv.rectangle(img, start_pt, end_pt, color, thickness=thickness)
        cv.imshow('detected faces',img)
        cv.waitKey()
        cv.destroyAllWindows()

def cv_crop_rectangle(pil_obj, face_rectangle, show = False):

    if len(face_rectangle) <= 1:
        if show is False:
            for x,y,w,h in face_rectangle:
                face = pil_obj.crop((x,y,x+w,y+h))
                face = np.array(face)
        else:
            for x,y,w,h in face_rectangle:
                face = pil_obj.crop((x,y,x+w,y+h))
                face = np.array(face)
                cv.imshow('image', face)
                cv.waitKey()
                cv.destroyAllWindows()
    else:
        if show is False:
            for i in face_rectangle:
                for x,y,w,h in face_rectangle:
                    face = pil_obj.crop((x,y,x+w,y+h))
                    face = np.array(face)
        else:
            for x,y,w,h in face_rectangle:
                face = pil_obj.crop((x,y,x+w,y+h))
                face = np.array(face)
                cv.imshow('image', face)
                cv.waitKey()
                cv.destroyAllWindows()
            return face   
    
#choose classifier
def use_builtin_face_classifier():
    opencv_base_dir = os.path.dirname(os.path.abspath(cv.__file__))
    haar_algo = os.path.join(opencv_base_dir, 'data/haarcascade_frontalface_default.xml') #haar_classifier = cv.data.haarcascades + 'haarcascade_frontalface_alt.xml'; used alone and notice the alt there
    return haar_algo

def use_builtin_eye_classifier():
    opencv_base_dir = os.path.dirname(os.path.abspath(cv.__file__))
    haar_algo = os.path.join(opencv_base_dir, 'data/haarcascade_eye.xml') #haar_classifier = cv.data.haarcascades + 'haarcascade_frontalface_alt.xml'; used alone and notice the alt there
    return haar_algo

def is_tuple(s):
  if isinstance(s, tuple):
    return True
  return False

img_list = ["imaging.seesaw10.jpg","imaging.seesaw7.jpg", "imaging.seesaw10.jpg","imaging.seesaw11.jpg","imaging.seesaw15.jpg","imaging.seesaw26.jpg"]

for i in img_list:
    n = cv.imread(i) 
    p=convert_arr_pil(n)
    grayimg=cv.cvtColor(n, cv.COLOR_BGR2GRAY)
    haar_classifier = use_builtin_face_classifier()
    haar_cascade = cv.CascadeClassifier(haar_classifier) 
    faces_rect = haar_cascade.detectMultiScale(grayimg, scaleFactor=1.3, minNeighbors=3)

    if len(faces_rect) == 0:
        print(f'No images forund in {i}')
    else:
        canvas_control = Image.fromarray(faces_rect)
        
        #canvas building (balanced)
        ncol = math.ceil(len(faces_rect)/2) *400
        nrow = math.ceil(len(faces_rect)/ncol) * 200
        canvas = Image.new(canvas_control.mode, (int(nrow*canvas_control.width), int(ncol*canvas_control.height) ))
        curr_x = 0
        curr_y = 0

        #heuristics
        for x,y,w,h in faces_rect:
            face = p.crop((x,y,x+w,y+h))
            MAX_SIZE = (100,100)
            face = face.resize(MAX_SIZE)
            canvas.paste(face, (curr_x, curr_y) )
            if curr_x + face.width == canvas.width:
                curr_x = 0
                curr_y = curr_y + face.height
            else:
                curr_x = curr_x + face.width
        
        canvas.show()




