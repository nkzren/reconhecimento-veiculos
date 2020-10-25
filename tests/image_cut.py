import cv2
import numpy as np

image = cv2.imread('../resources/test.jpg')
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
_, thresh = cv2.threshold(gray, 200, 255, cv2.THRESH_BINARY_INV)

contours, _ = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

mask = np.zeros_like(thresh)

cv2.imwrite('test-threshold.jpg', thresh)
