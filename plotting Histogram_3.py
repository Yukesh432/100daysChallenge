import cv2
import matplotlib.pyplot as plt
import numpy as np

#Loading the image from directory
img= cv2.imread("../images/bottlecaps.jpg")
#viewing the image
# cv2.imshow("image", img)

#image img is a 3 channel array
print("The shape of the image is: ", img.shape)

#converting image into single channel/1-d array
flatten_image= img.ravel()
print(flatten_image)
print("the shape of image after flattening is: ", flatten_image.shape)

##Plotting the histogram
#bins represents how many lines of histogram to plot

plt.hist(flatten_image, bins=256, range=[0,255])
plt.show()
# ........................................................
colors= ('b', 'g', 'r')
img_ravel= [img[:, :, 0].ravel(), img[:, :, 1].ravel(), img[:, :, 2].ravel()]

#here labels is given for color label and plt legend shows the label
plt.hist(img_ravel, color=colors, label=colors)
plt.legend()
plt.show()
# # ............................................................
# the parameter [i] represents the channel index
#mask image: to find histogram of full image, it is given as "None". But if we want to find histogram of
# particular region of image, we have to create a mask image for it and give it as mask.
# [256] represents our BIN count, and need to be given in square brackets
for i, color in enumerate(colors):
    histogram= cv2.calcHist([img], [i], None, [256], [0,256])
    plt.plot(histogram, color= color)

plt.show()
# ...........................................................



cv2.waitKey()
cv2.destroyAllWindows()
