#Band Thresholding
import cv2
import numpy as np

"""creating the function for the band width->>>>> This is used when we want to highlight the specific intensities in the image"""
def band_thresholding(img,start,ending):
    img=np.where((img>=start) &  (img<=ending),255,0).astype(np.uint8)
    return img

#reading image
img=cv2.imread("/users/devanshusharma/desktop/image1.jpg",0)

band_thresh=band_thresholding(img,100,150)

#creating band thresh using inbuilt function
thresh1,img1=cv2.threshold(img,100,255,cv2.THRESH_BINARY)
thresh2,img2=cv2.threshold(img,150,255,cv2.THRESH_BINARY_INV)
img_final=cv2.bitwise_and(img1,img2)

cv2.imshow("band_thresh",band_thresh)
cv2.imshow("inbuilt_band_thresh",img_final)
cv2.waitKey(0)
cv2.destroyAllWindows()
