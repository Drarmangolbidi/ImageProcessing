#!/usr/bin/env python
# coding: utf-8

# In[1]:


import cv2


# In[2]:


myvideo = cv2.VideoCapture('ArmanVideo.mp4')
while True:
    ret, frame = myvideo.read() 
    cv2.imshow('myvideo', frame) 
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
myvideo.release() 
cv2.destroyAllwindows()


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




