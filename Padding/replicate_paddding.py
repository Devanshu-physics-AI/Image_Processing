#creating the image with zero padding
import cv2
import numpy as np
import matplotlib.pyplot as plt
def replicate_padding(img,kernal):
    img_shape=img.shape
    k_shape=kernal.shape
    if(len(img_shape)!=len(k_shape)):
        print("image and kernal channel are different")
        return
    if(len(img_shape)==3):
        final_img=np.zeros(((img_shape[0]+k_shape[0]-1),(img_shape[1]+k_shape[1]-1),3),dtype=np.uint8)
    elif(len(img_shape)==2):
        final_img=np.zeros(((img_shape[0]+k_shape[0]-1),(img_shape[1]+k_shape[1]-1)),dtype=np.uint8)
    final_img_shape=final_img.shape
    final_img[k_shape[0]//2:final_img_shape[0]-(k_shape[0]-k_shape[0]//2)+1,k_shape[1]//2:final_img_shape[1]-(k_shape[1]-k_shape[1]//2)+1,:]=img
    for i in range(0,k_shape[0]//2):
        final_img[i,k_shape[1]//2:final_img_shape[0]-(k_shape[0]-k_shape[0]//2)+1]=img[0]

    for j in range(final_img_shape[0]-(k_shape[0]-k_shape[0]//2)+1,final_img_shape[0]):
        final_img[j,k_shape[1]//2:final_img_shape[0]-(k_shape[0]-k_shape[0]//2)+1]=img[-1]

    for i in range(0,k_shape[0]//2):
        final_img[:,i]=final_img[:,k_shape[1]//2]

    
    for j in range(final_img_shape[0]-(k_shape[0]-k_shape[0]//2)+1,final_img_shape[0]):
        final_img[:,j]=final_img[:,final_img_shape[1]-(k_shape[1]-k_shape[1]//2)]

    
    return final_img

img=cv2.imread("/users/devanshusharma/desktop/img2.jpg")
img=cv2.resize(img,(1000,1000))
shape=img.shape
kernal=np.ones((1000,1000,shape[2]))

padding_img=replicate_padding(img,kernal)
print(padding_img.shape)
cv2.imshow("image",img)
cv2.imshow("padding_img",padding_img)
cv2.waitKey(0)
cv2.destroyAllWindows()