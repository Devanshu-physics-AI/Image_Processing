#convert image to the binary image
import numpy as np
import cv2
#read image
img=cv2.imread("/users/devanshusharma/desktop/x-ray1.jpg",0)
#Let set the threshold value be 100 for greyscale image and [100,100,100] for the coloured image

#function for the binary conversion
def convert_binary(img):
    final_img=np.where(img[:,:]>128,255,0)
    return final_img.astype(np.uint8)

#converting image to binary
my_binary=convert_binary(img)


cv2.imshow("my_binary",my_binary)
cv2.waitKey(0)
cv2.destroyAllWindows()


