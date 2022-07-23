#!/usr/bin/env python
# coding: utf-8

# In[5]:


import cv2 
import face_recognition
image_to_detect = cv2.imread('CR7.jpg')
all_faces = face_recognition.face_locations (image_to_detect , model = 'hog') 
print('There Are {} Number of Faces'.format(len(all_faces)))
print(list(enumerate(all_faces,1))) 
for index, current_location in enumerate(all_faces , 1):
    top, right, bottom, left = current_location
    print('Found Face Number {} at Top: {}, Right: {}, Bottom: {}, Left: {}'.format(index , top, right , bottom , left))
    current_face = image_to_detect[top:bottom, left:right] 
    cv2.imshow ('Face' +str(index), current_face)
    cv2.waitKey (0) 
    cv2.destroyAllWindows()


# In[ ]:




