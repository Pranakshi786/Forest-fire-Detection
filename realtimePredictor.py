from tensorflow.python.keras.utils import np_utils
import keras
import numpy as np
import tensorflow as tf
from os import path, listdir
import matplotlib.pyplot as plt
from tensorflow.keras.preprocessing.image import ImageDataGenerator, array_to_img, img_to_array, load_img
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras.applications.mobilenet_v2 import preprocess_input
from tensorflow. keras.layers import Input,GlobalMaxPooling2D,Dense
from tensorflow.keras.applications import MobileNetV2, ResNet50, InceptionV3
from tensorflow.keras.models import load_model
from tensorflow.keras.models import Model
from playsound import playsound
import smtplib
from email.message import EmailMessage
import glob
import cv2
import imutils
model = load_model('./Fire_mobilenet1.h5')
label_map = {'Fire': 0, 'Neutral': 1, 'Smoke': 2}
def get_key(val): 
    for key, value in label_map.items(): 
         if val == value: 
             return key 
def process():
    
    

    
    size = 256
    

    # resize the frame to required dimensions and predict
    def predict_pothole(imgpath):

        im = load_img(imgpath, target_size=(256,256))
        im =img_to_array(im)
        im = preprocess_input(im)
        im = np.expand_dims(im, axis=0)
        prediction = model.predict(im)
        print("prediction",prediction)
        return get_key(np.argmax(prediction))


    

    

    camera = cv2.VideoCapture(0)

    show_pred = False
    # loop until interrupted
    while (True):

        (grabbed,frame) = camera.read()
        frame = imutils.resize(frame,width = 256,height=256)
        frame = cv2.flip(frame,1)
        
        clone = frame.copy()
        
        cv2.imwrite("test.png",frame)
        pothole=predict_pothole("./test.png")
        print("Result====",pothole)
        if pothole=="Fire":
            msg=EmailMessage()
            msg.set_content("Fire or Smoke Deteced")
            msg['Subject']='OTP'
            msg['From']="evotingotp4@gmail.com"
            msg['To']="pranakshi786@gmail.com"
            s=smtplib.SMTP('smtp.gmail.com',587)
            s.starttls()
            s.login("evotingotp4@gmail.com","xowpojqyiygprhgr")
            s.send_message(msg)
            s.quit()

            playsound("alarm.wav")




        keypress_toshow = cv2.waitKey(1)
        
        if(keypress_toshow == ord("e")):
            show_pred = not show_pred
        
        if(show_pred):
            cv2.putText(clone , str(pothole), (30,30) , cv2.FONT_HERSHEY_DUPLEX , 1 , (0,255,0) , 1)

        #cv2.imshow("GrayClone",grayClone)

        cv2.imshow("Video Feed",clone)

        keypress = cv2.waitKey(1) & 0xFF

        if(keypress == ord("q")):
            break

    camera.release()

    cv2.destroyAllWindows()

