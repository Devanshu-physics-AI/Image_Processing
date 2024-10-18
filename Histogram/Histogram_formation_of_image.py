import numpy as np, cv2,matplotlib.pyplot as plt, seaborn as sns
#read the image
img=cv2.imread("/users/devanshusharma/desktop/image1.jpg")

#convert to the greyscale image or we can directly read the greyscale image using "0", at the time of reading
img=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

#count the different values
value,counts=(np.unique(img,return_counts=True))

#draw the histogram of the pixcels data
axis,axis=plt.subplots(1,2)
axis[0].bar(value,counts)
axis[0].set_title("Histplot")
axis[0].set_xlabel("Number of pixcels")
axis[0].set_ylabel("Pixcel values")

#plot the distplot of the function
sns.distplot(img.flatten(),hist=True,ax=axis[1])
axis[1].set_title("Distplot")
axis[1].set_ylabel("Pixcel density")
axis[1].set_xlabel("Number of pixcels")
axis[1].set_ylabel("Pixcel values")


plt.show()
