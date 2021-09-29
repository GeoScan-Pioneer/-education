import cv2

""" Пример показывает вывод изображения с обнулением 2 из 3 каналов"""

# считывание изображения
image = cv2.imread("image.jpg")
# уменьшение размера для удобства вывода
image = cv2.resize(image, (0, 0), fx=0.5, fy=0.5)
cv2.imshow("1", image)

# создание копий
image_R = image.copy()
image_G = image.copy()
image_B = image.copy()

# обнуление каналов B и G
image_R[:, :, 0] = 0
image_R[:, :, 1] = 0

# обнуление каналов
image_G[:, :, 0] = 0
image_G[:, :, 2] = 0

image_B[:, :, 1] = 0
image_B[:, :, 2] = 0

# вывод изображения
cv2.imshow("G", image_G)
cv2.imshow("B", image_B)
cv2.imshow("R", image_R)
# пауза программы
cv2.waitKey()