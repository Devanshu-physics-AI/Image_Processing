import cv2
import numpy as np
import matplotlib.pyplot as plt
import time

#reading the image
img=cv2.imread("/users/devanshusharma/desktop/image1.jpg")


#creating the kernal
size=(input("Entre the size of kernal you want to cross-correlation"))
size=size.split(" ")
size=np.array(size,np.uint16)
img_size=1
for i in size:
    img_size=img_size*i


#creating the mean filter
kernal=np.ones(size,np.float32)/(img_size)


#finding cross correlation
final_img=cv2.filter2D(img,kernel=kernal,ddepth=-1)

#inbuilt mean filter

mean_filter=cv2.blur(img,size)


cv2.imshow("img",img)
cv2.imshow("my_mean_filer",final_img)
cv2.imshow("mean_filter",mean_filter)
cv2.waitKey(0)
cv2.destroyAllWindows()