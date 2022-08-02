import cv2
import numpy as np

#loading an image from directory
sample_image= cv2.imread('../images/tobago.jpg')

#resizing the original image
sample_image= cv2.resize(sample_image, (720, 500))

#printing the pixel intensity value for each channel
print(sample_image[:, :, 0]) #for blue channel 
print(sample_image[:, :, 1]) #for green channel
print(sample_image[:, :, 2]) #for red channel

#we can seperate image channels using cv2.split method also
b, g, r= cv2.split(sample_image)

#display individual channel image
#These images are in grayscale and the brighness of these images shows how each color contribute for the whole image
cv2.imshow('Blue channel', b)
cv2.imshow('Green channel', g)
cv2.imshow('Red channel', r)

#To visualize the actual red or green or blue image we use merge function
zeros= np.zeros(sample_image.shape[0:2], dtype="uint8")
print(zeros)
#For blue image
blue_image= cv2.merge([b, zeros, zeros])
cv2.imshow('red image', blue_image)
##Similary we can visualize for red and green...

#display the image
# cv2.imshow('Image', sample_image)

cv2.waitKey()
cv2.destroyAllWindows()
