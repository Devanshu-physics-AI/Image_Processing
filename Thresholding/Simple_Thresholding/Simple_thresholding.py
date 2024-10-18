#Simple thresholding model
import cv2
import numpy as np


#binary thersholding
def binary_thresh(img,thresholding_val):
    img=np.where(img>thresholding_val,255,0).astype(np.uint8)
    return img

#binary thersholding inverse->>>> opposite of binary thresholding
def binary_thresh_inverse(img,thresholding_val):
    img=np.where(img<thresholding_val,255,0).astype(np.uint8)
    return img

#zero thresholding
def zero_thresh(img,thresholding_val):
    img=np.where(img>thresholding_val,img,0).astype(np.uint8)
    return img


#zero thersholding inverse ->>>> opposite to the zero thersholding
def zero_thresh_inverse(img,thresholding_val):
    img=np.where(img>thresholding_val,0,img).astype(np.uint8)
    return img

#truncated thersh
def truncated_thresh(img,thresholding_val):
    img=np.where(img>thresholding_val,thresholding_val,img).astype(np.uint8)
    return img

img=cv2.imread("/users/devanshusharma/desktop/image1.jpg",0)
print(img.shape)
# if(img==None):
#     print("NO image is found on this path")


binary=binary_thresh(img,100)
threshold_val,inbuilt_binary=cv2.threshold(img,100,255,cv2.THRESH_BINARY)
cv2.imshow("binary",binary)
cv2.imshow("inbuilt_binary",inbuilt_binary)
cv2.waitKey(0)

binary_inverse=binary_thresh_inverse(img,100)
threshold_val1,inbuilt_binary_inverse=cv2.threshold(img,100,255,cv2.THRESH_BINARY_INV)
cv2.imshow("binary_inverse",binary_inverse)
cv2.imshow("inbuilt_binary_inverse",inbuilt_binary_inverse)
cv2.waitKey(0)

zero=zero_thresh(img,100)
threshold_val2,inbuilt_zero=cv2.threshold(img,100,255,cv2.THRESH_TOZERO)
cv2.imshow("zero",zero)
cv2.imshow("inbuilt_zero",inbuilt_zero)
cv2.waitKey(0)

zero_inverse=zero_thresh_inverse(img,100)
threshold_val3,inbuilt_zero_inverse=cv2.threshold(img,100,255,cv2.THRESH_TOZERO_INV)
cv2.imshow("zero_inverse",zero_inverse)
cv2.imshow("inbuilt_zero_inverse",inbuilt_zero_inverse)
cv2.waitKey(0)


truncated=truncated_thresh(img,100)
threshold_val3,inbuilt_truncated=cv2.threshold(img,100,255,cv2.THRESH_TRUNC)
cv2.imshow("truncated",truncated)
cv2.imshow("inbuilt_truncated",inbuilt_truncated)
cv2.waitKey(0)




cv2.destroyAllWindows()