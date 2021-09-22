import cv2


if __name__ == '__main__':
    image = cv2.imread("image.jpg")
    cv2.imshow("Image", image)
    # для завершения нажать любую клавишу
    cv2.waitKey(0)
    cv2.destroyAllWindows()
