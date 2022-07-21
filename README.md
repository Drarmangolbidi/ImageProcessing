# ImageProcessing
## :blush:Branch ofStep three :(Play video Frame by Frame ):blush:</b>
<br> 
in this branch we can see the webcame :👇
<br>
videocapture input is "0"
<br>

```python
import cv2
myvideo = cv2.VideoCapture(0)
while True:
    ret, frame = myvideo.read() 
    cv2.imshow('myvideo', frame) 
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
myvideo.release() 
cv2.destroyAllwindows()
```





