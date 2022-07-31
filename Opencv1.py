from email.mime import image
from genericpath import samefile
import cv2
import numpy as np
#loading an image using 'imread' and specifying the path to the image
sample_image= cv2.imread('../images/input.jpg')

#The first parameter is title shown on image window and next parameter is the above loaded image
cv2.imshow('Image', sample_image)

#By leaving the waitKey blank it just waits for any key to be pressed before continuing. 
#By pplacing the number we can specify the delay time to keep the image window open
# waitKey(0) method is waiting for an input infinitely.

cv2.waitKey()

#this closes all open windows
cv2.destroyAllWindows()

print("The size of the image is: ", sample_image.shape)
print("Height of the image is : ", sample_image.shape[0])
print("Width of the image is : ", sample_image.shape[1])
print(".................................")
#Saving the image
#saving in jpg and png format
cv2.imwrite('output.jpg', sample_image)
cv2.imwrite('output.png', sample_image)

#Grayscaling: In openCv many functions grayscales the images before preprocessing. because it simplifies
#the image, acting almost as a noise reduction and imcreasing processing time as there is less informaton
# in the image

# opencv loads in BGR format by default
gray_image= cv2.cvtColor(sample_image, cv2.COLOR_BGR2GRAY)

#After the conversion of RGB image into grayscale image the shape changes
print("the shape of the grayscale image is: ", gray_image.shape)
print(".................................")
cv2.imshow('Grayscale', gray_image)
cv2.waitKey()
cv2.destroyAllWindows()


#looking at the individual color levels for the individual pixel(x,y)
B, G, R= sample_image[10,20]
print(B, G, R)


