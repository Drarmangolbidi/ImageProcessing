#!/usr/bin/env python
# coding: utf-8

# In[3]:


import cv2


# In[4]:


face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml') 
eye_cascade = cv2.CascadeClassifier('haarcascade_eye.xml')
def detect(gray , frame):
    faces = face_cascade.detectMultiScale(gray , 1.3, 5) 
    for (x, y, w, h) in faces:
        cv2.rectangle(frame , (x, y), (x+w , y+h), (255,0,0), 2) 
        detected_face = gray[y:y+h , x:x+w] 
        detected_colored_face = frame[y:y+h, x:x+w] 
        eyes = eye_cascade.detectMultiScale(detected_face , 1.1, 3) 
        for (a, b,c,d) in eyes:
            cv2.rectangle(detected_colored_face, (a,b), (a+c , b+d), (0,255,0), 2)
    return frame
video_capture = cv2.VideoCapture(0)
while True:
    ret , frame = video_capture.read()
    gray = cv2.cvtColor(frame , cv2.COLOR_BGR2GRAY) 
    my_output = detect(gray, frame) 
    cv2.imshow ('OUT PUT' , my_output) 
    if cv2.waitKey(1) & 0xFF == ord('9'):
        break 
video_capture.release()
cv2.destroyAllWindows()


# In[ ]:





# In[46]:





# In[ ]:




