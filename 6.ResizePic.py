#!/usr/bin/env python
# coding: utf-8

# In[1]:


import cv2


# In[3]:


img = cv2.imread('Arman.jpg')
print(img.shape)
size = (img.shape[1] ,350) 
output = cv2.resize(img , size , interpolation=cv2.INTER_AREA) 
cv2.imshow('mypic' ,output) 
cv2.waitKey(0)
cv2.destroyAllwindows()


# In[ ]:




