# edge detection using the difference of gaussian
import cv2
import numpy as np

#function for the difference of gaussian
def difference_of_gaussian(img,sigma_x1,sigma_y1,sigma_x2,sigma_y2,kernal_size):
    img_shape=img.shape
    if(len(img_shape)==3):
        print("convert the image into greyscale first")
        return
    img1=cv2.GaussianBlur(img,kernal_size,sigma_x1,sigmaY=sigma_y1)
    img2=cv2.GaussianBlur(img,kernal_size,sigma_x2,sigmaY=sigma_y2)
    return (img1-img2).astype(np.uint8)

#read the image
img=cv2.imread("/users/devanshusharma/desktop/dog1.jpg",0)
if img is None:
    print("No image is found")
else:
 #Diffrence of gaussian image
 dof_before_medianblur=difference_of_gaussian(img,7,7,1,1,(5,5))

 #applying the medain blur because have skewed image intensities
 after_medianblur=cv2.medianBlur(dof_before_medianblur,5)
 #we can also apply the histogram plot to make it normal intensity distribution

 cv2.imshow("img",img)
 cv2.imshow("dof_before_medianblur",dof_before_medianblur)
 cv2.imshow("after_medianblur",after_medianblur)

 cv2.waitKey(0)

 #saving the images
 cv2.imwrite("/users/devanshusharma/documents/difference_of_gaussian.jpg")

 cv2.destroyAllWindows()