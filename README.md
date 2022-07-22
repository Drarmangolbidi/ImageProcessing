# ImageProcessing

Hi... 
In this repository I shared my code about ImageProcessing that Iuse in broad casting for Sport

<br>

My Instagram is [@artificialintelligenceSIB](https://instagram.com/artificialintelligenceSIB)

<br>

## :blush:Step one:(Convert color image to Gray scale):blush:</b>

download :"Arman.jpg" & "1.ColortoGrayCode.py"

<br>

Main Photo is:

<br>

<br>

![Arman](https://user-images.githubusercontent.com/109248678/180061693-f49af923-15e8-4b0b-a483-de01b1b3d9b5.jpg)

<br>

You can run py file and see my image color convert to black&white photo

<br>

<br>

![1](https://user-images.githubusercontent.com/109248678/180053645-273b2b13-4565-4145-b3b4-d9c7070cc013.jpg)

<br>

```python
import cv2
print(cv2.__version__)
img=cv2.imread("Arman.jpg",cv2.IMREAD_GRAYSCALE)
cv2.imshow("Arman Golbidi",img)
cv2.waitKey(0)
cv2.destroyAllWindows()
```
<br>

#### EX1_Leve :
- [x] Simple! 
- [ ] Intermediate!
- [ ] Hard!

<br>

## :blush:Step two:(Drow Line, cycle and rectongel on photo ):blush:</b>

![2 ArmanGolbidi](https://user-images.githubusercontent.com/109248678/180068468-1fe329a4-8f4d-4287-aa21-5524d0f3cf07.jpg)

<br>

download :"Arman.jpg" & "2.LineOrCycleOrRectengle.py"

<br>

```python
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
```
<br>

#### EX2_Leve :
- [x] Simple! 
- [ ] Intermediate!
- [ ] Hard!

<br>

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

Download video: "" and code ""

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

<br>

This program has Branch ("https://github.com/Drarmangolbidi/ImageProcessing/tree/3.VideoPlayer_FromWebcam")

<br>

#### EX3_Leve :
- [x] Simple! 
- [ ] Intermediate!
- [ ] Hard!

<br>

## :blush:Step Four :(Text On Picture ):blush:</b>

<br> 

Download "Arman.jpg" and "4.Text.py".

<br>

You can see this out put :

<br>

![A3](https://user-images.githubusercontent.com/109248678/180468314-f85cb2f1-5b39-4d99-a747-10064de9fce8.jpg)

<br>

Python code is :

<br>

```python
import cv2
img = cv2.imread('Arman.jpg')
# image, 'text', (,), font, fontscale, color, thickness , lineType
font = cv2.FONT_HERSHEY_COMPLEX 
img = cv2.putText(img, 'My Picture', (20 , 100), font, 1, (0,255,0), 2, cv2.LINE_AA)
cv2.imshow('mypic', img) 
cv2.waitKey(0) 
cv2.destroyAllwindows()
```
<br>

#### EX4_Leve :
- [x] Simple! 
- [ ] Intermediate!
- [ ] Hard!

<br>

## :blush:Step Four :(Text On Picture ):blush:</b>

<br>

