import numpy as np
import imutils
import cv2

image = cv2.imread('M4kmGZK1fkI.jpg')
image = imutils.resize(image, width=1000)

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
gray = cv2.bilateralFilter(gray, 11, 17, 17)
cv2.imshow("1", gray)
edged = cv2.Canny(gray, 60, 200)
cv2.imshow("2", edged)

cnts = cv2.findContours(edged.copy(), cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
cnts = imutils.grab_contours(cnts)
cnts = sorted(cnts, key = cv2.contourArea, reverse = True)[:20]
screenCnt = []


# loop over our contours
for c in cnts:
    # approximate the contour
    peri = cv2.arcLength(c, True)
    approx = cv2.approxPolyDP(c, 0.02 * peri, True)
 
    # if our approximated contour has four points, then
    # we can assume that we have found our screen
    if len(approx) == 4:
        screenCnt.append(approx)
        

print(screenCnt)

cv2.drawContours(image, screenCnt, -1, (0, 255, 0), 2)
cv2.imshow("Game Boy Screen", image)
cv2.waitKey(0)