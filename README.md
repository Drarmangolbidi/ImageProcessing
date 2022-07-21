# ImageProcessing
## :blush:Branch of Step three :(Play video Frame by Frame ):blush:</b>
<br>

https://user-images.githubusercontent.com/109248678/180234451-cf9380f7-d150-42ee-a8dd-1b17da7a1564.mp4

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
