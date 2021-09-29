import cv2

""" Пример показывает вывод каналов изображения как одноканальных изображений"""

image = cv2.imread("image.jpg")
image = cv2.resize(image, (0, 0), fx=0.5, fy=0.5)

cv2.imshow('Color all', image)
cv2.imshow('Color blue', image[:, :, 0])
cv2.imshow('Color green', image[:, :, 1])
cv2.imshow('Color red', image[:, :, 2])
cv2.waitKey(0)