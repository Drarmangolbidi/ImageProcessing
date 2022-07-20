#!/usr/bin/env python
# coding: utf-8

# In[3]:


import cv2


# In[4]:


print(cv2.__version__)


# In[ ]:


img=cv2.imread("Arman.jpg",cv2.IMREAD_GRAYSCALE)
cv2.imshow("Arman Golbidi",img)
cv2.waitKey(0)
cv2.destroyAllWindows()


# In[ ]:





# In[ ]:




