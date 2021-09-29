import cv2

""" Пример показывает работу фильтра выделяющего границы"""

image = cv2.imread("image.jpg")
image = cv2.resize(image, (0, 0), fx=0.5, fy=0.5)

image_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

result = cv2.Laplacian(image_gray, -1, ksize=3)

cv2.imshow("laplacian", result)
cv2.imshow("image", image)
cv2.waitKey(0)