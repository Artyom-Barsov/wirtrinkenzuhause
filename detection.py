import cv2
import sys
import numpy as np
import queue

def bfs(mask, x, y):
    pixels = queue.Queue()
    pixels.put((x, y))
    while !pixels.empty():
        newx, newy = pixels.pop()
        if newx > 0 and newx < len(mask[0]) and newy > 0 and newy < len(mask):
            pixels.push((newx, newy))

def suchen(mask):
    for i in range(len(mask)):
        for j in range(len(mask[i])):
            if mask[i][j] == 255:
                bfs(mask, x=j, y=i)

while True:
    frame = cv2.imread(sys.argv[1])
    x, y = sys.argv[2], sys.argv[3]
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    l_b = np.array([104, 0, 0])
    u_b = np.array([255, 255, 255])

    mask = cv2.inRange(hsv, l_b, u_b)
    suchen(mask)
    res = cv2.bitwise_and(frame, frame, mask=mask)


    cv2.imshow("fr", frame)
    cv2.imshow("msk", mask)
    cv2.imshow("res", res)

    key = cv2.waitKey(1)
    if key == 27:
        break

cv2.destroyAllWindows()
