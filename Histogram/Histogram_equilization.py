import cv2
import matplotlib.pyplot as plt
import numpy as np
# from Histogram_of_image import Hist_dist_plot
#read image in greyscale
img=cv2.imread("/users/devanshusharma/desktop/img2.jpg",0)

#resizing image to match with real histogram equiliser
img=cv2.resize(img,(500,500))

value,count=np.unique(img,return_counts=True)

#density of the different pixcel values
density=count/count.sum()

#find cumulative sum we can peroform the cumulative sum pixce wise but that will be too slow so using the cumsum function
cumulative_sum=np.cumsum(density)

#real pixcel values
count=((cumulative_sum)*np.max(value)).astype(np.uint8)


#creating the sample image to replace the pixcels
hist_img=np.zeros(img.shape,np.uint8)

#using for loop
# length,width=img.shape
# for i in range(0,length):
#     for j in range(0,width):
#         hist_img[i,j]=count[np.where(img[i,j]==value)]


all_pixcel=np.zeros(256,np.uint8)
all_pixcel[value]=count
hist_img=all_pixcel[img]

#making real histogram equiliser image
real_hist_img=cv2.equalizeHist(img)




cv2.imshow("img",img)
cv2.imshow("hist_img",hist_img)
cv2.imshow("real_hist_img",real_hist_img)
cv2.waitKey()
cv2.destroyAllWindows()