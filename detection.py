import cv2
import sys
import numpy as np
import queue

components = []

def bfs(mask, x, y):
    pixels = queue.Queue()
    pixels.put((x, y))
    miny, maxy, minx, maxx = len(mask), 0, len(mask[0]), 0
    while not pixels.empty():
        newx, newy = pixels.get()
        mask[newy][newx] = 0
        minx = min(minx, newx)
        maxx = max(maxx, newx)
        miny = min(miny, newy)
        maxy = max(maxy, newy)
        if newx-1 > 0 and newx-1 < len(mask[0]) and newy-1 > 0 and newy-1 < len(mask) and mask[newy-1][newx-1] == 255:
            pixels.put((newx-1, newy-1))
        if newx+1 > 0 and newx+1 < len(mask[0]) and newy-1 > 0 and newy-1 < len(mask) and mask[newy-1][newx+1] == 255:
            pixels.put((newx+1, newy-1))
        if newx-1 > 0 and newx-1 < len(mask[0]) and newy+1 > 0 and newy+1 < len(mask) and mask[newy+1][newx-1] == 255:
            pixels.put((newx-1, newy+1))
        if newx+1 > 0 and newx+1 < len(mask[0]) and newy+1 > 0 and newy+1 < len(mask) and mask[newy+1][newx+1] == 255:
            pixels.put((newx+1, newy+1))

    components.append((miny, maxy, minx, maxx))

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
