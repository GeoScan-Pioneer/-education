import cv2

""" Пример показывает работу размывающих фильтров"""

image = cv2.imread("image.jpg")
image = cv2.resize(image, (0, 0), fx=0.5, fy=0.5)
cv2.imshow("image", image)

image_gauss = cv2.GaussianBlur(image, (11, 11), 0)
cv2.imshow("gauss", image_gauss)

image_box = cv2.boxFilter(image, -1, (11, 11), 0)
cv2.imshow("box", image_box)

cv2.waitKey(0)