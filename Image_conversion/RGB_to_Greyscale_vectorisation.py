#RGB to greyscale using the vectorisation

import numpy as np
import cv2
img=cv2.imread("/users/devanshusharma/desktop/image1.jpg")

#function to convert RGB image to greyscale
def grey_scale(img):
    img_shape=img.shape
    if(len(img_shape)==2):
        print("Image is already in the greyscale format or the binary format")
        return img
    elif(len(img_shape)==3):
        mat=np.array([0.1140,0.5870,0.2989])
        # final_img=np.dot(img[:,:,:],mat)
        g
        #other way to to using int create our own dot product
        final_img=img[:,:,:]*mat
        final_img=np.sum(final_img,axis=2)

        final_img=final_img.astype(np.uint8)
        print(final_img)
        return final_img

#converting image to binary
my_greyscale=grey_scale(img)
print(np.max(my_greyscale))

#opencv greyscale
grey_scale=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

cv2.imshow("my_greyscale",my_greyscale)
cv2.imshow("inbuilt_greyscale",grey_scale)
cv2.waitKey(0)
cv2.destroyAllWindows