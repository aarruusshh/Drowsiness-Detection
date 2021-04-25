'''We will use OpenCV's haarcascade (face and eye cascade) to detect face
and eyes in a video feed from live webcam.'''

#Import  libraries
import cv2 as cv
import numpy as np

#Load face cascade and eye cascade
face_cascade = cv.CascadeClassifier("haarcascades/haarcascade_frontalface_default.xml")
eye_cascade = cv.CascadeClassifier("haarcascades/haarcascade_eye.xml")

#Capture video from webcam
video_capture = cv.VideoCapture(0)

#Read all frames from webcam
while True:
    #ret if image was read or not true/false
    ret, frame = video_capture.read()
    #Flip so that video feed is not flipped, and appears mirror like.
    frame = cv.flip(frame,1)
    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)

    #we detect all the faces in frame
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)

    #we draw a red rectangle on the face
    for (x,y,w,h) in faces:
        cv.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),2)

        #we mark region of intrest which is inside the face
        roi_gray = gray[y:y+h, x:x+w]
        roi_color = frame[y:y+h, x:x+w]

        #cascade funtion is always implemented on grey image
        eyes = eye_cascade.detectMultiScale(roi_gray)

        #all the recatangles are drawn for eye
        for (ex,ey,ew,eh) in eyes:
            cv.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,255,0),2)

    #we show the vide frame wit updates        
    cv.imshow('Video', frame)

    if(cv.waitKey(1) & 0xFF == ord('q')):
        break

#Finally when video capture is over, release the video capture and destroyAllWindows
video_capture.release()
cv.destroyAllWindows()
