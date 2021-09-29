import cv2

""" Пример показывает работу детектора границы"""

image = cv2.imread("image.jpg")
image = cv2.resize(image, (0, 0), fx=0.5, fy=0.5)


cv2.namedWindow('Canny')
# Определить функцию обратного вызова
def nothing(x):
    pass

# Два ползунка для управления порогом 1 и порогом 2 соответственно
cv2.createTrackbar('threshold1','Canny',50,400,nothing)
cv2.createTrackbar('threshold2','Canny',100,400,nothing)

while(1):
    # Вернуть значение позиции ползунка
    threshold1=cv2.getTrackbarPos('threshold1','Canny')
    threshold2=cv2.getTrackbarPos('threshold2','Canny')

    # Детектор границ
    img_edges=cv2.Canny(image,threshold1,threshold2)

    # Вывод
    cv2.imshow('original',image)
    cv2.imshow('Canny',img_edges)

    if cv2.waitKey(1)==ord('q'):
        break

cv2.destroyAllWindows()