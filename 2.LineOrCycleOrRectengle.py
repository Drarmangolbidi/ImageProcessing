#!/usr/bin/env python
# coding: utf-8

# In[21]:


import cv2
img = cv2.imread('Arman.jpg')
print(img.shape)
#(wideth , Highest , channel num)
# img, (start point), (end point), color, thickness

img = cv2.line(img, (0,0), (600, 600), (255,0,0), 3) 

#image, center, radius, color, thickness 

img = cv2.circle(img, (100,80) , 50, (0,255,0), 1) 

# img, (start point), (end point), color, thickness

img = cv2.rectangle(img, (30,30), (60,160), (0,0,255), -1) 
cv2.imshow ('mypic', img) 
cv2.waitKey() 
cv2.destroyWindow('mypic')


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




