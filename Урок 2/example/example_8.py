import cv2
import numpy as np
import random


if __name__ == '__main__':
    # генерация стартового изображения
    width = 1200
    height = 800
    image = np.zeros((height, width, 3), np.uint8)

    # стартовые точки
    # задаем сами
    points = [[600, 100],
              [100, 700],
              [1150, 750]]

    # задаем рандомно
    # points2 = [[random.randint(0, width), random.randint(0, height)],
    #            [random.randint(0, width), random.randint(0, height)],
    #            [random.randint(0, width), random.randint(0, height)]]

    # Ставим стартовые точки
    image = cv2.circle(image, points[0], radius=5, color=(0, 0, 255), thickness=-1)
    image = cv2.circle(image, points[1], radius=5, color=(0, 255, 0), thickness=-1)
    image = cv2.circle(image, points[2], radius=5, color=(255, 0, 0), thickness=-1)

    # выбираем случайную стартовую точку
    current_point = points[random.randint(0, 2)]

    n = 0
    while n <= 2000:
        # выбираем новую случайную точку
        current_point2 = points[random.randint(0, 2)]

        # расчет средней точки
        midpoint = [(current_point[0] + current_point2[0]) / 2, (current_point[1] + current_point2[1]) / 2]

        # запоминаем эту точку
        current_point = midpoint

        # отрисовываем
        image = cv2.circle(image, (int(midpoint[0]), int(midpoint[1])), radius=4, color=(random.randint(0, 255), random.randint(0, 255),
                                                              random.randint(0, 255)), thickness=-1)

        n = n +1

    cv2.imshow('result', image)
    cv2.waitKey(0)

