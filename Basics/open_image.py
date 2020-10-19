import cv2

image = cv2.imread("myImage.jpg") # read image

cv2.imshow("My Image", image) # show image
cv2.waitKey(0) 
