import os
import numpy as np
import cv2


org = cv2.imread("1.png")
    
wid = org.shape[0]
hei = org.shape[1]
print("width height of image :  ", wid," x ",hei)

img = cv2.cvtColor(org, cv2.COLOR_BGR2GRAY)
img = cv2.medianBlur(img,1)
cv2.imshow("img", img)
ret,thresh = cv2.threshold(img,210,255,cv2.THRESH_BINARY)
cv2.imshow("proc", thresh)
# kernel = np.ones((2, 2), 'uint8')
# dilate_img = cv2.dilate(thresh, kernel, iterations=2)
# cv2.imshow("dilate_img", dilate_img)

cv2.imwrite("2.png", thresh)


cv2.waitKey(0)
cv2.destroyAllWindows()