image_url = "https://image2.tin247.com/pictures/2018/09/04/znm1536051981.png"
import cv2
from matplotlib import pyplot
from skimage import io
from mtcnn.mtcnn import MTCNN

image = io.imread(image_url)

pyplot.imshow(image)


detector = MTCNN()
result = detector.detect_faces(image)
l = [n['box'] for n in result]
print(l)
for a in l:
  x,y,w,h = a[:]
  print('x= ',x,'y= ',y,'w= ',w,'h= ',h)
  cv2.rectangle(image,(x,y),(x+w,y+h),(255,0,0),1 )
pyplot.imshow(image)

# chua the ve hoan chinh toan bo duong bao cua cac khuan mat

