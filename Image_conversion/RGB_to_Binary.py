import cv2, numpy
#read the image
img=cv2.imread("/users/devanshusharma/desktop/image1.jpg")

#Getting the dimension
height,width,channel=img.shape
# opencv read the image in BGR form in place of the RGB form
if(channel==1):
    print("Image is already in the BINARY or GREYSCALE form")
else:
    for i in range(0,height):
        for j in range(0,width):
            blue,green, red=img[i][j]
            value=0.299*(red/255)+0.587*(green/255)+ 0.114*(blue/255)
            value=value*255
            if(value>=128):
             img[i][j]=255
            else:
               img[i][j]=0
print(img)
cv2.imshow("img",img)
cv2.waitKey(0)
cv2.destroyAllWindows()


print("completed")