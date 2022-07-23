# ImageProcessing

Hi... 
In this repository I shared my code about ImageProcessing that Iuse in broad casting for Sport

<br>

at first i learn the basic of image Processing and after that you can use "Harr" features and cascade algoritm .

<br>

I try to use Ml and Deep learning like "Hog" or "CNN" to find the face .

<br>?

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

Python code is :👇

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

## :blush:Step Five :(Crop the picture ):blush:</b>

<br>

If you want to crop the picture like the below output you can use my Code :

<br>

![A4](https://user-images.githubusercontent.com/109248678/180470693-d07ccb28-e343-4fff-a9ea-31c7af6a4608.jpg)

<br>

Download "Arman.jpg" and "CropPic.py".

<br>
Python code is :👇

<br>

```python
import cv2
img = cv2.imread('Arman.jpg')
img = img[0:400 , 0:350]
cv2.imshow('mypic', img) 
cv2.waitKey() 
cv2.destroyAllwindows()
```

<br>

#### EX5_Leve :
- [x] Simple! 
- [ ] Intermediate!
- [ ] Hard!


<br>

## :blush:Step Six :(Resize the picture ):blush:</b>

<br>

When your picture is small or very big you can scale it to normal view . 

<br>

like this example . i resize my picture to small view :

<br>

![A5](https://user-images.githubusercontent.com/109248678/180472784-c2076c91-9c24-4c72-bb90-06f1e8c2aaa6.jpg)

<br>

Donloawd "6.ResizePic.py" and "Arman.jpg".

<br>

Python code is :👇

<br>

```python
import cv2
img = cv2.imread('Arman.jpg')
print(img.shape)
size = (img.shape[1] ,350) 
output = cv2.resize(img , size , interpolation=cv2.INTER_AREA) 
cv2.imshow('mypic' ,output) 
cv2.waitKey(0)
cv2.destroyAllwindows()
```

<br>

#### EX6_Leve :
- [x] Simple! 
- [ ] Intermediate!
- [ ] Hard!


<br>

## :blush:Step Seven  :(viola_jones algoritm for face and Eye detection ):blush:</b>

<br>

In this code we use "Harr" features and "casdcading" algoritm .

<br>

see it :

<br>

https://user-images.githubusercontent.com/109248678/180515930-a9e8e65a-e139-43da-90c0-125b235a360c.mp4

<br>

For use this Program you should download three files:

<br>

- [x] haarcascade_eye.xml
- [x] haarcascade_frontalface_default.xml
- [x] 7.viola_jones.py

<br>
Python code is :👇

<br>

```python
import cv2
#font=font = cv2.FONT_HERSHEY_COMPLEX
font = cv2.FONT_HERSHEY_COMPLEX

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml') 
eye_cascade = cv2.CascadeClassifier('haarcascade_eye.xml')
def detect(gray , frame):
    faces = face_cascade.detectMultiScale(gray , 1.3, 5) 
    for (x, y, w, h) in faces:
        cv2.rectangle(frame , (x, y), (x+w , y+h), (255,0,0), 2) 
        detected_face = gray[y:y+h , x:x+w] 
        detected_colored_face = frame[y:y+h, x:x+w] 
        eyes = eye_cascade.detectMultiScale(detected_face , 1.1, 3) 
        for (a, b,c,d) in eyes:
            cv2.rectangle(detected_colored_face, (a,b), (a+c , b+d), (0,255,0), 2)
    return frame

video_capture = cv2.VideoCapture(0)
while True:
    ret , frame = video_capture.read()
    gray = cv2.cvtColor(frame , cv2.COLOR_BGR2GRAY) 
    my_output = detect(gray, frame)
    my_output = cv2.putText(my_output, 'Welcome Arman Golbidi', (100 , 100), font, 1, (0,0,0), 2, cv2.LINE_AA)
    cv2.imshow ('OUT PUT' , my_output) 
    if cv2.waitKey(1) & 0xFF == ord('9'):
        break 
video_capture.release()
cv2.destroyAllWindows()
```

<br>

#### EX6_Leve :
- [ ] Simple! 
- [x] Intermediate!
- [ ] Hard!

<br>

If you want to detect laught you can use these code to program .
<br>
download : 
[haarcascade_smile.xml](https://github.com/opencv/opencv/blob/master/data/haarcascades/haarcascade_smile.xml)
```python
smile_cascade = cv2.CascadeClassifier('haarcascade_smile.xml') 
        smiles = smile_cascade.detectMultiScale(detected_face , 1.7, 22) 
        for (sx, sy,sw,sh) in smiles:
            cv2.rectangle(detected_colored_face, (sx,sy), (sx+sw , sy+sh), (0,0,255), 2)

```

<br>

## :blush:Step eight  :( " hog " algoritm from ML to find and crop the Face in Picture ):blush:</b>

<br>

for start this Project you should install new envierment on Anaconda .

<br>

Please download "8.AnacondaPrivateEn.pdf" file and wrtie command in Anaconda powershell 

<br>

after that you can download "9.Hog algoritm.py" and "CR7.jpg" .my favorit soccer player is cristiano ronaldo . in this picture we have him and his wife . we want crop his face and his wife 's face . 

<br>

https://user-images.githubusercontent.com/109248678/180607109-ea5a2d7a-6a7d-499b-8b43-dcccb78d8e6c.mp4

<br>
<br>
Python code is :👇

<br>

```python
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
```
<br>

#### EX6_Leve :
- [ ] Simple! 
- [x] Intermediate!
- [ ] Hard!

<br>

## :blush:Step Nine  :( " hog " algoritm from ML to find and crop the Face in Picture ):blush:</b>

<br>
