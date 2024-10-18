import cv2, numpy as np,time
#read the image
img=cv2.imread("/users/devanshusharma/desktop/image1.jpg")
a= time.time()
#Getting the dimension
height,width,channel=img.shape
#creating the new image of all pixcel values of 0 and channel is 1 because the image is greyscale so it have only 1 value for each pixcel
img1=np.zeros((height,width),np.uint8)
# opencv read the image in BGR form in place of the RGB form
if(channel==1):
    print("Image is already in the BINARY or GREYSCALE form")
else:
    for i in range(0,height):
        for j in range(0,width):
            blue,green,red=img[i][j]
            value=0.299*(red/255)+0.587*(green/255)+ 0.114*(blue/255)
            value=value*255
            img1[i][j]=value
print(img1)
cv2.imshow("Greyscale_img",img1)
b=time.time()
print(b-a)
cv2.waitKey(0)
cv2.destroyAllWindows()



