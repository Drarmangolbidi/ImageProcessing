# ImageProcessing
## :blush:Step three :(Play video Frame by Frame ):blush:</b>
<br> 
Main video is :👇
<br>

https://user-images.githubusercontent.com/109248678/180224735-830f46c1-4578-4f78-9ab3-8bdc144a3683.mp4

<br>
In this Program we play video ("ArmanVideo.mp4") with Python.
<br>
Like that :👇
<br>
<br>

https://user-images.githubusercontent.com/109248678/180222892-4630d87c-29ea-454d-ae1d-c39fab8ccc28.mp4

<br>
Download video: "ArmanVideo.mp4" and code "3.VideoPlayer.py"
<br>
Code is :👇
<br>

```python
import cv2
myvideo = cv2.VideoCapture('ArmanVideo.mp4')
while True:
    ret, frame = myvideo.read() 
    cv2.imshow('myvideo', frame) 
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
myvideo.release() 
cv2.destroyAllwindows()
```





