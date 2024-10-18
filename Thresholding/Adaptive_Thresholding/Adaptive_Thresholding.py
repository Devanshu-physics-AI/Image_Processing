# Applying the Adaptive thresholding
#It is better then the simple thresholding because its value depennds on the neighbour pixcel values
import cv2
import numpy as np


def mean_thresholding(img,kernal,constant=0):
    img_shape=img.shape
    kernal_shape=kernal.shape
    kernal=kernal/(kernal_shape[0]*kernal_shape[1])
    if(len(img_shape)==3):
        print("Your image is not greyscale format")
    #internal working of filter2D works like this this gives output image as the 
    img_mean=((cv2.filter2D(img,ddepth=-1,kernel=kernal))-constant).astype(np.float64)
    img=np.where(img>img_mean,255,0).astype(np.uint8)
    return img

def gaussian_thresholding(img,kernal,sigma_x,sigma_y):
    img_shape=img.shape
    kernal_shape=kernal.shape
    if(len(img_shape)==3):
        print("Your image is not greyscale format")
    img_gaussian=cv2.GaussianBlur(img,kernal_shape,sigma_x,sigma_y)
    img=np.where(img>img_gaussian,255,0).astype(np.uint8)
    return img

img=cv2.imread("/users/devanshusharma/desktop/image1.jpg",0)

#creating the kernal
kernal=(np.ones((3,3),np.float64))

# if(img==None):
#     print("No image is found on this address")
# else:
mean_thresh=mean_thresholding(img,kernal)
inbuilt_mean_thresh=cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY,3,0)
cv2.imshow("mean_thresh",mean_thresh)
cv2.imshow("inbuilt_mean_thresh",inbuilt_mean_thresh)
cv2.waitKey(0)

gaussian_thresh=gaussian_thresholding(img,kernal,1,1)
inbuilt_gaussian_thresh=cv2.adaptiveThreshold(img, 255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,3,0)
cv2.imshow("gaussian_thresh",gaussian_thresh)
cv2.imshow("inbuilt_gaussian_thresh",inbuilt_gaussian_thresh)
cv2.waitKey(0)

cv2.destroyAllWindows()



    