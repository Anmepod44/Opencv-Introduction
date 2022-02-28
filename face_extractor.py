#The role of this code is to loop through a given directory, detect a face and crop out the face in jpg format.

#importing all the libraries
import cv2
import numpy as np
import matplotlib.pyplot as plt
import os

#path to haarcascade should go here.
path_face_cascade=""

#path of image files
source_path=""
destination_path=""
 
#importing the cascade classifier xml files
face_cascade=cv2.CascadeClassifier(path_face_cascade)


#function to detect and return a face if found
def faceDetector(img):
    
    try:
        
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        
    except Exception as e:
        return False
    
    face=face_cascade.detectMultiScale(img,1.3,5)
    
    if face==():
        return False
    
    for x,y,w,h in face:
        img=cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,255),2)
        
        roi_gray=img[y:y+h,x:x+w]
        roi_colored=img[y:y+h,x:x+w]
        
#         #detect the eyes in the region of interest of the image
#         eyes=eye_cascade.detectMultiScale(roi_gray)
        
        #am slicing the image to obtain the localized images.
        img=img[y:y+h,x:x+w]
        
#         for X,Y,W,H in eyes:
#             cv2.rectangle(roi_colored,(X,Y),(X+W,Y+H),(0,255,0),1)
        
    
      

    return img


def extract_faces(source=source_path,destination=destination_path):
  #looping through the source_path.
    for count,i in enumerate(os.listdir(source_path)):

        return_=faceDetector(cv2.imread(os.path.join(source_path,i)))

        if type(return_)==bool:
            continue
        elif len(list(return_).copy())!=0:


            try:

                cv2.imwrite(f"{source_path}/{count}.jpg",return_)

            except Exception as e:
                pass
 
  
