import cv2
import numpy as np

img= cv2.imread("../images/obama.jpg")
img= cv2.resize(img, (720,600))

#parameters defined for writing text in an image
#cv putText() parameters..
text= "Obama smiling"
origin= (0,50)
font= cv2.FONT_HERSHEY_COMPLEX
fontScale= 2
color= (255, 0, 0) #(B, G, R)
thickness= 2
lineType= cv2.LINE_AA

#Displaying text in an image
img_text= cv2.putText(img, text, origin, font, fontScale, color, thickness, lineType)

#Parameter for drawing rectange in image
#cv2 rectangle() parameters
#With reference to Deep Learning face detection/ or any object detection, Neural Network model predict
# these coordinates point(point_a, point_b), but here we give these point static as for learning purpose.
point_a= (200, 60)
point_b= (600, 400)
color= (0, 255, 0)
thickness=5
lineType= cv2.LINE_4

image_with_rectangle= cv2.rectangle(img, point_a, point_b, color, thickness, lineType)
cv2.imshow("Image with rectangle disply", image_with_rectangle)


cv2.waitKey()
cv2.destroyAllWindows()