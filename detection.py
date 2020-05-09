import cv2
import numpy

def nothing(x):
    pass

while True:
    frame = cv2.imread('3.jpg')

    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    l_b = numpy.array([104, 0, 0])
    u_b = numpy.array([255, 255, 255])

    mask = cv2.inRange(hsv, l_b, u_b)

    res = cv2.bitwise_and(frame, frame, mask=mask)

    cv2.imshow("fr", frame)
    cv2.imshow("msk", mask)
    cv2.imshow("res", res)

    key = cv2.waitKey(1)
    if key == 27:
        break

cv2.destroyAllWindows()
