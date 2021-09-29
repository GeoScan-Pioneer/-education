import cv2

""" Пример показывает вывод изображения в разных цветовых пространствах"""

image = cv2.imread("image.jpg")
image = cv2.resize(image, (0, 0), fx=0.5, fy=0.5)

color_spaces = ('RGB','GRAY','HSV','LAB','XYZ','YUV')
# перевод в разные цветовые пространства
color_images = {color : cv2.cvtColor(image, getattr(cv2,'COLOR_BGR2' + color)) for color in color_spaces}
# Вывод всех изображений
for color in color_images:
    cv2.imshow(color, color_images[color])
cv2.waitKey(0)