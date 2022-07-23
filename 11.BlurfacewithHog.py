#!/usr/bin/env python
# coding: utf-8

# In[13]:


import cv2 
import face_recognition


# In[14]:


stream = cv2.VideoCapture(0)
all_face_locations = []
while True:
    ret , current_frame = stream.read()
    current_frame_small = cv2.resize(current_frame, (0,0) , fx= 0.25 , fy= 0.25 )
    all_face_locations = face_recognition.face_locations (current_frame_small , number_of_times_to_upsample=2 , model='hog')
    
    for index, current_location in enumerate(all_face_locations):
        top , right , bottom , left = current_location 
        top = top*4 
        right = right*4 
        bottom = bottom*4 
        left = left*4
        
        print('Founf Face {} at top: {}, right: {}, bottom: {}, left:{}'.format(index+1 , top, right, bottom, left))
        current_face_image=current_frame[top:bottom,left:right]
        current_face_image=cv2.GaussianBlur(current_face_image , (99,99) , 30)
        current_frame[top:bottom,left:right]=current_face_image
        
        cv2.rectangle(current_frame, (left , top), (right , bottom), (0,0,255),2)
    cv2.imshow ('web' , current_frame) 
    if cv2.waitKey(1) & 0xFF ==ord('q'):
        break
stream.release() 
cv2.destroyAllWindows()


# In[ ]:




