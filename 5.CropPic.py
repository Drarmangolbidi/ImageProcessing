#!/usr/bin/env python
# coding: utf-8

# In[6]:


import cv2


# In[7]:


img = cv2.imread('Arman.jpg')
img = img[0:400 , 0:350]
cv2.imshow('mypic', img) 
cv2.waitKey() 
cv2.destroyAllwindows()


# In[ ]:




