#Creating the gaussian filter
#In this gaussian blur we have created the gaussina with same blur value in x and y direction
import numpy as np
import cv2
#creating the gaussian kernal
def gaussian_kernal(size,sigma):
    #try to use the odd sized gaussian function it will be better
    kernal=np.empty((size[0],size[1]),np.float64)
    centre_x=size[0]//2
    centre_y=size[1]//2
    for i in range(0,size[0]):
        for j in range(0,size[1]):
            kernal[i][j]=(1/(2*np.pi*sigma**2))*np.exp(-1*((i-centre_x)**2+(j-centre_y)**2)/(2*sigma**2))
            # kernal[i, j] = (1 / (2 * np.pi * sigma**2)) * np.exp(-((i - centre_x)**2 + (j - centre_y)**2) / (2 * sigma**2))
    kernal=kernal/np.sum(kernal)
    return kernal
#read image
img=cv2.imread("/users/devanshusharma/desktop/image1.jpg")
#creating kernal
kernal=gaussian_kernal((11,11),5)
#creating my gaussian
my_gaussian=cv2.filter2D(img,ddepth=-1,kernel=kernal)

#inbuilt gaussian filter
gaussian=cv2.GaussianBlur(img,(11,11),sigmaX=5,sigmaY=5)

cv2.imshow("img",img)
cv2.imshow("my_gaussian",my_gaussian)
cv2.imshow("gaussian",gaussian)

while True:
    key=cv2.waitKey(0)

    if(key==ord("c")):
        break
cv2.destroyAllWindows






